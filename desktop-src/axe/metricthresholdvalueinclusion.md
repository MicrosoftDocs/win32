---
title: MetricThresholdValueInclusion enumeration
description: Indicates whether a comparison should be inclusive or exclusive.
ms.assetid: EBBA7629-AA33-4F8B-93AA-94E827EFCC51
keywords:
- MetricThresholdValueInclusion enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- MetricThresholdValueInclusion
api_location:
- AxeRuntime.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# MetricThresholdValueInclusion enumeration

Indicates whether a comparison should be inclusive or exclusive.

## Syntax


```C++
typedef enum _MetricThresholdValueInclusion { 
  MetricThresholdValueInclusion_NotSet    = 0,
  MetricThresholdValueInclusionInclusive,
  MetricThresholdValueInclusionExclusive,
  MetricThresholdValueInclusion_Max
} MetricThresholdValueInclusion;
```



## Constants

<dl> <dt>

<span id="MetricThresholdValueInclusion_NotSet"></span><span id="metricthresholdvalueinclusion_notset"></span><span id="METRICTHRESHOLDVALUEINCLUSION_NOTSET"></span>**MetricThresholdValueInclusion\_NotSet**
</dt> <dd>

Neither inclusive nor exclusive is specified.

</dd> <dt>

<span id="MetricThresholdValueInclusionInclusive"></span><span id="metricthresholdvalueinclusioninclusive"></span><span id="METRICTHRESHOLDVALUEINCLUSIONINCLUSIVE"></span>**MetricThresholdValueInclusionInclusive**
</dt> <dd>

Indicates that when AXE compares values to the [**MetricThresholdValue**](metricthresholdvalue.md) it is to use a greater-than or equal-to test or a less-than or equal-to test. The direction is determined by the [**BettterDirection**](betterdirection.md) of the metric's definition.

</dd> <dt>

<span id="MetricThresholdValueInclusionExclusive"></span><span id="metricthresholdvalueinclusionexclusive"></span><span id="METRICTHRESHOLDVALUEINCLUSIONEXCLUSIVE"></span>**MetricThresholdValueInclusionExclusive**
</dt> <dd>

Indicates that when AXE compares values to the [**MetricThresholdValue**](metricthresholdvalue.md) it is to use a greater-than test or a less-than test. The direction is determined by the [**BettterDirection**](betterdirection.md) of the metric's definition.

</dd> <dt>

<span id="MetricThresholdValueInclusion_Max"></span><span id="metricthresholdvalueinclusion_max"></span><span id="METRICTHRESHOLDVALUEINCLUSION_MAX"></span>**MetricThresholdValueInclusion\_Max**
</dt> <dd>

Invalid inclusion specification (the value of this member is one larger than the largest valid member).

</dd> </dl>

## Remarks

This enumeration maps to the [**Inclusion (MetricThresholdValue)**](inclusion--metricthresholdvalue-.md) element.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |



 

 





