---
title: Update method of the MSFT\_DedupVolumeStatus class
description: Scans the specified volumes to compute fresh data deduplication savings information and returns deduplication status objects containing fresh metadata, not cached.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1ADC201E-5FE8-491A-A138-424C53866EBA'
ms.prod: 'windows-server-dev'
ms.technology:
- 'data-deduplication'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Update method Data Deduplication API", "Update method Data Deduplication API , MSFT_DedupVolumeStatus interface", "MSFT_DedupVolumeStatus interface Data Deduplication API , Update method"]
topic_type:
- apiref
api_name:
- MSFT_DedupVolumeStatus.Update
api_location:
- DdpWmi.dll
api_type:
- COM
---

# Update method of the MSFT\_DedupVolumeStatus class

Scans the specified volumes to compute fresh data deduplication savings information and returns deduplication status objects containing fresh metadata, not cached.

## Syntax


```mof
uint32 Update(
  [in]  string                 Volume[],
  [out] MSFT_DedupVolumeStatus DedupVolumeStatus[]
);
```



## Parameters

<dl> <dt>

*Volume* \[in\]
</dt> <dd>

A list of file system volumes for which to scan and compute fresh data deduplication savings information. Volumes can be specified by drive letter (for example, D:) or volume GUID path. A volume GUID path is a string of the form "\\\\?\\Volume{*GUID*}\\" where *GUID* is a GUID that identifies the volume.

</dd> <dt>

*DedupVolumeStatus* \[out\]
</dt> <dd>

Array of references to the updated deduplication status objects.

</dd> </dl>

## Return value

This method returns either a WMI return code or a system error code.

## Remarks

When you call this method for multiple volumes at once, the analysis for each volume is done serially.

It is important to note that on large volumes this method can run for several minutes and will always perform a rescan after the initial scan. The default behavior is to wait for completion, regardless of the length of time required to run the scan and rescan.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[**MSFT\_DedupVolumeStatus**](msft-dedupvolumestatus.md)
</dt> </dl>

 

 





