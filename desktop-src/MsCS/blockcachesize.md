---
title: BlockCacheSize
description: Specifies the cache size of a cluster shared volume (CSV), in megabytes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: F1243F41-2A4D-4377-B911-C60A48E66499
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- BlockCacheSize Failover Cluster
topic_type:
- apiref
api_name:
- BlockCacheSize
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BlockCacheSize

Specifies the cache size of a cluster shared volume (CSV), in megabytes.

> [!Note]  
> This property was renamed from [**SharedVolumeBlockCacheSizeInMB**](clusters-sharedvolumeblockcachesizeinmb.md) in Windows Server 2012 R2.

 



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CSV\_BLOCK\_CACHE**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**BlockCacheSize**](blockcachesize.md)
</dt> </dl>

 

 





