---
title: PrefixLength
description: Describes the IPv6 prefix length that defines the local IPv6 subnet.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: db1d52a6-ed51-459b-9470-78dadaa2f357
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- PrefixLength Failover Cluster , for Ipv6 Address private properties
- PrefixLength Failover Cluster
topic_type:
- apiref
api_name:
- PrefixLength
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PrefixLength

Describes the IPv6 prefix length that defines the local IPv6 subnet. The following table summarizes the attributes of the **PrefixLength** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/) |
| Minimum   | 0                                         |
| Maximum   | 128                                       |
| Default   | 0                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[IPv6 Address Private Properties](ipv6-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





