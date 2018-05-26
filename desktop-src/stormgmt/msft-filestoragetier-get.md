---
title: Get method of the MSFT\_FileStorageTier class
description: Gets tier information for pinned files.
ms.assetid: 5EC4BA2D-159F-4CE4-995C-1690A1DAF3F4
keywords:
- Get method Windows Storage Management API
- Get method Windows Storage Management API , MSFT_FileStorageTier class
- MSFT_FileStorageTier class Windows Storage Management API , Get method
topic_type:
- apiref
api_name:
- MSFT_FileStorageTier.Get
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

# Get method of the MSFT\_FileStorageTier class

Gets tier information for pinned files.

## Syntax


```mof
UInt32 Get(
  [in]  String FilePath,
  [in]  Char16 VolumeDriveLetter,
  [in]  String VolumePath,
  [in]  String Volume,
  [out] String FileStorageTier[]
);
```



## Parameters

<dl> <dt>

*FilePath* \[in\]
</dt> <dd>

The path of the file.

</dd> <dt>

*VolumeDriveLetter* \[in\]
</dt> <dd>

The drive letter that identifies the drive where the file resides.

</dd> <dt>

*VolumePath* \[in\]
</dt> <dd>

The volume path.

</dd> <dt>

*Volume* \[in\]
</dt> <dd>

The volume, an [**MSFT\_Volume**](msft-volume.md) object.

</dd> <dt>

*FileStorageTier* \[out\]
</dt> <dd>

The tier information, an array of [**MSFT\_FileStorageTier**](msft-filestoragetier.md) objects.

</dd> </dl>

## Remarks

Only one of the input parameters is required to specify the file storage tier.

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileStorageTier**](msft-filestoragetier.md)
</dt> </dl>

 

 





