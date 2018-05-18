---
title: CIM\_StorageReplicationCapabilities class
description: This subclass defines the replication capabilities of a StorageConfigurationService.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5c3860c1-44b9-4825-ad5f-f6180dc1d722'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_StorageReplicationCapabilities class iSCSI Software Target API", "CIM_StorageReplicationCapabilities class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- CIM_StorageReplicationCapabilities
- CIM_StorageReplicationCapabilities.Caption
- CIM_StorageReplicationCapabilities.Description
- CIM_StorageReplicationCapabilities.InstanceID
- CIM_StorageReplicationCapabilities.ElementName
- CIM_StorageReplicationCapabilities.SupportedSynchronizationType
- CIM_StorageReplicationCapabilities.SupportedAsynchronousActions
- CIM_StorageReplicationCapabilities.SupportedSynchronousActions
- CIM_StorageReplicationCapabilities.InitialReplicationState
- CIM_StorageReplicationCapabilities.SupportedSpecializedElements
- CIM_StorageReplicationCapabilities.SupportedModifyOperations
- CIM_StorageReplicationCapabilities.ReplicaHostAccessibility
- CIM_StorageReplicationCapabilities.HostAccessibleState
- CIM_StorageReplicationCapabilities.SpaceLimitSupported
- CIM_StorageReplicationCapabilities.SpaceReservationSupported
- CIM_StorageReplicationCapabilities.LocalMirrorSnapshotSupported
- CIM_StorageReplicationCapabilities.RemoteMirrorSnapshotSupported
- CIM_StorageReplicationCapabilities.IncrementalDeltasSupported
- CIM_StorageReplicationCapabilities.PersistentReplicasSupported
- CIM_StorageReplicationCapabilities.BidirectionalConnectionsSupported
- CIM_StorageReplicationCapabilities.MaximumReplicasPerSource
- CIM_StorageReplicationCapabilities.MaximumPortsPerConnection
- CIM_StorageReplicationCapabilities.MaximumConnectionsPerPort
- CIM_StorageReplicationCapabilities.MaximumPeerConnections
- CIM_StorageReplicationCapabilities.MaximumLocalReplicationDepth
- CIM_StorageReplicationCapabilities.MaximumRemoteReplicationDepth
- CIM_StorageReplicationCapabilities.InitialSynchronizationDefault
- CIM_StorageReplicationCapabilities.ReplicationPriorityDefault
- CIM_StorageReplicationCapabilities.LowSpaceWarningThresholdDefault
- CIM_StorageReplicationCapabilities.SpaceLimitWarningThresholdDefault
- CIM_StorageReplicationCapabilities.RemoteReplicationServicePointAccess
- CIM_StorageReplicationCapabilities.AlternateReplicationServicePointAccess
- CIM_StorageReplicationCapabilities.DeltaReplicaPoolAccess
- CIM_StorageReplicationCapabilities.RemoteBufferElementType
- CIM_StorageReplicationCapabilities.RemoteBufferHost
- CIM_StorageReplicationCapabilities.RemoteBufferLocation
- CIM_StorageReplicationCapabilities.RemoteBufferSupported
- CIM_StorageReplicationCapabilities.UseReplicationBufferDefault
- CIM_StorageReplicationCapabilities.PeerConnectionProtocol
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# CIM\_StorageReplicationCapabilities class

This subclass defines the replication capabilities of a StorageConfigurationService. Multiple instances of StorageReplicationCapabilities may be associated with a StorageConfigurationService using ElementCapabilities. A provider should create one instance for each supported SynchronizationType.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("2.10.0"), UMLPackagePath("CIM::Device::StorageServices")]
class CIM_StorageReplicationCapabilities : CIM_Capabilities
{
  string  Caption;
  string  Description;
  string  InstanceID;
  string  ElementName;
  uint16  SupportedSynchronizationType;
  uint16  SupportedAsynchronousActions[];
  uint16  SupportedSynchronousActions[];
  uint16  InitialReplicationState;
  uint16  SupportedSpecializedElements[];
  uint16  SupportedModifyOperations[];
  uint16  ReplicaHostAccessibility;
  uint16  HostAccessibleState[];
  boolean SpaceLimitSupported;
  boolean SpaceReservationSupported;
  boolean LocalMirrorSnapshotSupported;
  boolean RemoteMirrorSnapshotSupported;
  boolean IncrementalDeltasSupported;
  boolean PersistentReplicasSupported;
  boolean BidirectionalConnectionsSupported;
  uint16  MaximumReplicasPerSource;
  uint16  MaximumPortsPerConnection;
  uint16  MaximumConnectionsPerPort;
  uint16  MaximumPeerConnections;
  uint16  MaximumLocalReplicationDepth = 1;
  uint16  MaximumRemoteReplicationDepth = 1;
  uint16  InitialSynchronizationDefault;
  uint16  ReplicationPriorityDefault;
  uint8   LowSpaceWarningThresholdDefault;
  uint8   SpaceLimitWarningThresholdDefault;
  uint16  RemoteReplicationServicePointAccess;
  uint16  AlternateReplicationServicePointAccess;
  uint16  DeltaReplicaPoolAccess;
  uint16  RemoteBufferElementType;
  uint16  RemoteBufferHost;
  uint16  RemoteBufferLocation;
  uint16  RemoteBufferSupported;
  uint16  UseReplicationBufferDefault;
  string  PeerConnectionProtocol;
};
```

## Members

The **CIM\_StorageReplicationCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_StorageReplicationCapabilities** class has these properties.

<dl> <dt>

**AlternateReplicationServicePointAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote replication provides StorageConfigurationService instances for source systems and target systems. A client determines that extrinsic methods of the service should be invoked to one instance or the other based on the value of this property. If the primary instance is unavailable, the provider may indicate an alternate instance. Values: None: no alternate exists. Source: invoke to source element service instance. Target: invoke to target element service instance. Proxy: find and invoke alternate proxy service instance.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>

**Source** (3)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (4)


</dt> <dd></dd> <dt>

<span id="Proxy"></span><span id="proxy"></span><span id="PROXY"></span>

**Proxy** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**BidirectionalConnectionsSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates peer-to-peer connections are bi-directional. False indicates connections are uni-directional.

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**DeltaReplicaPoolAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DeltaReplicaPool indicates that a specialized pool is required as a container for delta replica elements. Values: Any: delta replicas can be created in any pool. Exclusive: one specialized, exclusive pool must be created for each source element that has associated delta replicas. Shared: one specialized, shared pool must be created to be shared by all source elements with associated delta replicas.

<dt>

<span id="Any"></span><span id="any"></span><span id="ANY"></span>

**Any** (2)


</dt> <dd></dd> <dt>

<span id="Exclusive"></span><span id="exclusive"></span><span id="EXCLUSIVE"></span>

**Exclusive** (3)


</dt> <dd></dd> <dt>

<span id="Shared"></span><span id="shared"></span><span id="SHARED"></span>

**Shared** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains a textual description of the object.

This property is inherited from [**CIM\_ManagedElement**](cim-managedelement.md).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**HostAccessibleState**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSynchronized.SyncState")
</dt> </dl>

Lists the replica synchronization states in which the provider allows host access to replicas. Accessibility does not guarantee replica contents are valid or consistent.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Prepare_In_Progress"></span><span id="prepare_in_progress"></span><span id="PREPARE_IN_PROGRESS"></span>

**Prepare In Progress** (3)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (4)


</dt> <dd></dd> <dt>

<span id="Resync_In_Progress"></span><span id="resync_in_progress"></span><span id="RESYNC_IN_PROGRESS"></span>

**Resync In Progress** (5)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (6)


</dt> <dd></dd> <dt>

<span id="Fracture_In_Progress"></span><span id="fracture_in_progress"></span><span id="FRACTURE_IN_PROGRESS"></span>

**Fracture In Progress** (7)


</dt> <dd></dd> <dt>

<span id="Quiesce_In_Progress"></span><span id="quiesce_in_progress"></span><span id="QUIESCE_IN_PROGRESS"></span>

**Quiesce In Progress** (8)


</dt> <dd></dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

**Quiesced** (9)


</dt> <dd></dd> <dt>

<span id="Restore_In_Progress"></span><span id="restore_in_progress"></span><span id="RESTORE_IN_PROGRESS"></span>

**Restore In Progress** (10)


</dt> <dd></dd> <dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

**Idle** (11)


</dt> <dd></dd> <dt>

<span id="Broken"></span><span id="broken"></span><span id="BROKEN"></span>

**Broken** (12)


</dt> <dd></dd> <dt>

<span id="Fractured"></span><span id="fractured"></span><span id="FRACTURED"></span>

**Fractured** (13)


</dt> <dd></dd> <dt>

<span id="Frozen"></span><span id="frozen"></span><span id="FROZEN"></span>

**Frozen** (14)


</dt> <dd></dd> <dt>

<span id="Copy_In_Progress"></span><span id="copy_in_progress"></span><span id="COPY_IN_PROGRESS"></span>

**Copy In Progress** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**IncrementalDeltasSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates all delta replicas associated with the same source element can be incrementally dependent. Only the oldest replica in the set may be deleted or resynced.

</dd> <dt>

**InitialReplicationState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.AttachReplica", "CIM\_StorageConfigurationService.AttachOrModifyReplica", "CIM\_StorageConfigurationService.CreateReplica")
</dt> </dl>

InitialReplicationState specifies which initial ReplicationState is supported by a particular provider. Values are:

Initialized: The replication relationship is known and unsynchronized, but time required to synchronize may be long.

Prepared: The replication relationship is known and unsynchronized and the time required to synchronize will be short.

Synchronized: The replicas are synchronized.Idle: an UnSyncAssoc replica is ready to manage.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** (2)


</dt> <dd></dd> <dt>

<span id="Prepared"></span><span id="prepared"></span><span id="PREPARED"></span>

**Prepared** (3)


</dt> <dd></dd> <dt>

<span id="Synchronized"></span><span id="synchronized"></span><span id="SYNCHRONIZED"></span>

**Synchronized** (4)


</dt> <dd></dd> <dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

**Idle** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**InitialSynchronizationDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.InitialSynchronization")
</dt> </dl>

Start or do not start background copy when replica is created.

<dt>

<span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span>

**Not Managed** (0)


</dt> <dd></dd> <dt>

<span id="Start"></span><span id="start"></span><span id="START"></span>

**Start** (1)


</dt> <dd></dd> <dt>

<span id="Do_Not_Start"></span><span id="do_not_start"></span><span id="DO_NOT_START"></span>

**Do Not Start** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: &lt;OrgID&gt;:&lt;LocalID&gt; Where &lt;OrgID&gt; and &lt;LocalID&gt; are separated by a colon ':', and where &lt;OrgID&gt; MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the &lt;Schema Name&gt;\_&lt;Class Name&gt; structure of Schema class names.) In addition, to ensure uniqueness &lt;OrgID&gt; MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between &lt;OrgID&gt; and &lt;LocalID&gt;. &lt;LocalID&gt; is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. For DMTF defined instances, the 'preferred' algorithm MUST be used with the &lt;OrgID&gt; set to 'CIM'.

This property is inherited from [**CIM\_Capabilities**](cim-capabilities.md).

</dd> <dt>

**LocalMirrorSnapshotSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates local mirror can be snapshot source.

</dd> <dt>

**LowSpaceWarningThresholdDefault**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StoragePool.LowSpaceWarningThreshold"), **PUnit** ("percent")
</dt> </dl>

Warning threshold for generating an indication for RemainingManagedSpace. Value of zero means no warning generated.Triggered when RemainingManagedSpace &lt;= (TotalManagedSpace\*LowSpaceWarningThreshold)/100.

</dd> <dt>

**MaximumConnectionsPerPort**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of peer-to-peer connections to which a port maybe assigned.

</dd> <dt>

**MaximumLocalReplicationDepth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum local mirror replication depth allowed by this instance of StorageConfigurationService. Value 1 indicates multi-level replication not supported.

</dd> <dt>

**MaximumPeerConnections**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of peer connections supported by this instance of StorageConfigurationService.

</dd> <dt>

**MaximumPortsPerConnection**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of port pairs assigned to a peer-to-peer connection.

</dd> <dt>

**MaximumRemoteReplicationDepth**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum remote mirror replication depth allowed by this instance of StorageConfigurationService. Value N means that remote replicas can span N linked peer-to-peer connections. Value 1 indicates multi-level replication not supported.

</dd> <dt>

**MaximumReplicasPerSource**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum number of replicas that can be associated with one source element.

</dd> <dt>

**PeerConnectionProtocol**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Peer connection protocol is a private, vendor-specific protocol for replication data transport. A client verifies that two peers support the same protocol before establishing a peer-to-peer connection.

</dd> <dt>

**PersistentReplicasSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates replicas can persist during power off or system reset. False indicates replicas lost during these events.

</dd> <dt>

**RemoteBufferElementType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote replication buffer elements are instances of CIM\_Memory. A buffer element may be created from a component extent with a BasedOn association or in a storage pool with an AllocatedFromStoragePool association. The provider can also make the size and element type opaque to a client. Values:

Not specified: client allows provider to determine size and container element type.

InExtent: buffer must be created from passed component extent.

InPool: buffer must be created in passed pool.

<dt>

<span id="Not_specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

**Not specified** (0)


</dt> <dd></dd> <dt>

<span id="InExtent"></span><span id="inextent"></span><span id="INEXTENT"></span>

**InExtent** (2)


</dt> <dd></dd> <dt>

<span id="InPool"></span><span id="inpool"></span><span id="INPOOL"></span>

**InPool** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**RemoteBufferHost**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array provider may require multiple buffer elements per array instance as indicated by this property. Values:

Array: one buffer element for the entire array.

ComponentCS: one buffer element per ComputerSystem element in a clustered array.

Pipe: one or two buffer elements per replication pipe.

<dt>

<span id="Array"></span><span id="array"></span><span id="ARRAY"></span>

**Array** (2)


</dt> <dd></dd> <dt>

<span id="ComponentCS"></span><span id="componentcs"></span><span id="COMPONENTCS"></span>

**ComponentCS** (3)


</dt> <dd></dd> <dt>

<span id="Pipe"></span><span id="pipe"></span><span id="PIPE"></span>

**Pipe** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**RemoteBufferLocation**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property allows the provider to indicate the required location for remote buffer elements. Values:

Source: buffer needed only on platforms hosting source elements.

Target: buffer needed only on platforms hosting target elements.

Both: buffers needed for both source and target platforms.

<dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>

**Source** (2)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (3)


</dt> <dd></dd> <dt>

<span id="Both"></span><span id="both"></span><span id="BOTH"></span>

**Both** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**RemoteBufferSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Peer may require a write buffer for remote replica elements with async I/O buffering. Typically used to increase remote mirror replication engine performance while maintaining high availability. Values:

Required: must have buffer if any Async remote replicas are created.

Optional: may have buffer if any Async remote replicas are created.

<dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

**Not Supported** (0)


</dt> <dd></dd> <dt>

<span id="Required"></span><span id="required"></span><span id="REQUIRED"></span>

**Required** (2)


</dt> <dd></dd> <dt>

<span id="Optional"></span><span id="optional"></span><span id="OPTIONAL"></span>

**Optional** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**RemoteMirrorSnapshotSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates remote mirror can be snapshot source.

</dd> <dt>

**RemoteReplicationServicePointAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote replication provides StorageConfigurationService instances for source systems and target systems. A client determines that extrinsic methods of the service should be invoked to one instance or the other based on the value of this property. Values: Not Specified: invoke a method to either system instance. Source: invoke to source element service instance. Target: invoke to target element service instance. Proxy: find and invoke to proxy service instance.

<dt>

<span id="Not_Specified"></span><span id="not_specified"></span><span id="NOT_SPECIFIED"></span>

**Not Specified** (2)


</dt> <dd></dd> <dt>

<span id="Source"></span><span id="source"></span><span id="SOURCE"></span>

**Source** (3)


</dt> <dd></dd> <dt>

<span id="Target"></span><span id="target"></span><span id="TARGET"></span>

**Target** (4)


</dt> <dd></dd> <dt>

<span id="Proxy"></span><span id="proxy"></span><span id="PROXY"></span>

**Proxy** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**ReplicaHostAccessibility**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates host access restrictions for replicas with thesecapabilities. Values: 2 = not accessible.

3 = no restrictions. Any host may access. 4 = only accessible by associated source element hosts. 5 = not accessible by source element hosts. Other hosts OK.

<dt>

<span id="Not_Accessible"></span><span id="not_accessible"></span><span id="NOT_ACCESSIBLE"></span>

**Not Accessible** (2)


</dt> <dd></dd> <dt>

<span id="No_Restrictions"></span><span id="no_restrictions"></span><span id="NO_RESTRICTIONS"></span>

**No Restrictions** (3)


</dt> <dd></dd> <dt>

<span id="Source_Hosts_Only"></span><span id="source_hosts_only"></span><span id="SOURCE_HOSTS_ONLY"></span>

**Source Hosts Only** (4)


</dt> <dd></dd> <dt>

<span id="Source_Hosts_Excluded"></span><span id="source_hosts_excluded"></span><span id="SOURCE_HOSTS_EXCLUDED"></span>

**Source Hosts Excluded** (5)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>6–65535</dd> </dl>

</dd> <dt>

**ReplicationPriorityDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.ReplicationPriority")
</dt> </dl>

ReplicationPriority allows the priority of background Replication I/O to be managed relative to host I/O. Default applies to initial or deferred background Replication operations. Value can be modified while in Replication-in-progress state. Values: Low: Replication engine I/O lower priority than host I/O.

Same: Replication engine I/O has the same priority as host I/O.

High: Replication engine I/O has higher priority than host I/O.

<dt>

<span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span>

**Not Managed** (0)


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** (1)


</dt> <dd></dd> <dt>

<span id="Same"></span><span id="same"></span><span id="SAME"></span>

**Same** (2)


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SpaceLimitSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AllocatedFromStoragePool.SpaceLimit")
</dt> </dl>

True indicates space limits on allocation from StoragePools may be enforced.

</dd> <dt>

**SpaceLimitWarningThresholdDefault**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Percentage"), [**MinValue**](https://msdn.microsoft.com/library/aa393650) (0), [**MaxValue**](https://msdn.microsoft.com/library/aa393650) (100), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_AllocatedFromStoragePool.SpaceLimitWarningThreshold"), **PUnit** ("percent")
</dt> </dl>

Warning threshold for instance modification indication for SpaceConsumed by a replica element. Value of zero means no warning generated. Triggered when SpaceConsumed &gt;= (SpaceLimit\*SpaceLimitWarningThreshold)/100.

</dd> <dt>

**SpaceReservationSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

True indicates space reserved for replicas can be from a specialized pool.

</dd> <dt>

**SupportedAsynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageReplicationCapabilities.SupportedSynchronousActions")
</dt> </dl>

Enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and SupportedSynchronousActions then the underlying implementation is indicating that it may or may not create a job.

<dt>

<span id="Local_Replica_Creation"></span><span id="local_replica_creation"></span><span id="LOCAL_REPLICA_CREATION"></span>

**Local Replica Creation** (2)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Creation"></span><span id="remote_replica_creation"></span><span id="REMOTE_REPLICA_CREATION"></span>

**Remote Replica Creation** (3)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Modification"></span><span id="local_replica_modification"></span><span id="LOCAL_REPLICA_MODIFICATION"></span>

**Local Replica Modification** (4)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Modification"></span><span id="remote_replica_modification"></span><span id="REMOTE_REPLICA_MODIFICATION"></span>

**Remote Replica Modification** (5)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Attachment"></span><span id="local_replica_attachment"></span><span id="LOCAL_REPLICA_ATTACHMENT"></span>

**Local Replica Attachment** (6)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Attachment"></span><span id="remote_replica_attachment"></span><span id="REMOTE_REPLICA_ATTACHMENT"></span>

**Remote Replica Attachment** (7)


</dt> <dd></dd> <dt>

<span id="Buffer_Creation"></span><span id="buffer_creation"></span><span id="BUFFER_CREATION"></span>

**Buffer Creation** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–65535</dd> </dl>

</dd> <dt>

**SupportedModifyOperations**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageConfigurationService.ModifySynchronization")
</dt> </dl>

Enumeration indicating which ModifySynchronization operations are supported by this instance of StorageReplicationCapabilities.

<dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

**Detach** (2)


</dt> <dd></dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

**Fracture** (3)


</dt> <dd></dd> <dt>

<span id="Resync"></span><span id="resync"></span><span id="RESYNC"></span>

**Resync** (4)


</dt> <dd></dd> <dt>

<span id="Restore"></span><span id="restore"></span><span id="RESTORE"></span>

**Restore** (5)


</dt> <dd></dd> <dt>

<span id="Prepare"></span><span id="prepare"></span><span id="PREPARE"></span>

**Prepare** (6)


</dt> <dd></dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

**Unprepare** (7)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (8)


</dt> <dd></dd> <dt>

<span id="Unquiesce"></span><span id="unquiesce"></span><span id="UNQUIESCE"></span>

**Unquiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

**Reset To Sync** (10)


</dt> <dd></dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

**Reset To Async** (11)


</dt> <dd></dd> <dt>

<span id="Start_Copy"></span><span id="start_copy"></span><span id="START_COPY"></span>

**Start Copy** (12)


</dt> <dd></dd> <dt>

<span id="Stop_Copy"></span><span id="stop_copy"></span><span id="STOP_COPY"></span>

**Stop Copy** (13)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportedSpecializedElements**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.IntendedUsage")
</dt> </dl>

Enumeration indicating which specialized storage element types are supported by this instance of StorageReplicationCapabilities. Specialized types are indicated by the value of the IntendedUsage in StorageSetting.

<dt>

<span id="Delta_Pool"></span><span id="delta_pool"></span><span id="DELTA_POOL"></span>

**Delta Pool** (2)


</dt> <dd></dd> <dt>

<span id="Delta_Pool_Component"></span><span id="delta_pool_component"></span><span id="DELTA_POOL_COMPONENT"></span>

**Delta Pool Component** (3)


</dt> <dd></dd> <dt>

<span id="Remote_Mirror"></span><span id="remote_mirror"></span><span id="REMOTE_MIRROR"></span>

**Remote Mirror** (4)


</dt> <dd></dd> <dt>

<span id="Local_Mirror"></span><span id="local_mirror"></span><span id="LOCAL_MIRROR"></span>

**Local Mirror** (5)


</dt> <dd></dd> <dt>

<span id="Full_Snapshot"></span><span id="full_snapshot"></span><span id="FULL_SNAPSHOT"></span>

**Full Snapshot** (6)


</dt> <dd></dd> <dt>

<span id="Delta_Snapshot"></span><span id="delta_snapshot"></span><span id="DELTA_SNAPSHOT"></span>

**Delta Snapshot** (7)


</dt> <dd></dd> <dt>

<span id="Replication_Buffer"></span><span id="replication_buffer"></span><span id="REPLICATION_BUFFER"></span>

**Replication Buffer** (8)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>9–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportedSynchronizationType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

SupportedSynchronizationType describes the type of Synchronization that is characterized by this instance of StorageReplicationCapabilities. Values are:

Async: create a mirror that is nearly always synchronized. Sync: create a mirror that is always synchronized.

UnSyncAssocFull: create a full size snapshot (Point In Time image).

UnSyncAssocDelta: create a delta snapshot (Point In Time image).

UnSyncUnAssoc: create a full size, independent replica.

<dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> <dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (3)


</dt> <dd></dd> <dt>

<span id="UnSyncAssoc-Full"></span><span id="unsyncassoc-full"></span><span id="UNSYNCASSOC-FULL"></span>

**UnSyncAssoc-Full** (4)


</dt> <dd></dd> <dt>

<span id="UnSyncAssoc-Delta"></span><span id="unsyncassoc-delta"></span><span id="UNSYNCASSOC-DELTA"></span>

**UnSyncAssoc-Delta** (5)


</dt> <dd></dd> <dt>

<span id="UnSyncUnAssoc"></span><span id="unsyncunassoc"></span><span id="UNSYNCUNASSOC"></span>

**UnSyncUnAssoc** (6)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>7–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportedSynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageReplicationCapabilities.SupportedAsynchronousActions")
</dt> </dl>

Enumeration indicating what operations will be executed without the creation of a job. If an operation is included in both this and SupportedAsynchronousActions then the underlying instrumentation is indicating that it may or may not create a job.

<dt>

<span id="Local_Replica_Creation"></span><span id="local_replica_creation"></span><span id="LOCAL_REPLICA_CREATION"></span>

**Local Replica Creation** (2)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Creation"></span><span id="remote_replica_creation"></span><span id="REMOTE_REPLICA_CREATION"></span>

**Remote Replica Creation** (3)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Modification"></span><span id="local_replica_modification"></span><span id="LOCAL_REPLICA_MODIFICATION"></span>

**Local Replica Modification** (4)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Modification"></span><span id="remote_replica_modification"></span><span id="REMOTE_REPLICA_MODIFICATION"></span>

**Remote Replica Modification** (5)


</dt> <dd></dd> <dt>

<span id="Local_Replica_Attachment"></span><span id="local_replica_attachment"></span><span id="LOCAL_REPLICA_ATTACHMENT"></span>

**Local Replica Attachment** (6)


</dt> <dd></dd> <dt>

<span id="Remote_Replica_Attachment"></span><span id="remote_replica_attachment"></span><span id="REMOTE_REPLICA_ATTACHMENT"></span>

**Remote Replica Attachment** (7)


</dt> <dd></dd> <dt>

<span id="Buffer_Creation"></span><span id="buffer_creation"></span><span id="BUFFER_CREATION"></span>

**Buffer Creation** (8)


</dt> <dd></dd> <dt>

<span id="NetworkPipe_Creation"></span><span id="networkpipe_creation"></span><span id="NETWORKPIPE_CREATION"></span>

**NetworkPipe Creation** (9)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>10–65535</dd> </dl>

</dd> <dt>

**UseReplicationBufferDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_StorageSetting.UseReplicationBuffer")
</dt> </dl>

Indicate if an async remote replica pair is allowed to use a write buffer for asynchronous write buffering. - Not Managed: use or not of the buffer is up to the implementation. - Use Buffer: use of a buffer is required. - Do Not Use Buffer: a buffer shall not be used.

<dt>

<span id="Not_Managed"></span><span id="not_managed"></span><span id="NOT_MANAGED"></span>

**Not Managed** (0)


</dt> <dd></dd> <dt>

<span id="Use_Buffer"></span><span id="use_buffer"></span><span id="USE_BUFFER"></span>

**Use Buffer** (1)


</dt> <dd></dd> <dt>

<span id="Do_Not_Use_Buffer"></span><span id="do_not_use_buffer"></span><span id="DO_NOT_USE_BUFFER"></span>

**Do Not Use Buffer** (2)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>3–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> </dl>

 

 





