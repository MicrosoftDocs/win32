---
Description: 'Retrieves the number of tasks being configured.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '80ddeca4-349a-4095-8447-4903e8e4af6c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJobCounters::ConfiguringTaskCount property'
---

# ISchedulerJobCounters::ConfiguringTaskCount property

Retrieves the number of tasks being configured.

This property is read-only.

## Syntax


```C++
HRESULT get_ConfiguringTaskCount(
  [out] long *pConfiguringTaskCount
);
```



## Property value

The number of tasks being configured.

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

 

 




