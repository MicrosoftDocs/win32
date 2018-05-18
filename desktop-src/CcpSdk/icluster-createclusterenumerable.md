---
Description: 'Creates an enumerable object.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a37a4778-997e-48fd-a464-6d01c99429c3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::CreateClusterEnumerable method'
---

# ICluster::CreateClusterEnumerable method

Creates an enumerable object.

## Syntax


```C++
HRESULT CreateClusterEnumerable(
  [out] IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that you use to add objects to the enumeration.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Examples

For an example that creates and adds items to the enumerable object, see [Submitting a Job to the Scheduling Queue](submitting-a-job-to-the-scheduling-queue.md).

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

[**ICluster::AddTasks**](icluster-addtasks.md)
</dt> <dt>

[**ICluster::CancelJobs**](icluster-canceljobs.md)
</dt> <dt>

[**ICluster::CancelTasks**](icluster-canceltasks.md)
</dt> <dt>

[**ICluster::QueueJobs**](icluster-queuejobs.md)
</dt> <dt>

[**ICluster::RequeueJobs**](icluster-requeuejobs.md)
</dt> <dt>

[**ICluster::RequeueTasks**](icluster-requeuetasks.md)
</dt> <dt>

[**ICluster::SubmitJobs**](icluster-submitjobs.md)
</dt> </dl>

 

 




