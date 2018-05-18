---
Description: 'Defines how to run the command for a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4FFE00F9-39C5-4439-B2F0-EBD6D299AEB5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: TaskType enumeration
---

# TaskType enumeration

Defines how to run the command for a task.

## Syntax


```C++
typedef enum  { 
  TaskType_Basic            = 0,
  TaskType_ParametricSweep  = 1,
  TaskType_NodePrep         = 2,
  TaskType_NodeRelease      = 3,
  TaskType_Service          = 4
} TaskType;
```



## Constants

<dl> <dt>

<span id="TaskType_Basic"></span><span id="tasktype_basic"></span><span id="TASKTYPE_BASIC"></span>**TaskType\_Basic**
</dt> <dd>

Runs a single instance of a serial application or a Message Passing Interface (MPI) application. An MPI application typically runs concurrently on multiple cores, and it can span multiple nodes. This task type is the default.

</dd> <dt>

<span id="TaskType_ParametricSweep"></span><span id="tasktype_parametricsweep"></span><span id="TASKTYPE_PARAMETRICSWEEP"></span>**TaskType\_ParametricSweep**
</dt> <dd>

Runs a command a specified number of times as indicated by the start, end, and increment values, generally across indexed input and output files. The steps of the sweep may or may not run in parallel, depending on the resources that are available on the HPC cluster when the task is running.

</dd> <dt>

<span id="TaskType_NodePrep"></span><span id="tasktype_nodeprep"></span><span id="TASKTYPE_NODEPREP"></span>**TaskType\_NodePrep**
</dt> <dd>

Runs a command or script on each compute node as it is allocated to the job. The Node Prep task runs on a node before any other task in the job. If the Node Prep task fails to run on a node, then that node is not added to the job.

</dd> <dt>

<span id="TaskType_NodeRelease"></span><span id="tasktype_noderelease"></span><span id="TASKTYPE_NODERELEASE"></span>**TaskType\_NodeRelease**
</dt> <dd>

Runs a command or script on each compute node as it is released from the job. Node Release tasks run when the job is canceled by the user or by graceful preemption. Node Release tasks do not run when the job is canceled by immediate preemption.

</dd> <dt>

<span id="TaskType_Service"></span><span id="tasktype_service"></span><span id="TASKTYPE_SERVICE"></span>**TaskType\_Service**
</dt> <dd>

Runs a command or service on all resources that are assigned to the job. New instances of the command start when new resources are added to the job, or if a previously running instance exits and the resource that the previously running instance was running on is still allocated to the job. A service task continues to start new instances until the task is canceled, the maximum run time expires, or the maximum number of instances is reached. A service task can create up to 1,000,000 subtasks. Tasks that you submit through a service-oriented architecture (SOA) client run as Service tasks. You cannot add a Basic task or a Parametric Sweep task to a job that contains a Service task.

</dd> </dl>

## Remarks

The following properties do not apply to tasks that you start on a per-resource basis, and thus you cannot set these properties if you set the [**ISchedulerTask::Type**](ischedulertask-type.md) property to **NodePrep**, **NodeRelease**, or **Service**:

-   [**MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md)

-   [**MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md)

-   [**MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md)

-   [**MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md)

-   [**MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md)

-   [**MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md)

-   [**RequiredNodes**](ischedulertask-requirednodes.md)

-   [**IsExclusive**](ischedulertask-isexclusive.md)

-   [**IsRerunnable**](ischedulertask-isrerunnable.md)

-   [**DependsOn**](ischedulertask-dependson.md)

-   [**EndValue**](ischedulertask-endvalue.md)

-   [**IncrementValue**](ischedulertask-incrementvalue.md)

-   [**IsParametric**](ischedulertask-isparametric.md)

-   [**StartValue**](ischedulertask-startvalue.md)

You cannot add a Basic task or a Parametric Sweep task to a job that contains a Service task.

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask::Type**](ischedulertask-type.md)
</dt> </dl>

 

 




