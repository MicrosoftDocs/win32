---
Description: 'Retrieves the identifier that uniquely identifies the task in a job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9b2a90d0-3cae-407d-b2f7-e70cda81266f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskStateEventArg::TaskId property'
---

# ITaskStateEventArg::TaskId property

Retrieves the identifier that uniquely identifies the task in a job.

This property is read-only.

## Syntax


```C++
HRESULT get_TaskId(
  [out] ITaskId **pTaskId
);
```



## Property value

An [**ITaskId**](itaskid.md) interface that uniquely identifies the task.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use the task identifier when calling the [**ISchedulerJob::OpenTask**](ischedulerjob-opentask.md) method to get an interface to the task.

## Examples

For an example, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITaskStateEventArg**](itaskstateeventarg.md)
</dt> </dl>

 

 




