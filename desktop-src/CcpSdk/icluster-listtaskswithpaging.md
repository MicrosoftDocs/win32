---
Description: 'Retrieves all tasks in the specified job. The tasks are returned in blocks of tasks from a specified snapshot of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a04fb25c-e1af-4908-958f-ec1d8ad8e3c9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ListTasksWithPaging method'
---

# ICluster::ListTasksWithPaging method

Retrieves all tasks in the specified job. The tasks are returned in blocks of tasks from a specified snapshot of the job.

## Syntax


```C++
HRESULT ListTasksWithPaging(
  [in]      long               jobId,
  [in, out] VARIANT            *Timestamp,
  [in, out] VARIANT            *Version,
  [in]      long               pageSize,
  [out]     IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*Timestamp* \[in, out\]
</dt> <dd>

The opaque value used by the method to track the tasks that have been returned. Set to **NULL** on first call. See Remarks for details.

</dd> <dt>

*Version* \[in, out\]
</dt> <dd>

The opaque value used by the method to track the snapshot of the list. Set to **NULL** on first call. See Remarks for details.

</dd> <dt>

*pageSize* \[in\]
</dt> <dd>

The number of tasks to retrieve. The minimum number of tasks to retrieve is 1, and the maximum is 10,000. If the value is outside this range, the method uses 10,000.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains the collection of tasks. To retrieve the list of [**ITask**](itask.md) interfaces, call the [**IClusterEnumerable::GetEnumerator**](iclusterenumerable-getenumerator.md) method. The variant type of each item is VT\_DISPATCH. Query the **pdispVal** member of the variant for the **ITask** interface. The enumerable object is empty when there are no tasks left to return.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

This method is meant to be called in a loop. Set the *Timestamp* and *Version* parameters to **NULL** on the first call and do not change their values on subsequent calls. The first call takes a snapshot of the list of tasks and returns the requested number of tasks. The loop ends when the enumerable object is empty.

To get the delta of the tasks that were added or whose state has changed since the last snapshot, set *Version* to **NULL**, but leave the *Timestamp* value unchanged.

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

[**ICluster::ListTasks**](icluster-listtasks.md)
</dt> <dt>

[**ICluster::ListTasksOnNode**](icluster-listtasksonnode.md)
</dt> <dt>

[**IJob::GetEnumerator**](ijob-getenumerator.md)
</dt> </dl>

 

 




