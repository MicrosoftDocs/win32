---
title: SetFriendlyName method of the MSFT\_StoragePool class
description: Sets the friendly name for the storage pool.
ms.assetid: 6FD041BB-0554-4E20-896E-4E54DB287384
keywords:
- SetFriendlyName method Windows Storage Management API
- SetFriendlyName method Windows Storage Management API , MSFT_StoragePool class
- MSFT_StoragePool class Windows Storage Management API , SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_StoragePool.SetFriendlyName
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

# SetFriendlyName method of the MSFT\_StoragePool class

Sets the friendly name for the storage pool.

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

The friendly name to be set for the storage pool. This parameter is required and cannot be NULL.

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

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> </dl>

 

 





