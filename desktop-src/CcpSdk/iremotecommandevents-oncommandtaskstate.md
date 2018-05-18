---
Description: 'Is called when the state of the command changes on a node in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0107ee7c-5b15-490b-961e-94a81634f598'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommandEvents::OnCommandTaskState method'
---

# IRemoteCommandEvents::OnCommandTaskState method

Is called when the state of the command changes on a node in the cluster.

## Syntax


```C++
void OnCommandTaskState(
  [in] VARIANT                   Sender,
  [in] ICommandTaskStateEventArg *pArgs
);
```



## Parameters

<dl> <dt>

*Sender* \[in\]
</dt> <dd>

A variant that contains the Scheduler object.

</dd> <dt>

*pArgs* \[in\]
</dt> <dd>

An [**ICommandTaskStateEventArg**](icommandtaskstateeventarg.md) interface that provides information related to the state of the command.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To get the job that contains the command, query the **pdispVal** member of *Sender* for the [**IScheduler**](ischeduler.md) interface. Then, query the **pdispVal** member of *pArgs* for the [**ITaskStateEventArg**](itaskstateeventarg.md) interface. Use the [**ITaskStateEventArg.JobId**](itaskstateeventarg-jobid.md) property to call the [**IScheduler::OpenJob**](ischeduler-openjob.md) method to get the job. You can then use the [**ITaskStateEventArg::TaskId**](itaskstateeventarg-taskid.md) property to call the [**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md) method to get the task that contains the command.

The dispatch identifier for this method is 0x60020002.

## Examples

For an example, see Implementing the [Event Handlers for Command Events in C++](implementing-the-event-handlers-for-command-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IRemoteCommandEvents**](iremotecommandevents.md)
</dt> <dt>

[**IRemoteCommandEvents::OnCommandJobState**](iremotecommandevents-oncommandjobstate.md)
</dt> </dl>

 

 




