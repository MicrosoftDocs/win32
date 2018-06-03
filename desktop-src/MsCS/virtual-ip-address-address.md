---
title: Address
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ECC49B31-C90C-4E78-A3D4-0CF5442F8637
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Address Failover Cluster
topic_type:
- apiref
api_name:
- Address
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Address

TBD



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | A NULL-terminated Unicode string<br/>                   |
| Access<br/>    | [Read/write](read-write-properties.md)                       |
| Structure<br/> | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)<br/>                |
| Minimum<br/>   | **NULL**                                                      |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)) |
| Default<br/>   | "0.0.0.0" (for IPv4) or "::" (for IPv6)<br/>            |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_VIP\_ADDRESS**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Virtual IP Address Private Properties](virtual-ip-address-private-properties.md)
</dt> </dl>

 

 





