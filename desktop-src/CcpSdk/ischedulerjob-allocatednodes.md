---
Description: 'Retrieves the names of the nodes that have been allocated to run the tasks in the job or have run the tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '17041a3c-28bb-42c1-93ca-57e49a356985'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::AllocatedNodes property'
---

# ISchedulerJob::AllocatedNodes property

Retrieves the names of the nodes that have been allocated to run the tasks in the job or have run the tasks.

This property is read-only.

## Syntax


```C++
HRESULT get_AllocatedNodes(
  [out] IStringCollection **pNodeNames
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains the names of the nodes that have been allocated to run the tasks or have run the tasks.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The list of allocated nodes are available after the job transitions to the Running state.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.RequestedNodes**](ischedulerjob-requestednodes.md)
</dt> <dt>

[**ISchedulerTask.AllocatedNodes**](ischedulertask-allocatednodes.md)
</dt> <dt>

[**ISchedulerTask.RequiredNodes**](ischedulertask-requirednodes.md)
</dt> </dl>

 

 




