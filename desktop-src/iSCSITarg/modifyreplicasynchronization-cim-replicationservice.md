---
title: ModifyReplicaSynchronization method of the CIM\_ReplicationService class
description: Modify (or start a job to modify) the synchronization association between two storage objects or replication groups.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7ab7dcf3-7e92-474b-bef8-c0b5666b93a3
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ModifyReplicaSynchronization method iSCSI Software Target API
- ModifyReplicaSynchronization method iSCSI Software Target API , CIM_ReplicationService class
- CIM_ReplicationService class iSCSI Software Target API , ModifyReplicaSynchronization method
topic_type:
- apiref
api_name:
- CIM_ReplicationService.ModifyReplicaSynchronization
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifyReplicaSynchronization method of the CIM\_ReplicationService class

Modify (or start a job to modify) the synchronization association between two storage objects or replication groups. If 0 is returned, the function completed successfully and no ConcreteJob instance was created. If 0x1000 is returned, a ConcreteJob was started and a reference to this Job is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

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

Operation describes the type of modification to be made to the replica and/or to the related associations. Abort: Abort the copy operation if it is possible. Activate Consistency: if consistency was not requested when CreateGroupReplica was called. If Consistency is already active, no modification is made. Activate: Activate an inactive or prepared Synchronized association. AddSyncPair: Add pairs of elements already in a relationship to source and target groups -- see SyncPair parameter. Deactivate Consistency: Deactivate consistency. If consistency was not enabled, this operation has no effect. Deactivate: Stop the data flow. Writes to source element are not copied to target. For Snapshots, writes to target are lost as the pointers to changed data are deleted. Detach: 'Forget' the synchronization between two storage objects. Start to treat the objects as independent. Dissolve: Dissolve the synchronization between two storage objects, however, the target element continues to exist. Failover: Use the target element as the source elements. Failback: Reverse the effect of failback. Fracture: Suspend the synchronization between two storage objects. The association and (typically) changes are remembered to allow a fast resynchronization. This may be used during a backup cycle to allow one of the objects to be copied while the other remains in production. RemoveSyncPair: Remove the pair associated via StorageSynchronized from the source and target groups. The pair continue to remain associated but not in the groups. Resync Replica: Re-establish the synchronization. This will negate the action of a previous Fracture/Split operation. Recreate a Point In Time image for a Snapshot or a Clone replication. Restart a Broken or Aborted synchronization relationship. Restore from Replica: Renew the contents of the original storage object from a replica. Resume: Continue the copy operation of a suspended association. Reset To Sync: Change the Mode of the copy operation to Synchronous (e.g., from the Asynchronous Mode). Reset To Async: Change the Mode of the copy operation to Asynchronous (e.g., from the Synchronous Mode). Return to ResourcePool: Dissolve a snapshot and free up its space back to the storage pool. Reverse Roles: Source element becomes the target element and vise versa. Split: Same as Fracture, however steps are taken to ensure the target elements are consistent. For example, stop I/O to source elements, wait for in-transit copy operations between source and target elements to stop, then instantly split source/target groups/elements. Suspend: Stop the background copy previously started. Unprepare: Causes the synchronization to be reinitialized.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

**Abort** (2)


</dt> <dd></dd> <dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

**Activate Consistency** (3)


</dt> <dd></dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

**Activate** (4)


</dt> <dd></dd> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>

**AddSyncPair** (5)


</dt> <dd></dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

**Deactivate Consistency** (6)


</dt> <dd></dd> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>

**Deactivate** (7)


</dt> <dd></dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

**Detach** (8)


</dt> <dd></dd> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>

**Dissolve** (9)


</dt> <dd></dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

**Failover** (10)


</dt> <dd></dd> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>

**Failback** (11)


</dt> <dd></dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

**Fracture** (12)


</dt> <dd></dd> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>

**RemoveSyncPair** (13)


</dt> <dd></dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

**Resync Replica** (14)


</dt> <dd></dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

**Restore from Replica** (15)


</dt> <dd></dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

**Resume** (16)


</dt> <dd></dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

**Reset To Sync** (17)


</dt> <dd></dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

**Reset To Async** (18)


</dt> <dd></dd> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>

**Return To ResourcePool** (19)


</dt> <dd></dd> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>

**Reverse Roles** (20)


</dt> <dd></dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

**Split** (21)


</dt> <dd></dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

**Suspend** (22)


</dt> <dd></dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

**Unprepare** (23)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>24 32767</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>32768 65535</dd> </dl> </dd> <dt>

*Synchronization* \[in\]
</dt> <dd>

The reference to the replication association describing the elements/groups relationship.

</dd> <dt>

*ReplicationSettingData* \[in\]
</dt> <dd>

If provided, it overrides the default replication setting data for the given SyncType. If not provided, the management server uses the default replication setting data.

</dd> <dt>

*SyncPair* \[in\]
</dt> <dd>

This parameter applies to AddSyncPair/RemoveSyncPair Operations.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be NULL if the task completed).

</dd> <dt>

*SettingsState* \[out\]
</dt> <dd>

Reference to the association between the source element and an instance of SynchronizationAspect. This parameters applies to operations such as Dissolve, which dissolves the Synchronized relationship, but causes the SettingDefineState association to be created.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Some operations may cause an inconsistency among the target elements. If true, the client is not warned and the operation is performed.

</dd> <dt>

*WaitForCopyState* \[in\]
</dt> <dd>

Method must wait until this CopyState is reached before returning. Only a subset of valid CopyStates apply. For example, Initialized: Associations have been established, but there is no data flow. Inactive: Initialization is complete, but the data flow remains idle until it is activated. Synchronized: Replicas are an exact copy of the source. UnSynchronized: Copy operation is in progress. Fractured/Split: Target elements are separated from the source elements. Etc.

</dd> </dl>

## Return value

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

**Vendor Specific** (32768 4294967295)
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

**CIM\_ReplicationService**
</dt> </dl>

 

 





