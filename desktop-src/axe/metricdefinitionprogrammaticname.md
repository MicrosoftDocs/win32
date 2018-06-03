---
title: MetricDefinitionProgrammaticName element
description: Each metric threshold must be associated with one metric definition.
ms.assetid: 8FA8E5FE-4596-45D2-A844-CF414A2FCA33
keywords:
- MetricDefinitionProgrammaticName element Access Execution Engine
topic_type:
- apiref
api_name:
- MetricDefinitionProgrammaticName
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MetricDefinitionProgrammaticName element

Each metric threshold must be associated with one metric definition.

## Usage

``` syntax
<MetricDefinitionProgrammaticName>
  text
</MetricDefinitionProgrammaticName>
```

## Attributes

There are no attributes.

## Text value

This node contains the name of a metric definition contained in the MetricDefinitions collection.

## Child elements

There are no child elements.

## Parent elements



| Element                                               | Description                                                                               |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------|
| [**MetricThreshold**](metricthreshold.md)<br/> | Each metric threshold describes how a Metric value is interpreted.<br/> <br/> |



## Remarks

Only one metric threshold per combination of metric definition and test case key is allowed.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> </dl>

 

 





