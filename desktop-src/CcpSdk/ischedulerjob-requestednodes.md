---
Description: 'Retrieves or sets the list of nodes that are requested for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ea5b6083-3960-4e24-bf78-1b4abc52ed18'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::RequestedNodes property'
---

# ISchedulerJob::RequestedNodes property

Retrieves or sets the list of nodes that are requested for the job.

This property is read/write.

## Syntax


```C++
HRESULT get_RequestedNodes(
  [out] IStringCollection **pRequestedNodes
);
```



## Property value

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

This is the list of nodes on which your job is capable of running. For example, the nodes contain the required software for your job.

If you also specify node group names in the [**ISchedulerJob::NodeGroups**](ischedulerjob-nodegroup.md) property, the job can be run on the intersection of the two lists.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.AllocatedNodes**](ischedulerjob-allocatednodes.md)
</dt> <dt>

[**ISchedulerTask.RequiredNodes**](ischedulertask-requirednodes.md)
</dt> </dl>

 

 




