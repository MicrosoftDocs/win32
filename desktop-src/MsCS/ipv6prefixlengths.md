---
title: IPv6PrefixLengths
description: IPv6 prefix lengths for the network resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1c8a77c0-187e-4edf-9c8a-d5f3bbeb2496
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IPv6PrefixLengths Failover Cluster , for Network common properties
- IPv6PrefixLengths Failover Cluster
topic_type:
- apiref
api_name:
- IPv6PrefixLengths
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IPv6PrefixLengths

Specifies the IPv6 prefix lengths for the network resource. The following table summarizes the attributes of the **IPv6PrefixLengths** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | **LPCWSTR** pointer or a **WCHAR** array                         |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Network Common Properties](common-properties.md)
</dt> <dt>

[**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)
</dt> </dl>

 

 





