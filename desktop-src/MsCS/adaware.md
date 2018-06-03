---
title: ADAware
description: A DNS suffix for a Network Name resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: D6E6B6BB-0268-4905-BD40-91B4C1A5DC22
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ADAware Failover Cluster
topic_type:
- apiref
api_name:
- ADAware
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ADAware

A DNS suffix for a Network Name resource.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 2<br/>                              |
| Default<br/>   | 0xFFFFFFFF<br/>                     |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_AD\_AWARE**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> </dl>

 

 





