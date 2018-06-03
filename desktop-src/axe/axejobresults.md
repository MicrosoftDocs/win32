---
title: AxeJobResults element
description: Assessments produce one or more XML files that contain individual results.
ms.assetid: DBB2BAE8-55D0-4A08-B835-C68D049230DA
keywords:
- AxeJobResults element Access Execution Engine
topic_type:
- apiref
api_name:
- AxeJobResults
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AxeJobResults element

Assessments produce one or more XML files that contain individual results. AXE aggregates all of the assessment result files into the final job results file. During that process, Axe adds this node around all of the aggregated results from individual assessments. Assessments do not write this node into their own results files.

## Usage

``` syntax
<AxeJobResults>
  child elements
</AxeJobResults>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                         | Description                                                                                                               |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**AnalysisJobInfo**](analysisjobinfo.md)<br/>           | Information about the analysis job, including platform version, run times, and log files.<br/> <br/>          |
| [**AssessmentResults**](assessmentresults.md)<br/>       | This element is a container for one or more [**AssessmentResult**](assessmentresult.md) elements.<br/> <br/> |
| [**Id**](id.md)<br/>                                     | A unique **GUID** identifier.<br/> <br/>                                                                      |
| [**MachineConfiguration**](machineconfiguration.md)<br/> | Contains elements that hold information about the computer.<br/> <br/>                                        |
| [**Meta**](meta.md)<br/>                                 | This node contains the entirety of the job used to generate a set of results.<br/> <br/>                      |



### Child element sequence

``` syntax
AssessmentResultsIdMachineConfigurationMetaAnalysisJobInfo
```

## Parent elements

There are no parent elements.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





