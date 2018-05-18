---
Description: 'Retrieves a value that determines whether other tasks from the job can run on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5b4ea726-4f65-4793-a809-6000ce1d4eed'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_IsExclusive method'
---

# ITask::get\_IsExclusive method

Retrieves a value that determines whether other tasks from the job can run on the node.

## Syntax


```C++
HRESULT get_IsExclusive(
  [out] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if other tasks from the same job cannot run on the node; otherwise, VARIANT\_FALSE.

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

[**ITask::put\_IsExclusive**](itask-put-isexclusive.md)
</dt> </dl>

 

 




