---
title: RDID
description: Specifies the Routing Domain ID (RDID) of a virtual IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'FB4B567B-3207-4759-9DA0-E11B33BF790E'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RDID Failover Cluster"]
topic_type:
- apiref
api_name:
- RDID
api_type:
- NA
---

# RDID

Specifies the Routing Domain ID (RDID) of a virtual IP address.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | A NULL-terminated Unicode string<br/>                   |
| Access<br/>    | [Read/write](read-write-properties.md)                       |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                |
| Minimum<br/>   | **NULL**                                                      |
| Maximum<br/>   | None (but see [Maximum String Size](maximum-string-size.md)) |
| Default<br/>   | **NULL**                                                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_VIP\_RDID**.

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Virtual IP Address Private Properties](virtual-ip-address-private-properties.md)
</dt> </dl>

 

 





