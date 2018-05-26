---
title: SetReplicationRelationship method of the MSFT\_ReplicationGroup class
description: Modifies the relationship between replication groups.
ms.assetid: AEA4DB91-51E2-4F47-BC45-D58C82580AAA
keywords:
- SetReplicationRelationship method Windows Storage Management API
- SetReplicationRelationship method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , SetReplicationRelationship method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.SetReplicationRelationship
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetReplicationRelationship method of the MSFT\_ReplicationGroup class

Modifies the relationship between replication groups.

## Syntax


```mof
UInt32 SetReplicationRelationship(
  [in]  UInt16 Operation,
  [in]  String TargetGroup,
  [in]  String SourceStorageObjects[],
  [in]  String TargetStorageObjects[],
  [in]  String SyncPairs[],
  [out] String CreatedReplicaPeer,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

One of the following values:

<dl> <dt>

<span id="Abort"></span><span id="abort"></span><span id="ABORT"></span>**Abort** (2)
</dt> <dt>

<span id="ActivateConsistency"></span><span id="activateconsistency"></span><span id="ACTIVATECONSISTENCY"></span>**ActivateConsistency** (3)
</dt> <dt>

<span id="Activate"></span><span id="activate"></span><span id="ACTIVATE"></span>**Activate** (4)
</dt> <dt>

<span id="AddSyncPair"></span><span id="addsyncpair"></span><span id="ADDSYNCPAIR"></span>**AddSyncPair** (5)
</dt> <dt>

<span id="DeactivateConsistency"></span><span id="deactivateconsistency"></span><span id="DEACTIVATECONSISTENCY"></span>**DeactivateConsistency** (6)
</dt> <dt>

<span id="Deactivate"></span><span id="deactivate"></span><span id="DEACTIVATE"></span>**Deactivate** (7)
</dt> <dt>

<span id="Detach"></span><span id="detach"></span><span id="DETACH"></span>**Detach** (8)
</dt> <dt>

<span id="Dissolve"></span><span id="dissolve"></span><span id="DISSOLVE"></span>**Dissolve** (9)
</dt> <dt>

<span id="Failover"></span><span id="failover"></span><span id="FAILOVER"></span>**Failover** (10)
</dt> <dt>

<span id="Failback"></span><span id="failback"></span><span id="FAILBACK"></span>**Failback** (11)
</dt> <dt>

<span id="Fracture"></span><span id="fracture"></span><span id="FRACTURE"></span>**Fracture** (12)
</dt> <dt>

<span id="RemoveSyncPair"></span><span id="removesyncpair"></span><span id="REMOVESYNCPAIR"></span>**RemoveSyncPair** (13)
</dt> <dt>

<span id="ResyncReplica"></span><span id="resyncreplica"></span><span id="RESYNCREPLICA"></span>**ResyncReplica** (14)
</dt> <dt>

<span id="RestoreFromReplica"></span><span id="restorefromreplica"></span><span id="RESTOREFROMREPLICA"></span>**RestoreFromReplica** (15)
</dt> <dt>

<span id="Resume"></span><span id="resume"></span><span id="RESUME"></span>**Resume** (16)
</dt> <dt>

<span id="ResetToSync"></span><span id="resettosync"></span><span id="RESETTOSYNC"></span>**ResetToSync** (17)
</dt> <dt>

<span id="ResetToAsync"></span><span id="resettoasync"></span><span id="RESETTOASYNC"></span>**ResetToAsync** (18)
</dt> <dt>

<span id="ReturnToResourcePool"></span><span id="returntoresourcepool"></span><span id="RETURNTORESOURCEPOOL"></span>**ReturnToResourcePool** (19)
</dt> <dt>

<span id="ReverseRoles"></span><span id="reverseroles"></span><span id="REVERSEROLES"></span>**ReverseRoles** (20)
</dt> <dt>

<span id="Split"></span><span id="split"></span><span id="SPLIT"></span>**Split** (21)
</dt> <dt>

<span id="Suspend"></span><span id="suspend"></span><span id="SUSPEND"></span>**Suspend** (22)
</dt> <dt>

<span id="Unprepare"></span><span id="unprepare"></span><span id="UNPREPARE"></span>**Unprepare** (23)
</dt> </dl> </dd> <dt>

*TargetGroup* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica peer for the target group.

</dd> <dt>

*SourceStorageObjects* \[in\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying source objects by Id to be replicated. Consistency ordering is based on the order of objects in this array.

</dd> <dt>

*TargetStorageObjects* \[in\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying target objects by Id to be replicated. Consistency ordering is based on the order of objects in this array.

</dd> <dt>

*SyncPairs* \[in\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_Synchronized**](msft-synchronized.md) objects specifying the element replicas for **AddSyncPair** or **RemoveSyncPair**.

</dd> <dt>

*CreatedReplicaPeer* \[out\]
</dt> <dd>

This parameter receives a string that contains an embedded [**MSFT\_Synchronized**](msft-synchronized.md) object representing the association between the replication groups.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

</dd> </dl>

## Return value

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
</dt> <dt>

**The operation is not supported while the cluster is being upgraded.** (40009)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> </dl>

 

 





