---
Description: 'Checks whether the resources that are allocated to a job are reserved for the job even when the job has no active tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5fb76b3f-02cb-465c-ab48-a6b086120c65'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_RunUntilCanceled method'
---

# IJob::get\_RunUntilCanceled method

Checks whether the resources that are allocated to a job are reserved for the job even when the job has no active tasks.

## Syntax


```C++
HRESULT get_RunUntilCanceled(
  [out] VARIANT_BOOL *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The value is VARIANT\_TRUE if the resources that are allocated to a job are reserved for the job even when it has no active tasks; otherwise, VARIANT\_FALSE.

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

[**IJob::get\_Runtime**](ijob-get-runtime.md)
</dt> <dt>

[**IJob::put\_RunUntilCanceled**](ijob-put-rununtilcanceled.md)
</dt> </dl>

 

 




