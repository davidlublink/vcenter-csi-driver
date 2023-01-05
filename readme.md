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
VMWARE_HOSTNAME="127.0.0.1"

VMWARE_USERNAME="alice"
VMWARE_PASSWORD="password"

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

# Caveats

This job does not descriminate the nomad clients and if you run the plugin on a client that is not a vmware client, it is likely to simply crash with exotic error messages ( unable to identify virtual machine !).

After 4-5 disks on a single vm in nomad, linux seems to stop detecting disks added by vmware. I don't know if this is a bug with csi, nomad or vmware.

Nomad jobs are easily managed via nomad web interface, but volumes can only be created/removed from the API


# Troubleshooting

When troubleshooting, run the plugin as a type=service instead of a type=system. Open the stderr console for the plugin and watch it as you run the action you are troubleshooting. When creating a volume, the plugin connects to your vcenter and will create the volume. Bad permissions and misconfigurations on your vmware can interfere. Testing creation of a volume is a good sanity test as it requires a functional setup to connect to the disk and format it.

Be careful with volume name, any CSI related commands ( create,delete volume ) will have an index ( ie volume-235[0] ), but the nomad jobs will not ( ie volume-235 ).

If you are stuck, please use the issue tracker to log any issues you find.

Include your Nomad Jobs, volume definitions, logs and any output from any of the daemons.






