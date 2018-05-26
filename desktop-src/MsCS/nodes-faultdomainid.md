---
title: FaultDomainId
description: Specifies the ID of the fault domain for a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7A0E6199-9A8C-486C-B7AD-A8AE5C2B3F79
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- FaultDomainId Failover Cluster
topic_type:
- apiref
api_name:
- FaultDomainId
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# FaultDomainId

Specifies the ID of the fault domain for a node.



| Attribute            | Value                                                            |
|----------------------|------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string                                   |
| Access<br/>    | [Read/write](read-write-properties.md)                          |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default<br/>   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NODE\_FDID**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Node Common Properties](node-common-properties.md)
</dt> </dl>

 

 





