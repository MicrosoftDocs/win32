---
title: ObjectGUID
description: GUID of an Active Directory object corresponding to this network name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e42c68a8-c755-425d-9761-279768fa0ae6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ObjectGUID Failover Cluster , for Network Name properties
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

**GUID** of an Active Directory object corresponding to this network name. The following table summarizes the attributes of the **ObjectGUID** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> </dl>

 

 





