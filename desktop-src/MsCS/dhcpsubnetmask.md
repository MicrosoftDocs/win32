---
title: DhcpSubnetMask
description: Contains the subnet mask to be applied for routing for the IPv4 address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '56ac2c64-e64d-44ff-93d6-1d59e42820f6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["DhcpSubnetMask Failover Cluster , for IPv4 Address private properties", "DhcpSubnetMask Failover Cluster"]
topic_type:
- apiref
api_name:
- DhcpSubnetMask
api_type:
- NA
---

# DhcpSubnetMask

Contains the subnet mask to be applied for routing for the [IPv4 address](ip-address.md). The following table summarizes the attributes of the **DhcpSubnetMask** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The data in the **DhcpSubnetMask** property must be formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255. The value 255.255.255.255 is not valid.

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

 

 





