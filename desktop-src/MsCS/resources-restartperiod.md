---
title: RestartPeriod
description: Defines an interval of time, in milliseconds, during which a specified number of restart attempts can be made on a nonresponsive resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b98f3f99-91c6-45e9-9eda-ce3c6e75c771
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- RestartPeriod Failover Cluster ,for resources
- RestartPeriod Failover Cluster
topic_type:
- apiref
api_name:
- RestartPeriod
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RestartPeriod

Defines an interval of time, in milliseconds, during which a specified number of restart attempts can be made on a nonresponsive [resource](resources.md). The [**RestartThreshold**](resources-restartthreshold.md) property specifies the allowable number of restart attempts that can occur within the interval defined by **RestartPeriod**. The following table summarizes the attributes of the **RestartPeriod** property:



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**<br/>                      |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 0xFFFFFFFF<br/>                     |
| Default<br/>   | 900000<br/>                         |



 

## Remarks

When a resource fails, the [Cluster service](cluster-service.md) attempts to restart the resource (unless the [**RestartAction**](resources-restartaction.md) property is set to **ClusterResourceDontRestart**).

The **RestartPeriod** and [**RestartThreshold**](resources-restartthreshold.md) properties work together to limit restart attempts. For example, if the **RestartPeriod** property is set to 200 milliseconds, and the **RestartThreshold** property is set to two retry attempts, the [Cluster service](cluster-service.md) tolerates two restart failures within any 200 millisecond interval. More than two failures can occur, as long as they occur over an interval that is greater than 200 milliseconds. On the third restart failure within the 200 millisecond interval, the Cluster service considers the resource to have failed and may, depending on the [**RestartAction**](resources-restartaction.md) property, attempt to [fail over](failover.md) the resource's [group](groups.md) to another [node](nodes.md).

After the interval defined by the **RestartPeriod** property is exceeded, the Cluster service resets the property to zero.

If not specified, the default value for the **RestartPeriod** property is 90000 milliseconds.

## Examples

The property value portion of a [property list](property-lists.md) entry for **RestartPeriod** can be set with the following example code:


```C++
DWORD          RestartPeriodData = 1800000;
CLUSPROP_DWORD RestartPeriodValue;

RestartPeriodValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
RestartPeriodValue.cbLength =  sizeof(DWORD);
RestartPeriodValue.dw =        RestartPeriodData;
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

[**RestartThreshold**](resources-restartthreshold.md)
</dt> </dl>

 

 





