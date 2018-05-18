---
title: StatusKerberos
description: Contains the returned status code from the last Kerberos operation that the resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '559A7EF8-27BD-4CBB-BFF5-24FD085E4267'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["StatusKerberos Failover Cluster , for distributed network names", "StatusKerberos Failover Cluster"]
topic_type:
- apiref
api_name:
- StatusKerberos
api_type:
- NA
---

# StatusKerberos

Contains the returned status code from the last Kerberos operation that the resource performed. The following table summarizes the attributes of the **StatusKerberos** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 0                                         |
| Default   | 0xFFFFFFFF                                |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_STATUS\_KERBEROS**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





