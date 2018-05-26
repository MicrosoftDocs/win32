---
title: Disable method of the MSFT\_DedupVolume class
description: Disables further data deduplication activity on one or more volumes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 33426258-4D9A-44EF-AE68-1BE8C35B0460
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Disable method Data Deduplication API
- Disable method Data Deduplication API , MSFT_DedupVolume interface
- MSFT_DedupVolume interface Data Deduplication API , Disable method
topic_type:
- apiref
api_name:
- MSFT_DedupVolume.Disable
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Disable method of the MSFT\_DedupVolume class

Disables further data deduplication activity on one or more volumes.

## Syntax


```mof
uint32 Disable(
  [in]  string           Volume[],
  [in]  boolean          DataAccess,
  [out] MSFT_DedupVolume DedupVolume[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

A list of file system volumes for which to disable data deduplication. Volumes can be specified by drive letter (for example, D:) or volume GUID path. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> <dt>

*DataAccess* \[in\]
</dt> <dd>

Set to **TRUE** to cause data access to deduplicated files on the volume to be disabled.

</dd> <dt>

*DedupVolume* \[out\]
</dt> <dd>

Array of references to the disabled volumes.

</dd> </dl>

## Return value

This method returns either a WMI return code or a system error code.

## Remarks

After data deduplication is disabled, the volume remains in its deduplicated state, but no more data deduplication jobs will be run for the specified volumes; new data will not be deduplicated. Previously deduplicated data is accessible. To undo deduplication on the volume, call the [**MSFT\_DedupJob::Start**](msft-dedupjob-start.md) method and pass **Unoptimization** for the *Type* parameter.

When a volume is Dedup-disabled, all read-only deduplication operations will continue to work (for example, the **Get** methods for deduplication class properties), but calls to deduplication job-related methods will fail, with the exception of unoptimization and read-only scrubbing jobs.

## Examples

For an example that uses the **Disable** method, please see [Data deduplication backup and restore sample](selective-file-restore-using-data-deduplication-backup-restore-api.md).

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

[**MSFT\_DedupVolume::Enable**](msft-dedupvolume-enable.md)
</dt> </dl>

 

 





