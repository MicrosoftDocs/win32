---
Description: 'Checks for tasks in the job that have finished, failed, or been canceled and returns the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2957a594-cf0d-4633-9900-e1081401561b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CheckAnyTask method'
---

# ICluster::CheckAnyTask method

Checks for tasks in the job that have finished, failed, or been canceled and returns the task.

## Syntax


```C++
HRESULT CheckAnyTask(
  [in]      long    jobId,
  [in, out] VARIANT *Timestamp,
  [out]     ITask   **pRetVal
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

An opaque value used by the method to determine the tasks that have finished, failed, or been canceled since the last call. Set this value to **NULL** on the first call and then do not change the value on subsequent calls.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**ITask**](itask.md) interface that represents the task that finished, failed, or was canceled. Is **NULL** otherwise.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

This method is meant to be called in a loop for the number of tasks in a job. To determine the number of tasks in a job, call the [**IJob::get\_TaskCount**](ijob-get-taskcount.md) method. The loop should sleep between iterations. The order that the tasks are returned is arbitrary.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**IJobCounter**](ijobcounter.md)
</dt> <dt>

[**ITask::get\_Status**](itask-get-status.md)
</dt> </dl>

 

 




