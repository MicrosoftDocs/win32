---
title: MSFT\_SMReplicationCapabilities class
description: Represents the replication capabilities of a storage subsystem.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f30f181a-65ba-4101-97e1-bc25600ce515'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSFT_SMReplicationCapabilities class", "MSFT_SMReplicationCapabilities class, described"]
topic_type:
- apiref
api_name:
- MSFT_SMReplicationCapabilities
- MSFT_SMReplicationCapabilities.ObjectId
- MSFT_SMReplicationCapabilities.Identifier
- MSFT_SMReplicationCapabilities.SupportedStorageObjects
- MSFT_SMReplicationCapabilities.SupportedReplicationTypes
- MSFT_SMReplicationCapabilities.DefaultRecoveryPointObjective
- MSFT_SMReplicationCapabilities.SupportsReplicationGroup
- MSFT_SMReplicationCapabilities.SupportsEmptyReplicationGroup
- MSFT_SMReplicationCapabilities.SupportsFullDiscovery
- MSFT_SMReplicationCapabilities.SupportsCreateReplicationRelationshipMethod
- MSFT_SMReplicationCapabilities.SupportedAsynchronousActions
- MSFT_SMReplicationCapabilities.SupportedSynchronousActions
api_location:
- StorageService.dll
api_type:
- DllExport
---

# MSFT\_SMReplicationCapabilities class

Represents the replication capabilities of a storage subsystem.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("WMIStorage"), AMENDMENT]
class MSFT_SMReplicationCapabilities : MSFT_SMStorageObject
{
  String  ObjectId;
  String  Identifier;
  uint16  SupportedStorageObjects[];
  uint16  SupportedReplicationTypes[];
  UInt32  DefaultRecoveryPointObjective;
  Boolean SupportsReplicationGroup;
  Boolean SupportsEmptyReplicationGroup;
  Boolean SupportsFullDiscovery;
  Boolean SupportsCreateReplicationRelationshipMethod;
  uint16  SupportedAsynchronousActions[];
  uint16  SupportedSynchronousActions[];
};
```

## Members

The **MSFT\_SMReplicationCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_SMReplicationCapabilities** class has these methods.



| Method                                                                                            | Description                                                                                          |
|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------|
| [**GetRecoveryPointData**](getrecoverypointdata-msft-smreplicationcapabilities.md)               | Retrieves recovery point data for a storage subsystem.<br/>                                    |
| [**GetSupportedCopyStates**](getsupportedcopystates-msft-smreplicationcapabilities.md)           | Retrieves the supported copy states for the specified replication type.<br/>                   |
| [**GetSupportedFeatures**](getsupportedfeatures-msft-smreplicationcapabilities.md)               | Retrieves the supported features for the specified replication type.<br/>                      |
| [**GetSupportedGroupCopyStates**](getsupportedgroupcopystates-msft-smreplicationcapabilities.md) | Retrieves the supported replication group copy states for the specified replication type.<br/> |
| [**GetSupportedGroupFeatures**](getsupportedgroupfeatures-msft-smreplicationcapabilities.md)     | Retrieves the supported group features for the specified replication type.<br/>                |
| [**GetSupportedGroupOperations**](getsupportedgroupoperations-msft-smreplicationcapabilities.md) | Retrieves the supported replication group operations for the specified replication type.<br/>  |
| [**GetSupportedOperations**](getsupportedoperations-msft-smreplicationcapabilities.md)           | Retrieves the supported operations for the specified replication type.<br/>                    |



 

### Properties

The **MSFT\_SMReplicationCapabilities** class has these properties.

<dl> <dt>

**DefaultRecoveryPointObjective**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The default value for the recovery point.

</dd> <dt>

**Identifier**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of the logical instance of the object. This ID must be unique within the scope of the storage system.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**ObjectId**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The ID of this class instance. This ID must be unique within the scope of the Windows Storage Management server that hosts the provider object.

This property is inherited from [**MSFT\_SMStorageObject**](msft-smstorageobject.md).

</dd> <dt>

**SupportedAsynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ReplicationServiceCapabilities.SupportedSynchronousActions")
</dt> </dl>

An array that contains indicators of the operations to run as asynchronous jobs.

The possible values are:

<dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>

**CreateElementReplica** (2)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>

**CreateGroupReplica** (3)


</dt> <dd></dd> <dt>

<span id="CreateSynchronizationAspect"></span><span id="createsynchronizationaspect"></span><span id="CREATESYNCHRONIZATIONASPECT"></span>

**CreateSynchronizationAspect** (4)


</dt> <dd></dd> <dt>

<span id="ModifyReplicaSynchronization"></span><span id="modifyreplicasynchronization"></span><span id="MODIFYREPLICASYNCHRONIZATION"></span>

**ModifyReplicaSynchronization** (5)


</dt> <dd></dd> <dt>

<span id="ModifyListSynchronization"></span><span id="modifylistsynchronization"></span><span id="MODIFYLISTSYNCHRONIZATION"></span>

**ModifyListSynchronization** (6)


</dt> <dd></dd> <dt>

<span id="ModifySettingsDefineState"></span><span id="modifysettingsdefinestate"></span><span id="MODIFYSETTINGSDEFINESTATE"></span>

**ModifySettingsDefineState** (7)


</dt> <dd></dd> <dt>

<span id="GetAvailableTargetElements"></span><span id="getavailabletargetelements"></span><span id="GETAVAILABLETARGETELEMENTS"></span>

**GetAvailableTargetElements** (8)


</dt> <dd></dd> <dt>

<span id="GetPeerSystems"></span><span id="getpeersystems"></span><span id="GETPEERSYSTEMS"></span>

**GetPeerSystems** (9)


</dt> <dd></dd> <dt>

<span id="GetReplicationRelationships"></span><span id="getreplicationrelationships"></span><span id="GETREPLICATIONRELATIONSHIPS"></span>

**GetReplicationRelationships** (10)


</dt> <dd></dd> <dt>

<span id="GetServiceAccessPoints"></span><span id="getserviceaccesspoints"></span><span id="GETSERVICEACCESSPOINTS"></span>

**GetServiceAccessPoints** (11)


</dt> <dd></dd> <dt>

<span id="CreateListReplica"></span><span id="createlistreplica"></span><span id="CREATELISTREPLICA"></span>

**CreateListReplica** (19)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplicaFromElements"></span><span id="creategroupreplicafromelements"></span><span id="CREATEGROUPREPLICAFROMELEMENTS"></span>

**CreateGroupReplicaFromElements** (20)


</dt> <dd></dd> <dt>

<span id="GetReplicationRelationshipInstances"></span><span id="getreplicationrelationshipinstances"></span><span id="GETREPLICATIONRELATIONSHIPINSTANCES"></span>

**GetReplicationRelationshipInstances** (21)


</dt> <dd></dd> <dt>

<span id="ModifyListSettingsDefineState"></span><span id="modifylistsettingsdefinestate"></span><span id="MODIFYLISTSETTINGSDEFINESTATE"></span>

**ModifyListSettingsDefineState** (22)


</dt> <dd></dd> <dt>

<span id="CreateRemoteReplicationCollection"></span><span id="createremotereplicationcollection"></span><span id="CREATEREMOTEREPLICATIONCOLLECTION"></span>

**CreateRemoteReplicationCollection** (23)


</dt> <dd></dd> <dt>

<span id="AddToRemoteReplicationCollection"></span><span id="addtoremotereplicationcollection"></span><span id="ADDTOREMOTEREPLICATIONCOLLECTION"></span>

**AddToRemoteReplicationCollection** (24)


</dt> <dd></dd> <dt>

<span id="RemoveFromRemoteReplicationCollection"></span><span id="removefromremotereplicationcollection"></span><span id="REMOVEFROMREMOTEREPLICATIONCOLLECTION"></span>

**RemoveFromRemoteReplicationCollection** (25)


</dt> <dd></dd> <dt>

<span id="GetSynchronizationAspects"></span><span id="getsynchronizationaspects"></span><span id="GETSYNCHRONIZATIONASPECTS"></span>

**GetSynchronizationAspects** (26)


</dt> <dd></dd> <dt>

<span id="GetSynchronizationAspectInstances"></span><span id="getsynchronizationaspectinstances"></span><span id="GETSYNCHRONIZATIONASPECTINSTANCES"></span>

**GetSynchronizationAspectInstances** (27)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplicaFromElementSynchronizations"></span><span id="creategroupreplicafromelementsynchronizations"></span><span id="CREATEGROUPREPLICAFROMELEMENTSYNCHRONIZATIONS"></span>

**CreateGroupReplicaFromElementSynchronizations** (28)


</dt> <dd></dd> <dt>

<span id="AddElementsToGroupSynchronized"></span><span id="addelementstogroupsynchronized"></span><span id="ADDELEMENTSTOGROUPSYNCHRONIZED"></span>

**AddElementsToGroupSynchronized** (29)


</dt> <dd></dd> <dt>

<span id="ConfirmTargetData"></span><span id="confirmtargetdata"></span><span id="CONFIRMTARGETDATA"></span>

**ConfirmTargetData** (30)


</dt> <dd></dd> <dt>

<span id="CreateListSynchronizationAspect"></span><span id="createlistsynchronizationaspect"></span><span id="CREATELISTSYNCHRONIZATIONASPECT"></span>

**CreateListSynchronizationAspect** (31)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>32–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportedReplicationTypes**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the replication types that are supported by the storage subsystem.

The possible values are:

<dt>

<span id="Synchronous_Mirror_Local"></span><span id="synchronous_mirror_local"></span><span id="SYNCHRONOUS_MIRROR_LOCAL"></span>

**Synchronous Mirror Local** (2)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Local"></span><span id="asynchronous_mirror_local"></span><span id="ASYNCHRONOUS_MIRROR_LOCAL"></span>

**Asynchronous Mirror Local** (3)


</dt> <dd></dd> <dt>

<span id="Synchronous_Mirror_Remote"></span><span id="synchronous_mirror_remote"></span><span id="SYNCHRONOUS_MIRROR_REMOTE"></span>

**Synchronous Mirror Remote** (4)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Mirror_Remote"></span><span id="asynchronous_mirror_remote"></span><span id="ASYNCHRONOUS_MIRROR_REMOTE"></span>

**Asynchronous Mirror Remote** (5)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Local"></span><span id="synchronous_snapshot_local"></span><span id="SYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Synchronous Snapshot Local** (6)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Local"></span><span id="asynchronous_snapshot_local"></span><span id="ASYNCHRONOUS_SNAPSHOT_LOCAL"></span>

**Asynchronous Snapshot Local** (7)


</dt> <dd></dd> <dt>

<span id="Synchronous_Snapshot_Remote"></span><span id="synchronous_snapshot_remote"></span><span id="SYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Synchronous Snapshot Remote** (8)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Snapshot_Remote"></span><span id="asynchronous_snapshot_remote"></span><span id="ASYNCHRONOUS_SNAPSHOT_REMOTE"></span>

**Asynchronous Snapshot Remote** (9)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Local"></span><span id="synchronous_clone_local"></span><span id="SYNCHRONOUS_CLONE_LOCAL"></span>

**Synchronous Clone Local** (10)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Local"></span><span id="asynchronous_clone_local"></span><span id="ASYNCHRONOUS_CLONE_LOCAL"></span>

**Asynchronous Clone Local** (11)


</dt> <dd></dd> <dt>

<span id="Synchronous_Clone_Remote"></span><span id="synchronous_clone_remote"></span><span id="SYNCHRONOUS_CLONE_REMOTE"></span>

**Synchronous Clone Remote** (12)


</dt> <dd></dd> <dt>

<span id="Asynchronous_Clone_Remote"></span><span id="asynchronous_clone_remote"></span><span id="ASYNCHRONOUS_CLONE_REMOTE"></span>

**Asynchronous Clone Remote** (13)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Local"></span><span id="synchronous_tokenizedclone_local"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Synchronous TokenizedClone Local** (14)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Local"></span><span id="asynchronous_tokenizedclone_local"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_LOCAL"></span>

**Asynchronous TokenizedClone Local** (15)


</dt> <dd></dd> <dt>

<span id="Synchronous_TokenizedClone_Remote"></span><span id="synchronous_tokenizedclone_remote"></span><span id="SYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Synchronous TokenizedClone Remote** (16)


</dt> <dd></dd> <dt>

<span id="Asynchronous_TokenizedClone_Remote"></span><span id="asynchronous_tokenizedclone_remote"></span><span id="ASYNCHRONOUS_TOKENIZEDCLONE_REMOTE"></span>

**Asynchronous TokenizedClone Remote** (17)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Local"></span><span id="adaptive_mirror_local"></span><span id="ADAPTIVE_MIRROR_LOCAL"></span>

**Adaptive Mirror Local** (18)


</dt> <dd></dd> <dt>

<span id="Adaptive_Mirror_Remote"></span><span id="adaptive_mirror_remote"></span><span id="ADAPTIVE_MIRROR_REMOTE"></span>

**Adaptive Mirror Remote** (19)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Local"></span><span id="adaptive_snapshot_local"></span><span id="ADAPTIVE_SNAPSHOT_LOCAL"></span>

**Adaptive Snapshot Local** (20)


</dt> <dd></dd> <dt>

<span id="Adaptive_Snapshot_Remote"></span><span id="adaptive_snapshot_remote"></span><span id="ADAPTIVE_SNAPSHOT_REMOTE"></span>

**Adaptive Snapshot Remote** (21)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Local"></span><span id="adaptive_clone_local"></span><span id="ADAPTIVE_CLONE_LOCAL"></span>

**Adaptive Clone Local** (22)


</dt> <dd></dd> <dt>

<span id="Adaptive_Clone_Remote"></span><span id="adaptive_clone_remote"></span><span id="ADAPTIVE_CLONE_REMOTE"></span>

**Adaptive Clone Remote** (23)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Local"></span><span id="adaptive_tokenizedclone_local"></span><span id="ADAPTIVE_TOKENIZEDCLONE_LOCAL"></span>

**Adaptive TokenizedClone Local** (24)


</dt> <dd></dd> <dt>

<span id="Adaptive_TokenizedClone_Remote"></span><span id="adaptive_tokenizedclone_remote"></span><span id="ADAPTIVE_TOKENIZEDCLONE_REMOTE"></span>

**Adaptive TokenizedClone Remote** (25)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportedStorageObjects**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type storage objects that are supported by the storage subsystem.

The possible values are:

<dt>

<span id="StorageVolume"></span><span id="storagevolume"></span><span id="STORAGEVOLUME"></span>

**StorageVolume** (2)


</dt> <dd></dd> <dt>

<span id="LogicalDisk"></span><span id="logicaldisk"></span><span id="LOGICALDISK"></span>

**LogicalDisk** (3)


</dt> <dd></dd> <dt>

<span id="ReplicationEntity"></span><span id="replicationentity"></span><span id="REPLICATIONENTITY"></span>

**ReplicationEntity** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5–32767</dd> <dt>

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

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ReplicationServiceCapabilities.SupportedAsynchronousActions")
</dt> </dl>

An array that contains indicators of the operations to run as synchronous jobs.

The possible values are:

<dt>

<span id="CreateElementReplica"></span><span id="createelementreplica"></span><span id="CREATEELEMENTREPLICA"></span>

**CreateElementReplica** (2)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplica"></span><span id="creategroupreplica"></span><span id="CREATEGROUPREPLICA"></span>

**CreateGroupReplica** (3)


</dt> <dd></dd> <dt>

<span id="CreateSynchronizationAspect"></span><span id="createsynchronizationaspect"></span><span id="CREATESYNCHRONIZATIONASPECT"></span>

**CreateSynchronizationAspect** (4)


</dt> <dd></dd> <dt>

<span id="ModifyReplicaSynchronization"></span><span id="modifyreplicasynchronization"></span><span id="MODIFYREPLICASYNCHRONIZATION"></span>

**ModifyReplicaSynchronization** (5)


</dt> <dd></dd> <dt>

<span id="ModifyListSynchronization"></span><span id="modifylistsynchronization"></span><span id="MODIFYLISTSYNCHRONIZATION"></span>

**ModifyListSynchronization** (6)


</dt> <dd></dd> <dt>

<span id="ModifySettingsDefineState"></span><span id="modifysettingsdefinestate"></span><span id="MODIFYSETTINGSDEFINESTATE"></span>

**ModifySettingsDefineState** (7)


</dt> <dd></dd> <dt>

<span id="GetAvailableTargetElements"></span><span id="getavailabletargetelements"></span><span id="GETAVAILABLETARGETELEMENTS"></span>

**GetAvailableTargetElements** (8)


</dt> <dd></dd> <dt>

<span id="GetPeerSystems"></span><span id="getpeersystems"></span><span id="GETPEERSYSTEMS"></span>

**GetPeerSystems** (9)


</dt> <dd></dd> <dt>

<span id="GetReplicationRelationships"></span><span id="getreplicationrelationships"></span><span id="GETREPLICATIONRELATIONSHIPS"></span>

**GetReplicationRelationships** (10)


</dt> <dd></dd> <dt>

<span id="GetServiceAccessPoints"></span><span id="getserviceaccesspoints"></span><span id="GETSERVICEACCESSPOINTS"></span>

**GetServiceAccessPoints** (11)


</dt> <dd></dd> <dt>

<span id="CreateGroup"></span><span id="creategroup"></span><span id="CREATEGROUP"></span>

**CreateGroup** (12)


</dt> <dd></dd> <dt>

<span id="DeleteGroup"></span><span id="deletegroup"></span><span id="DELETEGROUP"></span>

**DeleteGroup** (13)


</dt> <dd></dd> <dt>

<span id="AddMembers"></span><span id="addmembers"></span><span id="ADDMEMBERS"></span>

**AddMembers** (14)


</dt> <dd></dd> <dt>

<span id="RemoveMembers"></span><span id="removemembers"></span><span id="REMOVEMEMBERS"></span>

**RemoveMembers** (15)


</dt> <dd></dd> <dt>

<span id="AddReplicationEntity"></span><span id="addreplicationentity"></span><span id="ADDREPLICATIONENTITY"></span>

**AddReplicationEntity** (16)


</dt> <dd></dd> <dt>

<span id="AddServiceAccessPoint"></span><span id="addserviceaccesspoint"></span><span id="ADDSERVICEACCESSPOINT"></span>

**AddServiceAccessPoint** (17)


</dt> <dd></dd> <dt>

<span id="AddSharedSecret"></span><span id="addsharedsecret"></span><span id="ADDSHAREDSECRET"></span>

**AddSharedSecret** (18)


</dt> <dd></dd> <dt>

<span id="CreateListReplica"></span><span id="createlistreplica"></span><span id="CREATELISTREPLICA"></span>

**CreateListReplica** (19)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplicaFromElements"></span><span id="creategroupreplicafromelements"></span><span id="CREATEGROUPREPLICAFROMELEMENTS"></span>

**CreateGroupReplicaFromElements** (20)


</dt> <dd></dd> <dt>

<span id="GetReplicationRelationshipInstances"></span><span id="getreplicationrelationshipinstances"></span><span id="GETREPLICATIONRELATIONSHIPINSTANCES"></span>

**GetReplicationRelationshipInstances** (21)


</dt> <dd></dd> <dt>

<span id="ModifyListSettingsDefineState"></span><span id="modifylistsettingsdefinestate"></span><span id="MODIFYLISTSETTINGSDEFINESTATE"></span>

**ModifyListSettingsDefineState** (22)


</dt> <dd></dd> <dt>

<span id="CreateRemoteReplicationCollection"></span><span id="createremotereplicationcollection"></span><span id="CREATEREMOTEREPLICATIONCOLLECTION"></span>

**CreateRemoteReplicationCollection** (23)


</dt> <dd></dd> <dt>

<span id="AddToRemoteReplicationCollection"></span><span id="addtoremotereplicationcollection"></span><span id="ADDTOREMOTEREPLICATIONCOLLECTION"></span>

**AddToRemoteReplicationCollection** (24)


</dt> <dd></dd> <dt>

<span id="RemoveFromRemoteReplicationCollection"></span><span id="removefromremotereplicationcollection"></span><span id="REMOVEFROMREMOTEREPLICATIONCOLLECTION"></span>

**RemoveFromRemoteReplicationCollection** (25)


</dt> <dd></dd> <dt>

<span id="GetSynchronizationAspects"></span><span id="getsynchronizationaspects"></span><span id="GETSYNCHRONIZATIONASPECTS"></span>

**GetSynchronizationAspects** (26)


</dt> <dd></dd> <dt>

<span id="GetSynchronizationAspectInstances"></span><span id="getsynchronizationaspectinstances"></span><span id="GETSYNCHRONIZATIONASPECTINSTANCES"></span>

**GetSynchronizationAspectInstances** (27)


</dt> <dd></dd> <dt>

<span id="CreateGroupReplicaFromElementSynchronizations"></span><span id="creategroupreplicafromelementsynchronizations"></span><span id="CREATEGROUPREPLICAFROMELEMENTSYNCHRONIZATIONS"></span>

**CreateGroupReplicaFromElementSynchronizations** (28)


</dt> <dd></dd> <dt>

<span id="AddElementsToGroupSynchronized"></span><span id="addelementstogroupsynchronized"></span><span id="ADDELEMENTSTOGROUPSYNCHRONIZED"></span>

**AddElementsToGroupSynchronized** (29)


</dt> <dd></dd> <dt>

<span id="ConfirmTargetData"></span><span id="confirmtargetdata"></span><span id="CONFIRMTARGETDATA"></span>

**ConfirmTargetData** (30)


</dt> <dd></dd> <dt>

<span id="CreateListSynchronizationAspect"></span><span id="createlistsynchronizationaspect"></span><span id="CREATELISTSYNCHRONIZATIONASPECT"></span>

**CreateListSynchronizationAspect** (31)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>32–32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768–65535</dd> </dl>

</dd> <dt>

**SupportsCreateReplicationRelationshipMethod**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if the [**CreateReplicationRelationship**](createreplicationrelationship-msft-smsystem.md) method is supported by the storage subsystem; otherwise, **False**.

</dd> <dt>

**SupportsEmptyReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if empty replication groups are supported by the storage subsystem; otherwise, **False**.

</dd> <dt>

**SupportsFullDiscovery**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if this is a fully discovered model; otherwise, **False**.

</dd> <dt>

**SupportsReplicationGroup**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**True** if replication groups are supported by the storage subsystem; otherwise, **False**.

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageObject**](msft-smstorageobject.md)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 





