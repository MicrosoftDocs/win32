---
Description: 'Retrieves or sets the maximum number of nodes that the scheduler may allocate for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '44c61b27-8ffc-4bb8-9232-6f207c045773'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MaximumNumberOfNodes property'
---

# ISchedulerTask::MaximumNumberOfNodes property

Retrieves or sets the maximum number of nodes that the scheduler may allocate for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_MaximumNumberOfNodes(
  [in]  long maxNodes
);

HRESULT get_MaximumNumberOfNodes(
  [out] long *pMaxNodes
);
```



## Property value

The maximum number of nodes. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Node.

This property tells the scheduler that the task requires at most *n* nodes to run (the scheduler will not allocate more than this number of nodes for the task).

The value cannot:

-   Exceed the value of the [**MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md) job property.
-   Be less than the value of the [**MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md)
</dt> <dt>

[**ISchedulerTask.MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md)
</dt> </dl>

 

 




