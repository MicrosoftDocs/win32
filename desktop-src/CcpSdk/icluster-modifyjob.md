---
Description: 'Modifies the specified job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e1b940c4-cecf-4d39-964d-fc6e2ff00a51'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ModifyJob method'
---

# ICluster::ModifyJob method

Modifies the specified job.

## Syntax


```C++
HRESULT ModifyJob(
  [in] long jobId,
  [in] IJob *Job
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*Job* \[in\]
</dt> <dd>

An [**IJob**](ijob.md) interface that contains the new properties of the job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

This method overwrites all the properties of the job specified in the *jobId* parameter with all the properties of the job specified in the *Job* parameter (the method does not update the tasks of the job, only its properties).

If the job is running, you must use the [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) method to modify the job.

To modify single property values, call the [**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::ModifyJobTerm**](icluster-modifyjobterm.md)
</dt> </dl>

 

 




