---
title: ProgrammaticName element
description: This is the programmatic name of the parameter or metric.
ms.assetid: 9b3aded9-1688-40c5-a572-41b2223aa323
keywords:
- ProgrammaticName element Access Execution Engine
topic_type:
- apiref
api_name:
- ProgrammaticName
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ProgrammaticName element

This is the programmatic name of the parameter or metric. A name that applications can use to identify the item for programmatic tasks such as reflection.

## Usage

``` syntax
<ProgrammaticName>
  text
</ProgrammaticName>
```

## Attributes

There are no attributes.

## Text value

This is the programmatic name of the item.

## Child elements

There are no child elements.

## Parent elements



| Element                                             | Description                                                                             |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**Description**](description.md)<br/>       | Provides a human-readable description.<br/> <br/>                           |
| [**Flag**](flag.md)<br/>                     | Describes a flag.<br/> <br/>                                                |
| [**MetricValue**](metricvalue.md)<br/>       | Describes a single metric value.<br/> <br/>                                 |
| [**ParameterValue**](parametervalue.md)<br/> | Describes a single assessment parameter.<br/> <br/>                         |
| [**TracingProfile**](tracingprofile.md)<br/> | Holds information that describes and directs a tracing activity.<br/> <br/> |



## Remarks

This is used to lookup the parameter type and other information in the assessment manifest information that is marshaled in the [**AssessmentManfests**](assessmentmanifests.md) collection.

Like a GUID, users should never see the programmatic name except when authoring an assessment.

This element can contain the programmatic name for a metric. This is defined by the assessment author and is never localized. The programmatic name is used as a key to look up the metric s definition it its corresponding assessment manifest.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[AXE Assessment Manifest](axeassessmentmanifest.md)
</dt> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





