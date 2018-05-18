---
Description: 'Retrieves the number of failed tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '061b4d84-1028-408e-8a77-fff1d3911f6f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobCounter::get\_NumberOfFailedTasks method'
---

# IJobCounter::get\_NumberOfFailedTasks method

Retrieves the number of failed tasks in the job.

## Syntax


```C++
HRESULT get_NumberOfFailedTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of failed tasks (tasks with the status **TaskStatus\_Failed**).

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IJobCounter**](ijobcounter.md)
</dt> </dl>

 

 




