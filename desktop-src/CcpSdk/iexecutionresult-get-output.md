---
Description: 'Retrieves the output from the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'acaedf65-a5b6-45e3-9028-fd6dd0958ea8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExecutionResult::get\_Output method'
---

# IExecutionResult::get\_Output method

Retrieves the output from the command.

## Syntax


```C++
HRESULT get_Output(
  [out] BSTR *pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

The output string.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The string includes the output from standard out and standard error.

If you call the [**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md) or [**ICluster::WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md) method, use the [**ICluster::ReadExecutionResult**](icluster-readexecutionresult.md) method instead of this method to read the output.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExecutionResult**](iexecutionresult.md)
</dt> </dl>

 

 




