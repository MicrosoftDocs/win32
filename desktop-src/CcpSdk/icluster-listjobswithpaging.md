---
Description: 'Retrieves all jobs in the cluster that were submitted by the specified user and that have the specified status. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '16c88dc3-dc32-4eea-ad65-f2dd08661e77'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListJobsWithPaging method'
---

# ICluster::ListJobsWithPaging method

Retrieves all jobs in the cluster that were submitted by the specified user and that have the specified status. The jobs are returned in blocks of jobs from a specified snapshot of the cluster.

## Syntax


```C++
HRESULT ListJobsWithPaging(
  [in, optional] BSTR               SubmittedBy,
  [in]           JobStatus          Status,
  [in]           VARIANT_BOOL       withTasks,
  [in, out]      VARIANT            *Timestamp,
  [in, out]      VARIANT            *Version,
  [in]           long               pageSize,
  [out]          IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*SubmittedBy* \[in, optional\]
</dt> <dd>

The name of the user, in the form *domain*\\*user*, that submitted the job. If **NULL** or "", the method retrieves all jobs with the specified status.

</dd> <dt>

*Status* \[in\]
</dt> <dd>

The job status. For a list of values, see [**JobStatus**](jobstatus.md).

</dd> <dt>

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

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of jobs. To retrieve the list of [**IJob**](ijob.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **IJob** interface. The enumerable object is empty when there are no jobs left to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If there are more than 2,000 jobs in the cluster or if your application requires quick response time, consider calling this method instead of calling the [**ICluster::ListJobs**](icluster-listjobs.md) method.

This method is meant to be called in a loop. Set the *Timestamp* and *Version* parameters to **NULL** on the first call and do not change their values on subsequent calls. The first call takes a snapshot of the list of jobs and returns the requested number of jobs. The loop ends when the enumerable object is empty.

To get the delta of the jobs that were added or whose state has changed since the last snapshot, set *Version* to **NULL**, but leave *Timestamp* unchanged.

To reset the snapshot to the beginning, set *Timestamp* to **NULL**, but leave *Version* unchanged.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ListAllJobsWithPaging**](icluster-listalljobswithpaging.md)
</dt> <dt>

[**ICluster::ListJobs**](icluster-listjobs.md)
</dt> </dl>

 

 




