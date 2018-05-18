---
Description: 'Retrieves the number of queued tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ced162fe-286b-4870-bb28-4e84afbf63e4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobCounter::get\_NumberOfQueuedTasks method'
---

# IJobCounter::get\_NumberOfQueuedTasks method

Retrieves the number of queued tasks in the job.

## Syntax


```C++
HRESULT get_NumberOfQueuedTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of queued tasks (tasks with the status **TaskStatus\_Queued**).

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

 

 




