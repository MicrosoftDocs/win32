---
title: AssessmentResult element
description: Describes the result for an individual assessment.
ms.assetid: 71F1C816-03E2-49FB-B73E-F55029A532BC
keywords:
- AssessmentResult element Access Execution Engine
topic_type:
- apiref
api_name:
- AssessmentResult
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AssessmentResult element

Describes the result for an individual assessment. Assessments write their results files as XML files that use this node as the root node for the DOM. The assessment result files must also contain an XML declaration in order to be a valid XML file.

## Usage

``` syntax
<AssessmentResult>
  child elements
</AssessmentResult>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                   | Description                                                                                                                                          |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AnalysisInfo**](analysisinfo.md)<br/>           | Information about the execution of the assessment analysis.<br/> <br/>                                                                   |
| [**ErrorsAndWarnings**](errorsandwarnings.md)<br/> | A container element to hold assessment errors and warnings. <br/> <br/>                                                                  |
| [**ExecutionInfo**](executioninfo.md)<br/>         | Information about the execution of the assessment. <br/> <br/>                                                                           |
| [**ExitCode**](exitcode.md)<br/>                   | This element holds the exit code for an assessment s process.<br/> <br/>                                                                 |
| [**Guid**](guid.md)<br/>                           | The unique identifier for the assessment run.<br/> <br/>                                                                                 |
| [**Iterations**](iterations.md)<br/>               | A container element to hold [**Iteration**](iteration.md) elements.<br/> <br/>                                                          |
| [**LogFiles**](logfiles.md)<br/>                   | A container to hold [**LogFile**](logfile.md) elements.<br/> <br/>                                                                      |
| [**ResultsLocation**](resultslocation.md)<br/>     | The relative path from the directory containing the job results file to the directory containing the assessment results file.<br/> <br/> |



### Child element sequence

``` syntax
(
  Guid, 
  ExitCode, 
  LogFiles, 
  ErrorsAndWarnings, 
  Iterations, 
  ResultsLocation, 
  AnalysisInfo, 
  ExecutionInfo
)
```

## Parent elements



| Element                                                   | Description                                                                                       |
|-----------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| [**AssessmentResults**](assessmentresults.md)<br/> | This element is a container for one or more **AssessmentResult** elements.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





