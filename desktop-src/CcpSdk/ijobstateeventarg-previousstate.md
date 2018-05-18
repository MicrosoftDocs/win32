---
Description: 'Retrieves the previous state of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9c9ea299-adb8-44f4-bd72-3d5873d743ba'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobStateEventArg::PreviousState property'
---

# IJobStateEventArg::PreviousState property

Retrieves the previous state of the job.

This property is read-only.

## Syntax


```C++
HRESULT get_PreviousState(
  [out] JobState *pPreviousState
);
```



## Property value

The previous state of the job. For possible values, see the [**JobState**](jobstate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJobStateEventArg**](ijobstateeventarg.md)
</dt> </dl>

 

 




