---
title: SharedVolumeCompatibleFilters
description: Overrides cluster service determination of filters as incompatible.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 93A81F51-EA4C-4EB3-B529-47873D4D0B30
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SharedVolumeCompatibleFilters Failover Cluster
topic_type:
- apiref
api_name:
- SharedVolumeCompatibleFilters
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SharedVolumeCompatibleFilters

Overrides cluster service determination of filters as incompatible. Certain classes of filter drivers may be flagged as incompatible with the direct I/O mode of shared volumes.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSTER\_CSV\_COMPATIBLE\_FILTERS**.

Compatible filter driver names are specified without the .sys extension.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





