---
title: GetSupportedOperations method of the MSISCSITARGET\_ReplicationServiceCapabilities class
description: Retrieves a list of supported operations that can be performed by using the ModifyReplicaSynchronization method on a specified replication type and association type.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3054dffc-db21-4a4a-ab57-a66fb5b893b5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetSupportedOperations method iSCSI Software Target API", "GetSupportedOperations method iSCSI Software Target API , MSISCSITARGET_ReplicationServiceCapabilities class", "MSISCSITARGET_ReplicationServiceCapabilities class iSCSI Software Target API , GetSupportedOperations method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_ReplicationServiceCapabilities.GetSupportedOperations
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# GetSupportedOperations method of the MSISCSITARGET\_ReplicationServiceCapabilities class

Retrieves a list of supported operations that can be performed by using the [**ModifyReplicaSynchronization**](modifyreplicasynchronization-msiscsitarget-replicationservice.md) method on a specified replication type and association type.

This method is inherited from the **CIM\_ReplicationServiceCapabilities** class.

## Syntax


```mof
uint32 GetSupportedOperations(
  [in]  uint16 ReplicationType,
  [out] uint16 SupportedOperations[]
);
```



## Parameters

<dl> <dt>

*ReplicationType* \[in\]
</dt> <dd>

Specifies the replication type.

The [**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md).**SupportedReplicationTypes** property values are.

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


</dt> <dd>14–0x7FFF</dd> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>

**Vendor Specific**


</dt> <dd>0x8000 = *value* </dd> </dl> </dd> <dt>

*SupportedOperations* \[out\]
</dt> <dd>

On return, contains the list of supported operations.

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)


</dt> <dd>

Aborts the copy operation if possible.

</dd> <dt>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>

<span id="Activate_Consistency"></span><span id="activate_consistency"></span><span id="ACTIVATE_CONSISTENCY"></span>**Activate Consistency** (3)


</dt> <dd>

Activates consistency if it is not already enabled. If consistency is already enabled, this operation has no effect.

</dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)


</dt> <dd>

Activates an inactive or prepared synchronized association.

</dd> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>**AddSyncPair** (5)


</dt> <dd>

Adds pairs of elements already in a relationship to source and target groups, as specified in the *SyncPair* parameter.

</dd> <dt>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>

<span id="Deactivate_Consistency"></span><span id="deactivate_consistency"></span><span id="DEACTIVATE_CONSISTENCY"></span>**Deactivate Consistency** (6)


</dt> <dd>

Deactivates consistency if enabled. If consistency was not enabled, this operation has no effect.

</dd> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)


</dt> <dd>

Stops the data flow. Write operations to the source element are not copied to the target element. For Snapshot replications, write operations to the target element are lost because the pointers to changed data are deleted.

</dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)


</dt> <dd>

Deletes the synchronization between two storage objects. Treats the objects as independent thereafter.

</dd> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)


</dt> <dd>

Dissolves the synchronization between two storage objects; however, the target element continues to exist.

</dd> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)


</dt> <dd>

Uses the target element as the source element.

</dd> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)


</dt> <dd>

Reverses the effect of **Failover**.

</dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)


</dt> <dd>

Suspends the synchronization between two storage objects. The implementation records the association to enable a faster re-synchronization.

This operation can be used during a backup cycle to enable one of the objects to be copied while the other object remains in production.

</dd> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>**RemoveSyncPair** (13)


</dt> <dd>

Removes the pair that is specified in the *SyncPair* property from the source and target groups. The pair continues to remain associated but does not remain in the groups.

</dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>**Resync Replica** (14)


</dt> <dd>

Re-establishes the synchronization. This operation negates the action of a previous **Fracture** or **Split** operation. Re-creates a point-in-time (PIT) image for a **Snapshot** or a **Clone** replication. Restarts a **Broken** or **Aborted** synchronization relationship.

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

Changes the **Mode** of the copy operation to **Synchronous** from the **Asynchronous** mode.

</dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>**Reset To Async** (18)


</dt> <dd>

Changes the **Mode** of the copy operation to **Asynchronous** from the **Synchronous** mode.

</dd> <dt>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>

<span id="Return_To_ResourcePool"></span><span id="return_to_resourcepool"></span><span id="RETURN_TO_RESOURCEPOOL"></span>**Return To ResourcePool** (19)


</dt> <dd>

Dissolves a snapshot and returns the space that it used back to the storage pool.

</dd> <dt>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>

<span id="Reverse_Roles"></span><span id="reverse_roles"></span><span id="REVERSE_ROLES"></span>**Reverse Roles** (20)


</dt> <dd>

Reverses the roles so that the source element becomes the target element and vise versa.

</dd> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)


</dt> <dd>

Same as **Fracture**; however, steps are taken to ensure the target elements are consistent. For example, stops changes to the source elements, waits for copy operations between source and target elements to stop, then splits the source and target groups or elements.

</dd> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)


</dt> <dd>

Stops the background copy previously started.

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

</dd> </dl> </dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unknown** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**In Use** (6)
</dt> <dt>

**DMTF Reserved** (7–0x7FFF)
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

[**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
</dt> <dt>

[**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
</dt> <dt>

[**ModifyReplicaSynchronization**](modifyreplicasynchronization-msiscsitarget-replicationservice.md)
</dt> </dl>

 

 





