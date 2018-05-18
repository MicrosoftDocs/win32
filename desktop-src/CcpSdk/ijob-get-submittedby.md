---
Description: 'Retrieves the name of the user who added, submitted, or queued the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7b6b24f8-e4bd-4155-b1fa-deebca74a04a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IJob::get\_SubmittedBy method'
---

# IJob::get\_SubmittedBy method

Retrieves the name of the user who added, submitted, or queued the job.

## Syntax


```C++
HRESULT get_SubmittedBy(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The user name.

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

[**IJob::put\_User**](ijob-put-user.md)
</dt> </dl>

 

 




