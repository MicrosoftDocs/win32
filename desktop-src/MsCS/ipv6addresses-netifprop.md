---
title: IPv6Addresses
description: IPv4 addresses for the network interface resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 34a9a031-e39d-4d3c-8c26-afe7d9cd073d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IPv6Addresses Failover Cluster , for Network Interface common properties
- IPv6Addresses Failover Cluster
topic_type:
- apiref
api_name:
- IPv6Addresses
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPv6Addresses

Specifies the IPv4 addresses for the network interface resource. The following table summarizes the attributes of the **IPv6Addresses** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Network Interface Common Properties](network-interface-common-properties.md)
</dt> <dt>

[**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)
</dt> </dl>

 

 





