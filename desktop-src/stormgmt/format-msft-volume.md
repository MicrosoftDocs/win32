---
title: Format method of the MSFT\_Volume class
description: Formats the volume.
ms.assetid: 007dd46a-4812-4273-beaa-74fbe9520c7d
keywords:
- Format method Windows Storage Management API
- Format method Windows Storage Management API , MSFT_Volume class
- MSFT_Volume class Windows Storage Management API , Format method
topic_type:
- apiref
api_name:
- MSFT_Volume.Format
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

# Format method of the MSFT\_Volume class

Formats the volume.

## Syntax


```mof
UInt32 Format(
  [in]  String  FileSystem,
  [in]  String  FileSystemLabel,
  [in]  UInt32  AllocationUnitSize,
  [in]  Boolean Full,
  [in]  Boolean Force,
  [in]  Boolean Compress,
  [in]  Boolean ShortFileNameSupport,
  [in]  Boolean SetIntegrityStreams,
  [in]  Boolean UseLargeFRS,
  [in]  Boolean DisableHeatGathering,
  [out] String  FormattedVolume,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FileSystem* \[in\]
</dt> <dd>

The file system to apply to the volume. One of the following:

-   "ExFAT"
-   "FAT"
-   "FAT32"
-   "NTFS"
-   "ReFS"

</dd> <dt>

*FileSystemLabel* \[in\]
</dt> <dd>

The file system label for the volume.

</dd> <dt>

*AllocationUnitSize* \[in\]
</dt> <dd>

The allocation unit size, in bytes.

</dd> <dt>

*Full* \[in\]
</dt> <dd>

**TRUE** for a full format, or **FALSE** for a quick format.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**TRUE** to force the format operation; otherwise, **FALSE**.

</dd> <dt>

*Compress* \[in\]
</dt> <dd>

**TRUE** to compress the volume; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

</dd> <dt>

*ShortFileNameSupport* \[in\]
</dt> <dd>

**TRUE** if the volume should support short names; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

</dd> <dt>

*SetIntegrityStreams* \[in\]
</dt> <dd>

**TRUE** to set integrity streams. Leave undefined unless *FileSystem* is set to  ReFS .

</dd> <dt>

*UseLargeFRS* \[in\]
</dt> <dd>

**TRUE** to use large FRS; otherwise, **FALSE**. Leave undefined if *FileSystem* is set to  ReFS .

</dd> <dt>

*DisableHeatGathering* \[in\]
</dt> <dd>

**TRUE** to disable heat gathering; otherwise, **FALSE**.

</dd> <dt>

*FormattedVolume* \[out\]
</dt> <dd>

Receives a [**MSFT\_Volume**](msft-volume.md) object that represents the formatted volume.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

Contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

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

**This command is not supported on x86 running in x64 environment.** (7)
</dt> <dt>

**Access Denied** (40001)
</dt> <dt>

**An unexpected I/O error has occured** (40004)
</dt> <dt>

**The specified object is managed by the Microsoft Failover Clustering component. The disk must be in cluster maintenance mode and the cluster resource status must be online to perform this operation.** (40018)
</dt> <dt>

**The operation is not allowed on a system or critical partition.** (42010)
</dt> <dt>

**The specified cluster size is invalid** (43000)
</dt> <dt>

**The specified file system is not supported** (43001)
</dt> <dt>

**The volume cannot be quick formatted** (43002)
</dt> <dt>

**The number of clusters exceeds 32 bits** (43003)
</dt> <dt>

**The specified UDF version is not supported** (43004)
</dt> <dt>

**The cluster size must be a multiple of the disk's physical sector size** (43005)
</dt> <dt>

**Cannot perform the requested operation when the drive is read only** (43006)
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

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





