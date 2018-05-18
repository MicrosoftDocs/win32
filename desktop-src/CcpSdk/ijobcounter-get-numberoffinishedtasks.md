---
Description: 'Retrieves the number of finished tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9f069762-4c22-41ae-8f2a-b7d851042a2d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobCounter::get\_NumberOfFinishedTasks method'
---

# IJobCounter::get\_NumberOfFinishedTasks method

Retrieves the number of finished tasks in the job.

## Syntax


```C++
HRESULT get_NumberOfFinishedTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of finished tasks (tasks with the status **TaskStatus\_Finished**).

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

 

 




