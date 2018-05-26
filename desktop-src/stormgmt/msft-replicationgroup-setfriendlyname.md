---
title: SetFriendlyName method of the MSFT\_ReplicationGroup class
description: Sets the friendly name for the replication group.
ms.assetid: 3336F133-E1D6-43CA-AF8C-A90313CA097B
keywords:
- SetFriendlyName method Windows Storage Management API
- SetFriendlyName method Windows Storage Management API , MSFT_ReplicationGroup class
- MSFT_ReplicationGroup class Windows Storage Management API , SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_ReplicationGroup.SetFriendlyName
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

# SetFriendlyName method of the MSFT\_ReplicationGroup class

Sets the friendly name for the replication group.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]  String FriendlyName,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The friendly name to be set. This parameter is required and cannot be NULL.

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

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
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

 

 





