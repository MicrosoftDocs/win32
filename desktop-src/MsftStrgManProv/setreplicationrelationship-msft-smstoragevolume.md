---
title: SetReplicationRelationship method of the MSFT\_SMStorageVolume class
description: Updates a replication relationship between virtual disks.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 06d75d4b-f3f6-48aa-829e-3aabf10305ce
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetReplicationRelationship method
- SetReplicationRelationship method, MSFT_SMStorageVolume class
- MSFT_SMStorageVolume class, SetReplicationRelationship method
topic_type:
- apiref
api_name:
- MSFT_SMStorageVolume.SetReplicationRelationship
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetReplicationRelationship method of the MSFT\_SMStorageVolume class

Updates a replication relationship between virtual disks.

## Syntax


```mof
UInt32 SetReplicationRelationship(
  [in]            UInt16                 Operation,
  [in]            MSFT_SMReplicaPeer REF TargetStorageVolume,
  [in, optional]  String                 username,
  [in, optional]  String                 password,
  [out]           MSFT_SMJob         REF Job,
  [out, optional] MSFT_SMExtendedStatus  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

An integer that indicates the operation to perform on the replication relationship.

The possible values are:

<dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>

**Abort** (2)


</dt> <dd></dd> <dt>

<span id="ActivateConsistency"></span><span id="activateconsistency"></span><span id="ACTIVATECONSISTENCY"></span>

**ActivateConsistency** (3)


</dt> <dd></dd> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>

**Activate** (4)


</dt> <dd></dd> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>

**AddSyncPair** (5)


</dt> <dd></dd> <dt>

<span id="DeactivateConsistency"></span><span id="deactivateconsistency"></span><span id="DEACTIVATECONSISTENCY"></span>

**DeactivateConsistency** (6)


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

<span id="ResyncReplica"></span><span id="resyncreplica"></span><span id="RESYNCREPLICA"></span>

**ResyncReplica** (14)


</dt> <dd></dd> <dt>

<span id="RestoreFromReplica"></span><span id="restorefromreplica"></span><span id="RESTOREFROMREPLICA"></span>

**RestoreFromReplica** (15)


</dt> <dd></dd> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>

**Resume** (16)


</dt> <dd></dd> <dt>

<span id="ResetToSync"></span><span id="resettosync"></span><span id="RESETTOSYNC"></span>

**ResetToSync** (17)


</dt> <dd></dd> <dt>

<span id="ResetToAsync"></span><span id="resettoasync"></span><span id="RESETTOASYNC"></span>

**ResetToAsync** (18)


</dt> <dd></dd> <dt>

<span id="ReturnToResourcePool"></span><span id="returntoresourcepool"></span><span id="RETURNTORESOURCEPOOL"></span>

**ReturnToResourcePool** (19)


</dt> <dd></dd> <dt>

<span id="ReverseRoles"></span><span id="reverseroles"></span><span id="REVERSEROLES"></span>

**ReverseRoles** (20)


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



 (24)


</dt> <dd></dd> </dl> </dd> <dt>

*TargetStorageVolume* \[in\]
</dt> <dd>

A [**MSFT\_SMReplicaPeer**](msft-smreplicapeer.md) object that ndicates the replica target system to use when setting up a relationship of storage objects within the system.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password to use to authenticate the SMI-S provider. If this parameter is not set, the storage service will attempt to retrieve the credentials from the configuration provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

A reference to the [**MSFT\_SMJob**](msft-smjob.md) object that specifies a reference to a job if this method returns "Method Parameters Checked - Job Started". If this operation performs synchronously, this parameter is set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

A [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that specifies detailed status information about the result of this operation.

</dd> </dl>

## Return value

The possible return values are:

<dl> <dt>

**Success** (0)
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

**Object Not Found** (8)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMStorageVolume**](msft-smstoragevolume.md)
</dt> </dl>

 

 





