import tools.disks
import tools.diskmanager
import csi_pb2
import csi_pb2_grpc

import sys
import pprint


pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)


class VSphereDiskControllerServicer(csi_pb2_grpc.ControllerServicer):
    """Provides methods that implement functionality of route guide server."""
    def ControllerGetCapabilities( self,request,context):
        eprint("ControllerServicer.ControllerGetCapabilities")

        tmp=csi_pb2.ControllerGetCapabilitiesResponse()

        tmp3 = csi_pb2.ControllerServiceCapability.RPC(type=1)
        tmp2 = csi_pb2.ControllerServiceCapability(rpc=tmp3)
        tmp.capabilities.append(tmp2)

        tmp3 = csi_pb2.ControllerServiceCapability.RPC(type=2)
        tmp2 = csi_pb2.ControllerServiceCapability(rpc=tmp3)
        tmp.capabilities.append(tmp2)

        eprint(tmp)

        return tmp
    def ListVolumes(self,request,context):
        eprint('ControllerServicer.ListVolumes')
        tmp = csi_pb2.ListVolumesResponse()
        #eprint(tmp)
        return tmp

    def ControllerPublishVolume(self,request,context):

        eprint('ControllerServicer.ControllerPublishVolume')
        tmp = csi_pb2.ControllerPublishVolumeResponse() 
        eprint(request)
        eprint(context)
        return tmp

        
    def ControllerUnpublishVolume(self,request,context):

        eprint('ControllerServicer.ControllerUnpublishVolume')
        tmp = csi_pb2.ControllerUnpublishVolumeResponse() 
        eprint(request)
        eprint(context)
        return tmp

    def CreateVolume(self, request, context):
        eprint(request)
        size=request.capacity_range.limit_bytes
        eprint(size)
        x = csi_pb2.Volume(capacity_bytes=size)
        r = csi_pb2.CreateVolumeResponse(volume=x)
        
        obj = tools.diskmanager.DiskManager()
        
        obj.createDisk( 'NomadStore/', request.name, size )
        
        return r
    def DeleteVolume(self, request, context):
        
        eprint('DeleteVolume')
        eprint(request.name)
        eprint("YOLO!")
        eprint(request)
        r = csi_pb2.DeleteVolumeResponse()
        
        obj = tools.diskmanager.DiskManager()

        obj.deleteDisk( 'NomadStore/', request.name )

        return r