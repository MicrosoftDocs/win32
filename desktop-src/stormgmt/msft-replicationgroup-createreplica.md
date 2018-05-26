---
title: CreateReplica method of the MSFT\_ReplicationGroup class
description: Creates a replication relationship between replication groups.
ms.assetid: 785C38FF-635A-4146-ABBC-8C28027B24A4
keywords:
- CreateReplica method Windows Storage Management API
- CreateReplica method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , CreateReplica method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.CreateReplica
api_location:
- adojet.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CreateReplica method of the MSFT\_ReplicationGroup class

Creates a replication relationship between replication groups.

## Syntax


```mof
UInt32 CreateReplica(
  [in]           String              FriendlyName,
  [in]           String              TargetStorageSubsystem,
  [in]           String              TargetGroupObjectId,
  [in, optional] String              TargetStoragePoolObjectId,
  [in, optional] UInt32              RecoveryPointObjective,
  [in]           String              ReplicationSettings,
  [in]           UInt16              SyncType,
  [out]          String              CreatedReplicaPeer,
  [out]          MSFT_StorageJob REF CreatedStorageJob,
  [out]          String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

An end-user relevant name for the element being created. If **NULL**, then a system-supplied default name can be used. The value will be stored in the **FriendlyName** property for the created element.

</dd> <dt>

*TargetStorageSubsystem* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicaPeer**](msft-replicapeer.md) object specifying the replica target subsystem.

</dd> <dt>

*TargetGroupObjectId* \[in\]
</dt> <dd>

Specifies the replication group target on the target machine.

</dd> <dt>

*TargetStoragePoolObjectId* \[in, optional\]
</dt> <dd>

A storage pool on the target to be used as the source for creating the necessary target storage elements. This parameter is ignored if the target group contains any elements.

</dd> <dt>

*RecoveryPointObjective* \[in, optional\]
</dt> <dd>

Indicates the maximum interval in which data might be lost. For synchronous copy operations, *RecoveryPointObjective* is 0. For asynchronous copy operations *RecoveryPointObjective* represents the interval since the most recent transmission of data to the target element.

</dd> <dt>

*ReplicationSettings* \[in\]
</dt> <dd>

A string that contains an embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) object to be applied.

</dd> <dt>

*SyncType* \[in\]
</dt> <dd>

The type of copy that will be made. One of the following values:



| Value                                                                                                                                                                                                                                                              | Meaning                                                          |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>..</dt> </dl>               | This value is reserved for system use.<br/>                |
| <span id="Mirror"></span><span id="mirror"></span><span id="MIRROR"></span><dl> <dt>**Mirror**</dt> <dt>6</dt> </dl>                                            | Create and maintain a copy of the source.<br/>             |
| <span id="Snapshot"></span><span id="snapshot"></span><span id="SNAPSHOT"></span><dl> <dt>**Snapshot**</dt> <dt>7</dt> </dl>                                    | Create a volume shadow copy of the source.<br/>            |
| <span id="Clone"></span><span id="clone"></span><span id="CLONE"></span><dl> <dt>**Clone**</dt> <dt>8</dt> </dl>                                                | Create a point-in-time, full copy of the source.<br/>      |
| <span id="TokenizedClone"></span><span id="tokenizedclone"></span><span id="TOKENIZEDCLONE"></span><dl> <dt>**TokenizedClone**</dt> <dt>9</dt> </dl>            | Create a point-in-time, tokenized copy of the source.<br/> |
| <span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span><dl> <dt>**DMTF Reserved**</dt> <dt>..</dt> </dl>               | This value is reserved for system use.<br/>                |
| <span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span><dl> <dt>**Vendor Specific**</dt> <dt>0x8000..</dt> </dl> | These values are reserved for vendors.<br/>                |



 

</dd> <dt>

*CreatedReplicaPeer* \[out\]
</dt> <dd>

This parameter receives a string that contains an embedded [**MSFT\_Synchronized**](msft-synchronized.md) object representing the association between the replication groups.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

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
| Header<br/>                   | <dl> <dt>Adojet.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ReplicationGroup**](msft-replicationgroup.md)
</dt> </dl>

 

 





