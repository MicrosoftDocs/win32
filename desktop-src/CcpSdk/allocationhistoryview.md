---
Description: 'Lists the allocations of tasks or subtasks in high-performance computing (HPC) jobs to cores on the nodes in the HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3bfa261c-a025-439a-aff0-b3206cf57b22'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: AllocationHistoryView
---

# AllocationHistoryView

Lists the allocations of tasks or subtasks in high-performance computing (HPC) jobs to cores on the nodes in the HPC cluster.



| Column name                    | Data type               | Can be **NULL** | Description                                                                                                                                                                                                                                                                                                                           |
|--------------------------------|-------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AllocationHistoryID<br/> | int<br/>          | No<br/>   | A unique numeric identifier for allocating a task or subtask in a job to a core on a node.<br/>                                                                                                                                                                                                                                 |
| JobID<br/>               | int<br/>          | No<br/>   | The identifier of the job that the HPC Job Scheduler Service allocated to a core on the node.<br/>                                                                                                                                                                                                                              |
| RequeueID<br/>           | int<br/>          | No<br/>   | A numeric identifier for queuing of the job. Each time a user requeues the job, a new RequeueID is assigned for the job. The RequeueID starts at 0 when the user submits a job for the first time, and is incremented each time the user cancels and requeues the job. <br/>                                                    |
| NodeName<br/>            | nvarchar(64)<br/> | No<br/>   | The name of the node to which the HPC Job Scheduler Service allocated the job.<br/>                                                                                                                                                                                                                                             |
| UniqueCoreID<br/>        | int<br/>          | No<br/>   | A unique identifier for the core to which the HPC Job Scheduler Service allocated the job for a regular job. The identifier is unique across all of the cores on all of the nodes in the HPC cluster. For an administrative job that runs clusrun commands, this unique identifier is not associated with a specific core.<br/> |
| StartTime<br/>           | datetime<br/>     | No<br/>   | The date and time in Coordinated Universal Time (UTC) of the start of the period for which the HPC Job Scheduler Service allocated the job to the core.<br/>                                                                                                                                                                    |
| EndTime<br/>             | datetime<br/>     | Yes<br/>  | The date and time in UTC of the end of the period for which the HPC Job Scheduler Service allocated the job to the core. A **NULL** value indicates that the job is still allocated to the resource. When the allocation ends, this value is updated.<br/>                                                                      |



 

## Remarks

A new row is added to the view after a short delay whenever the HPC Job Scheduler Service allocates a core on a node to a task in a job. For parametric tasks, the task is expanded so that a row is added whenever the HPC Job Scheduler Service allocates a core to a subtask. The EndTime value in the row is updated when the HPC Job Scheduler Service ends the allocation and takes back the core.

This view includes entries for both regular jobs and administrative jobs that run clusrun commands. The built-in reports that Windows HPC Server 2008 R2 provides, however, do not include the administrative jobs that run clusrun commands when calculating resource use.

If you want to exclude administrative jobs that run clusrun commands in the calculations for your reports, your query should exclude rows for which the job is an administrative job. You can exclude these rows by performing a JOIN operation with the [**JobHistoryView**](jobhistoryview.md) and testing in a WHERE clause that the value of the Type column for the job in the **JobHistoryView** is not equal to Admin. The following example is a query that excludes administrative jobs.

``` syntax
SELECT A.* FROM 
AllocationHistoryView A JOIN JobHistoryView J 
ON A.JobID = J.JobId AND A.RequeueID = J.RequeueId 
WHERE J.Type!='Admin'  
```

The reporting database stores information about the allocation of jobs only for the number of days that the AllocationHistoryTtl configuration parameter specifies, as long as the database has added the information to the daily totals. The information is not deleted if it the database has not added it to the daily totals. The value of the AllocationHistoryTtl parameter is usually small, and it is 5 by default.

To view the current value of the AllocationHistoryTtl configuration parameter, use the Get-HpcClusterProperty cmdlet with the Parameter and Name parameters, for example:


```PowerShell
Get-HpcClusterProperty -Parameter -Name AllocationHistoryTtl
```



To set or change the value of the AllocationHistoryTtl configuration parameter, use the Set-HpcClusterParameter cmdlet with the AllocationHistoryTtl parameters, for example:


```PowerShell
Set-HpcClusterProperty -AllocationHistoryTtl 6
```



## Requirements



|                    |                                       |
|--------------------|---------------------------------------|
| Product<br/> | Windows HPC Server 2008 R2<br/> |



## See also

<dl> <dt>

[**JobHistoryView**](jobhistoryview.md)
</dt> </dl>

 

 




