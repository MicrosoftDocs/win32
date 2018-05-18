---
title: StatusNetBIOS
description: The returned status code from the last NetBIOS operation that the NetName resource performed.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4fc44075-3561-4445-a995-ba6e6c2ac09d'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["StatusNetBIOS Failover Cluster , for Network Name properties", "StatusNetBIOS Failover Cluster"]
topic_type:
- apiref
api_name:
- StatusNetBIOS
api_type:
- NA
---

# StatusNetBIOS

The returned status code from the last NetBIOS operation that the NetName resource performed. The following table summarizes the attributes of the **StatusNetBIOS** property.



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

The constant for this property is **CLUSREG\_NAME\_NETNAME\_STATUS\_NETBIOS**.

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

 

 





