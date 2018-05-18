---
title: Metric
description: Provides the Metric of the network in the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4e3f8b1a-744e-4de6-ac2e-1b85e7af6586'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Metric Failover Cluster ,for networks", "Metric Failover Cluster"]
topic_type:
- apiref
api_name:
- Metric
api_type:
- NA
---

# Metric

Provides the **Metric** of the [network](networks.md) in the [*cluster*](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **Metric** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](clusprop-dword.md)<br/> |
| Minimum<br/>   | 1<br/>                                         |
| Maximum<br/>   | 0x0FFFFFFF<br/>                                |
| Default<br/>   | 100<br/>                                       |



 

## Remarks

The **Metric** property is used by the cluster service to select the network path; the network path with the lowest sum of metrics will be used. If the **Metric** property is set to a value then the [**AutoMetric**](networks-autometric.md) property is set to 0.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Metric** can be set with the following example code:


```C++
DWORD          MetricData = 50;
CLUSPROP_DWORD MetricValue;

MetricValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
MetricValue.cbLength  = sizeof(DWORD);
MetricValue.dw        = MetricData;
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Enterprise, Windows Server 2008 R2 Datacenter<br/> |



## See also

<dl> <dt>

[Network Common Properties](common-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> <dt>

[**AutoMetric**](networks-autometric.md)
</dt> </dl>

 

 





