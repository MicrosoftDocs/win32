---
Description: 'Sets the value that indicates if the resources allocated to a job are reserved until the job is canceled.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5cb8391d-1476-41d4-9e6d-c016bf7a433b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::put\_RunUntilCanceled method'
---

# IJob::put\_RunUntilCanceled method

Sets the value that indicates if the resources allocated to a job are reserved until the job is canceled (even if the job has no active tasks).

## Syntax


```C++
HRESULT put_RunUntilCanceled(
  [in] VARIANT_BOOL pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[in\]
</dt> <dd>

Set the value to **VARIANT\_TRUE** if the resources that are allocated to a job are reserved for the job even when the job has no active tasks; otherwise, **VARIANT\_FALSE**. The default is **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code.

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
</dt> </dl>

 

 




