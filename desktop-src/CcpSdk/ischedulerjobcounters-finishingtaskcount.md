---
Description: 'Gets the number of tasks in the job for which the node is cleaning up the resources that were allocated to the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16D0B98B-B629-40EC-893F-8D2A8C8BD754'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::FinishingTaskCount property'
---

# ISchedulerJobCounters::FinishingTaskCount property

Gets the number of tasks in the job for which the node is cleaning up the resources that were allocated to the task.

This property is read-only.

## Syntax


```C++
HRESULT get_FinishingTaskCount(
  [out, retval] long *pRetVal
);
```



## Property value

The number of tasks in the job for which the node is cleaning up the resources that were allocated to the task.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




