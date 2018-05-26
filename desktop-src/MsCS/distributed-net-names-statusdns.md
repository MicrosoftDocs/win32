---
title: StatusDNS
description: Contains the returned status code from the last DNS operation that the resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: FB7CC4C7-FEA4-4FEE-AF71-B7D9078077BD
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- StatusDNS Failover Cluster , for distributed network names
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

Contains the returned status code from the last [*DNS*](d-gly.md#-wolf-domain-name-system-gly) operation that the resource performed. The following table summarizes the attributes of the **StatusDNS** property.



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



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





