---
title: AssessmentRun element
description: Defines the instance of an assessment for execution.
ms.assetid: 88FBBFD1-8E26-45DD-9C33-A5DD09541CE4
keywords:
- AssessmentRun element Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentRun
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AssessmentRun element

Defines the instance of an assessment for execution.

## Usage

``` syntax
<AssessmentRun>
  child elements
</AssessmentRun>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                                                                  |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [**AssessmentId**](assessmentid.md)<br/>         | This is the identity of the assessment.<br/> <br/>                                                                               |
| [**CommandLine**](commandline.md)<br/>           | Contains the command line that is passed to the assessment process.<br/> <br/>                                                   |
| [**Id**](id.md)<br/>                             | A unique ID for an assessment run. This is a GUID in registry format.<br/> <br/>                                                 |
| [**MetricThresholds**](metricthresholds.md)<br/> | This node contains one or more metric thresholds.<br/> <br/>                                                                     |
| [**Name**](name.md)<br/>                         | This is the name of the assessment run. This value is set by a user using a solution.<br/> <br/>                                 |
| [**ParameterValues**](parametervalues.md)<br/>   | Contains zero or more [**ParameterValue**](parametervalue.md) elements.<br/> <br/>                                              |
| [**SolutionData**](solutiondata.md)<br/>         | This optional node contains any valid XML that the solution chooses to include in the job for a specific assessment. <br/> <br/> |



### Child element sequence

``` syntax
(
  Id, 
  Name, 
  AssessmentId, 
  SolutionData, 
  ParameterValues, 
  MetricThresholds, 
  CommandLine
)
```

## Parent elements



| Element                                             | Description                                                                                |
|-----------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**AssessmentRuns**](assessmentruns.md)<br/> | This node holds a collection of assessment instances for execution.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> </dl>

 

 





