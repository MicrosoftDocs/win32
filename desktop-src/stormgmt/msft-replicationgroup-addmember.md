---
title: AddMember method of the MSFT\_ReplicationGroup class
description: Adds members to this replication group.
ms.assetid: 1E6A5089-40BB-4401-AC4D-7A266FB18C46
keywords:
- AddMember method Windows Storage Management API
- AddMember method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , AddMember method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.AddMember
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

# AddMember method of the MSFT\_ReplicationGroup class

Adds members to this replication group.

## Syntax


```mof
UInt32 AddMember(
  [in]  String StorageObjects[],
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*StorageObjects* \[in\]
</dt> <dd>

An array of strings containing embedded [**MSFT\_StorageObject**](msft-storageobject.md) objects specifying the storage objects to add to the group.

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

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**The operation is not supported while the cluster is being upgraded.** (40009)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
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

 

 





