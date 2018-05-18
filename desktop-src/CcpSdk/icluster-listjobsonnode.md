---
Description: 'Retrieves all jobs that are running on the specified node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7027c607-6b3d-4e7c-8d3d-4c61530b8e08'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListJobsOnNode method'
---

# ICluster::ListJobsOnNode method

Retrieves all jobs that are running on the specified node.

## Syntax


```C++
HRESULT ListJobsOnNode(
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

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of jobs. To retrieve the list of [**IJob**](ijob.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IJob** interface. The enumerable object is empty when there are no jobs to return.

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

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> </dl>

 

 




