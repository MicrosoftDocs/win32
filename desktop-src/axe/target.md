---
title: Target element
description: If present, this is the target value for a metric threshold.
ms.assetid: 'A1A29086-D089-496F-91B8-03C98C71282C'
keywords: ["Target element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Target
api_type:
- Schema
---

# Target element

If present, this is the target value for a metric threshold. Metric threshold values can be computed relative to this value. For example, a failing value can be computed as a percentage (like 120%) of the target value.

## Usage

``` syntax
<Target>
  child elements
</Target>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                         | Description                                                                               |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**MetricThresholdValue**](metricthresholdvalue.md)<br/> | This element contains the data defining a metric threshold value. <br/> <br/> |



### Child element sequence

``` syntax
MetricThresholdValue
```

## Parent elements



| Element                                               | Description                                                                               |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**MetricThreshold**](metricthreshold.md)<br/> | Each metric threshold describes how a Metric value is interpreted.<br/> <br/> |



## Remarks

The contents of this tag must be consistent with the data type of the Metric Definition associated with this threshold using the &lt;MetricDefinitionProgrammaticName&gt; tag. This node must contain one or two &lt;MetricThresholdValue&gt; child nodes.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





