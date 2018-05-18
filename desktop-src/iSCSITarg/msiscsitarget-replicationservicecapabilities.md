---
title: MSISCSITARGET\_ReplicationServiceCapabilities class
description: Defines the capabilities of a MSISCSITARGET\_ReplicationService.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ff10513f-fde7-418b-a43e-17e8406d1622'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , described"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities
- MSISCSITARGET_ReplicationServiceCapabilities.Caption
- MSISCSITARGET_ReplicationServiceCapabilities.Description
- MSISCSITARGET_ReplicationServiceCapabilities.InstanceID
- MSISCSITARGET_ReplicationServiceCapabilities.ElementName
- MSISCSITARGET_ReplicationServiceCapabilities.SupportedReplicationTypes
- MSISCSITARGET_ReplicationServiceCapabilities.SupportedStorageObjects
- MSISCSITARGET_ReplicationServiceCapabilities.SupportedAsynchronousActions
- MSISCSITARGET_ReplicationServiceCapabilities.SupportedSynchronousActions
api_location:
- SMiSCSITargetProv.dll
api_type:
- DllExport
---

# MSISCSITARGET\_ReplicationServiceCapabilities class

Defines the capabilities of a [**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md). An instance of this class is associated with a [**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md) instance by using a [**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md) instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Static, Version("1.0.0")]
class MSISCSITARGET_ReplicationServiceCapabilities : CIM_ReplicationServiceCapabilities
{
  string Caption;
  string Description;
  string InstanceID;
  string ElementName;
  uint16 SupportedReplicationTypes[];
  uint16 SupportedStorageObjects[];
  uint16 SupportedAsynchronousActions[];
  uint16 SupportedSynchronousActions[];
};
```

## Members

The **MSISCSITARGET\_ReplicationServiceCapabilities** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSISCSITARGET\_ReplicationServiceCapabilities** class has these methods.



| Method                                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ConvertReplicationTypeToSyncType**](convertreplicationtypetosynctype-msiscsitarget-replicationservicecapabilities.md)                   | Returns a **SupportedReplicationTypes** value that represents the specified *SyncType*, *Mode*, and *LocalOrRemote* values.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                   |
| [**ConvertSyncTypeToReplicationType**](convertsynctypetoreplicationtype-msiscsitarget-replicationservicecapabilities.md)                   | Converts the specified *SyncType*, *Mode*, and *LocalOrRemote* parameter values to a **SupportedReplicationTypes** value. This method is the inverse of the [**ConvertReplicationTypeToSyncType**](convertreplicationtypetosynctype-msiscsitarget-replicationservicecapabilities.md) method.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/> |
| [**GetDefaultConsistency**](getdefaultconsistency-msiscsitarget-replicationservicecapabilities.md)                                         | Retrieves the default consistency value for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                     |
| [**GetDefaultGroupPersistency**](getdefaultgrouppersistency-msiscsitarget-replicationservicecapabilities.md)                               | Retrieves the default persistency for a newly created group.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                                  |
| [**GetDefaultReplicationSettingData**](getdefaultreplicationsettingdata-msiscsitarget-replicationservicecapabilities.md)                   | Retrieves a default **CIM\_ReplicationSettingData** instance for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                |
| [**GetSupportedConnectionFeatures**](getsupportedconnectionfeatures-msiscsitarget-replicationservicecapabilities.md)                       | Retrieves specific features of a specified protocol endpoint.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                                 |
| [**GetSupportedConsistency**](getsupportedconsistency-msiscsitarget-replicationservicecapabilities.md)                                     | Retrieves the supported consistency for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                         |
| [**GetSupportedCopyStates**](getsupportedcopystates-msiscsitarget-replicationservicecapabilities.md)                                       | Retrieves the supported copy states for a specified replication type and indicates if the target element is host accessible for each copy state.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                              |
| [**GetSupportedFeatures**](getsupportedfeatures-msiscsitarget-replicationservicecapabilities.md)                                           | Retrieves the supported features for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                            |
| [**GetSupportedGroupCopyStates**](getsupportedgroupcopystates-msiscsitarget-replicationservicecapabilities.md)                             | Retrieves the supported replication group copy states for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                       |
| [**GetSupportedGroupFeatures**](getsupportedgroupfeatures-msiscsitarget-replicationservicecapabilities.md)                                 | Retrieves the supported group features for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                      |
| [**GetSupportedGroupOperations**](getsupportedgroupoperations-msiscsitarget-replicationservicecapabilities.md)                             | Retrieves the operations that can be performed by the [**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md).[**ModifyReplicaSynchronization**](modifyreplicasynchronization-msiscsitarget-replicationservice.md) method for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>            |
| [**GetSupportedListOperations**](getsupportedlistoperations-msiscsitarget-replicationservicecapabilities.md)                               | Retrieves a list of supported operations that can be performed by using the [**ModifyListSynchronization**](modifylistsynchronization-msiscsitarget-replicationservice.md) method on a specified replication type and association type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                      |
| [**GetSupportedMaximum**](getsupportedmaximum-msiscsitarget-replicationservicecapabilities.md)                                             | Retrieves the maximum number of the specified component type that the service supports for the specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                    |
| [**GetSupportedOperations**](getsupportedoperations-msiscsitarget-replicationservicecapabilities.md)                                       | Retrieves a list of supported operations that can be performed by using the [**ModifyReplicaSynchronization**](modifyreplicasynchronization-msiscsitarget-replicationservice.md) method on a specified replication type and association type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                |
| [**GetSupportedReplicationSettingData**](getsupportedreplicationsettingdata-msiscsitarget-replicationservicecapabilities.md)               | Retrieves the supported property values for the specified **CIM\_ReplicationSettingData** property and replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                      |
| [**GetSupportedSettingsDefineStateOperations**](getsupportedsettingsdefinestateoperations-msiscsitarget-replicationservicecapabilities.md) | Retrieves a list of supported operations that can be performed on a settings define state association by using the [**ModifyReplicaSynchronization**](modifyreplicasynchronization-msiscsitarget-replicationservice.md) method for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                             |
| [**GetSupportedThinProvisioningFeatures**](getsupportedthinprovisioningfeatures-msiscsitarget-replicationservicecapabilities.md)           | Retrieves the supported features that are related to thin provisioning for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                      |
| [**GetSupportedWaitForCopyStates**](getsupportedwaitforcopystates-msiscsitarget-replicationservicecapabilities.md)                         | Retrieves the copy states that are valid in the *WaitForCopyState* parameter of the specified method for a specified replication type.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                        |
| [**GetSynchronizationSupported**](getsynchronizationsupported-msiscsitarget-replicationservicecapabilities.md)                             | Retrieves the supported synchronization operations for the specified element.<br/> This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.<br/>                                                                                                                                                                                                                 |



 

### Properties

The **MSISCSITARGET\_ReplicationServiceCapabilities** class has these properties.

<dl> <dt>

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

**SupportedAsynchronousActions**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ReplicationServiceCapabilities.SupportedSynchronousActions")
</dt> </dl>

Enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and SupportedSynchronousActions properties then the underlying implementation is indicating that it may or may not create a job.Note: the following methods are not supported asynchronously, hence the gap between 11 and 19: \\t - CreateGroup \\t - DeleteGroup \\t - AddMembers \\t - RemoveMembers \\t - AddReplicationEntity \\t - AddServiceAccessPoint \\t - AddSharedSecret.

This property is inherited from [**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26–32767</dd> <dt>

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

Enumeration indicating the supported SyncType/Mode/Local-or-Remote combinations.

This property is inherited from [**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>14–32767</dd> <dt>

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

Enumeration indicating the supported storage objects.

This property is inherited from [**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md).

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

Enumeration indicating what operations will be executed synchronously -- without the creation of a job. If an operation is included in both this property and SupportedAsynchronousActions then the underlying implementation is indicating that it may or may not create a job.Note: the following methods are not supported asynchronously: \\t - CreateGroup \\t - DeleteGroup \\t - AddMembers \\t - RemoveMembers \\t - AddReplicationEntity \\t - AddServiceAccessPoint \\t - AddSharedSecret.

This property is inherited from [**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md).

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

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>26–32767</dd> <dt>

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

[**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
</dt> <dt>

[iSCSI Target Server Reference](https://msdn.microsoft.com/library/hh830439)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md)
</dt> </dl>

 

 





