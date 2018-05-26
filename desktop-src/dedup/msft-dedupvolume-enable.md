---
title: Enable method of the MSFT\_DedupVolume class
description: Enables deduplication on the specified volumes by using default settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E9F3E75B-E317-48BB-B841-BAF0D243AB6C
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Enable method Data Deduplication API
- Enable method Data Deduplication API , MSFT_DedupVolume interface
- MSFT_DedupVolume interface Data Deduplication API , Enable method
topic_type:
- apiref
api_name:
- MSFT_DedupVolume.Enable
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enable method of the MSFT\_DedupVolume class

Enables deduplication on the specified volumes by using default settings.

## Syntax


```mof
uint32 Enable(
  [in]  string           Volume[],
  [in]  boolean          DataAccess,
  [in]  uint32           UsageType,
  [out] MSFT_DedupVolume DedupVolume[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

A list of file system volumes for which to enable data deduplication. Volumes can be specified by drive letter (for example, D:) or volume **GUID** path. A volume **GUID** path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a **GUID** that identifies the volume.

</dd> <dt>

*DataAccess* \[in\]
</dt> <dd>

If **True**, grants data access to deduplicated files on the volume to be enabled.

</dd> <dt>

*UsageType* \[in\]
</dt> <dd>

The type of data to store on the volume.

**Windows Server 2012:** This parameter is not supported until Windows Server 2012 R2.

The possible values are:

<dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>**Default** (1)


</dt> <dd>

General purpose files shares. This is the default value.

</dd> <dt>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>

<span id="HyperV"></span><span id="hyperv"></span><span id="HYPERV"></span>**HyperV** (2)


</dt> <dd>

Hyper-V storage.

</dd> <dt>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>

<span id="Backup"></span><span id="backup"></span><span id="BACKUP"></span>**Backup** (3)


</dt> <dd>

Backup storage.

**Windows Server 2012 R2 and Windows Server 2012:** This value is not supported before Windows Server 2016.

</dd> </dl> </dd> <dt>

*DedupVolume* \[out\]
</dt> <dd>

Array of references to the enabled volumes.

</dd> </dl>

## Return value

This method returns either a Windows Management Instrumentation (WMI) return code or a system error code.

## Remarks

The [**MSFT\_DedupVolume**](msft-dedupvolume.md) object references that are returned in the *DedupVolume* parameter can be used to customize the data deduplication settings.

Deduplication is disabled by default.

Certain volumes are not supported for data deduplication such as any volume that is not NTFS or any volume that is smaller than 100 MB. If you attempt to enable data deduplication for unsupported volumes, the call fails.

## Examples

For an example that uses the **Enable** method, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[**MSFT\_DedupVolume**](msft-dedupvolume.md)
</dt> <dt>

[**MSFT\_DedupVolume::Disable**](msft-dedupvolume-disable.md)
</dt> </dl>

 

 





