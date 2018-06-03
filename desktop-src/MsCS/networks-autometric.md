---
title: AutoMetric
description: Provides the AutoMetric of the network in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3961413d-7d87-42c1-ade2-64ffb8324eb3
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AutoMetric Failover Cluster ,for networks
- AutoMetric Failover Cluster
topic_type:
- apiref
api_name:
- AutoMetric
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AutoMetric

Provides the **AutoMetric** of the [network](networks.md) in the [*cluster*](https://www.bing.com/search?q=*cluster*). The following table summarizes the attributes of the **AutoMetric** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 1<br/>                                         |
| Default<br/>   | 1<br/>                                         |



 

## Remarks

The **AutoMetric** property determines whether the cluster service is allowed to automatically adjust the network [**Metric**](networks-metric.md) property. If the **Metric** property is set to a value then the **AutoMetric** property is set to 0. To allow the cluster to adjust the **Metric** automatically, set the **AutoMetric** property to 1. The cluster service selects the network path with the lowest sum of metrics.

## Examples

The property value portion of a [property list](property-lists.md) entry for **AutoMetric** can be set with the following example code:


```C++
DWORD          AutoMetricData = 0;
CLUSPROP_DWORD AutoMetricValue;

AutoMetricValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
AutoMetricValue.cbLength  = sizeof(DWORD);
AutoMetricValue.dw        = AutoMetricData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Network Common Properties](common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**Metric**](networks-metric.md)
</dt> </dl>

 

 





