---
Description: 'Is called when the job that contains the command changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6eac5695-a102-4c20-98d5-9dc3b564195f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommandEvents::OnCommandJobState method'
---

# IRemoteCommandEvents::OnCommandJobState method

Is called when the job that contains the command changes.

## Syntax


```C++
void OnCommandJobState(
  [in] VARIANT           Sender,
  [in] IJobStateEventArg *pArgs
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

An [**IJobStateEventArg**](ijobstateeventarg.md) interface that provides information related to the state of the command.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To get the job that contains the command, query the **pdispVal** member of *Sender* for the [**IScheduler**](ischeduler.md) interface. Then, use the [**IJobStateEventArg.JobId**](ijobstateeventarg-jobid.md) property to call the [**IScheduler::OpenJob**](ischeduler-openjob.md) method to get the job. The first task in the job is the task that contains the command.

The dispatch identifier for this method is 0x60020003.

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

[**IRemoteCommandEvents::OnCommandTaskState**](iremotecommandevents-oncommandtaskstate.md)
</dt> </dl>

 

 




