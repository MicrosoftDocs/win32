---
title: VSID
description: Specifies the Virtual Subnet ID (VSID) of a virtual IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7AC7D5CB-7CEC-4DD2-A19B-086030BBE471
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VSID Failover Cluster
topic_type:
- apiref
api_name:
- VSID
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# VSID

Specifies the Virtual Subnet ID (VSID) of a virtual IP address.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 0xFFFFFFFF<br/>                     |
| Default<br/>   | 0<br/>                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_VIP\_VSID**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Virtual IP Address Private Properties](virtual-ip-address-private-properties.md)
</dt> </dl>

 

 





