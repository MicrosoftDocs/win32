---
title: CreatingDC
description: Stores the name of the domain controller.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 43FF686A-F831-4BA5-9025-1051567315DF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- CreatingDC Failover Cluster ,for message queuings
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

Stores the name of the domain controller. The following table summarizes the attributes of the **CreatingDC** property.



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

[Message Queuing Private Properties](message-queuing-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**ResourceData**](message-queuings-resourcedata.md)
</dt> </dl>

 

 





