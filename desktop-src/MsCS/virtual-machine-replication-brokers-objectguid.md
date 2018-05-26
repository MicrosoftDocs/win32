---
title: ObjectGUID
description: Specifies the GUID of an Active Directory object corresponding to this resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92C1431D-25BC-4B39-BB98-77E4A3874B99
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ObjectGUID Failover Cluster , for virtual machine replication brokers
- ObjectGUID Failover Cluster
topic_type:
- apiref
api_name:
- ObjectGUID
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ObjectGUID

Specifies the **GUID** of an Active Directory object corresponding to this resource. The following table summarizes the attributes of the **ObjectGUID** property.



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

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





