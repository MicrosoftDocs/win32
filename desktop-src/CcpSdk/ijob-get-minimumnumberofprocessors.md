---
Description: 'Retrieves the minimum number of processors that are required by the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b144d16a-494a-48da-a988-769e71a2243b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_MinimumNumberOfProcessors method'
---

# IJob::get\_MinimumNumberOfProcessors method

Retrieves the minimum number of processors that are required by the job.

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

[**IJob**](ijob.md)
</dt> <dt>

[**IJob::get\_MaximumNumberOfProcessors**](ijob-get-maximumnumberofprocessors.md)
</dt> <dt>

[**IJob::put\_MinimumNumberOfProcessors**](ijob-put-minimumnumberofprocessors.md)
</dt> </dl>

 

 




