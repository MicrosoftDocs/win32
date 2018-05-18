---
title: ModifySynchronization method of the CIM\_StorageConfigurationService class
description: Modify (or start a job to modify) the synchronization association between two storage objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '11d9980a-f373-44f9-a44a-16e0bb9ca5d0'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["ModifySynchronization method iSCSI Software Target API", "ModifySynchronization method iSCSI Software Target API , CIM_StorageConfigurationService class", "CIM_StorageConfigurationService class iSCSI Software Target API , ModifySynchronization method"]
topic_type:
- apiref
api_name:
- CIM_StorageConfigurationService.ModifySynchronization
api_location:
- SMiSCSITargetProv.dll
api_type:
- COM
---

# ModifySynchronization method of the CIM\_StorageConfigurationService class

Modify (or start a job to modify) the synchronization association between two storage objects. If 0 is returned, the function completed successfully and no ConcreteJob instance was created. If 0x1000 is returned, a ConcreteJob was started and a reference to this Job is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

## Syntax


```mof
uint32 ModifySynchronization(
  [in]  uint16                      Operation,
  [out] CIM_ConcreteJob         REF Job,
  [in]  CIM_StorageSynchronized REF Synchronization
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

Operation describes the type of modification to be made to the replica. Values are:

Detach: 'Forget' the synchronization between two storage objects. Start to treat the objects as independent.

Fracture: Suspend the synchronization between two storage objects using Sync or Async replication.

The association and (typically) changes are remembered to allow a fast resynchronization. This may be used during a backup cycle to allow one of the objects to be copied while the other remains in production.

Resync Replica: Re-establish the synchronization of a Sync or Async replication. This will negate the action of a previous Fracture operation. Recreate a Point In Time image for an UnSyncAssoc replication.

Restore from Replica: Renew the contents of the original storage object from a replica.

Prepare: Get the link ready for a Resync operation to take place. Some implementations will require this operation to be invoked to keep the Resync operation as fast as possible. May start the copy engine.

Unprepare: Clear a prepared state if a Prepare is not to be followed by a Resync operation.

Quiesce: Some applications require notification so that they can ready the link for an operation. For example flush any cached data or buffered changes. The copy engine is stopped for UnSyncAssoc replications.

Unquiesce: Take the link from the quiesced state (without executing the intended operation.

Start Copy: initiate a full background copy of the source to the UnSyncAssoc replica. Replica enters Frozen state when copy operation is completed.

Stop Copy: stop the background copy previously started. Reset To Sync: Change the CopyType of the association to Sync (e.g., from the Async CopyType).

Reset To Async: Change the CopyType of the association to Async (e.g., from the Sync CopyType).

<dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (0)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved** (1)


</dt> <dd></dd> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>

**Detach** (2)


</dt> <dd></dd> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>

**Fracture** (3)


</dt> <dd></dd> <dt>

<span id="Resync_Replica"></span><span id="resync_replica"></span><span id="RESYNC_REPLICA"></span>

**Resync Replica** (4)


</dt> <dd></dd> <dt>

<span id="Restore_from_Replica"></span><span id="restore_from_replica"></span><span id="RESTORE_FROM_REPLICA"></span>

**Restore from Replica** (5)


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


</dt> <dd>32768–65535</dd> </dl> </dd> <dt>

*Job* \[out\]
</dt> <dd>

Reference to the job (may be null if the task completed).

</dd> <dt>

*Synchronization* \[in\]
</dt> <dd>

The referenced to the StorageSynchronized association describing the storage source/replica relationship.

</dd> </dl>

## Return value

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

**DMTF Reserved** (7–4095)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Method Reserved** (4097–32767)
</dt> <dt>

**Vendor Specific** (32768–65535)
</dt> </dl>

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

[**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
</dt> </dl>

 

 





