---
title: LastDNSUpdateTime
description: The Last time, in 100 nanosecond units, recorded by the Netname registered DNS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a2b9f5ee-3826-41ec-ba51-20af219d62fc
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LastDNSUpdateTime Failover Cluster , for Network Name properties
- LastDNSUpdateTime Failover Cluster
topic_type:
- apiref
api_name:
- LastDNSUpdateTime
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LastDNSUpdateTime

The Last time, in 100 nanosecond units, recorded by the Netname registered DNS. The following table summarizes the attributes of the **LastDNSUpdateTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Status    | Optional                                        |
| Structure | [**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime) |
| Minimum   | 0                                               |
| Maximum   | see [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)           |
| Default   | 0                                               |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_LAST\_DNS\_UPDATE**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime)
</dt> </dl>

 

 





