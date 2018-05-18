---
Description: 'Adds the specified task to the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b8f5254a-7da2-480b-8a4d-901dd2e779c5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::AddTask method'
---

# ICluster::AddTask method

Adds the specified task to the specified job.

## Syntax


```C++
HRESULT AddTask(
  [in]  long  jobId,
  [in]  ITask *Task,
  [out] long  *pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*Task* \[in\]
</dt> <dd>

An [**ITask**](itask.md) interface to the task that you want to add to the job. To create a task, call the [**ICluster::CreateTask**](icluster-createtask.md), [**ICluster::CreateTaskFromXml**](icluster-createtaskfromxml.md), or [**ICluster::CreateTaskFromXmlFile**](icluster-createtaskfromxmlfile.md) method.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

The task identifier. The identifier is unique within the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The number of tasks that you can add to a job is limited by the size of an integer.

The task cannot be modified after it is added to the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddTasks**](icluster-addtasks.md)
</dt> <dt>

[**ICluster::CancelTask**](icluster-canceltask.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**IJob::AddTask**](ijob-addtask.md)
</dt> </dl>

 

 




