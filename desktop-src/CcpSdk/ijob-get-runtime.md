---
Description: 'Retrieves the run-time limit for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '32d8ab76-3383-417d-878c-9beb8a5ac9da'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_Runtime method'
---

# IJob::get\_Runtime method

Retrieves the run-time limit for the job.

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

The run-time limit. The value is either "Infinite" or a string in the format *dd*:*hh*:*mm*.

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

[**IJob::get\_RunUntilCanceled**](ijob-get-rununtilcanceled.md)
</dt> <dt>

[**IJob::put\_Runtime**](ijob-put-runtime.md)
</dt> </dl>

 

 




