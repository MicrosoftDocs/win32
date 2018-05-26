---
title: ResourceData
description: Stores the virtual computer objects encrypted password.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 20148CD2-DBE0-4985-BE65-E0DB040E47DE
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ResourceData Failover Cluster ,for distributed network names
- ResourceData Failover Cluster
topic_type:
- apiref
api_name:
- ResourceData
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ResourceData

Stores the virtual computer object's encrypted password. The following table summarizes the attributes of the **ResourceData** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_BINARY**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_binary?branch=master)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

Access to **ResourceData** is limited to the local administrator, system, and creator owner.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CreatingDC**](virtual-machine-replication-brokers-creatingdc.md)
</dt> </dl>

 

 





