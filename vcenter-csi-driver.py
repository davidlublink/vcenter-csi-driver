from concurrent import futures

import tools.vspheredisknodeservicer
import tools.vspherediskcontrollerservicer
import tools.vspherediskidentityservicer

import logging

import os 
import sys

import pprint

import grpc

import csi_pb2
import csi_pb2_grpc

obj = csi_pb2.GetPluginInfoResponse
obj.name='cloudli_vmware'
obj.vendor_version='1'

pp = pprint.PrettyPrinter(stream=sys.stderr)

def eprint(*args, **kwargs):
    pp.pprint(*args, **kwargs)

if __name__ == '__main__':
    eprint("Starting gRPC daemon Cloudli-CSI Wamba")
    logging.basicConfig()
    eprint("The service is setting up!!!1!!")
    
    eprint(os.environ.get('CSI_ENDPOINT','unix:csi.sock' ))
    
    monolith = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add identity service - common services between Node and service 
    csi_pb2_grpc.add_IdentityServicer_to_server( tools.vspherediskidentityservicer.VSphereDiskIdentityServicer(), monolith )

    # Add node service - needed to publishing and unpublishing volumes ( 2 minimum requirements for this setup )
    if os.getenv( "CSI_NODE", "1" ):
        csi_pb2_grpc.add_NodeServicer_to_server( tools.vspheredisknodeservicer.VSphereDiskNodeServicer(), monolith )

    # All Controller, this implements volume creation/deletion and other cluster level tasks
    if os.getenv( "CSI_CONTROLLER", "1" ):
        csi_pb2_grpc.add_ControllerServicer_to_server( tools.vspherediskcontrollerservicer.VSphereDiskControllerServicer(), monolith )  
    
    monolith.add_insecure_port( os.environ.get('CSI_ENDPOINT','unix:csi.sock' ) )
    monolith.start()
    monolith.wait_for_termination()
    eprint("exiting main")