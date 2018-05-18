---
Description: 'Retrieves the maximum number of processors required by the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'baeadb9c-906d-4c0f-8993-5dcba922f11e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_MaximumNumberOfProcessors method'
---

# ITask::get\_MaximumNumberOfProcessors method

Retrieves the maximum number of processors required by the task.

## Syntax


```C++
HRESULT get_MaximumNumberOfProcessors(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The maximum number of processors.

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

[**ITask::get\_MinimumNumberOfProcessors**](itask-get-minimumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MaximumNumberOfProcessors**](itask-put-maximumnumberofprocessors.md)
</dt> </dl>

 

 




