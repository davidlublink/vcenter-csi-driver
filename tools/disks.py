from pyVmomi import vim
from pyVim.task import WaitForTask

import time
import os
import socket
import pprint
import sys

from subprocess import CalledProcessError

import subprocess

from pyVim.connect import SmartConnect, Disconnect

pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)

def applyChanges( changes ):
    eprint( "applyChanges : Running " + changes )
    
    if os.getenv('PRODUCTION') == "YES!" :
        eprint("apply production change ahhhh!")
        eprint(changes)
        result = subprocess.run(changes, shell=True, capture_output=True)
        eprint(result.stdout.decode())
        eprint(result.stderr.decode())
        eprint(str(result.returncode))
        return result
    else:
        process = subprocess.run( 'true', shell=True, capture_output=True)
        eprint(changes)
        eprint("ignore process, it's not production")
        eprint(process)

        return process


# Everything after this line is mostly lifted from sample code / google        

def search_for_obj(content, vim_type, name, folder=None, recurse=True):
    """
    Search the managed object for the name and type specified
    Sample Usage:
    get_obj(content, [vim.Datastore], "Datastore Name")
    """
    if folder is None:
        folder = content.rootFolder

    obj = None
    container = content.viewManager.CreateContainerView(folder, vim_type, recurse)

    for managed_object_ref in container.view:
        if managed_object_ref.name == name:
            obj = managed_object_ref
            break
    container.Destroy()
    return obj

def get_obj(content, vim_type, name, folder=None, recurse=True):
    """
    Retrieves the managed object for the name and type specified
    Throws an exception if of not found.
    Sample Usage:
    get_obj(content, [vim.Datastore], "Datastore Name")
    """
    obj = search_for_obj(content, vim_type, name, folder, recurse)
    if not obj:
        raise RuntimeError("Managed Object " + name + " not found.")
    return obj

def find_disk( content, storage, datastore, name, raw = False):

    for i in storage.ListVStorageObject(datastore=datastore) :
        try:
            if ( storage.RetrieveVStorageObject(datastore=datastore,id=i).config.name == name ):
                if raw : 
                    return i
                else:
                    return storage.RetrieveVStorageObject(datastore=datastore,id=i)
        except:
            continue
    return None
def prepare_disk(vm, datastore, disk):
    eprint("Preparing disk!")
    r = add_fcd_to_vm( vm, disk, datastore )
    formatDisk( getDeviceName(r) )
    remove_fcd_from_vm(vm, disk, datastore)

def remove_disk( content,storage,datastore, name):
    disk = find_disk(content,storage,datastore,name, True)

    if disk == None : 
        eprint("Already deleted!")
        return
    eprint("Deleting storage")
    task = storage.DeleteVStorageObject_Task(id=disk,datastore=datastore )
    eprint("Done deleting storage")

    WaitForTask(task)

def create_disk( service_instance, content, vmware_folder, storage, datastore, name, size):

    disk = find_disk(content,storage,datastore,name)
    
    if ( disk != None ):
        eprint( "Found a disk!!!" )
        return disk

    spec = vim.vslm.CreateSpec()
    spec.name = str(name)
    spec.capacityInMB = int( round(size / 1000 / 1000 ) ) # bytes in, megabytes out
    eprint("Creating an image of this many megabytes")
    eprint (spec.capacityInMB)
    spec.metadata.append( vim.KeyValue(key="isnomad",value="yes") )
    spec.backingSpec = vim.vslm.CreateSpec.DiskFileBackingSpec()
    spec.backingSpec.provisioningType = os.getenv("PROVISIONING_TYPE", "eagerZeroedThick")
    #spec.backingSpec = vim.vslm.CreateSpec.DiskFileBackingSpec()
    spec.backingSpec.datastore = datastore
    #spec.backingSpec.path = ( '[%s]' % datastore.name ) + vmware_folder + '/' + name + '.vmdk'
    #spec.backingSpec.path = vmware_folder + '/' + name + '.vmdk'
    #spec.backingSpec.path = 'fcd/' + name + '.vmdk'
    #spec.backingSpec.path = vmware_folder + '/'
    #spec.backingSpec.path = ( '[%s]' % datastore.name ) + ' ' + vmware_folder + '/'

    # @todo use friendlier names...
    spec.backingSpec.path = '' + vmware_folder + '/'

    storage = content.vStorageObjectManager
    task = storage.CreateDisk_Task(spec)

    WaitForTask(task)

    return find_disk(content,storage,datastore,name)

def formatDisk(disk ):
    eprint("formatting disk")
    r = applyChanges('mkfs.ext4 /dev/' + disk)
    if r.returncode != 0:
        raise Exception("Failed to format disk :" + r.stderr.decode() )
    eprint(disk)

def getDeviceName( diskUnit ):
    return 'sd' + chr( 97 + diskUnit )

def add_fcd_to_vm(vm, vdisk, datastore):
    """
    Add already existing first class disk to vm
    """
    unit_number = 0
    found = None
    eprint("scanning devices on the given vm")
    for dev in vm.config.hardware.device:
        if hasattr(dev.backing, 'fileName'):
            eprint(dev.backing.fileName)
            if ( dev.backing.fileName == vdisk.config.backing.filePath ):
                found = dev
            unit_number = int(dev.unitNumber) + 1
            # unit_number 7 reserved for scsi controller
            if unit_number == 7:
                unit_number += 1
            if unit_number >= 16:
                raise Exception("We don't support this many disks.")
        if isinstance(dev, vim.vm.device.VirtualSCSIController):
            controller = dev

    if found != None :
        eprint("Looks like it was already mounted...")
        eprint( unit_number )
        eprint( dev) 
    else:
        eprint("Found empty sd slot "+ str(unit_number) )
        # Setting backings
        spec = vim.vm.ConfigSpec()
        disk_spec = vim.vm.device.VirtualDeviceSpec()
        disk_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.add
        disk_spec.device = vim.vm.device.VirtualDisk()
        disk_spec.device.backing = vim.vm.device.VirtualDisk.FlatVer2BackingInfo()
        disk_spec.device.backing.diskMode = 'persistent'
        disk_spec.device.backing.fileName = vdisk.config.backing.filePath
        disk_spec.device.backing.thinProvisioned = True
        disk_spec.device.unitNumber = unit_number
        disk_spec.device.controllerKey = controller.key

        #creating the list
        dev_changes = []
        dev_changes.append( disk_spec )
        spec.deviceChange = dev_changes

        #Sending the request
        task = vm.ReconfigVM_Task( spec=spec )

        # Wait for VM to finish deployment
        WaitForTask( task )

    # Tell scsi to rescan the bus for new hardware
    applyChanges('echo "- - -" > /sys/class/scsi_host/host2/scan' )
    applyChanges('echo "- - -" > /sys/class/scsi_host/host0/scan' )
    applyChanges('echo "- - -" > /sys/class/scsi_host/host1/scan' )

    # Refresh any existing hardware
    applyChanges('echo "1" > /sys/class/block/'+getDeviceName(unit_number)+'/device/rescan')

    eprint("wait for kernel to finish scanning")
    time.sleep(1)

    eprint("Disk has been added, let's look at our mounts")
    eprint(socket.gethostname())

    mounts = []
    with open('/proc/mounts','r') as f:
        mounts = [line.split()[0] for line in f.readlines()]   
    
    eprint(mounts)

    while "/dev/" + getDeviceName(unit_number) in mounts :
        eprint("Whoops, it's mounted, can we unmount it maybe?")
        r=applyChanges("umount /dev/" + getDeviceName(unit_number) )
        if r.returncode != 0 :
            raise Exception("Non zero return code from execution of " + str(r.stderr) )

    eprint("done connecting")

    return unit_number
def umount_fcd( disk ):
    applyChanges("umount " + disk +' || true ')

def mount_fcd( disk, target ):
    os.mkdir( target )
    applyChanges("mount " + disk + " " + target)

def remove_fcd_from_vm(vm, vdisk, datastore):
    """
    Remove first class disk from vm
    """
    eprint("remove_fcd_from_vm")
    unit_number = 0
    if vdisk == None : 
        eprint("No disk, no work to disconnect from fcd_from_vm")
        return 
    found = 0
    for dev in vm.config.hardware.device:
        if hasattr(dev.backing, 'fileName'):
            if ( dev.backing.fileName == vdisk.config.backing.filePath ):
                found = dev
            unit_number = int(dev.unitNumber) + 1
            # unit_number 7 reserved for scsi controller
            if unit_number == 7:
                unit_number += 1
            if unit_number >= 16:
                raise Exception("We don't support this many disks.")
        if isinstance(dev, vim.vm.device.VirtualSCSIController):
            controller = dev

    if found == 0 :
        return False

    virtual_hdd_spec = vim.vm.device.VirtualDeviceSpec()
    #virtual_hdd_spec.fileOperation = vim.vm.device.VirtualDeviceSpec.FileOperation.destroy
    virtual_hdd_spec.operation = vim.vm.device.VirtualDeviceSpec.Operation.remove
    virtual_hdd_spec.device = found
    spec = vim.vm.ConfigSpec()
    spec.deviceChange = [virtual_hdd_spec]
    WaitForTask(vm.ReconfigVM_Task(spec=spec))

    eprint("Disk was removed")
    
    return True
   
