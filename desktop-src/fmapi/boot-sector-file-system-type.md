---
title: BOOT\_SECTOR\_FILE\_SYSTEM\_TYPE enumeration
description: Defines the valid file system types that can be recognized by the DetectBootSector function.
ms.assetid: 305cf8e0-a71b-4ba6-b7df-6ac95c792585
keywords:
- BOOT_SECTOR_FILE_SYSTEM_TYPE enumeration Files
topic_type:
- apiref
api_name:
- BOOT_SECTOR_FILE_SYSTEM_TYPE
api_type:
- NA
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BOOT\_SECTOR\_FILE\_SYSTEM\_TYPE enumeration

Defines the valid file system types that can be recognized by the [**DetectBootSector**](detectbootsector.md) function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef enum  { 
  FileSystemUnknown,
  FileSystemFAT12,
  FileSystemFAT16,
  FileSystemFat32,
  FileSystemNTFS
} BOOT_SECTOR_FILE_SYSTEM_TYPE;
```



## Constants

<dl> <dt>

<span id="FileSystemUnknown"></span><span id="filesystemunknown"></span><span id="FILESYSTEMUNKNOWN"></span>**FileSystemUnknown**
</dt> <dd>

The file system is not known.

</dd> <dt>

<span id="FileSystemFAT12"></span><span id="filesystemfat12"></span><span id="FILESYSTEMFAT12"></span>**FileSystemFAT12**
</dt> <dd>

The file system is FAT12.

</dd> <dt>

<span id="FileSystemFAT16"></span><span id="filesystemfat16"></span><span id="FILESYSTEMFAT16"></span>**FileSystemFAT16**
</dt> <dd>

The file system is FAT16.

</dd> <dt>

<span id="FileSystemFat32"></span><span id="filesystemfat32"></span><span id="FILESYSTEMFAT32"></span>**FileSystemFat32**
</dt> <dd>

The file system is FAT32.

</dd> <dt>

<span id="FileSystemNTFS"></span><span id="filesystemntfs"></span><span id="FILESYSTEMNTFS"></span>**FileSystemNTFS**
</dt> <dd>

The file system is NTFS.

</dd> </dl>

## Remarks

Note that there is no associated header file for this enumeration.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**BOOT\_SECTOR\_INFO**](boot-sector-info.md)
</dt> </dl>

 

 





