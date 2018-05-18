---
Description: 'Retrieves the number of tasks being canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '91fd8a3f-6897-4ded-83b7-9c8d93148298'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::CancelingTaskCount property'
---

# ISchedulerJobCounters::CancelingTaskCount property

Retrieves the number of tasks being canceled.

This property is read-only.

## Syntax


```C++
HRESULT get_CancelingTaskCount(
  [out] long *pCancelingTaskCount
);
```



## Property value

The number of tasks being canceled.

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

 

 




