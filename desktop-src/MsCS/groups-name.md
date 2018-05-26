---
title: Name
description: Specifies the name of the group. The following table summarizes the attributes of the Name property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2395438e-14d6-4a62-b3d9-c525bed8f652
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Name Failover Cluster ,for groups
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

Specifies the name of the [group](groups.md). The following table summarizes the attributes of the **Name** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Name** property is read-only, it cannot be changed using the [CLUSCTL\_GROUP\_SET\_COMMON\_PROPERTIES](clusctl-group-set-common-properties.md) control code. Applications can change a group's name by calling the [Cluster API](cluster-api.md) function [**SetClusterGroupName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name?branch=master).

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**SetClusterGroupName**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_name?branch=master)
</dt> </dl>

 

 





