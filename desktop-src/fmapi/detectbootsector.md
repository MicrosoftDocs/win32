---
title: DetectBootSector function
description: Validates the correctness of the volume boot sector and provides data that is used to access the internal on-disk structures of the file system.
ms.assetid: 245641cb-1ee8-4ce5-84db-1d29489d2c3f
keywords:
- DetectBootSector function Files
topic_type:
- apiref
api_name:
- DetectBootSector
api_location:
- Fmapi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DetectBootSector function

Validates the correctness of the volume boot sector and provides data that is used to access the internal on-disk structures of the file system.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
BOOL WINAPI DetectBootSector(
  _In_  CONST UCHAR*      BootSector,
  _Out_ PBOOT_SECTOR_INFO BootSectorParams
);
```



## Parameters

<dl> <dt>

*BootSector* \[in\]
</dt> <dd>

A pointer to the first 512 bytes of the boot sector. The size of this buffer should always be 512 bytes, even if the sector size of the drive is not 512 bytes.

</dd> <dt>

*BootSectorParams* \[out\]
</dt> <dd>

A pointer to a [**BOOT\_SECTOR\_INFO**](boot-sector-info.md) structure that receives the boot sector information if a boot sector is detected.

</dd> </dl>

## Return value

If a boot sector is detected, the return value is nonzero.

If a boot sector is not detected, the return value is zero.

## Remarks

This function has no associated header file or import library. You must use the [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) and [**GetProcAddress**](https://msdn.microsoft.com/library/windows/desktop/ms683212) functions to dynamically link to fmapi.dll.

The **DetectBootSector** function supports FAT and NTFS file systems.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                 |
| DLL<br/>                      | <dl> <dt>Fmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[**BOOT\_SECTOR\_INFO**](boot-sector-info.md)
</dt> </dl>

 

 





