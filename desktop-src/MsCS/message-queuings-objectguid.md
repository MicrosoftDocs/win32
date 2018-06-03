---
title: ObjectGUID
description: Contains the GUID of an Active Directory object corresponding to this resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44ECC6BB-4099-4D9A-A236-6D2F24EC9446
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ObjectGUID Failover Cluster , for message queuings
- ObjectGUID Failover Cluster
topic_type:
- apiref
api_name:
- ObjectGUID
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ObjectGUID

Contains the **GUID** of an Active Directory object corresponding to this resource. The following table summarizes the attributes of the **ObjectGUID** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
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

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





