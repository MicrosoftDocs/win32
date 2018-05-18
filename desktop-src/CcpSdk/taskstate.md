---
Description: 'Defines the state of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '44c40002-aa81-42a6-822f-3e89868d3142'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: TaskState enumeration
---

# TaskState enumeration

Defines the state of the task.

## Syntax


```C++
typedef enum  { 
  TaskState_Configuring  = 1,
  TaskState_Submitted    = 2,
  TaskState_Validating   = 4,
  TaskState_Queued       = 8,
  TaskState_Dispatching  = 16,
  TaskState_Running      = 32,
  TaskState_Finishing    = 64,
  TaskState_Finished     = 128,
  TaskState_Failed       = 256,
  TaskState_Canceled     = 512,
  TaskState_Canceling    = 1024,
  TaskState_All          = 2047
} TaskState;
```



## Constants

<dl> <dt>

<span id="TaskState_Configuring"></span><span id="taskstate_configuring"></span><span id="TASKSTATE_CONFIGURING"></span>**TaskState\_Configuring**
</dt> <dd>

The task is being configured. The application called the [**ISchedulerJob::CreateTask**](ischedulerjob-createtask.md) method to create the task but has not called the [**ISchedulerJob::AddTask**](ischedulerjob-addtask.md) or [**ISchedulerJob::SubmitTask**](ischedulerjob-submittask.md) method to add the task to the job.

</dd> <dt>

<span id="TaskState_Submitted"></span><span id="taskstate_submitted"></span><span id="TASKSTATE_SUBMITTED"></span>**TaskState\_Submitted**
</dt> <dd>

The task was added to the scheduling queue.

</dd> <dt>

<span id="TaskState_Validating"></span><span id="taskstate_validating"></span><span id="TASKSTATE_VALIDATING"></span>**TaskState\_Validating**
</dt> <dd>

The scheduler is determining if the task is correctly configured and can run.

</dd> <dt>

<span id="TaskState_Queued"></span><span id="taskstate_queued"></span><span id="TASKSTATE_QUEUED"></span>**TaskState\_Queued**
</dt> <dd>

The task passed validation and was added to the scheduling queue.

</dd> <dt>

<span id="TaskState_Dispatching"></span><span id="taskstate_dispatching"></span><span id="TASKSTATE_DISPATCHING"></span>**TaskState\_Dispatching**
</dt> <dd>

The scheduler is in the process of sending the task to the node to run.

</dd> <dt>

<span id="TaskState_Running"></span><span id="taskstate_running"></span><span id="TASKSTATE_RUNNING"></span>**TaskState\_Running**
</dt> <dd>

The task is running.

</dd> <dt>

<span id="TaskState_Finishing"></span><span id="taskstate_finishing"></span><span id="TASKSTATE_FINISHING"></span>**TaskState\_Finishing**
</dt> <dd>

The node is cleaning up the resources that were allocated to the task.

</dd> <dt>

<span id="TaskState_Finished"></span><span id="taskstate_finished"></span><span id="TASKSTATE_FINISHED"></span>**TaskState\_Finished**
</dt> <dd>

The task successfully finished.

</dd> <dt>

<span id="TaskState_Failed"></span><span id="taskstate_failed"></span><span id="TASKSTATE_FAILED"></span>**TaskState\_Failed**
</dt> <dd>

The task failed, the job was canceled, or a system error occurred on the compute node. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

</dd> <dt>

<span id="TaskState_Canceled"></span><span id="taskstate_canceled"></span><span id="TASKSTATE_CANCELED"></span>**TaskState\_Canceled**
</dt> <dd>

The task was canceled (see [**ISchedulerJob::CancelTask**](ischedulerjob-canceltask.md)). If the caller provided the reason for canceling the task, then the [**ErrorMessage**](ischedulertask-errormessage.md) task property will contain the reason.

</dd> <dt>

<span id="TaskState_Canceling"></span><span id="taskstate_canceling"></span><span id="TASKSTATE_CANCELING"></span>**TaskState\_Canceling**
</dt> <dd>

The task is in the process of being canceled.

</dd> <dt>

<span id="TaskState_All"></span><span id="taskstate_all"></span><span id="TASKSTATE_ALL"></span>**TaskState\_All**
</dt> <dd>

A mask used to indicate all states.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerTask.State**](ischedulertask-state.md)
</dt> </dl>

 

 




