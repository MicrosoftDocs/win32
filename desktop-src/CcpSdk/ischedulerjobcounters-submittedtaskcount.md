---
Description: 'Retrieves the number of tasks that have been submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6f24e6c9-5826-486b-b1e1-77d312d684ec'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::SubmittedTaskCount property'
---

# ISchedulerJobCounters::SubmittedTaskCount property

Retrieves the number of tasks that have been submitted.

This property is read-only.

## Syntax


```C++
HRESULT get_SubmittedTaskCount(
  [out] long *pSubmittedTaskCount
);
```



## Property value

The number of tasks that have been submitted.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJobCounters**](ischedulerjobcounters.md)
</dt> </dl>

 

 




