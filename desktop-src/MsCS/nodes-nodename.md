---
title: NodeName
description: Provides the name of the node. The following table summarizes the attributes of the NodeName property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: a16f245e-6191-428a-acfa-b70294633ecb
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- NodeName Failover Cluster ,for nodes
- NodeName Failover Cluster
topic_type:
- apiref
api_name:
- NodeName
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# NodeName

Provides the name of the [node](nodes.md). The following table summarizes the attributes of the **NodeName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **NodeName** property is read-only, it cannot be changed using the [CLUSCTL\_NODE\_SET\_COMMON\_PROPERTIES](clusctl-node-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





