---
Description: 'Retrieves the file to which standard error has been redirected.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b325300c-a5b2-419d-87db-eef96527830a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_Stderr method'
---

# ITask::get\_Stderr method

Retrieves the file to which standard error has been redirected.

## Syntax


```C++
HRESULT get_Stderr(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The path to the file to which standard error has been redirected.

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

[**ITask::get\_Stdin**](itask-get-stdin.md)
</dt> <dt>

[**ITask::get\_Stdout**](itask-get-stdout.md)
</dt> <dt>

[**ITask::put\_Stderr**](itask-put-stderr.md)
</dt> </dl>

 

 




