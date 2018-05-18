---
Description: 'Retrieves the number of tasks in the job that have not been submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1ca35dec-24bc-42ab-833c-67e6983b6968'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJobCounter::get\_NumberOfNotSubmittedTasks method'
---

# IJobCounter::get\_NumberOfNotSubmittedTasks method

Retrieves the number of tasks in the job that have not been submitted.

## Syntax


```C++
HRESULT get_NumberOfNotSubmittedTasks(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The number of tasks that have not been submitted (tasks with the status **TaskStatus\_NotSubmitted**).

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

 

 




