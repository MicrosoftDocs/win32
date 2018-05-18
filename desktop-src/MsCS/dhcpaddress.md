---
title: DhcpAddress
description: Contains the address provided by the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'd29dbfeb-03a3-43ef-a23e-7ed6d67f6eaf'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DhcpAddress Failover Cluster , for IPv4 Address private properties", "DhcpAddress Failover Cluster"]
topic_type:
- apiref
api_name:
- DhcpAddress
api_type:
- NA
---

# DhcpAddress

Contains the address provided by the DHCP server. The following table summarizes the attributes of the **DhcpAddress** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The data in the **DhcpAddress** property must be formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255. The value 255.255.255.255 is not valid.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





