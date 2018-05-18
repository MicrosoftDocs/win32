---
Description: 'Adds one or more specified tasks to the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '98d55eb2-4b02-4380-8840-72a1fe9bf1f7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::AddTasks method'
---

# ICluster::AddTasks method

Adds one or more specified tasks to the specified job.

## Syntax


```C++
HRESULT AddTasks(
  [in]  long               jobId,
  [in]  IClusterEnumerable *tasks,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*tasks* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains one or more tasks that you want to add to the job. The variant type of each item that you add to the enumerable object is VT\_DISPATCH. Set the **pdispVal** member of the variant to the task's **IDispatch** interface. To get the **IDispatch** interface, call the **QueryInterface** method of [**ITask**](itask.md).

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the identifiers of the tasks that were added to the job. The identifiers in this collection correspond directly to the tasks passed in the *tasks* parameter. When you enumerate the identifiers in this collection, the identifiers are returned as variants. The variant type is VT\_I4. Use the **lVal** member of the variant to access the identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If you need to add multiple tasks to a job, calling this method provides better performance than calling the [**ICluster::AddTask**](icluster-addtask.md) method in a loop.

If this method fails to add one of the tasks to the job, none of the tasks are added to the job. The likely reason for failing to add a task to a job is if resource usage or run-time requirements of the task conflict with job.

A task cannot be modified after it is added to a job.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddTask**](icluster-addtask.md)
</dt> <dt>

[**ICluster::CancelTasks**](icluster-canceltask.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**IJob::AddTask**](ijob-addtask.md)
</dt> </dl>

 

 




