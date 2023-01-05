# vcenter-csi-driver

State of the project proof of concept with active interest in getting it done.

# Introduction

This CSI plugin allows you to setup your Nomad cluster so that Nomad clients that are on VMWare hosted virtual machines can use your vcenter connected SAN disks as storage. This plugin will connect the vmdk from your SAN to the server with iSCSI. This is accomplished by using the vmware library pyvmomi to connect to the vCenter and setup disks.

This repository contains a python based implementation of the CSI specification using the VmWare pyvmomi library.

This repository is in direct response to this issue : 

https://github.com/kubernetes-sigs/vsphere-csi-driver/issues/542

This plugin has been tested and developed on Nomad, however it is compatible with the CSI specification so it should also be functional with other clusters. 

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


# Opening tickets

Please use the issue tracker to log any issues you find.

Include your Nomad Jobs, volume definitions and any output from any of the daemons.

# Estimated time to configure

20 Minutes

Skill Level : Intermediate 


# Pre-requisites

* VmWare VCenter configured ( with API 6.7 or better )
* * VCenter controls 1 or more virtual machines that contain a nomad-client
* * VCenter controls 1 or more SANs ( virtual or otherwises ) with datastores
* User/password with appropriate access to the cluster
* IPs/Hostnames of vCenter
* Functional Nomad Cluster
* * Vault ( optional / recommended )

# Quick guide
* Deploy two included nomad jobs and generate a volume using the included volume sample.


# About Cloudli
Experts in Vmware, voice automation, etc....