---
title: MetricValue element
description: Describes a single metric value.
ms.assetid: 8CEC3D70-A064-42DF-8B4D-FDAAFB8BF0B8
keywords:
- MetricValue element Access Execution Engine
topic_type:
- apiref
api_name:
- MetricValue
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MetricValue element

Describes a single metric value.

A metric value is a single result and uniquely identified by:

<dl> Its programmatic name  
The iteration from an assessment run  
A specific assessment identified by an assessment [**Id**](id.md).  
A specific job, identified by an [**Id**](id.md) and a [**JobStartDateTime**](jobstartdatetime.md) when it was run.  
</dl>

A metric can be described by two things:

<dl> Its corresponding Metric Definition from the Assessment Manifest  
One or more Metric Validation Thresholds from the Job manifest.  
</dl>

## Usage

``` syntax
<MetricValue>
  child elements
</MetricValue>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                 |
|---------------------------------------------------------|-------------------------------------------------------------|
| [**ProgrammaticName**](programmaticname.md)<br/> | The programmatic name of the metric.<br/> <br/> |
| [**Value**](value.md)<br/>                       | This element contains a value.<br/> <br/>       |



### Child element sequence

``` syntax
(
  Value, 
  ProgrammaticName
)
```

## Parent elements



| Element                                         | Description                                                                          |
|-------------------------------------------------|--------------------------------------------------------------------------------------|
| [**MetricValues**](metricvalues.md)<br/> | A container element for one or more **MetricValue** elements.<br/> <br/> |



## Remarks

Metrics can have many different data types as described in the &lt;MetricDefintions&gt; node in an assessment manifest

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





