---
title: LastDNSUpdateTime
description: Specifies the last time, in 100 nanosecond units, recorded by the DNS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: BBF188DC-EED3-4A49-8601-00F8CB57A59E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- LastDNSUpdateTime Failover Cluster , for virtual machine replication brokers
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

Specifies the last time, in 100 nanosecond units, recorded by the [*DNS*](https://www.bing.com/search?q=*DNS*). The following table summarizes the attributes of the **LastDNSUpdateTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Structure | [**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime) |
| Minimum   | 0                                               |
| Maximum   | see [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)           |
| Default   | 0                                               |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime)
</dt> </dl>

 

 





