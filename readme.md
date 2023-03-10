# Introduction

This CSI plugin allows you to setup your Nomad cluster so that Nomad clients that are on VMWare hosted virtual machines can use your vcenter connected SAN disks as storage. This plugin will connect the vmdk from your SAN to the server with iSCSI. This is accomplished by using the vmware library pyvmomi to connect to the vCenter and setup disks.

This repository contains a python based implementation of the CSI specification using the VmWare pyvmomi library.

This repository is in direct response to this issue : 

https://github.com/kubernetes-sigs/vsphere-csi-driver/issues/542

This plugin has been tested and developed on Nomad, however it is compatible with the CSI specification so it should also be functional with other clusters. 

# CSI and Figure 8

CSI : https://github.com/container-storage-interface/spec/blob/master/spec.md

In figure 8 : 

```
       +-+  +-+
       |X|  | |
       +++  +^+
        |    |
   Node |    | Node
Publish |    | Unpublish
 Volume |    | Volume
    +---v----+---+
    | PUBLISHED  |
    +------------+

Figure 8: Plugins MAY forego other lifecycle steps by contraindicating
them via the capabilities API. Interactions with the volumes of such
plugins is reduced to `NodePublishVolume` and `NodeUnpublishVolume`
calls.

```

This plugin is based on the minimal set with partially implemented create/delete volumes.



# Environment variables

The following 3 variables are needed to configure CSI.

```
CSI_NODE=1
CSI_CONTROLLER=1
CSI_ENDPOINT="unix:/csi/csi.sock"
```

This variable is needed to run commands such as mount, mkfs and others.

```
PRODUCTION="YES!"
```

Use this variable to allow insecure certificates

```
INSECURE_CERTIFICATE=1
```

Enter your vmcenter credentials here

```
# Name in vmware vcenter
VMWARE_HOSTNAME=node.unique.name

VMWARE_USERNAME="alice"
VMWARE_PASSWORD="password"

#Host with the vmware ip, usually it's where you login to vcenter
VMWARE_HOST="192.168.11.1"
VMWARE_FOLDER="fcd/"
VMWARE_DATASTORE="mystore"
```


# Pre-requisites

* Vmware vcenter configured ( with API 6.7 or better )
    * At least 1 SAN connected to the same VMware vcenter
    * User/password with appropriate access to the cluster
    * IPs/Hostnames of vCenter
* Functional Nomad Cluster
    * At least 1 nomad client that is running inside a Vmware virtual machine

## Deploy the CSI plugin

1. Setup your variables in your job csi-nomad-plugin.hcl
2. Run the job

```
nomad run csi-nomad-plugin.hcl
```

Once your job is healthy, the plugin should appear in storage plugins tab.

It takes 1-2 minutes for the plugin to be healthy AFTER your job is healthy. So if you create a volume to quickly it might say creation is not supported.

## Create a volume

1. Setup your variables in csi-volume-demo.hcl
2. Create the volume

```
nomad volume create csi-volume-demo.hcl
```

Note that any volume you add must end with the index number. eg, the volume volume-235 would be set as volume-235 in this file. If you want to have multiple volumes with the same name, just recreate the volume and increment each time ( volume-235[0], volume-235[1], volume-235[2] etc...). In your nomad job, you do not specify the index. If unsure just put [0] ( ie volume-235[0]).

You should see the volume appear in vcenter when this is completed

## Use your storage

1. Setup your variables in csi-nomad-demo.hcl
2. Create your job

```
nomad run csi-nomad-demo.hcl
```

## Stop using your storage

1. Stop the job

```
nomad stop vcenter-csi-demo
```

## Delete your storage

1. Delete the volume

```
nomad volume delete volume-235[0]
```

## Remove CSI Plugin

1. Stop the job

```
nomad stop csi-nomad-plugin
```

Plugin seems to stay registered but unhealthy after you remove it, nomad gc doesn't seem to help




## Unregister your storage

This unregisters with nomad, but will not delete the volume in vstorage

```
nomad volume deregister volume-235[0]
```


# Building

Checkout a copy of this repository and run docker build


```
docker build .
```

# Life cycles

Under the hood it's python. I used the code generator gRPC with the official spec for CSI. Nomad and Vmware do most of the work. Here are the 4 implemented methods:

## Create a volume

When Nomad receives a volume creation command, CSI invokes the plugin. The plugin does the following :

1. Finds the virtual machine object that represents itself in vCenter ( assumes hostname is the same as vm name in vcenter )
2. Finds the identified datastore
3. Find if a file with the same name already exists, if it does, abort and use it
4. Creates a new volume ( vmdk ) in vcenter
5. The volume is then attached to the vm running the plugin ( it appears as /dev/sdX )
6. The volume is formatted ( ie mkfs.ext4 /dev/sdX )
7. The volume is detached from the vm and is now waiting and ready.
8. Plugin goes back to sleep

All of this happens transparently when you run 'nomad volume create foo.hcl'. 

There is no control over which filesystem is used for formatting, it's always ext4. At this point the volume is now mounted and ready to go. As a side effect of this process you'll notice every volume the plugin creates has a 'lost+found' folder as it is an ext4 file system.

## Publishing a volume

Now that you have a volume that is ready to go, Nomad has to use it. When nomad allocates a job that requires a volume provided by CSI, it'll only allocate to clients with a healthy csi plugin. During the allocation steps, Nomad will call our plugin which will do the following steps : 

1. Finds the virtual machine object that represents itself in vCenter ( assumes hostname is the same as vm name in vcenter )
2. Finds the provided datastore
3. Find volume ( vmdk ) with the correct name in the identified datastore, if file not found hard crash
5. The volume is then attached to the vm running the plugin ( it will appear as /dev/sdX )
6. The volume is mounted to the location CSI provides ( usually a VERY long file system path ) 
7. Plugin goes back to sleep

At this point the volume is now mounted and ready to go. As a side effect of this process you'll notice every volume the plugin creates has a 'lost+found' folder as it is an ext4 file system.

Once attached the plugin has nothing more to do, vcenter will have added the volume to the nomad client's iSCSI and so everything else is high performance access to the iSCSI.

At this point Nomad can continue it's allocation and will download the image ( if it's docker ) and start the job. The driver is idle again.

All of this happens transparently when you 'nomad run job-that-has-a-csi-based-volume.hcl'.

## Unpublishing a volume

When a job ends ( cleanly or not ) we have to detach the volume from the nomad client's iSCSI.

During Nomad's cleanup cycle, near the end, it invokes the CSI plugin indicating the volume is ready to be unmounted. At this point the driver does the following : 

1. Calls umount
2. Sends API request to vmware to detach the disk from the nomad client's iSCSI
3. Volume is back free to be used in your SAN with no iSCSI connections
4. Plugin goes back to sleep

Nomad finishes cleaning up and may do other work. Generally the volumes are removed at the very end of the Nomad cleanup cycle.


All of this happens transparently when you 'nomad stop job-that-had-a-csi-based-volume'.




# Caveats

This job does not detect that a nomad client is running on a vmware vm, if you run the plugin on a client that is not a vmware client, it is likely to simply crash with unexpected messages (like unable to identify virtual machine !).

Nomad jobs are easily managed via nomad web interface, but volumes can only be created/removed from the API

Garbage collection relies on the cluster to handle it. If anything goes wrong on the cluster or in the plugin, you will have rogue disks connected to your clients.


## Overconnected disk

```
Cannot open the disk '/vmfs/volumes/some-uuid/fcd/somedisk.vmdk' or one of the snapshot disks it depends on
```

This can happen if the plugin is not called to disconnect a disk after it was used. Be sure that the plugin is only ever stopped when all volumes in use are stopped. The plugin, being stateless, can be restarted as long as no changes happen to any of your jobs while it's being restarted. IE if all other jobs are healthy and are not changed, you can restart the plugin as much as you want. 


This happens when we try to connect the same disk to two virtual machines. Maybe the disk is still in use on a previous machine 


# Troubleshooting


* Run plugin in type=service instead of type=system mode
    * You can't change service types so create the job with a different name and stop the service
* Watch stderr of the plugin, it will tell you what is happening 99% of the time something fails.

Testing creation of a volume is a good sanity test as it requires a functional setup to connect to the disk and format it.

Be careful with volume name, any CSI related commands ( create, delete volume ) will have an index ( ie volume-235[0] ), but the nomad jobs will not ( ie volume-235 ).

If you are stuck, please use the issue tracker to log any issues you find.

Include your Nomad Jobs, volume definitions, logs and any output from any of the daemons.



# Contributing

Testing, troubleshooting, contributing code, etc... All help is welcome!

The next big step is to integrate automated testing

If you test this driver, please open an issue in GitHub and included any information you can about your test scenario ( even if everything succeeded ). In the description line add '[Test Results]'. 

If you run into any issues, please open an issue and include whatever information you have available.


# Test Results

This plugin has been tested with Nomad 1.4.3 and vcenter v.7. Testing is still ongoing.

# Upcoming Features / BugFixes
* Volume creation filenames is garbage ( fcd/hash.vmdk )
* Add notes to readme about adding an existing volume
* Add full disk encryption




