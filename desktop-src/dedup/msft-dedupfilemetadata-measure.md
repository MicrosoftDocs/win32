---
title: Measure method of the MSFT\_DedupFileMetadata class
description: Returns a class representing the deduplication metadata for a specified file.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88b83705-e1e6-4e94-862c-1c737165c376
ms.prod: windows-server-dev
ms.technology:
- data-deduplication
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Measure method Data Deduplication API
- Measure method Data Deduplication API , MSFT_DedupFileMetadata class
- MSFT_DedupFileMetadata class Data Deduplication API , Measure method
topic_type:
- apiref
api_name:
- MSFT_DedupFileMetadata.Measure
api_location:
- DdpWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Measure method of the MSFT\_DedupFileMetadata class

Returns a class representing the deduplication metadata for a specified file.

## Syntax


```mof
uint32 Measure(
  [in]  string                 Path[],
  [out] MSFT_DedupFileMetadata DedupFileMetadata
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Path to a file.

</dd> <dt>

*DedupFileMetadata* \[out\]
</dt> <dd>

Contains an instance of a [**MSFT\_DedupFileMetadata**](msft-dedupfilemetadata.md) class representing the metadata for the specified path.

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

[**MSFT\_DedupFileMetadata**](msft-dedupfilemetadata.md)
</dt> </dl>

 

 





