---
Description: 'Retrieves the previous state of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '06b26ea6-32ea-416f-825b-ced8c4d2f00b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITaskStateEventArg::PreviousState property'
---

# ITaskStateEventArg::PreviousState property

Retrieves the previous state of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_PreviousState(
  [out] TaskState *pPreviousState
);
```



## Property value

The previous state of the task. For possible values, see the [**TaskState**](taskstate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITaskStateEventArg**](itaskstateeventarg.md)
</dt> <dt>

[**ITaskStateEventArg.NewState**](itaskstateeventarg-newstate.md)
</dt> </dl>

 

 




