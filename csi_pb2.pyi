from google.protobuf import descriptor_pb2 as _descriptor_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ALPHA_ENUM_FIELD_NUMBER: _ClassVar[int]
ALPHA_ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
ALPHA_FIELD_FIELD_NUMBER: _ClassVar[int]
ALPHA_MESSAGE_FIELD_NUMBER: _ClassVar[int]
ALPHA_METHOD_FIELD_NUMBER: _ClassVar[int]
ALPHA_SERVICE_FIELD_NUMBER: _ClassVar[int]
CSI_SECRET_FIELD_NUMBER: _ClassVar[int]
DESCRIPTOR: _descriptor.FileDescriptor
alpha_enum: _descriptor.FieldDescriptor
alpha_enum_value: _descriptor.FieldDescriptor
alpha_field: _descriptor.FieldDescriptor
alpha_message: _descriptor.FieldDescriptor
alpha_method: _descriptor.FieldDescriptor
alpha_service: _descriptor.FieldDescriptor
csi_secret: _descriptor.FieldDescriptor

class CapacityRange(_message.Message):
    __slots__ = ["limit_bytes", "required_bytes"]
    LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_BYTES_FIELD_NUMBER: _ClassVar[int]
    limit_bytes: int
    required_bytes: int
    def __init__(self, required_bytes: _Optional[int] = ..., limit_bytes: _Optional[int] = ...) -> None: ...

class ControllerExpandVolumeRequest(_message.Message):
    __slots__ = ["capacity_range", "secrets", "volume_capability", "volume_id"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CAPACITY_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    capacity_range: CapacityRange
    secrets: _containers.ScalarMap[str, str]
    volume_capability: VolumeCapability
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., capacity_range: _Optional[_Union[CapacityRange, _Mapping]] = ..., secrets: _Optional[_Mapping[str, str]] = ..., volume_capability: _Optional[_Union[VolumeCapability, _Mapping]] = ...) -> None: ...

class ControllerExpandVolumeResponse(_message.Message):
    __slots__ = ["capacity_bytes", "node_expansion_required"]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    NODE_EXPANSION_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    capacity_bytes: int
    node_expansion_required: bool
    def __init__(self, capacity_bytes: _Optional[int] = ..., node_expansion_required: bool = ...) -> None: ...

class ControllerGetCapabilitiesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ControllerGetCapabilitiesResponse(_message.Message):
    __slots__ = ["capabilities"]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedCompositeFieldContainer[ControllerServiceCapability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[ControllerServiceCapability, _Mapping]]] = ...) -> None: ...

class ControllerGetVolumeRequest(_message.Message):
    __slots__ = ["volume_id"]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ...) -> None: ...

class ControllerGetVolumeResponse(_message.Message):
    __slots__ = ["status", "volume"]
    class VolumeStatus(_message.Message):
        __slots__ = ["published_node_ids", "volume_condition"]
        PUBLISHED_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
        VOLUME_CONDITION_FIELD_NUMBER: _ClassVar[int]
        published_node_ids: _containers.RepeatedScalarFieldContainer[str]
        volume_condition: VolumeCondition
        def __init__(self, published_node_ids: _Optional[_Iterable[str]] = ..., volume_condition: _Optional[_Union[VolumeCondition, _Mapping]] = ...) -> None: ...
    STATUS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    status: ControllerGetVolumeResponse.VolumeStatus
    volume: Volume
    def __init__(self, volume: _Optional[_Union[Volume, _Mapping]] = ..., status: _Optional[_Union[ControllerGetVolumeResponse.VolumeStatus, _Mapping]] = ...) -> None: ...

class ControllerPublishVolumeRequest(_message.Message):
    __slots__ = ["node_id", "readonly", "secrets", "volume_capability", "volume_context", "volume_id"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VolumeContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    readonly: bool
    secrets: _containers.ScalarMap[str, str]
    volume_capability: VolumeCapability
    volume_context: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., node_id: _Optional[str] = ..., volume_capability: _Optional[_Union[VolumeCapability, _Mapping]] = ..., readonly: bool = ..., secrets: _Optional[_Mapping[str, str]] = ..., volume_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ControllerPublishVolumeResponse(_message.Message):
    __slots__ = ["publish_context"]
    class PublishContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PUBLISH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    publish_context: _containers.ScalarMap[str, str]
    def __init__(self, publish_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ControllerServiceCapability(_message.Message):
    __slots__ = ["rpc"]
    class RPC(_message.Message):
        __slots__ = ["type"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        CLONE_VOLUME: ControllerServiceCapability.RPC.Type
        CREATE_DELETE_SNAPSHOT: ControllerServiceCapability.RPC.Type
        CREATE_DELETE_VOLUME: ControllerServiceCapability.RPC.Type
        EXPAND_VOLUME: ControllerServiceCapability.RPC.Type
        GET_CAPACITY: ControllerServiceCapability.RPC.Type
        GET_VOLUME: ControllerServiceCapability.RPC.Type
        LIST_SNAPSHOTS: ControllerServiceCapability.RPC.Type
        LIST_VOLUMES: ControllerServiceCapability.RPC.Type
        LIST_VOLUMES_PUBLISHED_NODES: ControllerServiceCapability.RPC.Type
        PUBLISH_READONLY: ControllerServiceCapability.RPC.Type
        PUBLISH_UNPUBLISH_VOLUME: ControllerServiceCapability.RPC.Type
        SINGLE_NODE_MULTI_WRITER: ControllerServiceCapability.RPC.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: ControllerServiceCapability.RPC.Type
        VOLUME_CONDITION: ControllerServiceCapability.RPC.Type
        type: ControllerServiceCapability.RPC.Type
        def __init__(self, type: _Optional[_Union[ControllerServiceCapability.RPC.Type, str]] = ...) -> None: ...
    RPC_FIELD_NUMBER: _ClassVar[int]
    rpc: ControllerServiceCapability.RPC
    def __init__(self, rpc: _Optional[_Union[ControllerServiceCapability.RPC, _Mapping]] = ...) -> None: ...

class ControllerUnpublishVolumeRequest(_message.Message):
    __slots__ = ["node_id", "secrets", "volume_id"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    node_id: str
    secrets: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., node_id: _Optional[str] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ControllerUnpublishVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CreateSnapshotRequest(_message.Message):
    __slots__ = ["name", "parameters", "secrets", "source_volume_id"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameters: _containers.ScalarMap[str, str]
    secrets: _containers.ScalarMap[str, str]
    source_volume_id: str
    def __init__(self, source_volume_id: _Optional[str] = ..., name: _Optional[str] = ..., secrets: _Optional[_Mapping[str, str]] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CreateSnapshotResponse(_message.Message):
    __slots__ = ["snapshot"]
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    snapshot: Snapshot
    def __init__(self, snapshot: _Optional[_Union[Snapshot, _Mapping]] = ...) -> None: ...

class CreateVolumeRequest(_message.Message):
    __slots__ = ["accessibility_requirements", "capacity_range", "name", "parameters", "secrets", "volume_capabilities", "volume_content_source"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCESSIBILITY_REQUIREMENTS_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_RANGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    accessibility_requirements: TopologyRequirement
    capacity_range: CapacityRange
    name: str
    parameters: _containers.ScalarMap[str, str]
    secrets: _containers.ScalarMap[str, str]
    volume_capabilities: _containers.RepeatedCompositeFieldContainer[VolumeCapability]
    volume_content_source: VolumeContentSource
    def __init__(self, name: _Optional[str] = ..., capacity_range: _Optional[_Union[CapacityRange, _Mapping]] = ..., volume_capabilities: _Optional[_Iterable[_Union[VolumeCapability, _Mapping]]] = ..., parameters: _Optional[_Mapping[str, str]] = ..., secrets: _Optional[_Mapping[str, str]] = ..., volume_content_source: _Optional[_Union[VolumeContentSource, _Mapping]] = ..., accessibility_requirements: _Optional[_Union[TopologyRequirement, _Mapping]] = ...) -> None: ...

class CreateVolumeResponse(_message.Message):
    __slots__ = ["volume"]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    volume: Volume
    def __init__(self, volume: _Optional[_Union[Volume, _Mapping]] = ...) -> None: ...

class DeleteSnapshotRequest(_message.Message):
    __slots__ = ["secrets", "snapshot_id"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    secrets: _containers.ScalarMap[str, str]
    snapshot_id: str
    def __init__(self, snapshot_id: _Optional[str] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteSnapshotResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class DeleteVolumeRequest(_message.Message):
    __slots__ = ["secrets", "volume_id"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    secrets: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class DeleteVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetCapacityRequest(_message.Message):
    __slots__ = ["accessible_topology", "parameters", "volume_capabilities"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCESSIBLE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    accessible_topology: Topology
    parameters: _containers.ScalarMap[str, str]
    volume_capabilities: _containers.RepeatedCompositeFieldContainer[VolumeCapability]
    def __init__(self, volume_capabilities: _Optional[_Iterable[_Union[VolumeCapability, _Mapping]]] = ..., parameters: _Optional[_Mapping[str, str]] = ..., accessible_topology: _Optional[_Union[Topology, _Mapping]] = ...) -> None: ...

class GetCapacityResponse(_message.Message):
    __slots__ = ["available_capacity", "maximum_volume_size", "minimum_volume_size"]
    AVAILABLE_CAPACITY_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_VOLUME_SIZE_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_VOLUME_SIZE_FIELD_NUMBER: _ClassVar[int]
    available_capacity: int
    maximum_volume_size: _wrappers_pb2.Int64Value
    minimum_volume_size: _wrappers_pb2.Int64Value
    def __init__(self, available_capacity: _Optional[int] = ..., maximum_volume_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., minimum_volume_size: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class GetPluginCapabilitiesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPluginCapabilitiesResponse(_message.Message):
    __slots__ = ["capabilities"]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedCompositeFieldContainer[PluginCapability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[PluginCapability, _Mapping]]] = ...) -> None: ...

class GetPluginInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetPluginInfoResponse(_message.Message):
    __slots__ = ["manifest", "name", "vendor_version"]
    class ManifestEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VENDOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    manifest: _containers.ScalarMap[str, str]
    name: str
    vendor_version: str
    def __init__(self, name: _Optional[str] = ..., vendor_version: _Optional[str] = ..., manifest: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListSnapshotsRequest(_message.Message):
    __slots__ = ["max_entries", "secrets", "snapshot_id", "source_volume_id", "starting_token"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    STARTING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    max_entries: int
    secrets: _containers.ScalarMap[str, str]
    snapshot_id: str
    source_volume_id: str
    starting_token: str
    def __init__(self, max_entries: _Optional[int] = ..., starting_token: _Optional[str] = ..., source_volume_id: _Optional[str] = ..., snapshot_id: _Optional[str] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ListSnapshotsResponse(_message.Message):
    __slots__ = ["entries", "next_token"]
    class Entry(_message.Message):
        __slots__ = ["snapshot"]
        SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
        snapshot: Snapshot
        def __init__(self, snapshot: _Optional[_Union[Snapshot, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[ListSnapshotsResponse.Entry]
    next_token: str
    def __init__(self, entries: _Optional[_Iterable[_Union[ListSnapshotsResponse.Entry, _Mapping]]] = ..., next_token: _Optional[str] = ...) -> None: ...

class ListVolumesRequest(_message.Message):
    __slots__ = ["max_entries", "starting_token"]
    MAX_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    STARTING_TOKEN_FIELD_NUMBER: _ClassVar[int]
    max_entries: int
    starting_token: str
    def __init__(self, max_entries: _Optional[int] = ..., starting_token: _Optional[str] = ...) -> None: ...

class ListVolumesResponse(_message.Message):
    __slots__ = ["entries", "next_token"]
    class Entry(_message.Message):
        __slots__ = ["status", "volume"]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        VOLUME_FIELD_NUMBER: _ClassVar[int]
        status: ListVolumesResponse.VolumeStatus
        volume: Volume
        def __init__(self, volume: _Optional[_Union[Volume, _Mapping]] = ..., status: _Optional[_Union[ListVolumesResponse.VolumeStatus, _Mapping]] = ...) -> None: ...
    class VolumeStatus(_message.Message):
        __slots__ = ["published_node_ids", "volume_condition"]
        PUBLISHED_NODE_IDS_FIELD_NUMBER: _ClassVar[int]
        VOLUME_CONDITION_FIELD_NUMBER: _ClassVar[int]
        published_node_ids: _containers.RepeatedScalarFieldContainer[str]
        volume_condition: VolumeCondition
        def __init__(self, published_node_ids: _Optional[_Iterable[str]] = ..., volume_condition: _Optional[_Union[VolumeCondition, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[ListVolumesResponse.Entry]
    next_token: str
    def __init__(self, entries: _Optional[_Iterable[_Union[ListVolumesResponse.Entry, _Mapping]]] = ..., next_token: _Optional[str] = ...) -> None: ...

class NodeExpandVolumeRequest(_message.Message):
    __slots__ = ["capacity_range", "secrets", "staging_target_path", "volume_capability", "volume_id", "volume_path"]
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CAPACITY_RANGE_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    STAGING_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
    capacity_range: CapacityRange
    secrets: _containers.ScalarMap[str, str]
    staging_target_path: str
    volume_capability: VolumeCapability
    volume_id: str
    volume_path: str
    def __init__(self, volume_id: _Optional[str] = ..., volume_path: _Optional[str] = ..., capacity_range: _Optional[_Union[CapacityRange, _Mapping]] = ..., staging_target_path: _Optional[str] = ..., volume_capability: _Optional[_Union[VolumeCapability, _Mapping]] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NodeExpandVolumeResponse(_message.Message):
    __slots__ = ["capacity_bytes"]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    capacity_bytes: int
    def __init__(self, capacity_bytes: _Optional[int] = ...) -> None: ...

class NodeGetCapabilitiesRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NodeGetCapabilitiesResponse(_message.Message):
    __slots__ = ["capabilities"]
    CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    capabilities: _containers.RepeatedCompositeFieldContainer[NodeServiceCapability]
    def __init__(self, capabilities: _Optional[_Iterable[_Union[NodeServiceCapability, _Mapping]]] = ...) -> None: ...

class NodeGetInfoRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NodeGetInfoResponse(_message.Message):
    __slots__ = ["accessible_topology", "max_volumes_per_node", "node_id"]
    ACCESSIBLE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    MAX_VOLUMES_PER_NODE_FIELD_NUMBER: _ClassVar[int]
    NODE_ID_FIELD_NUMBER: _ClassVar[int]
    accessible_topology: Topology
    max_volumes_per_node: int
    node_id: str
    def __init__(self, node_id: _Optional[str] = ..., max_volumes_per_node: _Optional[int] = ..., accessible_topology: _Optional[_Union[Topology, _Mapping]] = ...) -> None: ...

class NodeGetVolumeStatsRequest(_message.Message):
    __slots__ = ["staging_target_path", "volume_id", "volume_path"]
    STAGING_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    VOLUME_PATH_FIELD_NUMBER: _ClassVar[int]
    staging_target_path: str
    volume_id: str
    volume_path: str
    def __init__(self, volume_id: _Optional[str] = ..., volume_path: _Optional[str] = ..., staging_target_path: _Optional[str] = ...) -> None: ...

class NodeGetVolumeStatsResponse(_message.Message):
    __slots__ = ["usage", "volume_condition"]
    USAGE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONDITION_FIELD_NUMBER: _ClassVar[int]
    usage: _containers.RepeatedCompositeFieldContainer[VolumeUsage]
    volume_condition: VolumeCondition
    def __init__(self, usage: _Optional[_Iterable[_Union[VolumeUsage, _Mapping]]] = ..., volume_condition: _Optional[_Union[VolumeCondition, _Mapping]] = ...) -> None: ...

class NodePublishVolumeRequest(_message.Message):
    __slots__ = ["publish_context", "readonly", "secrets", "staging_target_path", "target_path", "volume_capability", "volume_context", "volume_id"]
    class PublishContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VolumeContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PUBLISH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    READONLY_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    STAGING_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    publish_context: _containers.ScalarMap[str, str]
    readonly: bool
    secrets: _containers.ScalarMap[str, str]
    staging_target_path: str
    target_path: str
    volume_capability: VolumeCapability
    volume_context: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., publish_context: _Optional[_Mapping[str, str]] = ..., staging_target_path: _Optional[str] = ..., target_path: _Optional[str] = ..., volume_capability: _Optional[_Union[VolumeCapability, _Mapping]] = ..., readonly: bool = ..., secrets: _Optional[_Mapping[str, str]] = ..., volume_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NodePublishVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NodeServiceCapability(_message.Message):
    __slots__ = ["rpc"]
    class RPC(_message.Message):
        __slots__ = ["type"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        EXPAND_VOLUME: NodeServiceCapability.RPC.Type
        GET_VOLUME_STATS: NodeServiceCapability.RPC.Type
        SINGLE_NODE_MULTI_WRITER: NodeServiceCapability.RPC.Type
        STAGE_UNSTAGE_VOLUME: NodeServiceCapability.RPC.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: NodeServiceCapability.RPC.Type
        VOLUME_CONDITION: NodeServiceCapability.RPC.Type
        VOLUME_MOUNT_GROUP: NodeServiceCapability.RPC.Type
        type: NodeServiceCapability.RPC.Type
        def __init__(self, type: _Optional[_Union[NodeServiceCapability.RPC.Type, str]] = ...) -> None: ...
    RPC_FIELD_NUMBER: _ClassVar[int]
    rpc: NodeServiceCapability.RPC
    def __init__(self, rpc: _Optional[_Union[NodeServiceCapability.RPC, _Mapping]] = ...) -> None: ...

class NodeStageVolumeRequest(_message.Message):
    __slots__ = ["publish_context", "secrets", "staging_target_path", "volume_capability", "volume_context", "volume_id"]
    class PublishContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VolumeContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PUBLISH_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    STAGING_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITY_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    publish_context: _containers.ScalarMap[str, str]
    secrets: _containers.ScalarMap[str, str]
    staging_target_path: str
    volume_capability: VolumeCapability
    volume_context: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., publish_context: _Optional[_Mapping[str, str]] = ..., staging_target_path: _Optional[str] = ..., volume_capability: _Optional[_Union[VolumeCapability, _Mapping]] = ..., secrets: _Optional[_Mapping[str, str]] = ..., volume_context: _Optional[_Mapping[str, str]] = ...) -> None: ...

class NodeStageVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NodeUnpublishVolumeRequest(_message.Message):
    __slots__ = ["target_path", "volume_id"]
    TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    target_path: str
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., target_path: _Optional[str] = ...) -> None: ...

class NodeUnpublishVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class NodeUnstageVolumeRequest(_message.Message):
    __slots__ = ["staging_target_path", "volume_id"]
    STAGING_TARGET_PATH_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    staging_target_path: str
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., staging_target_path: _Optional[str] = ...) -> None: ...

class NodeUnstageVolumeResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PluginCapability(_message.Message):
    __slots__ = ["service", "volume_expansion"]
    class Service(_message.Message):
        __slots__ = ["type"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        CONTROLLER_SERVICE: PluginCapability.Service.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: PluginCapability.Service.Type
        VOLUME_ACCESSIBILITY_CONSTRAINTS: PluginCapability.Service.Type
        type: PluginCapability.Service.Type
        def __init__(self, type: _Optional[_Union[PluginCapability.Service.Type, str]] = ...) -> None: ...
    class VolumeExpansion(_message.Message):
        __slots__ = ["type"]
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        OFFLINE: PluginCapability.VolumeExpansion.Type
        ONLINE: PluginCapability.VolumeExpansion.Type
        TYPE_FIELD_NUMBER: _ClassVar[int]
        UNKNOWN: PluginCapability.VolumeExpansion.Type
        type: PluginCapability.VolumeExpansion.Type
        def __init__(self, type: _Optional[_Union[PluginCapability.VolumeExpansion.Type, str]] = ...) -> None: ...
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_EXPANSION_FIELD_NUMBER: _ClassVar[int]
    service: PluginCapability.Service
    volume_expansion: PluginCapability.VolumeExpansion
    def __init__(self, service: _Optional[_Union[PluginCapability.Service, _Mapping]] = ..., volume_expansion: _Optional[_Union[PluginCapability.VolumeExpansion, _Mapping]] = ...) -> None: ...

class ProbeRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ProbeResponse(_message.Message):
    __slots__ = ["ready"]
    READY_FIELD_NUMBER: _ClassVar[int]
    ready: _wrappers_pb2.BoolValue
    def __init__(self, ready: _Optional[_Union[_wrappers_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ["creation_time", "ready_to_use", "size_bytes", "snapshot_id", "source_volume_id"]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    READY_TO_USE_FIELD_NUMBER: _ClassVar[int]
    SIZE_BYTES_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    creation_time: _timestamp_pb2.Timestamp
    ready_to_use: bool
    size_bytes: int
    snapshot_id: str
    source_volume_id: str
    def __init__(self, size_bytes: _Optional[int] = ..., snapshot_id: _Optional[str] = ..., source_volume_id: _Optional[str] = ..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., ready_to_use: bool = ...) -> None: ...

class Topology(_message.Message):
    __slots__ = ["segments"]
    class SegmentsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.ScalarMap[str, str]
    def __init__(self, segments: _Optional[_Mapping[str, str]] = ...) -> None: ...

class TopologyRequirement(_message.Message):
    __slots__ = ["preferred", "requisite"]
    PREFERRED_FIELD_NUMBER: _ClassVar[int]
    REQUISITE_FIELD_NUMBER: _ClassVar[int]
    preferred: _containers.RepeatedCompositeFieldContainer[Topology]
    requisite: _containers.RepeatedCompositeFieldContainer[Topology]
    def __init__(self, requisite: _Optional[_Iterable[_Union[Topology, _Mapping]]] = ..., preferred: _Optional[_Iterable[_Union[Topology, _Mapping]]] = ...) -> None: ...

class ValidateVolumeCapabilitiesRequest(_message.Message):
    __slots__ = ["parameters", "secrets", "volume_capabilities", "volume_context", "volume_id"]
    class ParametersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class SecretsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class VolumeContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    SECRETS_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    parameters: _containers.ScalarMap[str, str]
    secrets: _containers.ScalarMap[str, str]
    volume_capabilities: _containers.RepeatedCompositeFieldContainer[VolumeCapability]
    volume_context: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, volume_id: _Optional[str] = ..., volume_context: _Optional[_Mapping[str, str]] = ..., volume_capabilities: _Optional[_Iterable[_Union[VolumeCapability, _Mapping]]] = ..., parameters: _Optional[_Mapping[str, str]] = ..., secrets: _Optional[_Mapping[str, str]] = ...) -> None: ...

class ValidateVolumeCapabilitiesResponse(_message.Message):
    __slots__ = ["confirmed", "message"]
    class Confirmed(_message.Message):
        __slots__ = ["parameters", "volume_capabilities", "volume_context"]
        class ParametersEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        class VolumeContextEntry(_message.Message):
            __slots__ = ["key", "value"]
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str
            def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
        PARAMETERS_FIELD_NUMBER: _ClassVar[int]
        VOLUME_CAPABILITIES_FIELD_NUMBER: _ClassVar[int]
        VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
        parameters: _containers.ScalarMap[str, str]
        volume_capabilities: _containers.RepeatedCompositeFieldContainer[VolumeCapability]
        volume_context: _containers.ScalarMap[str, str]
        def __init__(self, volume_context: _Optional[_Mapping[str, str]] = ..., volume_capabilities: _Optional[_Iterable[_Union[VolumeCapability, _Mapping]]] = ..., parameters: _Optional[_Mapping[str, str]] = ...) -> None: ...
    CONFIRMED_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    confirmed: ValidateVolumeCapabilitiesResponse.Confirmed
    message: str
    def __init__(self, confirmed: _Optional[_Union[ValidateVolumeCapabilitiesResponse.Confirmed, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class Volume(_message.Message):
    __slots__ = ["accessible_topology", "capacity_bytes", "content_source", "volume_context", "volume_id"]
    class VolumeContextEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ACCESSIBLE_TOPOLOGY_FIELD_NUMBER: _ClassVar[int]
    CAPACITY_BYTES_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
    accessible_topology: _containers.RepeatedCompositeFieldContainer[Topology]
    capacity_bytes: int
    content_source: VolumeContentSource
    volume_context: _containers.ScalarMap[str, str]
    volume_id: str
    def __init__(self, capacity_bytes: _Optional[int] = ..., volume_id: _Optional[str] = ..., volume_context: _Optional[_Mapping[str, str]] = ..., content_source: _Optional[_Union[VolumeContentSource, _Mapping]] = ..., accessible_topology: _Optional[_Iterable[_Union[Topology, _Mapping]]] = ...) -> None: ...

class VolumeCapability(_message.Message):
    __slots__ = ["access_mode", "block", "mount"]
    class AccessMode(_message.Message):
        __slots__ = ["mode"]
        class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = []
        MODE_FIELD_NUMBER: _ClassVar[int]
        MULTI_NODE_MULTI_WRITER: VolumeCapability.AccessMode.Mode
        MULTI_NODE_READER_ONLY: VolumeCapability.AccessMode.Mode
        MULTI_NODE_SINGLE_WRITER: VolumeCapability.AccessMode.Mode
        SINGLE_NODE_MULTI_WRITER: VolumeCapability.AccessMode.Mode
        SINGLE_NODE_READER_ONLY: VolumeCapability.AccessMode.Mode
        SINGLE_NODE_SINGLE_WRITER: VolumeCapability.AccessMode.Mode
        SINGLE_NODE_WRITER: VolumeCapability.AccessMode.Mode
        UNKNOWN: VolumeCapability.AccessMode.Mode
        mode: VolumeCapability.AccessMode.Mode
        def __init__(self, mode: _Optional[_Union[VolumeCapability.AccessMode.Mode, str]] = ...) -> None: ...
    class BlockVolume(_message.Message):
        __slots__ = []
        def __init__(self) -> None: ...
    class MountVolume(_message.Message):
        __slots__ = ["fs_type", "mount_flags", "volume_mount_group"]
        FS_TYPE_FIELD_NUMBER: _ClassVar[int]
        MOUNT_FLAGS_FIELD_NUMBER: _ClassVar[int]
        VOLUME_MOUNT_GROUP_FIELD_NUMBER: _ClassVar[int]
        fs_type: str
        mount_flags: _containers.RepeatedScalarFieldContainer[str]
        volume_mount_group: str
        def __init__(self, fs_type: _Optional[str] = ..., mount_flags: _Optional[_Iterable[str]] = ..., volume_mount_group: _Optional[str] = ...) -> None: ...
    ACCESS_MODE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_FIELD_NUMBER: _ClassVar[int]
    MOUNT_FIELD_NUMBER: _ClassVar[int]
    access_mode: VolumeCapability.AccessMode
    block: VolumeCapability.BlockVolume
    mount: VolumeCapability.MountVolume
    def __init__(self, block: _Optional[_Union[VolumeCapability.BlockVolume, _Mapping]] = ..., mount: _Optional[_Union[VolumeCapability.MountVolume, _Mapping]] = ..., access_mode: _Optional[_Union[VolumeCapability.AccessMode, _Mapping]] = ...) -> None: ...

class VolumeCondition(_message.Message):
    __slots__ = ["abnormal", "message"]
    ABNORMAL_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    abnormal: bool
    message: str
    def __init__(self, abnormal: bool = ..., message: _Optional[str] = ...) -> None: ...

class VolumeContentSource(_message.Message):
    __slots__ = ["snapshot", "volume"]
    class SnapshotSource(_message.Message):
        __slots__ = ["snapshot_id"]
        SNAPSHOT_ID_FIELD_NUMBER: _ClassVar[int]
        snapshot_id: str
        def __init__(self, snapshot_id: _Optional[str] = ...) -> None: ...
    class VolumeSource(_message.Message):
        __slots__ = ["volume_id"]
        VOLUME_ID_FIELD_NUMBER: _ClassVar[int]
        volume_id: str
        def __init__(self, volume_id: _Optional[str] = ...) -> None: ...
    SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    snapshot: VolumeContentSource.SnapshotSource
    volume: VolumeContentSource.VolumeSource
    def __init__(self, snapshot: _Optional[_Union[VolumeContentSource.SnapshotSource, _Mapping]] = ..., volume: _Optional[_Union[VolumeContentSource.VolumeSource, _Mapping]] = ...) -> None: ...

class VolumeUsage(_message.Message):
    __slots__ = ["available", "total", "unit", "used"]
    class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    BYTES: VolumeUsage.Unit
    INODES: VolumeUsage.Unit
    TOTAL_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    UNKNOWN: VolumeUsage.Unit
    USED_FIELD_NUMBER: _ClassVar[int]
    available: int
    total: int
    unit: VolumeUsage.Unit
    used: int
    def __init__(self, available: _Optional[int] = ..., total: _Optional[int] = ..., used: _Optional[int] = ..., unit: _Optional[_Union[VolumeUsage.Unit, str]] = ...) -> None: ...
