---
Description: 'Retrieves the identifier of the job that contains the task whose state has changed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '98cc5921-0ec4-4013-b193-2e9822f3a20b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskStateEventArg::JobId property'
---

# ITaskStateEventArg::JobId property

Retrieves the identifier of the job that contains the task whose state has changed.

This property is read-only.

## Syntax


```C++
HRESULT get_JobId(
  [out] long *pJobId
);
```



## Property value

The job identifier.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Use the job identifier when calling the [**IScheduler::OpenJob**](ischeduler-openjob.md) method to get an interface to the job.

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

 

 




