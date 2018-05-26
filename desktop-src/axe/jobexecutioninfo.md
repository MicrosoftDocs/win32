---
title: JobExecutionInfo structure
description: This structure defines configuration information for how a Job is executed and returns information about the job execution.
ms.assetid: 9D336E58-763E-4CBF-8505-4F46B3062E74
keywords:
- JobExecutionInfo structure Access Execution Engine
topic_type:
- apiref
api_name:
- JobExecutionInfo
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

# JobExecutionInfo structure

This structure defines configuration information for how a Job is executed and returns information about the job execution

## Syntax


```C++
struct JobExecutionInfo {
  DWORD             Size;
  const Job         *Job;
  DWORD             Flags;
  DWORD             Timeout;
  LPCWSTR           RestartDirectory;
  LPCWSTR           RestartCommand;
  LPCWSTR           RestartMinimumCommand;
  LPCWSTR           WorkloadTempDirectory;
  INT               WorkloadAssessmentIndex;
  JobExecutionError Error;
  BOOL              Restarting;
};
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The number of bytes in the structure. Used to detect different versions of structure. This must be set to sizeof([**SolutionParameters**](solutionparameters.md)) before initializing the Solution interface with this structure.

</dd> <dt>

**Job**
</dt> <dd>

A pointer to the Job object to execute. The Job object is created by [**CreateJob**](solution-createjob-ovl.md).

</dd> <dt>

**Flags**
</dt> <dd>

Specifies flags that control how the job will be executed. This value can be a combination of the flags defined in the [**JobExecutionFlags**](jobexecutionflags.md) enumeration.

</dd> <dt>

**Timeout**
</dt> <dd>

The amount of time the engine will wait for a job running within another engine to finish. If the Solution API is configured in Workload mode, this value must be 0.

</dd> <dt>

**RestartDirectory**
</dt> <dd>

The directory where the solution application exists. If an assessment in the job causes the system to reboot, the solution will be relaunched from this directory. If the Solution API is configured in Workload mode, this value must be **NULL**. Otherwise, this member must not be **NULL**.

</dd> <dt>

**RestartCommand**
</dt> <dd>

The command string to execute in the [**RestartDirectory**](axe-jobexecutioninfo_restartdirectory_om) in order to run the solution if the job causes the system to reboot. If the Solution API is configured in Workload mode, this value must be **NULL**. Otherwise, this member must not be **NULL**.

</dd> <dt>

**RestartMinimumCommand**
</dt> <dd>

The command string to execute to restart the job in  console  mode. If the Solution API is configured in Workload mode, this value must be **NULL**.

</dd> <dt>

**WorkloadTempDirectory**
</dt> <dd>

The path that workloads should use for their temporary and results files. Workloads should not produce any files because workloads are used to exercise the system under test while another assessment measures the system. All of the files written out by workloads are deleted when the workload finishes. If the Solution API is configured in Workload mode, this member must not be **NULL**. Otherwise, this member must be **NULL**.

</dd> <dt>

**WorkloadAssessmentIndex**
</dt> <dd>

The position in the job manifest of the [**AssessmentRun**](assessmentrun.md) entry for the assessment that will be running as a solution assessment that executes workloads. This index is used to locate the nested [**AssessmentRuns**](assessmentruns.md) collection that describes the workloads to run. The **WorkloadAssessmentIndex** is zero-based. This field is ignored if the Solution API is not configured in Workload mode.

</dd> <dt>

**Error**
</dt> <dd>

An out value that contains the value of the last error that occurred in processing the job, i.e. the last error in the job error list, if the job was executed synchronously. If the job was executed asynchronously, this value will be **JobExecutionErrorNone**.

</dd> <dt>

**Restarting**
</dt> <dd>

An out parameter that indicates the job has not completed yet because an assessment or workload is rebooting the system.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





