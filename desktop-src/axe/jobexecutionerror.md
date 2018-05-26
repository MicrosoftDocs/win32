---
title: JobExecutionError enumeration
description: Provides an enumeration of AXE errors that are relevant to the execution of a job.
ms.assetid: AE12F4B9-0F69-49BC-B0BF-4D05C1A6546F
keywords:
- JobExecutionError enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- JobExecutionError
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# JobExecutionError enumeration

Provides an enumeration of AXE errors that are relevant to the execution of a job.

## Syntax


```C++
enum JobExecutionError {
  JobExecutionErrorNone                   = 0, 
  JobExecutionErrorCanceled               = AXE_E_JOB_CANCELED, 
  JobExecutionErrorAssessmentsFailed      = AXE_E_JOB_ASSESSMENTS_FAILED, 
  JobExecutionErrorAnotherRebootPending   = AXE_E_JOB_ANOTHER_REBOOT_PENDING, 
  JobExecutionErrorNoRebootPending        = AXE_E_JOB_NO_REBOOT_PENDING, 
  JobExecutionErrorPreparation            = AXE_E_JOB_PREPARATION, 
  JobExecutionErrorResultsFailed          = AXE_E_JOB_RESULTS_FAILED, 
  JobExecutionErrorAssessmentPreparation  = AXE_E_JOB_ASSESSMENT_PREPARATION, 
  JobExecutionErrorPostExecution          = AXE_E_JOB_POSTEXECUTION, 
  JobExecutionErrorWaitTimeout            = AXE_E_JOB_WAIT_TIMEOUT, 
  JobExecutionErrorChanged                = AXE_E_JOB_CHANGED, 
  JobExecutionErrorRestartFailed          = AXE_E_JOB_RESTART_FAILED, 
  JobExecutionErrorRestartBadData         = AXE_E_JOB_RESTART_BADDATA, 
  JobExecutionErrorRestart                = AXE_E_JOB_RESTART 

};
```



## Constants

<dl> <dt>

<span id="JobExecutionErrorNone"></span><span id="jobexecutionerrornone"></span><span id="JOBEXECUTIONERRORNONE"></span>**JobExecutionErrorNone**
</dt> <dd>

0

The job ran successfully.

</dd> <dt>

<span id="JobExecutionErrorCanceled"></span><span id="jobexecutionerrorcanceled"></span><span id="JOBEXECUTIONERRORCANCELED"></span>**JobExecutionErrorCanceled**
</dt> <dd>

0x80041013

The job was canceled or terminated.

</dd> <dt>

<span id="JobExecutionErrorAssessmentsFailed"></span><span id="jobexecutionerrorassessmentsfailed"></span><span id="JOBEXECUTIONERRORASSESSMENTSFAILED"></span>**JobExecutionErrorAssessmentsFailed**
</dt> <dd>

0x80041014

The job ended with one or more failed assessments.

</dd> <dt>

<span id="JobExecutionErrorAnotherRebootPending"></span><span id="jobexecutionerroranotherrebootpending"></span><span id="JOBEXECUTIONERRORANOTHERREBOOTPENDING"></span>**JobExecutionErrorAnotherRebootPending**
</dt> <dd>

0x80041015

The job could not start because another job is restarting.

</dd> <dt>

<span id="JobExecutionErrorNoRebootPending"></span><span id="jobexecutionerrornorebootpending"></span><span id="JOBEXECUTIONERRORNOREBOOTPENDING"></span>**JobExecutionErrorNoRebootPending**
</dt> <dd>

0x80041016

There is no job currently pending a reboot.

</dd> <dt>

<span id="JobExecutionErrorPreparation"></span><span id="jobexecutionerrorpreparation"></span><span id="JOBEXECUTIONERRORPREPARATION"></span>**JobExecutionErrorPreparation**
</dt> <dd>

0x80041017

The job could not be executed because some preparation step failed. Check the logs for more details.

</dd> <dt>

<span id="JobExecutionErrorResultsFailed"></span><span id="jobexecutionerrorresultsfailed"></span><span id="JOBEXECUTIONERRORRESULTSFAILED"></span>**JobExecutionErrorResultsFailed**
</dt> <dd>

0x80041018

There was an error generating or finalizing the results file.

</dd> <dt>

<span id="JobExecutionErrorAssessmentPreparation"></span><span id="jobexecutionerrorassessmentpreparation"></span><span id="JOBEXECUTIONERRORASSESSMENTPREPARATION"></span>**JobExecutionErrorAssessmentPreparation**
</dt> <dd>

0x80041019

There was an error preparing to execute an assessment.

</dd> <dt>

<span id="JobExecutionErrorPostExecution"></span><span id="jobexecutionerrorpostexecution"></span><span id="JOBEXECUTIONERRORPOSTEXECUTION"></span>**JobExecutionErrorPostExecution**
</dt> <dd>

0x8004101A

There was an error performing the job *PostExecutionAction*.

</dd> <dt>

<span id="JobExecutionErrorWaitTimeout"></span><span id="jobexecutionerrorwaittimeout"></span><span id="JOBEXECUTIONERRORWAITTIMEOUT"></span>**JobExecutionErrorWaitTimeout**
</dt> <dd>

0x8004101B

The job could not be executed because the timeout elapsed before the current running job finished.

</dd> <dt>

<span id="JobExecutionErrorChanged"></span><span id="jobexecutionerrorchanged"></span><span id="JOBEXECUTIONERRORCHANGED"></span>**JobExecutionErrorChanged**
</dt> <dd>

0x80041021

The job automatically executed by the solution after a reboot was modified or not the same.

</dd> <dt>

<span id="JobExecutionErrorRestartFailed"></span><span id="jobexecutionerrorrestartfailed"></span><span id="JOBEXECUTIONERRORRESTARTFAILED"></span>**JobExecutionErrorRestartFailed**
</dt> <dd>

0x80041022

The job restart state data was corrupt upon restart.

</dd> <dt>

<span id="JobExecutionErrorRestartBadData"></span><span id="jobexecutionerrorrestartbaddata"></span><span id="JOBEXECUTIONERRORRESTARTBADDATA"></span>**JobExecutionErrorRestartBadData**
</dt> <dd>

0x80041023

The job restart state data could not be saved while running.

</dd> <dt>

<span id="JobExecutionErrorRestart"></span><span id="jobexecutionerrorrestart"></span><span id="JOBEXECUTIONERRORRESTART"></span>**JobExecutionErrorRestart**
</dt> <dd>

0x80041025

There was an error while trying to change solutions.

</dd> </dl>

## Remarks

Managed code uses the [**JobExecutionError**](axe-jobexecutionerror_om) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





