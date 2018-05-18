---
Description: 'Retrieves the maximum number of processors that are required by the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1401affd-6de2-430e-892e-b604801f3cd5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_MaximumNumberOfProcessors method'
---

# IJob::get\_MaximumNumberOfProcessors method

Retrieves the maximum number of processors that are required by the job.

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

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_MinimumNumberOfProcessors**](ijob-get-minimumnumberofprocessors.md)
</dt> <dt>

[**IJob::put\_MaximumNumberOfProcessors**](ijob-put-maximumnumberofprocessors.md)
</dt> </dl>

 

 




