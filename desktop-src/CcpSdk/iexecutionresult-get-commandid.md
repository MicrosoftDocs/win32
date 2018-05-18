---
Description: 'Retrieves the identifier of the command that ran.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dc75efe4-10ad-43c5-a1b4-4f90912ba5b3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExecutionResult::get\_CommandId method'
---

# IExecutionResult::get\_CommandId method

Retrieves the identifier of the command that ran.

## Syntax


```C++
HRESULT get_CommandId(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The identifier of the command that ran.

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

[**IExecutionResult**](iexecutionresult.md)
</dt> </dl>

 

 




