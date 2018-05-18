---
Description: 'Retrieves the number of tasks that are being configured.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0b4d64c0-a2b1-4d86-a412-2287e8611fae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::ConfiguringTasks property'
---

# ISchedulerCounters::ConfiguringTasks property

Retrieves the number of tasks that are being configured.

This property is read-only.

## Syntax


```C++
HRESULT get_ConfiguringTasks(
  [out] long *pConfiguringTasks
);
```



## Property value

The number of tasks that are being configured.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> </dl>

 

 




