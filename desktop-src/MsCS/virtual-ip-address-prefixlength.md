---
title: PrefixLength
description: Specifies the prefix length of a virtual IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8A166042-7CFA-4BB8-9A61-CDA594DDE488
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrefixLength Failover Cluster
topic_type:
- apiref
api_name:
- PrefixLength
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrefixLength

Specifies the prefix length of a virtual IP address.



| Attribute            | Value                                      |
|----------------------|--------------------------------------------|
| Data type<br/> | **DWORD**                                  |
| Access<br/>    | [Read/write](read-write-properties.md)    |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)  |
| Minimum<br/>   | 0 (for IPv4) or 0 (for IPv6)<br/>    |
| Maximum<br/>   | 32 (for IPv4) or 128 (for IPv6)<br/> |
| Default<br/>   | 0<br/>                               |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_VIP\_PREFIX\_LENGTH**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Virtual IP Address Private Properties](virtual-ip-address-private-properties.md)
</dt> </dl>

 

 





