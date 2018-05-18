---
title: ModifySynchronization method of the MSISCSITARGET\_StorageConfigurationService class
description: Modifies the synchronization association between two storage objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f0779be3-c3bc-4bc9-814d-ce0fcbe940b5'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifySynchronization method iSCSI Software Target API", "ModifySynchronization method iSCSI Software Target API , MSISCSITARGET_StorageConfigurationService class", "MSISCSITARGET_StorageConfigurationService class iSCSI Software Target API , ModifySynchronization method"]
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageConfigurationService.ModifySynchronization
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
---

# ModifySynchronization method of the MSISCSITARGET\_StorageConfigurationService class

Modifies the synchronization association between two storage objects.

This method is inherited from the **CIM\_StorageConfigurationService** class.

## Syntax


```mof
uint32 ModifySynchronization(
  [in]  uint16                      Operation,
  [out] CIM_ConcreteJob Ref         Job,
  [in]  CIM_StorageSynchronized Ref Synchronization
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Specifies the type of modification that is applied to the replica.

The possible values are.

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved**


</dt> <dd>

Reserved.

</dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (2)


</dt> <dd>

Detaches the synchronization between two storage objects. Starts to treat the objects as independent.

</dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (3)


</dt> <dd>

Suspends the synchronization between two storage objects. The implementation records the association to enable a faster re-synchronization.

This operation can be used during a backup cycle to enable one of the objects to be copied while the other object remains in production.

</dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>**Resync Replica** (4)


</dt> <dd>

Re-establishes the synchronization. This operation negates the action of a previous **Fracture** or **Split** operation. Re-creates a point-in-time (PIT) image for a **Snapshot** or a **Clone** replication. Restarts a **Broken** or **Aborted** synchronization relationship.

</dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>**Restore from Replica** (5)


</dt> <dd>

Renews the contents of the original storage object from a replica.

</dd> <dt>

<span id="Prepare"></span><span id="prepare"></span><span id="PREPARE"></span>

<span id="Prepare"></span><span id="prepare"></span><span id="PREPARE"></span>**Prepare** (6)


</dt> <dd>

Gets the association ready for a **Resync Replica** operation to take place. Some implementations require performing this operation to keep the **Resync** operation as fast as possible. Some implementations might start the copy engine.

</dd> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (7)


</dt> <dd>

Clears a prepared state if a **Prepare** operation is not to be followed by a **Resync Replica** operation.

</dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>**Quiesce** (8)


</dt> <dd>

Some applications require notification so that they can ready the link for an operation. For example, flush any cached data or buffered changes. The copy engine is stopped for **UnSyncAssoc** replications.

</dd> <dt>

<span id="Unquiesce"></span><span id="unquiesce"></span><span id="UNQUIESCE"></span>

<span id="Unquiesce"></span><span id="unquiesce"></span><span id="UNQUIESCE"></span>**Unquiesce** (9)


</dt> <dd>

Take the link from the quiesced state without executing the intended operation.

</dd> <dt>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>

<span id="Reset_To_Sync"></span><span id="reset_to_sync"></span><span id="RESET_TO_SYNC"></span>**Reset To Sync** (10)


</dt> <dd>

Change the **Mode** of the copy operation to **Synchronous** from the **Asynchronous** mode.

</dd> <dt>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>

<span id="Reset_To_Async"></span><span id="reset_to_async"></span><span id="RESET_TO_ASYNC"></span>**Reset To Async** (11)


</dt> <dd>

Change the **Mode** of the copy operation to **Asynchronous** from the **Synchronous** mode.

</dd> <dt>

<span id="Start_Copy"></span><span id="start_copy"></span><span id="START_COPY"></span>

<span id="Start_Copy"></span><span id="start_copy"></span><span id="START_COPY"></span>**Start Copy** (12)


</dt> <dd>

Initiates a full background copy of the source to the **UnSyncAssoc** replica. The replica enters Frozen state when the copy operation is completed.

</dd> <dt>

<span id="Stop_Copy"></span><span id="stop_copy"></span><span id="STOP_COPY"></span>

<span id="Stop_Copy"></span><span id="stop_copy"></span><span id="STOP_COPY"></span>**Stop Copy** (13)


</dt> <dd>

Stops the background copy that was previously started.

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

*Job* \[out\]
</dt> <dd>

On return, contains a reference to the job, if a job is created and not completed.

</dd> <dt>

*Synchronization* \[in\]
</dt> <dd>

Specifies the [**MSISCSITARGET\_StorageSynchronized**](msiscsitarget-storagesynchronized.md) association to modify.

</dd> </dl>

## Return value

This method returns one of the following values.

<dl> <dt>

**Job Completed with No Error** (0)
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

**DMTF Reserved** (7–0x0FFF)
</dt> <dt>

**Method Parameters Checked - Job Started** (0x1000)
</dt> <dt>

**Method Reserved** (0x1001–0x7FFF)
</dt> <dt>

**Vendor Specific** (0x8000–0xFFFF)
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

[**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
</dt> <dt>

[**MSISCSITARGET\_StorageSynchronized**](msiscsitarget-storagesynchronized.md)
</dt> </dl>

 

 





