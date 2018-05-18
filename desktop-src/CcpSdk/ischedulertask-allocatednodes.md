---
Description: 'Retrieves the names of the nodes that have been allocated to run the task or have run the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2e509106-af56-4148-8dbf-fa1f4af2e186'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::AllocatedNodes property'
---

# ISchedulerTask::AllocatedNodes property

Retrieves the names of the nodes that have been allocated to run the task or have run the task.

This property is read-only.

## Syntax


```C++
HRESULT get_AllocatedNodes(
  [out] IStringCollection **pNodeNames
);
```



## Property value

An [**IStringCollection**](istringcollection.md) interface that contains the names of the nodes that have been allocated to run the task or have run the task.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob.AllocatedNodes**](ischedulerjob-allocatednodes.md)
</dt> <dt>

[**ISchedulerJob.NodeGroups**](ischedulerjob-nodegroup.md)
</dt> <dt>

[**ISchedulerJob.RequestedNodes**](ischedulerjob-requestednodes.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.RequiredNodes**](ischedulertask-requirednodes.md)
</dt> </dl>

 

 




