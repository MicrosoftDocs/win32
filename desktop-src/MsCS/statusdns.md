---
title: StatusDNS
description: The returned status code from the last DNS operation that the NetName resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 09eef3bc-5155-47cf-8384-de87fc009b61
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusDNS Failover Cluster , for Network Name properties
- StatusDNS Failover Cluster
topic_type:
- apiref
api_name:
- StatusDNS
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# StatusDNS

The returned status code from the last DNS operation that the NetName resource performed. The following table summarizes the attributes of the **StatusDNS** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0xFFFFFFFF                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_STATUS\_DNS**.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





