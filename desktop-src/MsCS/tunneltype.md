---
title: TunnelType
description: Describes the type of IPv6 tunnel used, if any. The following table summarizes the attributes of the TunnelType property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '544013b8-1dd5-4c44-a215-346150f79647'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["TunnelType Failover Cluster , for Ipv6 Address private properties", "TunnelType Failover Cluster"]
topic_type:
- apiref
api_name:
- TunnelType
api_type:
- NA
---

# TunnelType

Describes the type of IPv6 tunnel used, if any. The following table summarizes the attributes of the **TunnelType** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | ""                                                               |



 

The **TunnelType** property can be set to one of the following values.



| Value    | Description                                                                                       |
|----------|---------------------------------------------------------------------------------------------------|
| ""       | The IPv6 tunnel type is unspecified.<br/>                                                   |
| "ISATAP" | The IPv6 tunnel is an Intra-Site Automatic Tunnel Addressing Protocol (ISATAP) tunnel.<br/> |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **TunnelType** can be set with the following example code.


```C++
WCHAR                szTunnelTypeData[] = L"ISATAP";
CLUSPROP_SZ_DECLARE( TunnelTypeValue, 
                     sizeof( szTunnelTypeData ) / sizeof( WCHAR ) );

TunnelTypeValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
TunnelTypeValue.cbLength  = sizeof( szTunnelTypeData );
StringCbCopy( TunnelTypeValue.sz, 
              TunnelTypeValue.cbLength, 
              szTunnelTypeData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IPv6 Address Private Properties](ipv6-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





