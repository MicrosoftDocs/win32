---
title: IPv4Addresses
description: IPv4 addresses for the network interface resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a9aa4709-8728-4b6d-92c1-4d50e8389046'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["IPv4Addresses Failover Cluster , for Network Interface common properties", "IPv4Addresses Failover Cluster"]
topic_type:
- apiref
api_name:
- IPv4Addresses
api_type:
- NA
---

# IPv4Addresses

Specifies the IPv4 addresses for the network interface resource. The following table summarizes the attributes of the **IPv4Addresses** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array.                        |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_MULTI\_SZ**](clusprop-multi-sz.md)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Network Interface Common Properties](network-interface-common-properties.md)
</dt> <dt>

[**CLUSPROP\_MULTI\_SZ**](clusprop-multi-sz.md)
</dt> </dl>

 

 





