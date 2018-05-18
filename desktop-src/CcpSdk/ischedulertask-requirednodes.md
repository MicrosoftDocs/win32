---
Description: 'Retrieves or sets the list of required nodes for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '54857456-703a-46b6-bf19-073548f4ced6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::RequiredNodes property'
---

# ISchedulerTask::RequiredNodes property

Retrieves or sets the list of required nodes for the task.

This property is read/write.

## Syntax


```C++
HRESULT get_RequiredNodes(
  [out] IStringCollection **pNodes
);
```



## Property value

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The list specifies the nodes on which the task can run. The list of required nodes must be a subset of the nodes in the [**RequestedNodes**](ischedulerjob-requestednodes.md) job property, if set.

You cannot specify required nodes if the [**ISchedulerJob.AutoCalculateMax**](ischedulerjob-autocalculatemax.md) and [**ISchedulerJob.AutoCalculateMin**](ischedulerjob-autocalculatemin.md) properties are set to VARIANT\_TRUE.

The number of nodes in the required nodes list cannot exceed the maximum resource usage specified for the job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob.RequestedNodes**](ischedulerjob-requestednodes.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.AllocatedNodes**](ischedulertask-allocatednodes.md)
</dt> </dl>

 

 




