---
title: BOOT\_SECTOR\_INFO structure
description: Provides information about the boot sector. This structure is used by the DetectBootSector function.
ms.assetid: bb290c0a-5291-436c-98cb-0158f7e17b23
keywords:
- BOOT_SECTOR_INFO structure Files
- PBOOT_SECTOR_INFO structure pointer Files
topic_type:
- apiref
api_name:
- BOOT_SECTOR_INFO
api_type:
- NA
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BOOT\_SECTOR\_INFO structure

Provides information about the boot sector. This structure is used by the [**DetectBootSector**](detectbootsector.md) function.

> [!Note]  
> FMAPI can only be used in the Windows Preinstallation Environment (WinPE) for Windows Vista, Windows Server 2008, and later. Applications that use FMAPI must license WinPE.

 

## Syntax


```C++
typedef struct _BOOT_SECTOR_INFO {
  LONGLONG                     TotalSectors;
  BOOT_SECTOR_FILE_SYSTEM_TYPE FileSystem;
  ULONG                        BytePerSector;
  ULONG                        SectorPerCluster;
  BOOL                         IsEncrypted;
} BOOT_SECTOR_INFO, *PBOOT_SECTOR_INFO;
```



## Members

<dl> <dt>

**TotalSectors**
</dt> <dd>

The total number of sectors on the detected volume of the file system.

</dd> <dt>

**FileSystem**
</dt> <dd>

The type of the file system.

</dd> <dt>

**BytePerSector**
</dt> <dd>

The number of bytes per sector.

</dd> <dt>

**SectorPerCluster**
</dt> <dd>

The number of sectors per cluster.

</dd> <dt>

**IsEncrypted**
</dt> <dd>

This member is not used.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:  TRUE** if the volume is BitLocker encrypted; otherwise, **FALSE**.

</dd> </dl>

## Remarks

Note that there is no associated header file for this structure.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DetectBootSector**](detectbootsector.md)
</dt> </dl>

 

 





