---
title: CreateReplicationGroup method of the MSFT\_StorageSubSystem class
description: Creates a replication group on a storage subsystem.
ms.assetid: B6B5CCB3-1B4B-4323-8BE9-145112A5FD70
keywords:
- CreateReplicationGroup method Windows Storage Management API
- CreateReplicationGroup method Windows Storage Management API , MSFT_StorageSubSystem interface
- MSFT_StorageSubSystem interface Windows Storage Management API , CreateReplicationGroup method
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem.CreateReplicationGroup
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateReplicationGroup method of the MSFT\_StorageSubSystem class

Creates a replication group on a storage subsystem.

## Syntax


```mof
UInt32 CreateReplicationGroup(
  [in]  String              FriendlyName,
  [in]  String              Description,
  [in]  String              StorageElements[],
  [in]  String              ReplicationSettings[],
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              CreatedReplicationGroup,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

Allows the user to specify the *FriendlyName* when the replication group is created. A *FriendlyName* is expected to be descriptive, but it is not required to be unique.

Note that some storage subsystems do not allow setting a friendly name during replication group creation. If a subsystem doesn't support this, replication group creation will still succeed, but the replication group may have a different name assigned to it.

This parameter is required and cannot be NULL.

</dd> <dt>

*Description* \[in\]
</dt> <dd>

A description of the purpose of the replication group.

This parameter is required and cannot be NULL.

</dd> <dt>

*StorageElements* \[in\]
</dt> <dd>

An array of strings that contain embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects. These storage objects must be of the same type as the source elements to be replicated. The ordering in this array determines the consistency ordering of the element replicas.

</dd> <dt>

*ReplicationSettings* \[in\]
</dt> <dd>

An array of strings that contain embedded [**MSFT\_ReplicationSettings**](msft-replicationsettings.md) objects to be configured on each storage element.

</dd> <dt>

*CreatedStorageJob* \[out\]
</dt> <dd>

Returns a reference to the storage job object used to track the long-running operation.

</dd> <dt>

*CreatedReplicationGroup* \[out\]
</dt> <dd>

If the replication group is created successfully, this parameter receives a string that contains an embedded [**MSFT\_ReplicationGroup**](msft-replicationgroup.md) object.

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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





