---
title: RegisterAllProvidersIP
description: Determines whether or not the IP addresses of all provider IP address resources are registered or not.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1E4D7E95-3F4F-4A7B-9B3C-10DA424D9E6B'
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

Determines whether or not the IP addresses of all provider IP address resources are registered or not. The following table summarizes the attributes of the **RegisterAllProvidersIP** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 1                                         |
| Default   | 0                                         |



 

## Remarks

Setting this private property to 1 registers the IP addresses of all provider IP address resources, independent of the online status of any individual provider IP address resource.

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

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





