---
Description: 'Retrieves the file to which standard output has been redirected.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '79e5ee7a-b210-4090-93d0-82d74b1c0096'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::get\_Stdout method'
---

# ITask::get\_Stdout method

Retrieves the file to which standard output has been redirected.

## Syntax


```C++
HRESULT get_Stdout(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The path to the file to which standard output has been redirected.

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

[**ITask::get\_Stderr**](itask-get-stderr.md)
</dt> <dt>

[**ITask::get\_Stdin**](itask-get-stdin.md)
</dt> <dt>

[**ITask::put\_Stdout**](itask-put-stdout.md)
</dt> </dl>

 

 




