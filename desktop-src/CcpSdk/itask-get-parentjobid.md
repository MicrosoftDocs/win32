---
Description: 'Retrieves the identifier of the parent job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2fedeb5b-9430-4ccd-8e7f-d4cdc8585c31'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_ParentJobId method'
---

# ITask::get\_ParentJobId method

Retrieves the identifier of the parent job.

## Syntax


```C++
HRESULT get_ParentJobId(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The identifier of the parent job.

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

[**IJob::get\_Id**](ijob-get-id.md)
</dt> <dt>

[**ITask**](itask.md)
</dt> </dl>

 

 




