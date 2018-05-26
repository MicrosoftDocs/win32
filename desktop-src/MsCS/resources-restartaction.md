---
title: RestartAction
description: Describes the action to be taken by the cluster service if the resource fails.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88be809b-a338-490a-82f3-886bfc2e3f37
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RestartAction Failover Cluster ,for resources
- RestartAction Failover Cluster
topic_type:
- apiref
api_name:
- RestartAction
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RestartAction

Describes the action to be taken by the [cluster service](cluster-service.md) if the [resource](resources.md) [fails](resource-failure.md). The following table summarizes the attributes of the **RestartAction** property:



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | **ClusterResourceDontRestart** (0)<br/>        |
| Maximum<br/>   | **ClusterResourceRestartNotify** (2)<br/>      |
| Default<br/>   | **ClusterResourceRestartNotify**<br/>          |



 

## Remarks

The data value for the **RestartAction** property can be set to the values of the [**CLUSTER\_RESOURCE\_RESTART\_ACTION**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_restart_action?branch=master) enumeration. The following table summarizes the possible values:



| Name                                          | Value        | Description                                                                                                                                                                                                                                                                |
|-----------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **ClusterResourceDontRestart**<br/>     | 0<br/> | Do not restart the resource after a failure.<br/>                                                                                                                                                                                                                    |
| **ClusterResourceRestartNoNotify**<br/> | 1<br/> | Restart the resource after a failure. If the resource exceeds its restart threshold within its restart period, do not attempt to [failover](failover.md) the [group](groups.md) to another [node](nodes.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly).<br/> |
| **ClusterResourceRestartNotify**<br/>   | 2<br/> | Restart the resource after a failure. If the resource exceeds its restart threshold within its restart period, attempt to fail over the group to another node in the cluster. This is the default setting.<br/>                                                      |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **RestartAction** can be set with the following example code:


```C++
DWORD          RestartActionData = ClusterResourceDontRestart;
CLUSPROP_DWORD RestartActionValue;

RestartActionValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RestartActionValue.cbLength  = sizeof(DWORD);
RestartActionValue.dw        = RestartActionData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[Resource Common Properties](resource-common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSTER\_RESOURCE\_RESTART\_ACTION**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_restart_action?branch=master)
</dt> </dl>

 

 





