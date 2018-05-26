---
title: JobEndEventArgs structure
description: This structure defines the event arguments passed to an OnJobEnd event.
ms.assetid: 78F46399-B791-401F-9712-27166CCE7E54
keywords:
- JobEndEventArgs structure Access Execution Engine
topic_type:
- apiref
api_name:
- JobEndEventArgs
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# JobEndEventArgs structure

This structure defines the event arguments passed to an OnJobEnd event.

## Syntax


```C++
struct JobEndEventArgs {
  DWORD             Size;
  const Job         *Job;
  JobExecutionError Error;
  const ErrorList   *ErrorList;
  UINT              ExecutedAssessmentCount;
  UINT              FailedAssessmentCount;
  LPCWSTR           ResultPath;
  WCHAR             ResultFolder[RESULTS_MAX_FILENAME];
  WCHAR             ResultFileName[RESULTS_MAX_FILENAME];
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure.

</dd> <dt>

**Job**
</dt> <dd>

A pointer to the Job object that has been queued for execution. The Job object is owned by the AXE engine and should not be deleted.

</dd> <dt>

**Error**
</dt> <dd>

The value of the last error that occurred in processing the job, i.e. the last error in the job error list.

<dl> <dd>If the job succeeds, this field contains **S\_OK**.</dd> <dd>If the job could not start because another job is restarting, this field contains **AXE\_E\_JOB\_ANOTHER\_REBOOT\_PENDING**.</dd> <dd>If there was an error preparing to execute an assessment, this field contains **AXE\_E\_JOB\_ASSESSMENT\_PREPARATION**.</dd> <dd>If the job finished with one or more failed assessments, this field contains **AXE\_E\_JOB\_ASSESSMENTS\_FAILED**.</dd> <dd>If the job execution was canceled or terminated, this field contains **AXE\_E\_JOB\_CANCELED**.</dd> <dd>If the job that was automatically executed by the solution application after a restart was modified or different from the job that was running before the restart, this field contains **AXE\_E\_JOB\_CHANGED**.</dd> <dd>If there is no job currently pending a restart, but a restart command was not specified in the [**JobExecutionInfo**](jobexecutioninfo.md) parameter, this field contains **AXE\_E\_JOB\_NO\_REBOOT\_PENDING**.</dd> <dd>If there was an error performing the [**PostExecutionAction**](postexecutionaction.md) listed in the job manifest, this field contains **AXE\_E\_JOB\_POSTEXECUTION**.</dd> <dd>If the job could not be executed because some preparation step prior to running any assessments failed. , this field contains **AXE\_E\_JOB\_PREPARATION**. See the log files for information on the exact failure.</dd> <dd>If the job restart state data was corrupt upon restart, this field contains **AXE\_E\_JOB\_RESTART\_FAILED**.</dd> <dd>If there was an error generating or finalizing the results file, this field contains **AXE\_E\_JOB\_RESULTS\_FAILED**.</dd> <dd>If the job is already being executed. Only one job may be executed at a time, this field contains **AXE\_E\_JOB\_RUNNING**.</dd> <dd>If there was an error while trying to change solutions. If the job manifest specifies a SolutionUX of Console or Silent, the solution running the job will spawn a new solution running with the specified level of visibility. If Console is specified, the new solution is specified by the [**JobExecutionInfo.RestartMinimumCommand**](jobexecutioninfo.md) field. This field contains **AXE\_E\_JOB\_SOLUTION\_RESTART**.</dd> <dd>If a [**JobExecutionInfo**](jobexecutioninfo.md) object was not specified or one of the fields has an issue, this field contains **E\_INVALIDARG**. See the log files for information on the exact failure., </dd> </dl>

The **JobEndEventArgs.ErrorList** field contains additional errors and warnings that happened during the execution. These are frequently more detailed information about the failures.

</dd> <dt>

**ErrorList**
</dt> <dd>

The value of the last error that occurred in processing the job, i.e. the last error in the job error list.

</dd> <dt>

**ExecutedAssessmentCount**
</dt> <dd>

The total number of assessments that were executed.

</dd> <dt>

**FailedAssessmentCount**
</dt> <dd>

The number of assessments that did not complete successfully.

</dd> <dt>

**ResultPath**
</dt> <dd>

The absolute path to the directory that contains the folders of all job results. If the results could not be copied to the *ResultsPublishPath* location as specified in the job manifest this path will point to where the results files are generated during execution.

</dd> <dt>

**ResultFolder**
</dt> <dd>

The folder under **ResultPath** that contains all of the results from the job that just ended.

The value of **RESULTS\_MAX\_FILENAME** is 65.

</dd> <dt>

**ResultFileName**
</dt> <dd>

The name of the XML file that contains the aggregated results from all assessments that ran. This is the results file that is loaded by the Windows Assessment Console.

The value of **RESULTS\_MAX\_FILENAME** is 65.

</dd> </dl>

## Remarks

When a job finishes execution and the results of all assessments have been aggregated, and &lt;PostExecutionAction&gt; in the job manifest has been executed and debug logs have been produced, the engine raises an IJobEndEventHandler::OnJobEnd event and passes this structure to the handler.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





