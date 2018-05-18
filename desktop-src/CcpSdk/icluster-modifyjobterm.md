---
Description: 'Modifies the specified job term.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '35d2d0f6-8238-4e5b-9b3c-ae5e842be4a9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ModifyJobTerm method'
---

# ICluster::ModifyJobTerm method

Modifies the specified job term.

## Syntax


```C++
HRESULT ModifyJobTerm(
  [in] long jobId,
  [in] BSTR termName,
  [in] BSTR termValue
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*termName* \[in\]
</dt> <dd>

The name of the job term. The name is case sensitive. For a list of possible terms, see Remarks.

</dd> <dt>

*termValue* \[in\]
</dt> <dd>

The value of the job term.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

The following is the list of job terms that you can modify.



| Job term                  | Description                                                                                                                                                                       |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AskedNodes                | A comma-delimited list of nodes that your job requires. The node must exist in the cluster.                                                                                       |
| IsExclusive               | Indicates whether nodes are exclusively allocated to a job. The default is True.                                                                                                  |
| Name                      | The display name for the job.                                                                                                                                                     |
| SoftwareLicense           | The required license features. The format is *string*:*integer*{,*string*:*integer*}.                                                                                             |
| MaximumNumberOfProcessors | The maximum number of processors to be reserved for the job. The default is 1.                                                                                                    |
| MinimumNumberOfProcessors | The minimum number of processors to be reserved for the job. The default is 1.                                                                                                    |
| Priority                  | The priority of the job relative to other jobs in the queue. Possible values are: "Highest", "AboveNormal", "Normal", "BelowNormal", and "Lowest". The default value is "Normal". |
| Project                   | The project name that is associated with the job for accounting purposes.                                                                                                         |
| RunUntilCanceled          | Indicates whether the resources allocated to a job are reserved until the job is canceled (even if the job has no active tasks). The default is False.                            |
| Runtime                   | The run-time limit for the job. Can be "Infinite" or a string in the format *dd*:*hh*:*mm*.                                                                                       |



 

If you specify a term that is not in the list, the method searches for a matching [extended term](ijob-setextendedjobterm.md). If the extended term is found, its value is updated; otherwise, the job term is added to the list of extended terms for the job. The names of extended terms are case insensitive.

If the job is running, you can modify only the [**Runtime**](ijob-put-runtime.md), [**RunUntilCanceled**](ijob-put-rununtilcanceled.md), and [**Project**](ijob-put-project.md) terms. The changes take effect immediately. If the job is a [backfill](ijob-get-isbackfill.md) job, you cannot modify the **Runtime** property.

This method updates the job on the cluster. If you have an instance of the job object at the time you called this method, the instance will not reflect the update. You will need to retrieve a new instance of the job object to see the change.

To modify all the properties of a job, call the [**ICluster::ModifyJob**](icluster-modifyjob.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ModifyJob**](icluster-modifyjob.md)
</dt> </dl>

 

 




