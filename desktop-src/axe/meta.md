---
title: Meta element
description: Meta-information about the start time and duration.
ms.assetid: 3C10A806-1069-4C59-84BC-A58473065D8A
keywords:
- Meta element Access Execution Engine
topic_type:
- apiref
api_name:
- Meta
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Meta element

Meta-information about the start time and duration.

## Usage

``` syntax
<Meta>
  child elements
</Meta>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                 | Description                                                                                         |
|---------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| [**ExecutionGuid**](executionguid.md)<br/>       | The [**Guid**](guid.md) of the job execution.<br/> <br/>                               |
| [**JobDuration**](jobduration.md)<br/>           | The duration of the job in milliseconds.<br/> <br/>                                     |
| [**JobStartDateTime**](jobstartdatetime.md)<br/> | The date and time when the job started in Coordinated Universal Time format.<br/> <br/> |
| [**SessionLogFiles**](sessionlogfiles.md)<br/>   | The path of the folder that holds the log files for the job. <br/> <br/>                |



### Child element sequence

``` syntax
(
  JobStartDateTime, 
  JobDuration, 
  SessionLogFiles, 
  ExecutionGuid
)
```

## Parent elements



| Element                                           | Description                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| [**AxeJobResults**](axejobresults.md)<br/> | This node contains the entirety of the job used to generate a set of results.<br/> <br/> |



## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[AXE Results Manifest](https://msdn.microsoft.com/library/windows/desktop/hh449335)
</dt> </dl>

 

 





