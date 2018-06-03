---
title: Job class
description: This interface represents information about a job.
ms.assetid: BAF26A97-849A-4376-9628-C882EEF3F055
keywords:
- Job class Access Execution Engine
- Job class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Job
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Job class

This interface represents information about a job.

**Job** has these types of members:

-   [Methods](#methods)

### Methods

The **Job** class has these methods.



| Method                                               | Description                                                                      |
|:-----------------------------------------------------|:---------------------------------------------------------------------------------|
| [**~Job**](job--job.md)                             | Destructor method.<br/>                                                    |
| [**CheckPrerequisites**](job-checkprerequisites.md) | Retrieves a collection of unmet assessment prerequisites.<br/>             |
| [**GetAssessment**](job-getassessment.md)           | Retrieve a specific assessment from the job. <br/>                         |
| [**GetAssessmentCount**](job-getassessmentcount.md) | Retrieve the number of assessments in the job.<br/>                        |
| [**GetJobParameter**](job-getjobparameter.md)       | Retrieve the value of a specified job parameter.<br/>                      |
| [**GetName**](job-getname.md)                       | Retrieve the name of the job as specified in the job manifest.<br/>        |
| [**GetToolTip**](job-gettooltip.md)                 | Retrieve a tool tip for the job. <br/>                                     |
| [**SetJobParameter**](job-setjobparameter.md)       | Creates or updates a job parameter with the specified name and value.<br/> |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Execution Solution Interfaces**](execution-solution-interfaces.md)
</dt> </dl>

 

 





