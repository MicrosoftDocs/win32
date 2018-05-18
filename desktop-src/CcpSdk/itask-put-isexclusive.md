---
Description: 'Sets a value that determines whether other tasks from the job can run on the node at the same time as this task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '72737c55-c4c7-4493-b764-d946b41af091'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_IsExclusive method'
---

# ITask::put\_IsExclusive method

Sets a value that determines whether other tasks from the job can run on the node at the same time as this task.

## Syntax


```C++
HRESULT put_IsExclusive(
  [in] VARIANT_BOOL Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

Set the value to VARIANT\_TRUE to prevent other tasks from the same job from running on the node; otherwise, VARIANT\_FALSE. The default is VARIANT\_FALSE.

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

[**ITask::get\_IsExclusive**](itask-get-isexclusive.md)
</dt> <dt>

[**IJob::put\_IsExclusive**](ijob-put-isexclusive.md)
</dt> </dl>

 

 




