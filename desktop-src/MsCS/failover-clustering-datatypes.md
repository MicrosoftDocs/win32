---
title: Failover Clustering Datatypes
description: This section contains datatypes used for working with resources.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '07E8E1DB-527E-4ADC-A243-0CB137FBE310'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RESID", "RESOURCE_HANDLE", "PRES_CTL_CTX", "PRESTYPE_CTL_CTX"]
---

# Failover Clustering Datatypes

This section contains datatypes used for working with resources.


```C++
typedef PVOID RESID;
typedef HANDLE RESOURCE_HANDLE;
typedef INT64 PRES_CTL_CTX;
typedef INT64 PRESTYPE_CTL_CTX;
```



<dl> <dt>

**RESID**
</dt> <dd>

A resource identifier. For more information, see [Resource Identifiers](resource-identifiers.md).

</dd> <dt>

**RESOURCE\_HANDLE**
</dt> <dd>

A handle for a resource.

</dd> <dt>

**PRES\_CTL\_CTX**
</dt> <dd>

Resource control context.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:** Not available.

</dd> <dt>

**PRESTYPE\_CTL\_CTX**
</dt> <dd>

Resource type control context.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:** Not available.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>ResApi.h</dt> </dl> |



 

 





