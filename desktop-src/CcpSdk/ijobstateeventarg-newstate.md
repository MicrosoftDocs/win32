---
Description: 'Retrieves the state of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5123f673-3fa9-420b-bc60-43a6d816a809'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobStateEventArg::NewState property'
---

# IJobStateEventArg::NewState property

Retrieves the state of the job.

This property is read-only.

## Syntax


```C++
HRESULT get_NewState(
  [out] JobState *pState
);
```



## Property value

The state of the job. For possible values, see the [**JobState**](jobstate.md) enumeration.

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

[**IJobStateEventArg**](ijobstateeventarg.md)
</dt> </dl>

 

 




