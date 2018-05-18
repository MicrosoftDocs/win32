---
Description: 'Cancels the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9f140acb-37c7-478d-b53e-6907fdcf3af8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CancelJob method'
---

# ICluster::CancelJob method

Cancels the specified job.

## Syntax


```C++
HRESULT CancelJob(
  [in] long jobId,
  [in] BSTR Message
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A message that describes the reason why the job was canceled. The message is limited to 320 Unicode characters. Can be empty.

The message is stored with the job. To get the message, call the [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md) method.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The job is removed from the queue but remains in the cluster until the value of the *TTLCompletedJobs* cluster configuration parameter is exceeded. For a description of this parameter, see the [**ICluster::SetClusterParameter**](icluster-setclusterparameter.md) method.

To cancel a job, the job's status must be: not submitted, queued, or running. If the job is running tasks when the job is canceled, the tasks are terminated and marked as failed. If you [queue the job again](icluster-requeuejob.md), the tasks that were finished when the job was canceled stay finished, but all other tasks are queued (including those that failed).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::CancelJobs**](icluster-canceljobs.md)
</dt> <dt>

[**ICluster::CancelTask**](icluster-canceltask.md)
</dt> </dl>

 

 




