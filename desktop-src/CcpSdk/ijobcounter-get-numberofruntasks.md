---
Description: 'Retrieves the number of running tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '920506fc-4c2d-4177-9304-806bcf3a995d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobCounter::get\_NumberOfRunningTasks method'
---

# IJobCounter::get\_NumberOfRunningTasks method

Retrieves the number of running tasks in the job.

## Syntax


```C++
HRESULT get_NumberOfRunningTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of running tasks (tasks with the status **TaskStatus\_Running**).

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

 

 




