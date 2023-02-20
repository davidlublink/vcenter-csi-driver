import tools.disks
import csi_pb2
import csi_pb2_grpc

import sys
import pprint


pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)

class VSphereDiskIdentityServicer(csi_pb2_grpc.IdentityServicer):
    """Provides methods that implement functionality of route guide server."""
    def GetPluginInfo(self, request, context):
        eprint('IdentityService.GetPluginInfo')
        obj = csi_pb2.GetPluginInfoResponse()
        obj.name='cloudli_vmware'
        obj.vendor_version='1'
        return obj
    def GetPluginCapabilities(self, request, context):
        eprint('IdentityService.GetPluginCapabilities')

        tmp = csi_pb2.GetPluginCapabilitiesResponse()
        tmp3=csi_pb2.PluginCapability.Service(type=1)
        tmp2=csi_pb2.PluginCapability(service=tmp3)
        tmp.capabilities.append(tmp2)
        return tmp
    def Probe(self,request,context):
        eprint('IdentityService.Probe')
        obj = tools.diskmanager.DiskManager()
        obj.ping()
        return csi_pb2.ProbeResponse()


