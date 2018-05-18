---
title: RegisterAllProvidersIP
description: Determines whether the IP addresses of all provider IP address resources are registered.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3EB15DC0-79AC-4414-8597-12857CA91207'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["RegisterAllProvidersIP Failover Cluster"]
topic_type:
- apiref
api_name:
- RegisterAllProvidersIP
api_type:
- NA
---

# RegisterAllProvidersIP

Determines whether the IP addresses of all provider IP address resources are registered. The following table summarizes the attributes of the **RegisterAllProvidersIP** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

Setting this private property to 1 registers the IP addresses of all provider IP address resources, independent of the online status of any individual provider IP address resource.

The constant for this property is **CLUSREG\_NAME\_NETNAME\_REGISTER\_ALL\_IP**.

Setting this private property to 0, the default value, ensures that only online provider IP addresses are registered.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RegisterAllProvidersIP** can be set with the following example code.


```C++
DWORD          RegisterAllProvidersIPData = 0;
CLUSPROP_DWORD RegisterAllProvidersIPValue;

RegisterAllProvidersIPValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RegisterAllProvidersIPValue.cbLength  = sizeof(DWORD);
RegisterAllProvidersIPValue.dw        = RegisterAllProvidersIPData;
```



## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





