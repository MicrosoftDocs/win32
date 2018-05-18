---
Description: 'Retrieves the task end time.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1310b505-5b51-4578-adf3-2ad037b3a140'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_EndTime method'
---

# ITask::get\_EndTime method

Retrieves the task end time.

## Syntax


```C++
HRESULT get_EndTime(
  [out] DATE *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The time that the task ended.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The end time indicates when the task finished, failed, or was canceled. The value is MaxValue if the task has not finished, failed, or been canceled. The time is reset if you requeue a failed or canceled task.

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

[**ITask::get\_StartTime**](itask-get-starttime.md)
</dt> </dl>

 

 




