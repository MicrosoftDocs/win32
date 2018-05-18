---
Description: 'Retrieves the name of the node on which the command ran.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '51756fb2-2cde-44e8-9c5f-c6d1032fd0ae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExecutionResult::get\_NodeName method'
---

# IExecutionResult::get\_NodeName method

Retrieves the name of the node on which the command ran.

## Syntax


```C++
HRESULT get_NodeName(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The name of the node.

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

 

 




