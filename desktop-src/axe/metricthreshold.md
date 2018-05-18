---
title: MetricThreshold element
description: Each metric threshold describes how a Metric value is interpreted.
ms.assetid: 'D5D1C1D6-4483-4650-95E8-7E619CF6BC9D'
keywords: ["MetricThreshold element Access Execution Engine"]
topic_type:
- apiref
api_name:
- MetricThreshold
api_type:
- Schema
---

# MetricThreshold element

Each metric threshold describes how a Metric value is interpreted.

## Usage

``` syntax
<MetricThreshold>
  child elements
</MetricThreshold>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                                 | Description                                                                                                                                          |
|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Description**](description.md)<br/>                                           | Describes of the metric threshold.<br/> <br/>                                                                                            |
| [**MetricDefinitionProgrammaticName**](metricdefinitionprogrammaticname.md)<br/> | Each metric threshold must be associated with one metric definition. <br/> <br/>                                                         |
| [**Target**](target.md)<br/>                                                     | If present, this is the target value for a metric threshold. Metric threshold values can be computed relative to this value. <br/> <br/> |



### Child element sequence

``` syntax
(
  Description, 
  MetricDefinitionProgrammaticName, 
  Target
)
```

## Parent elements



| Element                                                 | Description                                                              |
|---------------------------------------------------------|--------------------------------------------------------------------------|
| [**MetricThresholds**](metricthresholds.md)<br/> | This node contains one or more metric thresholds.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





