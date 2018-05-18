---
Description: 'Cancels one or more specified tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd4ad679a-a0cb-4605-9f88-e94ef9e9e679'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CancelTasks method'
---

# ICluster::CancelTasks method

Cancels one or more specified tasks.

## Syntax


```C++
HRESULT CancelTasks(
  [in] long               jobId,
  [in] IClusterEnumerable *taskIds,
  [in] BSTR               Message
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*taskIds* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains one or more task identifiers of the tasks to cancel. The [**ITask::get\_Id**](itask-get-id.md) method returns the task identifier value.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A message that describes the reason why the tasks were canceled. The message is limited to 320 Unicode characters.

The message is stored with each canceled task. To get the message, call the [**ITask::get\_ErrorMessage**](itask-get-errormessage.md) method. This parameter can be **NULL**.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If you need to cancel multiple tasks, calling this method provides better performance than calling [**ICluster::CancelTask**](icluster-canceltask.md) in a loop.

To create the enumerable object, call the [**ICluster::CreateClusterEnumerable**](icluster-createclusterenumerable.md) method. Then, call the [**IClusterEnumerable::Add**](iclusterenumerable-add.md) method to add task identifiers to the enumerable object. Set the **lVal** member of the variant to the task identifier. Set the variant type of the item to VT\_I4.

To cancel a task, the task's status must be: not submitted, queued, or running. If a task is running when it is canceled, the task is terminated and the status of the task changes to **TaskStatus\_Cancelled**. To determine a task's status, call the [**ITask::get\_Status**](itask-get-status.md) method.

You can call the [**ICluster::RequeueTask**](icluster-requeuetask.md) method to queue the task again.

If the method fails, only those tasks canceled before the failure are canceled.

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

[**TaskStatus**](taskstatus.md)
</dt> </dl>

 

 




