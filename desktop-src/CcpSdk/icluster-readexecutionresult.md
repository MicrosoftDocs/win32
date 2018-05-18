---
Description: 'Retrieves the output from a command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fc173cdc-ca49-4170-a87a-4b22105c2d0d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ReadExecutionResult method'
---

# ICluster::ReadExecutionResult method

Retrieves the output from a command.

## Syntax


```C++
HRESULT ReadExecutionResult(
  [in]  IExecutionResult *result,
  [out] BSTR             *pRetVal
);
```



## Parameters

<dl> <dt>

*result* \[in\]
</dt> <dd>

An [**IExecutionResult**](iexecutionresult.md) interface that contains the result of the command. The [**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md) method returns this interface.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

The standard out and standard error output from the command.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Call this method when calling the [**ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md) or [**ICluster::WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md) method.

Calling this method is the same as calling the [**IExecutionResult::get\_Output**](iexecutionresult-get-output.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> </dl>

 

 




