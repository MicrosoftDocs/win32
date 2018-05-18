---
Description: 'Retrieves the state of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '90a79ecb-2b52-47eb-98f1-dca0a869e514'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskStateEventArg::NewState property'
---

# ITaskStateEventArg::NewState property

Retrieves the state of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_NewState(
  [out] TaskState *pState
);
```



## Property value

The state of the task. For possible values, see the [**TaskState**](taskstate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

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
</dt> <dt>

[**ITaskStateEventArg.PreviousState**](itaskstateeventarg-previousstate.md)
</dt> </dl>

 

 




