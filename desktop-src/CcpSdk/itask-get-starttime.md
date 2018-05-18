---
Description: 'Retrieves the time that the task started running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2d0c237f-c0ba-47fc-ac32-2b43cf03e74e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_StartTime method'
---

# ITask::get\_StartTime method

Retrieves the time that the task started running.

## Syntax


```C++
HRESULT get_StartTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time that the task started running.

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

[**ITask::get\_CreateTime**](itask-get-createtime.md)
</dt> <dt>

[**ITask::get\_EndTime**](itask-get-endtime.md)
</dt> </dl>

 

 




