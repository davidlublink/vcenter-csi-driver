import tools.disks
import tools.diskmanager
import csi_pb2
import csi_pb2_grpc

import sys
import pprint

pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)

class VSphereDiskNodeServicer(csi_pb2_grpc.NodeServicer):
    """Provides methods that implement functionality of route guide server."""
    def NodeGetInfo( self, request, context ):
        tmp = csi_pb2.NodeGetInfoResponse()
        tmp.node_id = 'potatoez'
        eprint("NodeServicer.NodeGetInfo")
        tmp.max_volumes_per_node = 15

        #eprint(tmp)
        return tmp

    def NodeUnpublishVolume( self, request, context):
        eprint(request)
        obj = tools.diskmanager.DiskManager()
        obj.umountDisk( request.volume_id, request.target_path )
        return csi_pb2.NodeUnpublishVolumeResponse()
        
    def NodePublishVolume( self, request, context):
        eprint(request)
        obj = tools.diskmanager.DiskManager()
        obj.mountDisk( request.volume_id, request.target_path  )
        return csi_pb2.NodePublishVolumeResponse()
    def NodeGetCapabilities(self, request, context):

        tmp = csi_pb2.NodeGetCapabilitiesResponse()

        eprint("NodeServicer.NodeGetCapabilities")
        #tmp3 = csi_pb2.NodeServiceCapability.RPC(type=1)
        #tmp2 = csi_pb2.NodeServiceCapability(rpc=tmp3)
        #tmp.capabilities.append(tmp2)

        #eprint(tmp)

        return tmp
        