---
title: AntiAffinityClassNames
description: Used to identify groups that should not be hosted on the same cluster node. The following table summarizes the attributes of the AntiAffinityClassNames property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 381973f9-db41-48b7-9833-483da3e79f92
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AntiAffinityClassNames Failover Cluster ,for Groups
- AntiAffinityClassNames Failover Cluster
topic_type:
- apiref
api_name:
- AntiAffinityClassNames
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# AntiAffinityClassNames

Used to identify [groups](groups.md) that should not be hosted on the same cluster [node](nodes.md). The following table summarizes the attributes of the **AntiAffinityClassNames** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | MULTI-SZ                                                         |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_MULTI\_SZ**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_sz?branch=master)                 |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

A group's **AntiAffinityClassNames** property consists of zero or more arbitrary user-defined strings. If the **AntiAffinityClassNames** properties of two or more groups contain at least one identical string, the groups are said to be anti-affined. By default, all groups are affined (because their **AntiAffinityClassNames** property is **NULL**).

When a group is moved during failover, anti-affinity affects the algorithm used to determine the destination node as follows:

1.  Using the [*preferred owner*](p-gly.md#-wolf-preferred-owner-gly) list of the group being moved, the Cluster service finds the next preferred node.
2.  If the node is not hosting any group anti-affined with the group being moved, it is selected as the destination node.
3.  If the next preferred available node is currently hosting a group anti-affined with the group being moved, the Cluster service moves to the next preferred available node in the preferred owner list.
4.  If the only available nodes are hosting anti-affined groups, the Cluster service ignores anti-affinity and selects the next preferred available node as the destination node.

Use this property to identify groups that should not be hosted on the same node. Generate a unique string value (such as a GUID) and add it to the **AntiAffinityClassNames** property of each group that should be anti-affined.

Note that because of the behavior described in point 4 above, anti-affinity does not guarantee that groups will never be hosted by the same node. If you have an application that cannot support more than one instance per node under any circumstances, you need to create a resource DLL to enforce that limitation.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



 

 





