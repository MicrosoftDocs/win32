---
Description: 'Retrieves the exit code of the command that ran.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a266eef9-5ce3-43bc-9d76-34f1498fee06'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExecutionResult::get\_ExitCode method'
---

# IExecutionResult::get\_ExitCode method

Retrieves the exit code of the command that ran.

## Syntax


```C++
HRESULT get_ExitCode(
  [out] long *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The exit code of the command.

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

 

 




