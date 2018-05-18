---
Description: 'Retrieves a list of all tasks running on the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c1fb0fbb-3f20-4971-a8d4-2e9e59588984'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListTasksOnNode method'
---

# ICluster::ListTasksOnNode method

Retrieves a list of all tasks running on the node.

## Syntax


```C++
HRESULT ListTasksOnNode(
  [in]  BSTR               NodeName,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*NodeName* \[in\]
</dt> <dd>

The name of the node.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of tasks. To retrieve the list of [**ITask**](itask.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **ITask** interface. The enumerable object is empty when there are no tasks to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The list contains tasks associated with jobs, not those associated with commands.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> </dl>

 

 




