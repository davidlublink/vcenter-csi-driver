/*
 Author David Lublink 2023

 Sample file how to use csi vcenter with nomad.

 This job provides the driver for storage. It coordinates with vcenter to provide volumes to jobs.

 You need this job to connect vcenter and csi
*/

  job "vcenter-csi-driver" {
    datacenters = [ "dc1" ]
    type = "system"

    group "csi-providers" {
      
      task "csi-san" {
        driver = "docker"

        config {
          privileged = true
          image = "davidlublink/vcenter-csi-driver:latest"
        }
        env {
          #GRPC_VERBOSITY="debug"
          VMWARE_CLUSTER="Cluster-01"
          VMWARE_DATASTORE="VOL-001"
          VMWARE_DATACENTER="dc1"
          VMWARE_HOST="127.0.0.1"
          VMWARE_FOLDER="fcd"
          VMWARE_HOSTNAME=node.unique.name
          VMWARE_USERNAME="alice"
          VMWARE_PASSWORD="password"
          INSECURE_CERTIFICATE="1"
          PRODUCTION="YES!"
          CSI_ENDPOINT="unix:/csi/csi.sock"
        }

        csi_plugin {
          id        = "vcenter-csi"
          type      = "monolith"
          mount_dir = "/csi"
          health_timeout="600s"
        }
      }

     } # csi-providers

} # Job
