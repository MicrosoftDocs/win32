---
title: LastDNSUpdateTime
description: Contains the last time, in 100 nanosecond units, recorded by the DNS that is associated with the message queuing resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: AC3BE7F4-DFC4-491B-83D0-83D76B1D0DD9
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LastDNSUpdateTime Failover Cluster ,for message queuings
- LastDNSUpdateTime Failover Cluster
topic_type:
- apiref
api_name:
- LastDNSUpdateTime
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LastDNSUpdateTime

Contains the last time, in 100 nanosecond units, recorded by the [*DNS*](d-gly.md#-wolf-domain-name-system-gly) that is associated with the [message queuing](message-queuing.md) resource. The following table summarizes the attributes of the **LastDNSUpdateTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Status    | Optional                                        |
| Structure | [**CLUSPROP\_FILETIME**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_filetime?branch=master) |
| Minimum   | 0                                               |
| Maximum   | see [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)           |
| Default   | 0                                               |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_LAST\_DNS\_UPDATE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_filetime?branch=master)
</dt> </dl>

 

 





