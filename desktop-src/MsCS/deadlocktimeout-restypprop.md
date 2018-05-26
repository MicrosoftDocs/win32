---
title: DeadlockTimeout
description: Specifies the period (in milliseconds) of the deadlock detection heartbeat.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 04a716f1-a79d-425f-b201-cd44645c37c5
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DeadlockTimeout Failover Cluster , for Resource Type common properties
- DeadlockTimeout Failover Cluster
topic_type:
- apiref
api_name:
- DeadlockTimeout
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DeadlockTimeout

Specifies the period (in milliseconds) of the deadlock detection heartbeat. The following table summarizes the attributes of the [**DeadlockTimeout**](deadlocktimeout.md) property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 30000 (30 seconds)<br/>                        |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 300000 (5 minutes)<br/>                        |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Resource Type Common Properties](resource-type-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





