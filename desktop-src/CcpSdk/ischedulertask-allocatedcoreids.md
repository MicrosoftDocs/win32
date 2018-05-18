---
Description: 'Retrieves the identifiers of the processor cores that have been allocated to run the task or that have run the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8E7C7476-9690-4833-857D-90B9215827B1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::AllocatedCoreIds property'
---

# ISchedulerTask::AllocatedCoreIds property

Retrieves the identifiers of the processor cores that have been allocated to run the task or that have run the task.

This property is read-only.

## Syntax


```C++
HRESULT get_AllocatedCoreIds(
  [out] BSTR *pRetVal
);
```



## Property value

Pointer to a **BSTR** that indicates the cores that have been allocated to run the task or that have run the task. The format of the string is *node1\_namecore1\_identifier* \[*node2\_namecore2\_identifier* ...\].

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask::AllocatedNodes**](ischedulertask-allocatednodes.md)
</dt> </dl>

 

 




