  job "vcenter-csi-demo" {
   datacenters = ["dc1"]
   type = "service"

    group "demo-storage" {

      count = 3
      
      network {
        port "http"{
          to = 80
        }
      }

      volume "data" {
            read_only       = false
            source          = "volume-235"
            type            = "csi" 
            attachment_mode = "file-system"
            access_mode     = "single-node-writer"
            per_alloc       = true
        }

      task "simple-webserver" {
        driver = "docker"
        
          volume_mount {
                volume = "data"
                /* Bug : + in name breaks the cycle somehow  and mount silently fails*/ 
                destination = "/usr/local/apache2/htdocs/"
            }

        config {
          image = "httpd"
          ports=["http"]
        }
      }
    }
  }
