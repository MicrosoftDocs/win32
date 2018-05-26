---
title: SharedVolumeIncompatibleFilters
description: Adds filters to be deemed as incompatible for direct I/O.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A12C5895-9327-4CCB-8B91-AC3F177256CF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SharedVolumeIncompatibleFilters Failover Cluster
topic_type:
- apiref
api_name:
- SharedVolumeIncompatibleFilters
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SharedVolumeIncompatibleFilters

Adds filters to be deemed as incompatible for direct I/O. Certain classes of filter drivers may be incompatible with the direct I/O mode of shared volumes.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSTER\_CSV\_INCOMPATIBLE\_FILTERS**.

Incompatible filter driver names are specified without the .sys extension.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





