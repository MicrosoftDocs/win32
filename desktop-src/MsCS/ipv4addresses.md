---
title: IPv4Addresses
description: IPv4 addresses for the network resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 51f84647-e105-4237-93da-3af6c79da33b
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IPv4Addresses Failover Cluster , for Network common properties
- IPv4Addresses Failover Cluster
topic_type:
- apiref
api_name:
- IPv4Addresses
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IPv4Addresses

Specifies the IPv4 addresses for the network resource. The following table summarizes the attributes of the **IPv4Addresses** property.



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

 

 





