---
Description: 'Retrieves all tasks in the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b9971f79-23ac-42f7-831e-c7fba709a78e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListTasks method'
---

# ICluster::ListTasks method

Retrieves all tasks in the specified job.

## Syntax


```C++
HRESULT ListTasks(
  [in]  long               jobId,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The identifier of the job whose tasks you want to retrieve. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of tasks. To retrieve the list of [**ITask**](itask.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **ITask** interface. The enumerable object is empty when there are no tasks to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ListTasksOnNode**](icluster-listtasksonnode.md)
</dt> <dt>

[**ICluster::ListTasksWithPaging**](icluster-listtaskswithpaging.md)
</dt> <dt>

[**IJob::GetEnumerator**](ijob-getenumerator.md)
</dt> </dl>

 

 




