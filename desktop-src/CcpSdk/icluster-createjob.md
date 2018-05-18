---
Description: 'Creates a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd8bf20e6-d232-44c7-b2a0-85f146eceeb3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateJob method'
---

# ICluster::CreateJob method

Creates a job.

## Syntax


```C++
HRESULT CreateJob(
  [out] IJob **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IJob**](ijob.md) interface that represents the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The initial state of the job is **JobStatus\_NotSubmitted**. After creating the job, call the [**ICluster::AddJob**](icluster-addjob.md) method to add the job to the cluster. You can then call the [**ICluster::AddTask**](icluster-addtask.md) or [**ICluster::AddTasks**](icluster-addtasks.md) method to add one or more tasks to the job. When the job is ready (you have added all the tasks and set all the job terms), call the [**ICluster::SubmitJob**](icluster-submitjob.md) method to add the job to the scheduling queue.

To add and submit the job in one step, call the [**ICluster::QueueJob**](icluster-queuejob.md) method. Before calling the **QueueJob** method, call the [**IJob::AddTask**](ijob-addtask.md) method to add tasks to the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::CreateJobFromXml**](icluster-createjobfromxml.md)
</dt> <dt>

[**ICluster::CreateTask**](icluster-createtask.md)
</dt> </dl>

 

 




