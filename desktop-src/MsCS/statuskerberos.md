---
title: StatusKerberos
description: The returned status code from the last Kerberos operation that the NetName resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'fbc1b89b-1f90-4fa2-bbea-0cf98c731b8d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["StatusKerberos Failover Cluster , for Network Name properties", "StatusKerberos Failover Cluster"]
topic_type:
- apiref
api_name:
- StatusKerberos
api_type:
- NA
---

# StatusKerberos

The returned status code from the last Kerberos operation that the NetName resource performed. The following table summarizes the attributes of the **StatusKerberos** property.



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



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





