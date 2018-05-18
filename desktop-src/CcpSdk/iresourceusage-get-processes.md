---
Description: 'Retrieves the list of processes being used by the job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b4a0f310-b93b-4c3b-b1a8-c330313137bb'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IResourceUsage::get\_Processes method'
---

# IResourceUsage::get\_Processes method

Retrieves the list of processes being used by the job or task.

## Syntax


```C++
HRESULT get_Processes(
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains a collection of strings that identify the processes being used by the job or task. To enumerate the list of processes, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type is VT\_BSTR. The **bstrVal** member of the variant contains the process identifiers.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The string contains the name of the node on which the process is running, the process identifier for the cmd.exe executable, and the process identifier for the task that is running. For example, "nodeA, 8464 4288".

Use this method only when the status of the job or task is Running.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IResourceUsage**](iresourceusage.md)
</dt> </dl>

 

 




