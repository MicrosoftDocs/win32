---
title: Description element
description: Describes a manifest or metric.
ms.assetid: '80EAEB04-EAD8-44EB-8040-F5A7695B8A5D'
keywords: ["Description element Access Execution Engine"]
topic_type:
- apiref
api_name:
- Description
api_type:
- Schema
---

# Description element

Describes a manifest or metric.

## Usage

``` syntax
<Description>
  child elements
</Description>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                    |
|---------------------------------------------------------|--------------------------------------------------------------------------------|
| [**Categories**](categories.md)<br/>             | Categories that enable the UX to handle multiple items.<br/> <br/> |
| [**DisplayName**](displayname.md)<br/>           | This is a human-readable name for the item.<br/> <br/>             |
| [**Information**](details.md)<br/>               | Localized information about what is being described.<br/> <br/>    |
| [**ProgrammaticName**](programmaticname.md)<br/> | This is the programmatic name of the item.<br/> <br/>              |
| [**Tags**](tags.md)<br/>                         | Contains one or more [**Tag**](tag.md) elements.<br/> <br/>       |
| [**ToolTip**](tooltip.md)<br/>                   | A short description that can be used in the UX.<br/> <br/>         |



### Child element sequence

``` syntax
(
  ProgrammaticName, 
  DisplayName, 
  ToolTip, 
  Information, 
  Tags, 
  Categories
)
```

## Parent elements



| Element                                                           | Description                                                                                                                                                                                                                  |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssessmentManifest**](https://msdn.microsoft.com/library/windows/desktop/hh449288)<br/>       | The root node of the assessment.<br/> <br/>                                                                                                                                                                      |
| [**AxeAssessmentManifest**](axeassessmentmanifest.md)<br/> | This is the root node of an assessment manifest.<br/> <br/>                                                                                                                                                      |
| [**AxeJobManifest**](axejobmanifest.md)<br/>               | Name of the root node of the assessment.<br/> <br/>                                                                                                                                                              |
| [**MetricDefinition**](metricdefinition.md)<br/>           | This element describes the metrics produced by an assessment.<br/> <br/>                                                                                                                                         |
| [**MetricThreshold**](metricthreshold.md)<br/>             | Each metric threshold describes how a Metric value is interpreted.<br/> <br/>                                                                                                                                    |
| [**MetricThresholdValue**](metricthresholdvalue.md)<br/>   | This node contains the data defining a metric threshold value.<br/> <br/>                                                                                                                                        |
| [**ParameterDefinition**](parameterdefinition.md)<br/>     | Information that fully describes an assessment parameter. <br/> <br/>                                                                                                                                            |
| [**Trace**](trace.md)<br/>                                 | An optional trace file associated with this iteration. Inside of a [**Trace**](trace.md) element, only the [**DisplayName**](displayname.md) and [**ToolTip**](tooltip.md) elements are supported.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





