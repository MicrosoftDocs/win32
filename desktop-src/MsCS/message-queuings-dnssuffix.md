---
title: DnsSuffix
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 283E60F2-205A-4292-ABB2-4C4E8F8E6331
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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsSuffix

TBD. The following table summarizes the attributes of the **DnsSuffix** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | A null-terminated Unicode string.                                |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_DNS\_SUFFIX**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> </dl>

 

 





