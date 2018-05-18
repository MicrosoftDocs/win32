---
Description: 'Retrieves the number of tasks that have not been submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a70031e9-0049-4949-9597-42f6795fe868'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IClusterCounter::get\_NumberOfNotSubmittedTasks method'
---

# IClusterCounter::get\_NumberOfNotSubmittedTasks method

Retrieves the number of tasks that have not been submitted.

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

The number of tasks whose parent job has not been submitted to the scheduling queue (tasks with the status **TaskStatus\_NotSubmitted**).

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

[**IClusterCounter**](iclustercounter.md)
</dt> </dl>

 

 




