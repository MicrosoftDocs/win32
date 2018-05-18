---
title: PreferredSite
description: Specifies the preferred site for a site-aware cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'E14657E6-DA2D-4897-B150-0CB9602E4F16'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["PreferredSite Failover Cluster"]
topic_type:
- apiref
api_name:
- PreferredSite
api_type:
- NA
---

# PreferredSite

Specifies the preferred site for a site-aware cluster.



| Attribute            | Value                                                                      |
|----------------------|----------------------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                                  |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>                         |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                             |
| Minimum<br/>   | 0<br/>                                                               |
| Maximum<br/>   | None (but see [Maximum Property Size](maximum-string-size.md))<br/> |
| Default<br/>   | 0<br/>                                                               |



 

## Remarks

The constant for this property is **CLUSTER\_NAME\_PREFERRED\_SITE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





