---
Description: 'Gets the list of nodes that should not be used for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ED0D430F-3A26-4E43-8B4E-B5D77B8D4867'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ExcludedNodes property'
---

# ISchedulerJob::ExcludedNodes property

Gets the list of nodes that should not be used for the job.

This property is read-only.

## Syntax


```C++
HRESULT get_ExcludedNodes(
  [out, retval] IStringCollection **pRetVal
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains the names of the nodes on which the job should not run.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

You cannot add nodes to or remove nodes from the set of nodes that should not be used for the job by adding node names to or removing node names from the [**IStringCollection**](istringcollection.md) that the **ISchedulerJob::ExcludedNodes** property contains. To add nodes to the set, use the [**ISchedulerJob::AddExcludedNodes**](ischedulerjob-addexcludednodes.md) method. To remove individual nodes from the set, use the [**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md) method. To remove all of the nodes from the set, use the [**ISchedulerJob::ClearExcludedNodes**](ischedulerjob-clearexcludednodes.md) method.

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

[**ISchedulerJob::RemoveExcludedNodes**](ischedulerjob-removeexcludednodes.md)
</dt> </dl>

 

 




