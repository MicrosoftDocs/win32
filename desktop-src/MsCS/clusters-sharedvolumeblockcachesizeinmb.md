---
title: SharedVolumeBlockCacheSizeInMB
description: Specifies the cache size of a cluster shared volume (CSV), in megabytes.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 32D2C698-4F9F-4F72-A6BF-19402EC35512
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SharedVolumeBlockCacheSizeInMB Failover Cluster
topic_type:
- apiref
api_name:
- SharedVolumeBlockCacheSizeInMB
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SharedVolumeBlockCacheSizeInMB

Specifies the cache size of a cluster shared volume (CSV), in megabytes.

**Windows Server 2012:** This property was renamed to [**BlockCacheSize**](blockcachesize.md) in Windows Server 2012 R2.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 0                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |
| End of client support<br/>    | None supported<br/>      |
| End of server support<br/>    | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> <dt>

[**BlockCacheSize**](blockcachesize.md)
</dt> </dl>

 

 





