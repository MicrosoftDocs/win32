---
title: ModifyListSynchronization method of the MSISCSITARGET\_ReplicationService class
description: Modifies an array of synchronization associations between two storage objects or replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5d381d25-ae4b-4f75-8f19-87047f05ee89'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifyListSynchronization method iSCSI Software Target API", "ModifyListSynchronization method iSCSI Software Target API , MSISCSITARGET_ReplicationService class", "MSISCSITARGET_ReplicationService class iSCSI Software Target API , ModifyListSynchronization method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.ModifyListSynchronization
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# ModifyListSynchronization method of the MSISCSITARGET\_ReplicationService class

Modifies an array of synchronization associations between two storage objects or replication groups.

This method is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 ModifyListSynchronization(
  [in]           uint16                      Operation,
  [in]           CIM_Synchronized Ref        Synchronization[],
  [in, optional] string                      ReplicationSettingData,
  [out]          CIM_ConcreteJob Ref         Job,
  [out]          CIM_SettingsDefineState Ref SettingsState[],
  [in]           boolean                     Force,
  [in, optional] uint16                      WaitForCopyState
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Specifies the type of modification to be made to the replica and the related associations. Required.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)


</dt> <dd>

Aborts a copy operation if possible.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (3)


</dt> <dd></dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)


</dt> <dd>

Activates an inactive or prepared **CIM\_Synchronized** association.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd></dd> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)


</dt> <dd>

Stops the data flow. Write operations to the source element are not copied to the target. For snapshot replications, write operations to the target are lost because the pointers to changed data are deleted.

</dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)


</dt> <dd>

Ends the synchronization between two storage objects. Starts to treat the objects as independent.

</dd> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)


</dt> <dd>

Dissolves the synchronization between two storage objects. The target element continues to exist.

</dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)


</dt> <dd>

Reverses the direction of the synchronization. Use the target element as the source element.

</dd> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)


</dt> <dd>

Reverses the effect of a **Failover**.

</dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)


</dt> <dd>

Suspends the synchronization between two storage objects that use mirror or snapshot replication. The association and, typically, the changes are saved for fast re-synchronization. This value can be used during a backup cycle to copy one of the objects while the other object remains in production.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (13)


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>**Resync Replica** (14)


</dt> <dd>

Re-establishes the synchronization. This negates the action of a previous Fracture/Split operation, re-creates a point-in-time image for a snapshot or a clone replication, or restarts a **Broken** or **Aborted** synchronization relationship.

</dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>**Restore from Replica** (15)


</dt> <dd>

Renews the contents of the original storage object from a replica.

</dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>**Resume** (16)


</dt> <dd>

Continues the copy operation of a suspended association.

</dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>**Reset To Sync** (17)


</dt> <dd>

Changes the **Mode** of the copy operations to **Synchronous**.

</dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>**Reset To Async** (18)


</dt> <dd>

Changes the **Mode** of the copy operations to **Asynchronous**.

</dd> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>**Return To ResourcePool** (19)


</dt> <dd>

Dissolves a snapshot and returns its space to the storage pool.

</dd> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>**Reverse Roles** (20)


</dt> <dd>

Makes the source element the target element and vise versa.

</dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)


</dt> <dd>

Suspends the synchronization between two storage objects like the **Fracture** operation; however, steps are taken to ensure the target elements are consistent. For example, stop I/O to the source elements, wait for in-transit copy operations between source and target elements to stop, then split the source and target elements.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)


</dt> <dd>

Stops the background copy that was previously started.

</dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (23)


</dt> <dd>

Reinitializes the synchronization.

</dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific**


</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

*Synchronization* \[in\]
</dt> <dd>

Specifies the replication associations on which to perform the operation. Required.

All elements of this array must be the same concrete class, for example **CIM\_StorageSynchronized** or **CIM\_GroupSynchronized**, and must have the same **SyncType** and **Mode** properties. The *Operation* parameter must be valid for the **ReplicationType**, **SyncType**, **Mode** properties, and whether it is local or remote.

</dd> <dt>

*ReplicationSettingData* \[in, optional\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data. Optional.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*SettingsState* \[out\]
</dt> <dd>

On return, contains references to the associations between the source element and a synchronization aspect instance. This parameter applies to operations such as **Dissolve**, which dissolves the synchronized relationship, but causes the **CIM\_SettingDefineState** association to be created.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Specifies how to handle operations that might cause an inconsistency among the target elements. If set to **True**, the client is not warned and the operation is performed.

</dd> <dt>

*WaitForCopyState* \[in, optional\]
</dt> <dd>

Specifies the **CopyState** value that must be reached before this method returns. Only a subset of valid values applies.

For example.

-   **Initialized**: Associations have been established, but there is no data flow.
-   **Inactive**: Initialization is complete, but the data flow remains idle until it is activated.
-   **Synchronized**: Replicas are an exact copy of the source.
-   **UnSynchronized**: Copy operation is in progress.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





