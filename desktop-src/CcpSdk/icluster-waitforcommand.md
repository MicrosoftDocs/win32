---
Description: 'Waits for execution of the command to be completed on at least one node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cefc3e5e-deee-444f-a343-15ac8d6b433c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::WaitForCommand method'
---

# ICluster::WaitForCommand method

Waits for execution of the command to be completed on at least one node.

## Syntax


```C++
HRESULT WaitForCommand(
  [in]  long               Id,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The command identifier. This is the same identifier passed to the [**ICluster::ExecuteCommand**](icluster-executecommand.md) method.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of results. To retrieve the list of [**IExecutionResult**](iexecutionresult.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IExecutionResult** interface. The enumerable object is empty when there are no results left to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Call this method only if you set the [**ICluster::put\_IsAsynchronous**](icluster-put-isasynchronous.md) method to VARIANT\_TRUE and called [**ExecuteCommand**](icluster-executecommand.md) to execute the command.

To retrieve all results, call this method in a loop until all results are retrieved (the enumerable object is empty).

To get the output for each result, call the [**IExecutionResult::get\_Output**](iexecutionresult-get-output.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::WaitForCommandWithPaging**](icluster-waitforcommandwithpaging.md)
</dt> </dl>

 

 




