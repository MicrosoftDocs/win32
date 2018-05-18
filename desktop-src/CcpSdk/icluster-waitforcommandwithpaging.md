---
Description: 'Waits for execution of the specified command to be completed on at least one node. The output is returned in the requested page size.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd6effcd6-b546-4e20-96d6-43f50c8e442f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::WaitForCommandWithPaging method'
---

# ICluster::WaitForCommandWithPaging method

Waits for execution of the specified command to be completed on at least one node. The output is returned in the requested page size.

## Syntax


```C++
HRESULT WaitForCommandWithPaging(
  [in]  long               Id,
  [in]  long               pageSize,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The command identifier. This is the same identifier passed to the [**ICluster::ExecuteCommand**](icluster-executecommand.md) method.

</dd> <dt>

*pageSize* \[in\]
</dt> <dd>

The number of Unicode characters to return in each page of the output. The minimum size is 2,048 Unicode characters, and the maximum size is 20,480. If the value is outside this range, the method determines the page size.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of results. To retrieve the list of [**IExecutionResult**](iexecutionresult.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IExecutionResult** interface. The enumerable object is empty when there are no results left to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Call this method only if you set the [**ICluster::put\_IsAsynchronous**](icluster-put-isasynchronous.md) method to VARIANT\_TRUE and called the [**ICluster::ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md) method to execute the command.

To retrieve all results, call this method in a loop until all results are retrieved (the enumerable object is empty).

To get the output for each result, call the [**ICluster::ReadExecutionResult**](icluster-readexecutionresult.md) method in a loop until the output string is empty.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::WaitForCommand**](icluster-waitforcommand.md)
</dt> </dl>

 

 




