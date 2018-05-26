---
title: DeleteObject method of the MSFT\_Volume class
description: Deletes the volume.
ms.assetid: FDD37FD3-D0F1-4357-ADFD-E8D2CCCBE383
keywords:
- DeleteObject method Windows Storage Management API
- DeleteObject method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , DeleteObject method
topic_type:
- apiref
api_name:
- MSFT_Volume.DeleteObject
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

# DeleteObject method of the MSFT\_Volume class

Deletes the volume.

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

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





