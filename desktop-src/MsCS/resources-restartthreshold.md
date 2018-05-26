---
title: RestartThreshold
description: Specifies the maximum number of restart attempts that can be made on a resource within an interval defined by the RestartPeriod property before the Cluster service initiates the action specified by the RestartAction property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0fc4a0bd-f74f-4aad-a369-f4adbe998122
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RestartThreshold Failover Cluster ,for resources
- RestartThreshold Failover Cluster
topic_type:
- apiref
api_name:
- RestartThreshold
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RestartThreshold

Specifies the maximum number of restart attempts that can be made on a [resource](resources.md) within an interval defined by the [**RestartPeriod**](resources-restartperiod.md) property before the [Cluster service](cluster-service.md) initiates the action specified by the [**RestartAction**](resources-restartaction.md) property. The following table summarizes the attributes of the **RestartThreshold** property:



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 3<br/>                                         |



 

## Remarks

When a resource does fails, the Cluster service attempts to restart the resource (unless the [**RestartAction**](resources-restartaction.md) property is set to **ClusterResourceDontRestart**).

The [**RestartPeriod**](resources-restartperiod.md) and **RestartThreshold** properties work together to limit restart attempts. For example, if the [**RestartPeriod**](resources-restartperiod.md) property is set to 200 milliseconds, and the **RestartThreshold** property is set to two retry attempts, then the Cluster service tolerates two restart failures within any 200 millisecond interval. More than two failures can occur, as long as they occur over an interval that is greater than 200 milliseconds. On the third restart failure within the 200 millisecond interval, the Cluster service considers the resource to have failed and may, depending on the [**RestartAction**](resources-restartaction.md) property, attempt to [fail over](failover.md) the resource's [group](groups.md) to another [node](nodes.md).

## Examples

The property value portion of a [property list](property-lists.md) entry for **RestartThreshold** can be set with the following example code:


```C++
DWORD          RestartThresholdData = 5;
CLUSPROP_DWORD RestartThresholdValue;

RestartThresholdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RestartThresholdValue.cbLength =  sizeof(DWORD);
RestartThresholdValue.dw =        RestartThresholdData;
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

[**RestartAction**](resources-restartaction.md)
</dt> <dt>

[**RestartPeriod**](resources-restartperiod.md)
</dt> </dl>

 

 





