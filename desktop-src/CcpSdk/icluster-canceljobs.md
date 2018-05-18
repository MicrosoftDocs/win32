---
Description: 'Cancels one or more specified jobs.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e63bd844-de6a-48e8-99ec-30ca20e68d8b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CancelJobs method'
---

# ICluster::CancelJobs method

Cancels one or more specified jobs.

## Syntax


```C++
HRESULT CancelJobs(
  [in] IClusterEnumerable *jobIds,
  [in] BSTR               Message
);
```



## Parameters

<dl> <dt>

*jobIds* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains one or more job identifiers of the jobs to cancel. The [**ICluster::AddJob**](icluster-addjob.md) method returns the job identifier. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*Message* \[in\]
</dt> <dd>

A message that describes the reason why the jobs were canceled. The message is limited to 320 Unicode characters. This parameter can be **NULL**.

The message is stored with each canceled job. To get the message, call the [**IJob::get\_ErrorMessage**](ijob-get-errormessage.md) method.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If you need to cancel multiple jobs, calling this method provides better performance than calling the [**ICluster::CancelJob**](icluster-canceljob.md) method in a loop.

To create the enumerable object, call the [**ICluster::CreateClusterEnumerable**](icluster-createclusterenumerable.md) method. Then, call the [**IClusterEnumerable::Add**](iclusterenumerable-add.md) method to add job identifiers to the enumerable object. Set the **lVal** member of the variant to the job identifier. Set the variant type of the item to VT\_I4.

The jobs are removed from the queue but remain in the cluster until the value of the *TTLCompletedJobs* cluster configuration parameter is exceeded. For a description of this parameter, see the [**ICluster::SetClusterParameter**](icluster-setclusterparameter.md) method.

To cancel a job, the job's status must be: not submitted, queued, or running. If a job is running tasks when the job is canceled, the tasks are terminated and marked as failed. If you [queue the job again](icluster-requeuejob.md), the tasks that were finished when the job was canceled stay finished, but all other tasks are queued (including those that failed).

If this method fails, only those jobs canceled before the failure are canceled.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJobs**](icluster-addjobs.md)
</dt> <dt>

[**ICluster::CancelJob**](icluster-canceljob.md)
</dt> <dt>

[**ICluster::CancelTasks**](icluster-canceltasks.md)
</dt> </dl>

 

 




