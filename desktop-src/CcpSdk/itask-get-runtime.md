---
Description: 'Retrieves the run-time limit for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '885f750a-d555-4e31-91de-ddb16e52a0bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_Runtime method'
---

# ITask::get\_Runtime method

Retrieves the run-time limit for the task.

## Syntax


```C++
HRESULT get_Runtime(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The run-time limit for the task. The value can be "Infinite" or a string in the format *dd*:*hh*:*mm*.

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

[**ITask::put\_Runtime**](itask-put-runtime.md)
</dt> </dl>

 

 




