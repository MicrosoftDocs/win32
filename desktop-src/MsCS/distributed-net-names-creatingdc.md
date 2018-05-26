---
title: CreatingDC
description: Stores the name of the domain controller that was used to obtain the VirtualServer Computer object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A4A0C4F6-4EE6-46B8-A6D2-33F1ED37C620
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreatingDC Failover Cluster ,for distributed network names
- CreatingDC Failover Cluster
topic_type:
- apiref
api_name:
- CreatingDC
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreatingDC

Stores the name of the domain controller that was used to obtain the **VirtualServer** Computer object. The following table summarizes the attributes of the **CreatingDC** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**ResourceData**](virtual-machine-replication-brokers-resourcedata.md)
</dt> </dl>

 

 





