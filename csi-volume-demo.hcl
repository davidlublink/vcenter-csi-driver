/*
nomad volume create csi-volume-demo.html
nomad volume deregister volume-235[0]
*/

type = "csi"
id = "volume-235[0]"
name = "volume-235[0]"

capability {
     access_mode = "multi-node-multi-writer"
     attachment_mode = "file-system"
}

plugin_id = "vcenter-csi"
capacity_max = "5G"

secrets {
  name="initial allocation was 5G"
}
