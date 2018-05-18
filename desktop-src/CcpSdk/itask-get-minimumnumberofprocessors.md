---
Description: 'Retrieves the minimum number of processors required by the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ff298b47-2a30-40db-b3dc-2e55d5cacae0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_MinimumNumberOfProcessors method'
---

# ITask::get\_MinimumNumberOfProcessors method

Retrieves the minimum number of processors required by the task.

## Syntax


```C++
HRESULT get_MinimumNumberOfProcessors(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The minimum number of processors.

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

[**ITask::get\_MaximumNumberOfProcessors**](itask-get-maximumnumberofprocessors.md)
</dt> <dt>

[**ITask::put\_MinimumNumberOfProcessors**](itask-put-minimumnumberofprocessors.md)
</dt> </dl>

 

 




