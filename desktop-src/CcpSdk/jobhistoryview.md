---
Description: 'Lists each queued instance of a job on an HPC cluster that finished, failed, or was canceled. Includes statistics and information about the properties and results, and tasks for the jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '70370920-9a31-498f-85b9-70341d8e12dd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobHistoryView
---

# JobHistoryView

Lists each queued instance of a job on an HPC cluster that finished, failed, or was canceled. Includes statistics and information about the properties and results, and tasks for the jobs.



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Column name</th>
<th>Data type</th>
<th>Can be null</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JobHistoryID<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>A unique numeric identifier for a job history entry.<br/> A job history entry is created each time a job reaches the finished, failed, or canceled state. For example, one job would correspond to three job history entries if you submit the job and cancel it before it finishes, requeue the job and it fails, and then fix and requeue the job so that it finishes.<br/></td>
</tr>
<tr class="even">
<td>JobID<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>The job identifier of the job that was queued and then finished, failed, or was canceled.<br/></td>
</tr>
<tr class="odd">
<td>RequeueID<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>A numeric identifier for the queuing of the job. Each time a user queues the job, a new RequeueID is assigned for the job. The RequeueID starts at 0 when the user submits a job for the first time, and it is incremented each time the user cancels and requeues the job.<br/></td>
</tr>
<tr class="even">
<td>Name<br/></td>
<td>nvarchar(80)<br/></td>
<td>Yes<br/></td>
<td>The name of the job.<br/></td>
</tr>
<tr class="odd">
<td>State<br/></td>
<td>varchar(8)<br/></td>
<td>No<br/></td>
<td>The state for the job. It is one of the following values:<br/>
<ul>
<li>Finished<br/></li>
<li>Failed<br/></li>
<li>Canceled<br/></li>
</ul></td>
</tr>
<tr class="even">
<td>EventTime<br/></td>
<td>datetime<br/></td>
<td>No<br/></td>
<td>The date and time in Coordinated Universal Time (UTC) when the job finished, failed, or was canceled.<br/></td>
</tr>
<tr class="odd">
<td>SubmitTime<br/></td>
<td>datetime<br/></td>
<td>Yes<br/></td>
<td>The date and time in UTC when the job was submitted.<br/></td>
</tr>
<tr class="even">
<td>StartTime<br/></td>
<td>datetime<br/></td>
<td>Yes<br/></td>
<td>The date and time in UTC when the job started running. If the job is canceled before it starts running, the StartTime is the same as the EventTime.<br/></td>
</tr>
<tr class="odd">
<td>Owner<br/></td>
<td>nvarchar(80)<br/></td>
<td>No<br/></td>
<td>The owner of the job.<br/></td>
</tr>
<tr class="even">
<td>Project<br/></td>
<td>nvarchar(80)<br/></td>
<td>No<br/></td>
<td>The project to which the job belongs.<br/></td>
</tr>
<tr class="odd">
<td>Template<br/></td>
<td>nvarchar(50)<br/></td>
<td>No<br/></td>
<td>The name of the job template that the job uses.<br/></td>
</tr>
<tr class="even">
<td>Service<br/></td>
<td>nvarchar(128)<br/></td>
<td>No<br/></td>
<td>The name of the service-oriented architecture (SOA) service that the job uses, if the job is a service job.<br/></td>
</tr>
<tr class="odd">
<td>KernelCpuTime<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The amount of CPU time in milliseconds that the job used while running in privileged or kernel mode. The sum of KernelCpuTime and UserCpuTime is the total CPU time for the job.<br/> If the job is canceled before it starts running, the KernelCpuTime is 0.<br/></td>
</tr>
<tr class="even">
<td>UserCpuTime<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The amount of CPU time in milliseconds that the job used while running in user mode. The sum of KernelCpuTime and UserCpuTime is the total CPU time for the job.<br/> If the job is canceled before it starts running, the UserCpuTime is 0.<br/></td>
</tr>
<tr class="odd">
<td>MemoryUsed<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The amount of memory in kilobytes that the tasks in the job were using when memory usage for the tasks were most recently sampled, summed over all of the tasks the job.<br/></td>
</tr>
<tr class="even">
<td>NumberOfCalls<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The total number of SOA calls that the tasks in the job made.<br/></td>
</tr>
<tr class="odd">
<td>CallDuration<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The average duration in milliseconds of the SOA calls made by the tasks in the job.<br/></td>
</tr>
<tr class="even">
<td>CallsPerSecond<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The average number of SOA calls that the tasks in the job made per second.<br/></td>
</tr>
<tr class="odd">
<td>RunTime<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The amount of time in milliseconds that all of the tasks in the job took to run. The value of the RunTime column is the sum of the differences between the entries in the EndTime and StartTime columns in the [<strong>AllocationHistoryView</strong>](allocationhistoryview.md) for each of the tasks in the job.<br/></td>
</tr>
<tr class="even">
<td>WaitTime<br/></td>
<td>bigint<br/></td>
<td>No<br/></td>
<td>The amount of time in milliseconds that the job waited in the job queue before the job started to run or was canceled if it never started to run.<br/> The value of the WaitTime column is the difference between the values of the StartTime and the SubmitTime columns.<br/> When a job is canceled after being queued but before it starts, the value of the StartTime column is the same as the value of the EventTime column. So in this case, the value of the WaitTime column is also the difference between the values of the EventTime and the SubmitTime columns. In this case, the values of the KernelCpuTime and UserCpuTime columns are 0.<br/></td>
</tr>
<tr class="odd">
<td>Priority<br/></td>
<td>varchar(11)<br/></td>
<td>Yes<br/></td>
<td>The priority for scheduling the job. The priority can be one of the following values:<br/>
<ul>
<li>Highest<br/></li>
<li>AboveNormal<br/></li>
<li>Normal<br/></li>
<li>BelowNormal<br/></li>
<li>Lowest<br/></li>
</ul>
The job template that the job uses specifies permissions that affect who can specify elevated priorities.<br/> The HPC Job Scheduler Service places jobs with the same priority into the job queue in the order that users submit the jobs, unless a user requeues a job. When a user requeues a job, the HPC Job Scheduler Service places that job first among the jobs with the same priority.<br/></td>
</tr>
<tr class="even">
<td>Type<br/></td>
<td>varchar(7)<br/></td>
<td>Yes<br/></td>
<td>The type of the job. It can be one of the following values:<br/>
<ul>
<li>Admin<br/> An administrative job that runs a clusrun command.<br/></li>
<li>Batch<br/> A normal batch job.<br/></li>
<li>Service<br/> An SOA job.<br/></li>
</ul></td>
</tr>
<tr class="odd">
<td>Preemptable<br/></td>
<td>bit<br/></td>
<td>Yes<br/></td>
<td>Indicates whether higher priority jobs could take resources away from this job when it was running.<br/> A value of true indicates that higher priority jobs could take resources away from this job when it was running. A value of false indicates that higher priority jobs could not take resources away from this job when it was running.<br/></td>
</tr>
<tr class="even">
<td>NumberOfTasks<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>The number of tasks in the job.<br/></td>
</tr>
<tr class="odd">
<td>CanceledTasksCount<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>The number of tasks that were canceled when the job ran.<br/></td>
</tr>
<tr class="even">
<td>FailedTasksCount<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>The number of tasks that failed when the job ran.<br/></td>
</tr>
<tr class="odd">
<td>FinishedTasksCount<br/></td>
<td>int<br/></td>
<td>No<br/></td>
<td>The number of tasks that finished when the job ran.<br/></td>
</tr>
<tr class="even">
<td>License<br/></td>
<td>nvarchar(160)<br/></td>
<td>Yes<br/></td>
<td>A list of features for which the job requires licenses, and the number of licenses required for each. The list uses a format of <em>license_name1</em>:<em>number1</em> [,<em>license_name2</em>:<em>number2</em>â€¦], for example, License1:10,License2:20,License3:12.<br/></td>
</tr>
<tr class="odd">
<td>RunUntilCanceled<br/></td>
<td>bit<br/></td>
<td>Yes<br/></td>
<td>Indicates whether the job continues to run and hold resources until the run-time limit expires or someone cancels the job.<br/> A value of true indicates that the job continues to run and hold resources until the run-time limit expires or someone cancels the job. A value of false indicates that the job should stop and release its resources when all of the tasks in the job are complete.<br/></td>
</tr>
<tr class="even">
<td>IsExclusive<br/></td>
<td>bit<br/></td>
<td>Yes<br/></td>
<td>Indicates whether the HPC Job Scheduler Service should ensure that no other job runs on the same node while this job runs.<br/> A value of true indicates that the HPC Job Scheduler Service should ensure that no other job runs on the same node while this job runs. A value of false indicates that this job can share compute nodes with other jobs.<br/></td>
</tr>
<tr class="odd">
<td>FailOnTaskFailure<br/></td>
<td>bit<br/></td>
<td>Yes<br/></td>
<td>Indicates whether the HPC Job Scheduler Service should stop the job and fail the entire job immediately when a task in the job fails.<br/> A value of true indicates that the HPC Job Scheduler Service should stop the job and fail the entire job immediately when a task in the job fails. A value of false indicates that the HPC Job Scheduler Service should continue to run the remaining tasks in the job after any task in the job fails.<br/></td>
</tr>
<tr class="even">
<td>CanceledBy<br/></td>
<td>nvarchar(80)<br/></td>
<td>Yes<br/></td>
<td>The user who requested that the job be canceled.<br/></td>
</tr>
</tbody>
</table>



 

## Remarks

Jobs that are running, queued, or still being configured are not reflected in this view.

The reporting database stores job history information only for the number of days that the DataExtensibilityTtl configuration parameter specifies. This value is 365 by default.

To view the current value of the DataExtensibilityTtl configuration parameter, use the Get-HpcClusterProperty cmdlet with the Parameter and Name parameters, for example:


```PowerShell
Get-HpcClusterProperty -Parameter -Name DataExtensibilityTtl
```



To set or change the value of the DataExtensibilityTtl configuration parameter, use the Set-HpcClusterParameter cmdlet with the DataExtensibilityTtl parameter, for example:


```PowerShell
Set-HpcClusterProperty -DataExtensibilityTtl 730
```



## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[**AllocationHistoryView**](allocationhistoryview.md)
</dt> </dl>

 

 




