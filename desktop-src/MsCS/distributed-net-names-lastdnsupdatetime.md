---
title: LastDNSUpdateTime
description: Specifies the last time, in 100 nanosecond units, recorded by the DNS.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8821B3C0-2950-4AF4-8230-6472CF630E8A'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["LastDNSUpdateTime Failover Cluster , for distributed network names", "LastDNSUpdateTime Failover Cluster"]
topic_type:
- apiref
api_name:
- LastDNSUpdateTime
api_type:
- NA
---

# LastDNSUpdateTime

Specifies the last time, in 100 nanosecond units, recorded by the [*DNS*](d-gly.md#-wolf-domain-name-system-gly). The following table summarizes the attributes of the **LastDNSUpdateTime** property.



| Attribute | Value                                           |
|-----------|-------------------------------------------------|
| Data type | [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)               |
| Access    | [Read-only](read-only-properties.md)           |
| Status    | Optional                                        |
| Structure | [**CLUSPROP\_FILETIME**](clusprop-filetime.md) |
| Minimum   | 0                                               |
| Maximum   | see [**FILETIME**](https://msdn.microsoft.com/library/windows/desktop/ms724284)           |
| Default   | 0                                               |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_LAST\_DNS\_UPDATE** or **PARAM\_NAME\_\_LAST\_DNS\_UPDATE**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_FILETIME**](clusprop-filetime.md)
</dt> </dl>

 

 





