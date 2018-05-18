---
Description: 'Is called each time the command on a node generates output or an error occurs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0032b7ac-8094-4460-a872-e1ce10bf7e61'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IRemoteCommandEvents::OnCommandRawOutput method'
---

# IRemoteCommandEvents::OnCommandRawOutput method

Is called each time the command on a node generates output or an error occurs.

## Syntax


```C++
void OnCommandRawOutput(
  [in] VARIANT                   Sender,
  [in] ICommandRawOutputEventArg *pArgs
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

An [**ICommandRawOutputEventArg**](icommandrawoutputeventarg.md) interface that contains the output as a byte blob.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To get the job that contains the command, query the **pdispVal** member of *Sender* for the [**IScheduler**](ischeduler.md) interface. Then, query the **pdispVal** member of *pArgs* for the [**ITaskStateEventArg**](itaskstateeventarg.md) interface. Use the [**ITaskStateEventArg.JobId**](itaskstateeventarg-jobid.md) property to call the [**IScheduler::OpenJob**](ischeduler-openjob.md) method to get the job. You can then use the [**ITaskStateEventArg::TaskId**](itaskstateeventarg-taskid.md) property to call the [**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md) method to get the task that contains the command.

The dispatch identifier for this method is 0x60020001.

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

[**IRemoteCommandEvents::OnCommandOutput**](iremotecommandevents-oncommandoutput.md)
</dt> </dl>

 

 




