---
title: Network
description: Specifies the name of the network for which the IP address is to be created.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ba63fde8-5d53-426b-b72e-6c3799a27cd0'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Network Failover Cluster , for Ipv6 Address private properties", "Network Failover Cluster"]
topic_type:
- apiref
api_name:
- Network
api_type:
- NA
---

# Network

Specifies the name of the network for which the [IP address](ip-address.md) is to be created. The following table summarizes the attributes of the **Network** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

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

 

 





