---
title: DeleteObject method of the MSFT\_FileServer class
description: Deletes the file server. If the file server contains any file shares, these shares must be removed first.
ms.assetid: 81C51A89-AB40-4125-919E-EFADB101AC83
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_FileServer class
- MSFT_FileServer class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_FileServer.DeleteObject
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

# DeleteObject method of the MSFT\_FileServer class

Deletes the file server. If the file server contains any file shares, these shares must be removed first.

## Syntax


```mof
UInt32 DeleteObject(
  [out] MSFT_StorageJob REF CreatedStorageJob,
  [out] String              ExtendedStatus
);
```



## Parameters

<dl> <dt>

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

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cache out of date** (40003)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**This operation is not supported on local file servers.** (58000)
</dt> <dt>

**The file server could not complete the operation because its health or operational status does not permit it.** (58006)
</dt> <dt>

**The file server could not complete the operation because its configuration is read-only.** (58007)
</dt> <dt>

**The file server contains virtual disks.** (58008)
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

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> </dl>

 

 





