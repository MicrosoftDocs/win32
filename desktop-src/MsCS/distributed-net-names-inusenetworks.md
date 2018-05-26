---
title: InUseNetworks
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: D4AAAA6F-F6CC-4EE1-BACA-84B7BF6843DB
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- InUseNetworks Failover Cluster
topic_type:
- apiref
api_name:
- InUseNetworks
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# InUseNetworks

TBD. The following table summarizes the attributes of the **InUseNetworks** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Array of null-terminated Unicode strings.                        |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_IN\_USE\_NETWORKS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> </dl>

 

 





