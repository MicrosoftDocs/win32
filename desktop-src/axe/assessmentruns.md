---
title: AssessmentRuns element
description: A collection of one or more assessment instances for execution.
ms.assetid: D96B03D7-737D-4630-9FDB-907120B5684D
keywords:
- AssessmentRuns element Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentRuns
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AssessmentRuns element

A collection of one or more assessment instances for execution. An assessment instance defines data needed to run a particular instance of an assessment. The assessment is described by the information the [**AssessmentManifests**](assessmentmanifests.md) element.

## Usage

``` syntax
<AssessmentRuns>
  child elements
</AssessmentRuns>
```

## Attributes

There are no attributes.

## Child elements



| Element                                           | Description                                                                 |
|---------------------------------------------------|-----------------------------------------------------------------------------|
| [**AssessmentRun**](assessmentrun.md)<br/> | Defines the instance of an assessment for execution.<br/> <br/> |



### Child element sequence

``` syntax
AssessmentRun
```

## Parent elements



| Element                                             | Description                                                     |
|-----------------------------------------------------|-----------------------------------------------------------------|
| [**AxeJobManifest**](axejobmanifest.md)<br/> | Name of the root node of the assessment.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





