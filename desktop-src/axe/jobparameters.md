---
title: JobParameters element
description: Describes the parameters of a job.
ms.assetid: BC14CEB1-7E8D-4739-89BC-E564B89B048A
keywords:
- JobParameters element Access Execution Engine
topic_type:
- apiref
api_name:
- JobParameters
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# JobParameters element

Describes the parameters of a job. These parameters control how a job runs and can be read by an assessment.

The parameter names and values that were used during the running of the job. They include job parameters that were defined in the job manifest as well as those parameters that were modified or added programmatically. This section uses the same format as the **JobParameters** section in the job manifest. See the AXE Job Manifest design document for the schema definition of this section.

## Usage

``` syntax
<JobParameters>
  child elements
</JobParameters>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                                 | Description                                                                                                                |
|-------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| [**AssessmentContentRoot**](assessmentcontentroot.md)<br/>       | The file path to assessment files. <br/> <br/>                                                                 |
| [**CollectOnly**](collectonly.md)<br/>                           | Run assessments but do not analyze.<br/> <br/>                                                                 |
| [**EarliestStartTime**](earlieststarttime.md)<br/>               | Earliest start time and date for the job in Coordinated Universal Time (UTC).<br/> <br/>                       |
| [**Image**](image.md)<br/>                                       | A UNC path to an offline image.<br/> <br/>                                                                     |
| [**KeepTempFiles**](keeptempfiles.md)<br/>                       | If this node is present then AXE will not delete each assessment's temporary files or report files.<br/> <br/> |
| [**PostExecutionAction**](postexecutionaction.md)<br/>           | After a job has completed, AXE may optionally run a program.<br/> <br/>                                        |
| [**ResultsPublishPath**](resultspublishpath.md)<br/>             | Specifies a UNC path to a file containing results.<br/> <br/>                                                  |
| [**RunSilently**](runsilently.md)<br/>                           | If this element is present, the solution displays no UX excepting errors.<br/> <br/>                           |
| [**SkipMachineConfiguration**](skipmachineconfiguration.md)<br/> | Omit machine configuration when running assessments.<br/> <br/>                                                |
| [**SolutionUX**](solutionux.md)<br/>                             | The mode of interacting with the user when the job runs.<br/> <br/>                                            |
| [**StopOnAssessmentError**](stoponassessmenterror.md)<br/>       | AXE stops the job if this element is present and an assessment returns a non-zero value. <br/> <br/>           |
| [**UserString**](userstring.md)<br/>                             | This string is provided by a solution.<br/> <br/>                                                              |



### Child element sequence

``` syntax
(
  Image, 
  EarliestStartTime, 
  KeepTempFiles, 
  ResultsPublishPath, 
  PostExecutionAction, 
  UserString, 
  StopOnAssessmentError, 
  RunSilently, 
  AssessmentContentRoot
, 
  CollectOnly
, 
  SkipMachineConfiguration, 
  SolutionUX
)
```

## Parent elements



| Element                         | Description                                                                |
|---------------------------------|----------------------------------------------------------------------------|
| [**Meta**](meta.md)<br/> | Meta-information about the start time and duration.<br/> <br/> |



## Remarks

As a solution assembles a job, the assessment management API's will check some of these parameters for consistency   returning warnings to the solution as appropriate.

The AXE assessment management object model will save and restore job parameters changed by a solution.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Job Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449330)
</dt> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





