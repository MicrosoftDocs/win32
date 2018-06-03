---
title: AutoFailbackType
description: Specifies whether the group should automatically be failed back to the node identified as its preferred owner when that node comes back online following a failover.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: cd06c375-2684-4943-8587-692e655b44a2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AutoFailbackType Failover Cluster ,for groups
- AutoFailbackType Failover Cluster
topic_type:
- apiref
api_name:
- AutoFailbackType
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AutoFailbackType

Specifies whether the [group](groups.md) should automatically be failed back to the [node](nodes.md) identified as its preferred owner when that node comes back online following a [failover](failover.md). The following table summarizes the attributes of the **AutoFailbackType** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | **ClusterGroupPreventFailback** (0)<br/>       |
| Maximum<br/>   | **ClusterGroupAllowFailback** (1)<br/>         |
| Default<br/>   | **ClusterGroupPreventFailback**<br/>           |



 

## Remarks

The data for the **AutoFailbackType** property can be set to one of the following values of the [**CLUSTER\_GROUP\_AUTOFAILBACK\_TYPE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_group_autofailback_type) enumeration.



| Name                                       | Value        | Description                                                                  |
|--------------------------------------------|--------------|------------------------------------------------------------------------------|
| **ClusterGroupPreventFailback**<br/> | 0<br/> | Prevents [failback](failback.md).<br/>                                |
| **ClusterGroupAllowFailback**<br/>   | 1<br/> | Allows failback (requires a preferred owners list for the group).<br/> |



 

Note that setting this property to **ClusterGroupAllowFailback** has no effect if you have not specified a preferred owners list for the group. Use the [**SetClusterGroupNodeList**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list) function to specify a preferred owners list.

## Examples

The property value portion of a [property list](property-lists.md) entry for **AutoFailbackType** can be set with the following example code:


```C++
DWORD          AutoFailbackTypeData = ClusterGroupAllowFailback;
CLUSPROP_DWORD AutoFailbackTypeValue;

AutoFailbackTypeValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
AutoFailbackTypeValue.cbLength  = sizeof(DWORD);
AutoFailbackTypeValue.dw        = AutoFailbackTypeData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Group Common Properties](common-properties-ref.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSTER\_GROUP\_AUTOFAILBACK\_TYPE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_group_autofailback_type)
</dt> <dt>

[**SetClusterGroupNodeList**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_group_node_list)
</dt> </dl>

 

 





