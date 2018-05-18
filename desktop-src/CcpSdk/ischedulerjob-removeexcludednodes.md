---
Description: 'Removes the specified nodes from the list of nodes that should not be used for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'DE04BE57-DAA6-4CA9-BEBE-05BF61C2A5B6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RemoveExcludedNodes method'
---

# ISchedulerJob::RemoveExcludedNodes method

Removes the specified nodes from the list of nodes that should not be used for the job.

## Syntax


```C++
HRESULT RemoveExcludedNodes(
  [in] IStringCollection *NodeNames
);
```



## Parameters

<dl> <dt>

*NodeNames* \[in\]
</dt> <dd>

An [**IStringCollection**](istringcollection.md) interface that specifies the names of the nodes that you want to remove from the list of nodes on which the job should not run.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

To remove all of the nodes on the list of nodes that should not be used for the job from that list, use the [**ISchedulerJob::ClearExcludedNodes**](ischedulerjob-clearexcludednodes.md) method.

If you specify a node that does not currently belong to the HPC cluster, an exception occurs. If you specify a node that is part of the HPC cluster but is not part of the current list of nodes that should not be used for the job, the **ISchedulerJob::RemoveExcludedNodes** method has no effect and no error occurs.

To verify that the method succeeded, check the value of the [**ISchedulerJob:ExcludedNodes**](ischedulerjob-excludednodes.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::AddExcludedNodes**](ischedulerjob-addexcludednodes.md)
</dt> <dt>

[**ISchedulerJob::ClearExcludedNodes**](ischedulerjob-clearexcludednodes.md)
</dt> <dt>

[**ISchedulerJob:ExcludedNodes**](ischedulerjob-excludednodes.md)
</dt> </dl>

 

 




