---
Description: 'Cancels the specified task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f351039b-d464-4a07-bd73-9b3fd940fd15'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CancelTask method'
---

# ICluster::CancelTask method

Cancels the specified task.

## Syntax


```C++
HRESULT CancelTask(
  [in] long jobId,
  [in] long taskId,
  [in] BSTR Message
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*taskId* \[in\]
</dt> <dd>

The task identifier. The [**ITask::get\_Id**](itask-get-id.md) method returns this value.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A message that describes the reason why the task was canceled. The message is limited to 320 Unicode characters.

The message is stored with the task. To get the message, call the [**ITask::get\_ErrorMessage**](itask-get-errormessage.md) method. This parameter can be **NULL**.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

To cancel a task, the task's status must be: not submitted, queued, or running. If a task is running when it is canceled, the task is terminated and the status of the task changes to **TaskStatus\_Cancelled**. To determine a task's status, call the [**ITask::get\_Status**](itask-get-status.md) method.

You can call the [**ICluster::RequeueTask**](icluster-requeuetask.md) method to queue the task again.

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

[**ICluster::CancelTasks**](icluster-canceltasks.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**TaskStatus**](taskstatus.md)
</dt> </dl>

 

 




