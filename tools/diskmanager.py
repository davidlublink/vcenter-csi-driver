from pyVmomi import vim

import os
import socket
import pprint
import sys

from tools.disks import create_disk, remove_disk,remove_fcd_from_vm,prepare_disk,get_obj,find_disk,add_fcd_to_vm,getDeviceName,mount_fcd,umount_fcd

import subprocess

from pyVim.connect import SmartConnect

pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)

def applyChanges( changes ):
    eprint( "applyChanges : Running " + changes )
    
    if os.getenv('PRODUCTION') == "YES!" :
        eprint("Executing the command!")
        result = subprocess.run(changes, shell=True, capture_output=True)
        eprint("Done executing!")
        eprint(str(result.returncode))
        eprint(result.stdout.decode())
        eprint(result.stderr.decode())
        
        return result
    else:
        process = subprocess.run( 'true', shell=True, capture_output=True)
        eprint(changes)
        eprint("ignore process, it's not production")
        eprint(process)
        return process


class DiskManager():

    def __init__(self):
        eprint("connect to vhost")
        self.service_instance = SmartConnect( host=os.getenv('VMWARE_HOST'),
            user=os.getenv('VMWARE_USERNAME'),
            pwd=os.getenv('VMWARE_PASSWORD'),
            disableSslCertValidation=os.getenv('INSECURE_CERTIFICATE') )
        eprint("Load content menu")
        self.content = self.service_instance.RetrieveContent()

        eprint("Loading container")
        self.container = self.content.viewManager.CreateContainerView(
            self.content.rootFolder,
            [vim.HostSystem],
            True)

        eprint("loading data store")
        self.datastore = get_obj( self.content, [vim.Datastore], os.getenv('VMWARE_DATASTORE') )    

        eprint("Reading hostname")
        self.hostname = os.getenv('VMWARE_HOSTNAME', socket.gethostname() )
    
    def createDisk(self, folder, name, size ):
        eprint("Create Disk")
        eprint(self.hostname)
        disk = create_disk( self.service_instance, self.content, os.getenv('VMWARE_FOLDER', 'fcd/'), self.content.vStorageObjectManager, self.datastore, name, size ) 
        eprint("Finding my vm" + self.hostname)
        vm = get_obj( self.content, [vim.VirtualMachine], self.hostname)
        prepare_disk( vm, self.datastore, disk )

    def removeDisk(self, folder, name):
        eprint("Search before removing disk")
        disk = find_disk( self.content, self.content.vStorageObjectManager, self.datastore, name )
        eprint("Removing disk")
        eprint(self.hostname)
        remove_disk( self.content, self.content.vStorageObjectManager, self.datastore, name )
        eprint("Remove Disk")

    def mountDisk(self, name, target):
        eprint("Mount Disk")
        eprint(self.hostname)
        vm = get_obj( self.content, [vim.VirtualMachine], self.hostname)
        disk = find_disk( self.content, self.content.vStorageObjectManager, self.datastore, name )
        r = add_fcd_to_vm( vm, disk, self.datastore )
        mount_fcd( '/dev/'+ getDeviceName(r), target )
    
    def umountDisk(self, name, target):
        eprint("umount Disk")
        eprint(name)
        eprint(target)
        eprint(self.hostname)
        vm = get_obj( self.content, [vim.VirtualMachine], self.hostname)
        disk = find_disk( self.content, self.content.vStorageObjectManager, self.datastore, name )
        umount_fcd( target )
        umount_fcd( target )
        remove_fcd_from_vm( vm, disk, self.datastore )