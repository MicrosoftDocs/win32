---
title: Node
description: Provides the name of the node in which the network interface is installed. The following table summarizes the attributes of the Node property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f1259293-be22-4d89-ab4a-d431fa5eddf0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Node Failover Cluster ,for network interfaces
- Node Failover Cluster
topic_type:
- apiref
api_name:
- Node
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Node

Provides the name of the [node](nodes.md) in which the [network interface](network-interfaces.md) is installed. The following table summarizes the attributes of the **Node** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Node** property is read-only, it cannot be changed using the [CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





