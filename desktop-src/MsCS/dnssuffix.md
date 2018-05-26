---
title: DnsSuffix
description: A DNS suffix for a Network Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 11A1C10B-FECE-41F6-8449-2FD32C65605A
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DnsSuffix Failover Cluster
topic_type:
- apiref
api_name:
- DnsSuffix
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsSuffix

A DNS suffix for a Network Name resource.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string.                                  |
| Access<br/>    | [Read-only](read-only-properties.md)                            |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_DNS\_SUFFIX**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> </dl>

 

 





