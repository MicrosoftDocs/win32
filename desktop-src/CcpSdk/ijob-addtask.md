---
Description: 'Adds the task to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '53b4ed5e-c0a3-4b1a-8df8-6d941441b523'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::AddTask method'
---

# IJob::AddTask method

Adds the task to the job.

## Syntax


```C++
HRESULT AddTask(
  [in] ITask *Task
);
```



## Parameters

<dl> <dt>

*Task* \[in\]
</dt> <dd>

An [**ITask**](itask.md) interface that represents the task that you want to add to the job. To create the task, call the [**ICluster::CreateTask**](icluster-createtask.md) method.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use this method only to add tasks to a job that has not been [added](icluster-addjob.md) to the cluster. After the job is added to the cluster, you must call the [**ICluster::AddTask**](icluster-addtask.md) method to add tasks to the job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster::AddTask**](icluster-addtask.md)
</dt> <dt>

[**ICluster::CancelTask**](icluster-canceltask.md)
</dt> <dt>

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::GetTask**](ijob-gettask.md)
</dt> </dl>

 

 




