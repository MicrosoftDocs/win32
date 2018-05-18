---
title: MSFT\_ReplicationCapabilities class
description: Represents the replication capabilities of a storage subsystem.
ms.assetid: 'EBD8AB73-BE3C-4AD8-9541-9853D3851900'
keywords: ["MSFT_ReplicationCapabilities class Windows Storage Management API", "MSFT_ReplicationCapabilities class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_ReplicationCapabilities
- MSFT_ReplicationCapabilities.SupportedObjectTypes
- MSFT_ReplicationCapabilities.SupportedReplicationTypes
- MSFT_ReplicationCapabilities.DefaultRecoveryPointObjective
- MSFT_ReplicationCapabilities.SupportsReplicationGroup
- MSFT_ReplicationCapabilities.SupportsEmptyReplicationGroup
- MSFT_ReplicationCapabilities.SupportsFullDiscovery
- MSFT_ReplicationCapabilities.SupportsCreateReplicationRelationshipMethod
- MSFT_ReplicationCapabilities.SupportedAsynchronousActions
- MSFT_ReplicationCapabilities.SupportedSynchronousActions
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_ReplicationCapabilities class

Represents the replication capabilities of a storage subsystem.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_ReplicationCapabilities : MSFT_StorageObject
{
  UInt16  SupportedObjectTypes[];
  UInt16  SupportedReplicationTypes[];
  UInt32  DefaultRecoveryPointObjective;
  Boolean SupportsReplicationGroup;
  Boolean SupportsEmptyReplicationGroup;
  Boolean SupportsFullDiscovery;
  Boolean SupportsCreateReplicationRelationshipMethod;
  Uint16  SupportedAsynchronousActions[];
  Uint16  SupportedSynchronousActions[];
};
```

## Members

The **MSFT\_ReplicationCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_ReplicationCapabilities** class has these methods.



| Method                                                                                          | Description                                                                                                                                                                             |
|:------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetRecoveryPointData**](msft-replicationcapabilities-getrecoverypointdata.md)               | Returns, for a given *ReplicationType*, recovery point data.<br/>                                                                                                                 |
| [**GetSupportedCopyStates**](msft-replicationcapabilities-getsupportedcopystates.md)           | Returns, for a given *ReplicationType*, the supported copy states.<br/>                                                                                                           |
| [**GetSupportedFeatures**](msft-replicationcapabilities-getsupportedfeatures.md)               | Returns, for a given *ReplicationType*, the supported features.<br/>                                                                                                              |
| [**GetSupportedGroupCopyStates**](msft-replicationcapabilities-getsupportedgroupcopystates.md) | Returns, for a given *ReplicationType*, the supported replication group copy states.<br/>                                                                                         |
| [**GetSupportedGroupFeatures**](msft-replicationcapabilities-getsupportedgroupfeatures.md)     | Returns, for a given *ReplicationType*, the supported group features.<br/>                                                                                                        |
| [**GetSupportedGroupOperations**](msft-replicationcapabilities-getsupportedgroupoperations.md) | Returns, for a given *ReplicationType*, the supported operations on a group synchronized association that can be supplied to the **ModifyReplicaSynchronization** operation.<br/> |
| [**GetSupportedOperations**](msft-replicationcapabilities-getsupportedoperations.md)           | Returns, for a given ReplicationType, the supported Operations on a StorageSynchronized association that can be supplied to the **ModifyReplicaSynchronization** operation.<br/>  |



 

### Properties

The **MSFT\_ReplicationCapabilities** class has these properties.

<dl> <dt>

**DefaultRecoveryPointObjective**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Default value for recovery point.

</dd> <dt>

**SupportedAsynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **Uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and *SupportedSynchronousActions* then the underlying implementation is indicating that it may or may not create a job.

> [!Note]  
> The following methods are not supported asynchronously:
>
> -   AddMembers
> -   AddReplicationEntity
> -   AddServiceAccessPoint
> -   AddSharedSecret
> -   CreateGroup
> -   DeleteGroup
> -   RemoveMembers

 

<dl> <dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>**CreateElementReplica** (2)
</dt> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>**CreateGroupReplica** (3)
</dt> <dt>

<span id="CreateSynchronizationAspect"></span><span id="createsynchronizationaspect"></span><span id="CREATESYNCHRONIZATIONASPECT"></span>**CreateSynchronizationAspect** (4)
</dt> <dt>

<span id="ModifyReplicaSynchronization"></span><span id="modifyreplicasynchronization"></span><span id="MODIFYREPLICASYNCHRONIZATION"></span>**ModifyReplicaSynchronization** (5)
</dt> <dt>

<span id="ModifyListSynchronization"></span><span id="modifylistsynchronization"></span><span id="MODIFYLISTSYNCHRONIZATION"></span>**ModifyListSynchronization** (6)
</dt> <dt>

<span id="ModifySettingsDefineState"></span><span id="modifysettingsdefinestate"></span><span id="MODIFYSETTINGSDEFINESTATE"></span>**ModifySettingsDefineState** (7)
</dt> <dt>

<span id="GetAvailableTargetElements"></span><span id="getavailabletargetelements"></span><span id="GETAVAILABLETARGETELEMENTS"></span>**GetAvailableTargetElements** (8)
</dt> <dt>

<span id="GetPeerSystems"></span><span id="getpeersystems"></span><span id="GETPEERSYSTEMS"></span>**GetPeerSystems** (9)
</dt> <dt>

<span id="GetReplicationRelationships"></span><span id="getreplicationrelationships"></span><span id="GETREPLICATIONRELATIONSHIPS"></span>**GetReplicationRelationships** (10)
</dt> <dt>

<span id="GetServiceAccessPoints"></span><span id="getserviceaccesspoints"></span><span id="GETSERVICEACCESSPOINTS"></span>**GetServiceAccessPoints** (11)
</dt> <dt>

<span id="CreateListReplica"></span><span id="createlistreplica"></span><span id="CREATELISTREPLICA"></span>**CreateListReplica** (19)
</dt> <dt>

<span id="CreateGroupReplicaFromElements"></span><span id="creategroupreplicafromelements"></span><span id="CREATEGROUPREPLICAFROMELEMENTS"></span>**CreateGroupReplicaFromElements** (20)
</dt> <dt>

<span id="GetReplicationRelationshipInstances"></span><span id="getreplicationrelationshipinstances"></span><span id="GETREPLICATIONRELATIONSHIPINSTANCES"></span>**GetReplicationRelationshipInstances** (21)
</dt> <dt>

<span id="ModifyListSettingsDefineState"></span><span id="modifylistsettingsdefinestate"></span><span id="MODIFYLISTSETTINGSDEFINESTATE"></span>**ModifyListSettingsDefineState** (22)
</dt> <dt>

<span id="CreateRemoteReplicationCollection"></span><span id="createremotereplicationcollection"></span><span id="CREATEREMOTEREPLICATIONCOLLECTION"></span>**CreateRemoteReplicationCollection** (23)
</dt> <dt>

<span id="AddToRemoteReplicationCollection"></span><span id="addtoremotereplicationcollection"></span><span id="ADDTOREMOTEREPLICATIONCOLLECTION"></span>**AddToRemoteReplicationCollection** (24)
</dt> <dt>

<span id="RemoveFromRemoteReplicationCollection"></span><span id="removefromremotereplicationcollection"></span><span id="REMOVEFROMREMOTEREPLICATIONCOLLECTION"></span>**RemoveFromRemoteReplicationCollection** (25)
</dt> <dt>

<span id="GetSynchronizationAspects"></span><span id="getsynchronizationaspects"></span><span id="GETSYNCHRONIZATIONASPECTS"></span>**GetSynchronizationAspects** (26)
</dt> <dt>

<span id="GetSynchronizationAspectInstances"></span><span id="getsynchronizationaspectinstances"></span><span id="GETSYNCHRONIZATIONASPECTINSTANCES"></span>**GetSynchronizationAspectInstances** (27)
</dt> <dt>

<span id="CreateGroupReplicaFromElementSynchronizations"></span><span id="creategroupreplicafromelementsynchronizations"></span><span id="CREATEGROUPREPLICAFROMELEMENTSYNCHRONIZATIONS"></span>**CreateGroupReplicaFromElementSynchronizations** (28)
</dt> <dt>

<span id="AddElementsToGroupSynchronized"></span><span id="addelementstogroupsynchronized"></span><span id="ADDELEMENTSTOGROUPSYNCHRONIZED"></span>**AddElementsToGroupSynchronized** (29)
</dt> <dt>

<span id="ConfirmTargetData"></span><span id="confirmtargetdata"></span><span id="CONFIRMTARGETDATA"></span>**ConfirmTargetData** (30)
</dt> <dt>

<span id="CreateListSynchronizationAspect"></span><span id="createlistsynchronizationaspect"></span><span id="CREATELISTSYNCHRONIZATIONASPECT"></span>**CreateListSynchronizationAspect** (31)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** ("..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..)
</dt> </dl>

</dd> <dt>

**SupportedObjectTypes**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration indicating the supported object types associated with these replication capabilities.

<dl> <dt>

<span id="VirtualDisk"></span><span id="virtualdisk"></span><span id="VIRTUALDISK"></span>**VirtualDisk** (2)
</dt> <dt>

<span id="Volume"></span><span id="volume"></span><span id="VOLUME"></span>**Volume** (3)
</dt> <dt>

<span id="ReplicaPeer"></span><span id="replicapeer"></span><span id="REPLICAPEER"></span>**ReplicaPeer** (4)
</dt> <dt>

<span id="Partition"></span><span id="partition"></span><span id="PARTITION"></span>**Partition** (..)
</dt> <dt>

<span id="ReplicationGroup"></span><span id="replicationgroup"></span><span id="REPLICATIONGROUP"></span>**ReplicationGroup** (0x8000)
</dt> <dt>

<span id="StorageSubSystem"></span><span id="storagesubsystem"></span><span id="STORAGESUBSYSTEM"></span>**StorageSubSystem** (0x8001)
</dt> <dt>

 (0x8002)
</dt> </dl>

</dd> <dt>

**SupportedReplicationTypes**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Write-only
</dt> </dl>

An enumeration indicating the supported SyncType/Mode/Local-or-Remote combinations.

<dl> <dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>**Synchronous Mirror Local** (2)
</dt> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>**Asynchronous Mirror Local** (3)
</dt> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>**Synchronous Mirror Remote** (4)
</dt> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>**Asynchronous Mirror Remote** (5)
</dt> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>**Synchronous Snapshot Local** (6)
</dt> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>**Asynchronous Snapshot Local** (7)
</dt> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>**Synchronous Snapshot Remote** (8)
</dt> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>**Asynchronous Snapshot Remote** (9)
</dt> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>**Synchronous Clone Local** (10)
</dt> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>**Asynchronous Clone Local** (11)
</dt> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>**Synchronous Clone Remote** (12)
</dt> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>**Asynchronous Clone Remote** (13)
</dt> <dt>

<span id="Synchronous_TokenizedClone_Local"></span><span id="synchronous_tokenizedclone_local"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>**Synchronous TokenizedClone Local** (14)
</dt> <dt>

<span id="Asynchronous_TokenizedClone_Local"></span><span id="asynchronous_tokenizedclone_local"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>**Asynchronous TokenizedClone Local** (15)
</dt> <dt>

<span id="Synchronous_TokenizedClone_Remote"></span><span id="synchronous_tokenizedclone_remote"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>**Synchronous TokenizedClone Remote** (16)
</dt> <dt>

<span id="Asynchronous_TokenizedClone_Remote"></span><span id="asynchronous_tokenizedclone_remote"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>**Asynchronous TokenizedClone Remote** (17)
</dt> <dt>

<span id="Adaptive_Mirror_Local"></span><span id="adaptive_mirror_local"></span><span id="ADAPTIVE_MIRROR_LOCAL"></span>**Adaptive Mirror Local** (18)
</dt> <dt>

<span id="Adaptive_Mirror_Remote"></span><span id="adaptive_mirror_remote"></span><span id="ADAPTIVE_MIRROR_REMOTE"></span>**Adaptive Mirror Remote** (19)
</dt> <dt>

<span id="Adaptive_Snapshot_Local"></span><span id="adaptive_snapshot_local"></span><span id="ADAPTIVE_SNAPSHOT_LOCAL"></span>**Adaptive Snapshot Local** (20)
</dt> <dt>

<span id="Adaptive_Snapshot_Remote"></span><span id="adaptive_snapshot_remote"></span><span id="ADAPTIVE_SNAPSHOT_REMOTE"></span>**Adaptive Snapshot Remote** (21)
</dt> <dt>

<span id="Adaptive_Clone_Local"></span><span id="adaptive_clone_local"></span><span id="ADAPTIVE_CLONE_LOCAL"></span>**Adaptive Clone Local** (22)
</dt> <dt>

<span id="Adaptive_Clone_Remote"></span><span id="adaptive_clone_remote"></span><span id="ADAPTIVE_CLONE_REMOTE"></span>**Adaptive Clone Remote** (23)
</dt> <dt>

<span id="Adaptive_TokenizedClone_Local"></span><span id="adaptive_tokenizedclone_local"></span><span id="ADAPTIVE_TOKENIZEDCLONE_LOCAL"></span>**Adaptive TokenizedClone Local** (24)
</dt> <dt>

<span id="Adaptive_TokenizedClone_Remote"></span><span id="adaptive_tokenizedclone_remote"></span><span id="ADAPTIVE_TOKENIZEDCLONE_REMOTE"></span>**Adaptive TokenizedClone Remote** (25)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..)
</dt> </dl>

</dd> <dt>

**SupportedSynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **Uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An enumeration indicating what operations will be executed synchronously—without the creation of a job. If an operation is included in both this and *SupportedAsynchronousActions* then the underlying implementation is indicating that it may or may not create a job.

> [!Note]  
> The following methods are not supported asynchronously:
>
> -   AddMembers
> -   AddReplicationEntity
> -   AddServiceAccessPoint
> -   AddSharedSecret
> -   CreateGroup
> -   DeleteGroup
> -   RemoveMembers

 

<dl> <dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>**CreateElementReplica** (2)
</dt> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>**CreateGroupReplica** (3)
</dt> <dt>

<span id="CreateSynchronizationAspect"></span><span id="createsynchronizationaspect"></span><span id="CREATESYNCHRONIZATIONASPECT"></span>**CreateSynchronizationAspect** (4)
</dt> <dt>

<span id="ModifyReplicaSynchronization"></span><span id="modifyreplicasynchronization"></span><span id="MODIFYREPLICASYNCHRONIZATION"></span>**ModifyReplicaSynchronization** (5)
</dt> <dt>

<span id="ModifyListSynchronization"></span><span id="modifylistsynchronization"></span><span id="MODIFYLISTSYNCHRONIZATION"></span>**ModifyListSynchronization** (6)
</dt> <dt>

<span id="ModifySettingsDefineState"></span><span id="modifysettingsdefinestate"></span><span id="MODIFYSETTINGSDEFINESTATE"></span>**ModifySettingsDefineState** (7)
</dt> <dt>

<span id="GetAvailableTargetElements"></span><span id="getavailabletargetelements"></span><span id="GETAVAILABLETARGETELEMENTS"></span>**GetAvailableTargetElements** (8)
</dt> <dt>

<span id="GetPeerSystems"></span><span id="getpeersystems"></span><span id="GETPEERSYSTEMS"></span>**GetPeerSystems** (9)
</dt> <dt>

<span id="GetReplicationRelationships"></span><span id="getreplicationrelationships"></span><span id="GETREPLICATIONRELATIONSHIPS"></span>**GetReplicationRelationships** (10)
</dt> <dt>

<span id="GetServiceAccessPoints"></span><span id="getserviceaccesspoints"></span><span id="GETSERVICEACCESSPOINTS"></span>**GetServiceAccessPoints** (11)
</dt> <dt>

<span id="CreateGroup"></span><span id="creategroup"></span><span id="CREATEGROUP"></span>**CreateGroup** (12)
</dt> <dt>

<span id="DeleteGroup"></span><span id="deletegroup"></span><span id="DELETEGROUP"></span>**DeleteGroup** (13)
</dt> <dt>

<span id="AddMembers"></span><span id="addmembers"></span><span id="ADDMEMBERS"></span>**AddMembers** (14)
</dt> <dt>

<span id="RemoveMembers"></span><span id="removemembers"></span><span id="REMOVEMEMBERS"></span>**RemoveMembers** (15)
</dt> <dt>

<span id="AddReplicationEntity"></span><span id="addreplicationentity"></span><span id="ADDREPLICATIONENTITY"></span>**AddReplicationEntity** (16)
</dt> <dt>

<span id="AddServiceAccessPoint"></span><span id="addserviceaccesspoint"></span><span id="ADDSERVICEACCESSPOINT"></span>**AddServiceAccessPoint** (17)
</dt> <dt>

<span id="AddSharedSecret"></span><span id="addsharedsecret"></span><span id="ADDSHAREDSECRET"></span>**AddSharedSecret** (18)
</dt> <dt>

<span id="CreateListReplica"></span><span id="createlistreplica"></span><span id="CREATELISTREPLICA"></span>**CreateListReplica** (19)
</dt> <dt>

<span id="CreateGroupReplicaFromElements"></span><span id="creategroupreplicafromelements"></span><span id="CREATEGROUPREPLICAFROMELEMENTS"></span>**CreateGroupReplicaFromElements** (20)
</dt> <dt>

<span id="GetReplicationRelationshipInstances"></span><span id="getreplicationrelationshipinstances"></span><span id="GETREPLICATIONRELATIONSHIPINSTANCES"></span>**GetReplicationRelationshipInstances** (21)
</dt> <dt>

<span id="ModifyListSettingsDefineState"></span><span id="modifylistsettingsdefinestate"></span><span id="MODIFYLISTSETTINGSDEFINESTATE"></span>**ModifyListSettingsDefineState** (22)
</dt> <dt>

<span id="CreateRemoteReplicationCollection"></span><span id="createremotereplicationcollection"></span><span id="CREATEREMOTEREPLICATIONCOLLECTION"></span>**CreateRemoteReplicationCollection** (23)
</dt> <dt>

<span id="AddToRemoteReplicationCollection"></span><span id="addtoremotereplicationcollection"></span><span id="ADDTOREMOTEREPLICATIONCOLLECTION"></span>**AddToRemoteReplicationCollection** (24)
</dt> <dt>

<span id="RemoveFromRemoteReplicationCollection"></span><span id="removefromremotereplicationcollection"></span><span id="REMOVEFROMREMOTEREPLICATIONCOLLECTION"></span>**RemoveFromRemoteReplicationCollection** (25)
</dt> <dt>

<span id="GetSynchronizationAspects"></span><span id="getsynchronizationaspects"></span><span id="GETSYNCHRONIZATIONASPECTS"></span>**GetSynchronizationAspects** (26)
</dt> <dt>

<span id="GetSynchronizationAspectInstances"></span><span id="getsynchronizationaspectinstances"></span><span id="GETSYNCHRONIZATIONASPECTINSTANCES"></span>**GetSynchronizationAspectInstances** (27)
</dt> <dt>

<span id="CreateGroupReplicaFromElementSynchronizations"></span><span id="creategroupreplicafromelementsynchronizations"></span><span id="CREATEGROUPREPLICAFROMELEMENTSYNCHRONIZATIONS"></span>**CreateGroupReplicaFromElementSynchronizations** (28)
</dt> <dt>

<span id="AddElementsToGroupSynchronized"></span><span id="addelementstogroupsynchronized"></span><span id="ADDELEMENTSTOGROUPSYNCHRONIZED"></span>**AddElementsToGroupSynchronized** (29)
</dt> <dt>

<span id="ConfirmTargetData"></span><span id="confirmtargetdata"></span><span id="CONFIRMTARGETDATA"></span>**ConfirmTargetData** (30)
</dt> <dt>

<span id="CreateListSynchronizationAspect"></span><span id="createlistsynchronizationaspect"></span><span id="CREATELISTSYNCHRONIZATIONASPECT"></span>**CreateListSynchronizationAspect** (31)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** ("..)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (0x8000..)
</dt> </dl>

</dd> <dt>

**SupportsCreateReplicationRelationshipMethod**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, then the [**CreateReplicationRelationship**](msft-storagesubsystem-createreplicationrelationship.md) operation is supported.

</dd> <dt>

**SupportsEmptyReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, then empty replication groups are allowed.

</dd> <dt>

**SupportsFullDiscovery**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, then this is a fully discovered model.

</dd> <dt>

**SupportsReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, then replication groups are supported.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





