---
Description: 'Retrieves the task creation time.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5d256f0d-5f5f-42b4-9806-6c94317be8dd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_CreateTime method'
---

# ITask::get\_CreateTime method

Retrieves the task creation time.

## Syntax


```C++
HRESULT get_CreateTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The task creation time.

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

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_EndTime**](itask-get-endtime.md)
</dt> <dt>

[**ITask::get\_StartTime**](itask-get-starttime.md)
</dt> </dl>

 

 




