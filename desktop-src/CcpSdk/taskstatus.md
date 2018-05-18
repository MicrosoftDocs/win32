---
Description: 'Defines the task status constants.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3b450789-70e5-4070-9301-e683528e2595'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: TaskStatus enumeration
---

# TaskStatus enumeration

Defines the task status constants.

## Syntax


```C++
typedef enum  { 
  TaskStatus_NotSubmitted  = 0,
  TaskStatus_Queued        = 1,
  TaskStatus_Running       = 2,
  TaskStatus_Finished      = 3,
  TaskStatus_Failed        = 4,
  TaskStatus_Cancelled     = 5
} TaskStatus;
```



## Constants

<dl> <dt>

<span id="TaskStatus_NotSubmitted"></span><span id="taskstatus_notsubmitted"></span><span id="TASKSTATUS_NOTSUBMITTED"></span>**TaskStatus\_NotSubmitted**
</dt> <dd>

The parent job was added to the cluster but not to the scheduling queue.

</dd> <dt>

<span id="TaskStatus_Queued"></span><span id="taskstatus_queued"></span><span id="TASKSTATUS_QUEUED"></span>**TaskStatus\_Queued**
</dt> <dd>

The parent job was added to the scheduling queue.

</dd> <dt>

<span id="TaskStatus_Running"></span><span id="taskstatus_running"></span><span id="TASKSTATUS_RUNNING"></span>**TaskStatus\_Running**
</dt> <dd>

The task is running.

</dd> <dt>

<span id="TaskStatus_Finished"></span><span id="taskstatus_finished"></span><span id="TASKSTATUS_FINISHED"></span>**TaskStatus\_Finished**
</dt> <dd>

The task successfully finished.

</dd> <dt>

<span id="TaskStatus_Failed"></span><span id="taskstatus_failed"></span><span id="TASKSTATUS_FAILED"></span>**TaskStatus\_Failed**
</dt> <dd>

The task failed due to an application error or a system error that occurred on the compute node. To get a description of the error, call the [**ITask::get\_ErrorMessage**](itask-get-errormessage.md) method.

</dd> <dt>

<span id="TaskStatus_Cancelled"></span><span id="taskstatus_cancelled"></span><span id="TASKSTATUS_CANCELLED"></span>**TaskStatus\_Cancelled**
</dt> <dd>

The task was canceled by the application. The application called the [**ICluster::CancelTask**](icluster-canceltask.md) or [**ICluster::CancelTasks**](icluster-canceltasks.md) method to cancel the task. If the caller provided the reason for canceling the job, then the [**ITask::get\_ErrorMessage**](itask-get-errormessage.md) method will contain that reason.

</dd> </dl>

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Enumerations](enumeration-types.md)
</dt> <dt>

[**ITask::get\_Status**](itask-get-status.md)
</dt> </dl>

 

 




