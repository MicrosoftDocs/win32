---
title: Engine class
description: Controls the execution, progress reporting and results generation for a job.
ms.assetid: 6293A248-6A3B-49F7-BCE5-76AC95246825
keywords:
- Engine class Access Execution Engine
- Engine class Access Execution Engine , described
topic_type:
- apiref
api_name:
- Engine
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Engine class

Controls the execution, progress reporting and results generation for a job. A job consists of a collection of assessments. A solution uses this interface to access AXE functionality.

## When to implement

Never. This is an exposed interface that is already implemented.

**Engine** has these types of members:

-   [Methods](#methods)

### Methods

The **Engine** class has these methods.



| Method                                                          | Description                                                                                                                                     |
|:----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------|
| [**~Engine**](engine--engine.md)                               | Destructor method.<br/>                                                                                                                   |
| [**AnalyzeResults**](engine-analyzeresults.md)                 | Analyzes the assessment results.<br/>                                                                                                     |
| [**CancelAssessment**](engine-cancelassessment.md)             | Requests that the specified assessment stop running.<br/>                                                                                 |
| [**CancelJob**](engine-canceljob.md)                           | Requests that the current assessment stop running and the job end without running any more assessments.<br/>                              |
| [**ExecuteJob**](engine-executejob.md)                         | Runs a loaded job.<br/>                                                                                                                   |
| [**GetEventThreadingModel**](engine-geteventthreadingmodel.md) | Retrieve the threading model that is being used to call the solution s native events that have been registered with the Engine.<br/>      |
| [**RemovePendingRebootJob**](engine-removependingrebootjob.md) | Removes an abandoned task that restarts job execution upon a system restart so that other jobs can be executed.<br/>                      |
| [**SetAssessmentBegin**](engine-setassessmentbegin.md)         | Specifies the native interface for the **Engine** to invoke to notify the solution of an assessment begin event.<br/>                     |
| [**SetAssessmentEnd**](engine-setassessmentend.md)             | Specifies the native interface for the **Engine** to invoke to notify the solution of an assessment end event. <br/>                      |
| [**SetEventThreadingModel**](job-seteventthreadingmodel.md)    | Specifies the threading model that is being used to call the solution s native events that have been registered with the **Engine**.<br/> |
| [**SetJobBegin**](engine-setjobbegin.md)                       | Specifies the native interface for the **Engine** to invoke to notify the solution of a job begin event.<br/>                             |
| [**SetJobEnd**](engine-setjobend.md)                           | Specifies the native interface for the **Engine** to invoke to notify the solution of a job end event.<br/>                               |
| [**SetJobPending**](engine-setjobpending.md)                   | Specifies the native interface for the **Engine** to invoke to notify the solution of a job pending event.<br/>                           |
| [**SetJobRestart**](engine-setjobrestart.md)                   | Specifies the native interface for the **Engine** to invoke to notify the solution of a job restart event.<br/>                           |
| [**SetProgressUpdate**](engine-setprogressupdate.md)           | Specifies the native interface for the **Engine** to invoke to notify the solution of a progress update event.<br/>                       |
| [**TerminateJob**](engine-terminatejob.md)                     | This method ends an entire job without waiting for any assessment to exit.<br/>                                                           |



 

## Remarks

Managed code uses the [**Engine**](https://msdn.microsoft.com/library/windows/desktop/hh802913) object.

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

 

 





