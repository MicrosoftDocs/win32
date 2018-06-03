---
title: IPv4PrefixLengths
description: IPv4 prefix lengths for the network resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f7ce4ebb-dbd2-4c16-aaba-e267b58f5f9d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- IPv4PrefixLengths Failover Cluster , for Network common properties
- IPv4PrefixLengths Failover Cluster
topic_type:
- apiref
api_name:
- IPv4PrefixLengths
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPv4PrefixLengths

Specifies the IPv4 prefix lengths for the network resource. The following table summarizes the attributes of the **IPv4PrefixLengths** property.



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

[Network Common Properties](common-properties.md)
</dt> <dt>

[**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)
</dt> </dl>

 

 





