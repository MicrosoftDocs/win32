---
title: ExpandFile method of the MSFT\_DedupVolume class
description: Reverts the deduplication process on a set of deduplicated files.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a9584c26-4dd8-472c-b8bf-ec760dd1106b
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- ExpandFile method Data Deduplication API
- ExpandFile method Data Deduplication API , MSFT_DedupVolume class
- MSFT_DedupVolume class Data Deduplication API , ExpandFile method
topic_type:
- apiref
api_name:
- MSFT_DedupVolume.ExpandFile
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ExpandFile method of the MSFT\_DedupVolume class

Reverts the deduplication process on a set of deduplicated files.

## Syntax


```mof
uint32 ExpandFile(
  [in] string Path[]
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path to the files to revert.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Deduplication<br/>                                                   |
| MOF<br/>                      | <dl> <dt>DeduplicationProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DdpWmi.dll</dt> </dl>                |



## See also

<dl> <dt>

[**MSFT\_DedupVolume**](msft-dedupvolume.md)
</dt> </dl>

 

 





