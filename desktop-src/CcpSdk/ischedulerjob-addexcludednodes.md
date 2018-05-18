---
Description: 'Adds the specified nodes to the list of nodes that should not be used for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'B192F47B-EDB5-4675-BAD1-7AC1ACC986A4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::AddExcludedNodes method'
---

# ISchedulerJob::AddExcludedNodes method

Adds the specified nodes to the list of nodes that should not be used for the job.

## Syntax


```C++
HRESULT AddExcludedNodes(
  [in] IStringCollection *NodeNames
);
```



## Parameters

<dl> <dt>

*NodeNames* \[in\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that specifies the names of the nodes that you want to add to the list of nodes on which the job should not run.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

If you add a node to the list of nodes that should not be used for the job while the job is running on that node, the tasks in the job that are running on the node are canceled and then requeued if the [**ISchedulerTask::IsRerunnable**](ischedulertask-isrerunnable.md) property for the task is VARIANT\_TRUE.

If a node is specified in the [**ISchedulerTask::RequiredNodes**](ischedulertask-requirednodes.md) property for any of the tasks in the job, an exception occurs if you also specify that node when you call the **ISchedulerJob::AddExcludedNodes** method.

If you call **ISchedulerJob::AddExcludedNodes** and specify a set of nodes that would cause the set of available resources to become smaller than the minimum number of resources that the job requires, an exception occurs. For example, if you have an HPC cluster than consists of three nodes and you include two of them in the NodeNames parameter when you call **ISchedulerJob::AddExcludedNodes**, that action makes only one node available, and an exception occurs if the job requires a minimum of two nodes.

If you specify the name of a node that does not currently belong to the HPC cluster, the method generates an exception.

If you add the same node twice to the list of nodes that should not be used for the job, the second time that you add the node has no effect.

To verify that the method succeeded, use the [**ISchedulerJob:ExcludedNodes**](ischedulerjob-excludednodes.md) property to get the full list of nodes that should not be used for the job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::ClearExcludedNodes**](ischedulerjob-clearexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md)
</dt> <dt>

[**ISchedulerJobs::ExcludedNodes**](ischedulerjob-excludednodes.md)
</dt> </dl>

 

 




