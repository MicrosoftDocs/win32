---
Description: 'Retrieves all jobs in the cluster that were submitted by the specified owner and that have the specified status.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2a6b7b68-a216-4c93-97c6-075f68eddcfd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListJobs method'
---

# ICluster::ListJobs method

Retrieves all jobs in the cluster that were submitted by the specified owner and that have the specified status.

## Syntax


```C++
HRESULT ListJobs(
  [in]  BSTR               SubmittedBy,
  [in]  JobStatus          Status,
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*SubmittedBy* \[in\]
</dt> <dd>

The name of the user, in the form *domain*\\*user*, that submitted the job. If **NULL**, the method retrieves all jobs with the specified status.

</dd> <dt>

*Status* \[in\]
</dt> <dd>

The job status. For a list of values, see [**JobStatus**](jobstatus.md).

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of jobs. To retrieve the list of [**IJob**](ijob.md) interfaces, use the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IJob** interface. The enumerable object is empty when there are no jobs to return.

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

[**ICluster::ListAllJobs**](icluster-listalljobs.md)
</dt> <dt>

[**ICluster::ListJobsWithPaging**](icluster-listjobswithpaging.md)
</dt> <dt>

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> </dl>

 

 




