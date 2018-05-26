---
title: ModifyReplicaSynchronization method of the MSISCSITARGET\_ReplicationService class
description: Modifies to modify the synchronization association between two storage objects or between two replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b464a74f-b5b1-4890-a49a-f44352bc6d20
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyReplicaSynchronization method iSCSI Software Target API
- ModifyReplicaSynchronization method iSCSI Software Target API , MSISCSITARGET_ReplicationService class
- MSISCSITARGET_ReplicationService class iSCSI Software Target API , ModifyReplicaSynchronization method
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationService.ModifyReplicaSynchronization
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ModifyReplicaSynchronization method of the MSISCSITARGET\_ReplicationService class

Modifies to modify the synchronization association between two storage objects or between two replication groups.

This method overrides the method that is inherited from the **CIM\_ReplicationService** class.

## Syntax


```mof
uint32 ModifyReplicaSynchronization(
  [in]  uint16                      Operation,
  [in]  CIM_Synchronized        REF Synchronization,
  [in]  string                      ReplicationSettingData,
  [in]  CIM_StorageSynchronized REF SyncPair[],
  [out] CIM_ConcreteJob         REF Job,
  [out] CIM_SettingsDefineState REF SettingsState,
  [in]  boolean                     Force,
  [in]  uint16                      WaitForCopyState
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Specifies the type of modification to be made to the replica and related associations. Required.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)


</dt> <dd>

Abort the copy operation if possible.

</dd> <dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>**Activate Consistency** (3)


</dt> <dd>

Activate consistency if it is not already enabled. If consistency is already enabled, this operation has no effect.

</dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)


</dt> <dd>

Activate an inactive or prepared synchronized association.

</dd> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>**AddSyncPair** (5)


</dt> <dd>

Add pairs of elements that are already in a relationship to source and target groups, as specified in the *SyncPair* parameter.

</dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>**Deactivate Consistency** (6)


</dt> <dd>

Deactivate consistency if it is enabled. If consistency was not enabled, this operation has no effect.

</dd> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)


</dt> <dd>

Stop the data flow. Write operations to source elements are not copied to target elements. For snapshot replications, write operations to target elements are lost because the pointers to changed data are deleted.

</dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)


</dt> <dd>

Delete the synchronization between two storage objects. Treat the objects as independent after the synchronization is deleted.

</dd> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)


</dt> <dd>

Dissolve the synchronization between two storage objects; however, the target element continues to exist.

</dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)


</dt> <dd>

Use the target element as the source element.

</dd> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)


</dt> <dd>

Reverse the effect of **Failover**.

</dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)


</dt> <dd>

Suspend the synchronization between two storage objects. The implementation records the association to enable a faster re-synchronization.

This value can be used during a backup cycle to copy one of the objects while the other object remains in production.

</dd> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>**RemoveSyncPair** (13)


</dt> <dd>

Remove the pair that is specified in the *SyncPair* property from the source and target groups. The elements in the pair remain associated but do not remain in the groups.

</dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>**Resync Replica** (14)


</dt> <dd>

Re-establish the synchronization. The re-synchronization negates the action of a previous **Fracture** or **Split** operation. Re-create a point-in-time image for a snapshot or a clone replication. Restart a **Broken** or **Aborted** synchronization relationship.

</dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>**Restore from Replica** (15)


</dt> <dd>

Renew the contents of the original storage object from a replica.

</dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>**Resume** (16)


</dt> <dd>

Continue the copy operation of a suspended association.

</dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>**Reset To Sync** (17)


</dt> <dd>

Change the mode of the copy operation to **Synchronous** from the **Asynchronous** mode.

</dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>**Reset To Async** (18)


</dt> <dd>

Change the mode property of the copy operation to **Asynchronous** from the **Synchronous** mode.

</dd> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>**Return To ResourcePool** (19)


</dt> <dd>

Dissolve a snapshot and return the space it used back to the storage pool.

</dd> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>**Reverse Roles** (20)


</dt> <dd>

Reverse the roles of the elements so that the source element becomes the target element and vise versa.

</dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)


</dt> <dd>

Suspend the synchronization between two storage objects in the same way as the **Fracture** operation; however, take steps to ensure the target elements are consistent. For example, stop changes to the source elements, wait for copy operations between source and target elements to stop, then split the source and target elements.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)


</dt> <dd>

Stop the background copy that was previously started.

</dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (23)


</dt> <dd>

Causes the synchronization to be reinitialized.

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

Specifies the replication association between the source and the target elements. Required.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, specifies the replication setting data for the given *SyncType* parameter in the form of an embedded **CIM\_ReplicationSettingData** instance. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*SyncPair* \[in\]
</dt> <dd>

Specifies the **CIM\_StorageSynchronized** instance that describes the replication.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, which can be **NULL**, if the job is completed.

</dd> <dt>

*SettingsState* \[out\]
</dt> <dd>

On return, contains a reference to the association between the source element and a synchronization aspect instance. This parameter applies to operations such as Dissolve, which dissolves the synchronized relationship, but causes the **CIM\_SettingDefineState** association to be created.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Specifies how to handle operations that might cause an inconsistency among the target elements. If set to **True**, the client is not warned and the operation is performed.

</dd> <dt>

*WaitForCopyState* \[in\]
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

**DMTF Reserved** (7 4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097 32767)
</dt> <dt>

**Vendor Specific** (32768 = *value* )
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>SmIscsiTarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SMiSCSITargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





