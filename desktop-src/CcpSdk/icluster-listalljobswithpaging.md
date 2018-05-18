---
Description: 'Retrieves all jobs in the cluster. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ed18851f-50b2-4cc8-abb5-e80b586e3afa'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListAllJobsWithPaging method'
---

# ICluster::ListAllJobsWithPaging method

Retrieves all jobs in the cluster. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.

## Syntax


```C++
HRESULT ListAllJobsWithPaging(
  [in]      VARIANT_BOOL       withTasks,
  [in, out] VARIANT            *Timestamp,
  [in, out] VARIANT            *Version,
  [in]      long               pageSize,
  [out]     IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*withTasks* \[in\]
</dt> <dd>

Specify VARIANT\_TRUE to retrieve only jobs that contain tasks; otherwise, VARIANT\_FALSE.

</dd> <dt>

*Timestamp* \[in, out\]
</dt> <dd>

The opaque value used by the method to track the jobs that have been returned. Set to **NULL** on first call. See Remarks for details.

</dd> <dt>

*Version* \[in, out\]
</dt> <dd>

The opaque value used by the method to track the snapshot of the list. Set to **NULL** on first call. See Remarks for details.

</dd> <dt>

*pageSize* \[in\]
</dt> <dd>

The number of jobs to retrieve. The minimum number of jobs to retrieve is 1, and the maximum is 10,000. If the value is outside this range, the method uses 10,000.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the list of jobs. To retrieve the list of [**IJob**](ijob.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IJob** interface. The enumerable object is empty when there are no jobs left to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If there are more than 2,000 jobs in the cluster or if your application requires quick response time, consider calling this method instead of calling the [**ICluster::ListAllJobs**](icluster-listalljobs.md) method.

This method is meant to be called in a loop. Set the *Timestamp* and *Version* parameters to **NULL** on the first call and do not change their values on subsequent calls. The first call takes a snapshot of the list of jobs and returns the requested number of jobs. The loop ends when the enumerable object is empty.

To get the delta of the jobs that were added or whose state has changed since the last snapshot, set the *Version* parameter to **NULL**, but leave the *Timestamp* parameter unchanged.

To reset the snapshot to the beginning, set the *Timestamp* parameter to **NULL**, but leave the *Version* parameter unchanged.

To determine the total number of jobs in the cluster, call the [**ICluster::get\_ClusterCounter**](icluster-get-clustercounter.md) method and then the [**IClusterCounter::get\_TotalNumberOfJobs**](iclustercounter-get-totalnumberofjobs.md) method.

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
</dt> </dl>

 

 




