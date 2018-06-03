---
title: Inclusion (MetricThresholdValue) element
description: Indicates whether a comparison should be inclusive or exclusive.
ms.assetid: 01F977EF-4FDE-4665-9951-BC638DA66230
keywords:
- Inclusion (MetricThresholdValue) element Access Execution Engine
topic_type:
- apiref
api_name:
- Inclusion (MetricThresholdValue)
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Inclusion (MetricThresholdValue) element

Indicates whether a comparison should be inclusive or exclusive. This element maps to the [**MetricThresholdValueInclusion**](metricthresholdvalueinclusion.md) enumeration.

## Usage

``` syntax
<Inclusion (MetricThresholdValue)>
  child elements
</Inclusion (MetricThresholdValue)>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                                                                                                                                                                                                                         |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Exclusive**](exclusive.md)<br/> | Indicates that when AXE compares values to the [**MetricThresholdValue**](metricthresholdvalue.md) it is to use a greater-than test or a less-than test. The direction is determined by the [**BettterDirection**](betterdirection.md) of the metric's definition.<br/> <br/>                         |
| [**Inclusive**](inclusive.md)<br/> | Indicates that when AXE compares values to the [**MetricThresholdValue**](metricthresholdvalue.md) it is to use a greater-than or equal-to test or a less-than or equal-to test. The direction is determined by the [**BettterDirection**](betterdirection.md) of the metric's definition.<br/> <br/> |



### Child element sequence

``` syntax
InclusiveExclusive
```

## Parent elements



| Element                                                         | Description                                                                           |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**MetricThresholdValue**](metricthresholdvalue.md)<br/> | This node contains the data defining a metric threshold value.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





