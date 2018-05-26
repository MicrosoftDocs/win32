---
title: Name
description: Provides the name of the network being managed by the resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 091482F0-C42C-451F-BFC9-F94329637D24
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for virtual machine replication brokers
- Name Failover Cluster
topic_type:
- apiref
api_name:
- Name
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Name

Provides the name of the [network](networks.md) being managed by the resource. The following table summarizes the attributes of the **Name** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





