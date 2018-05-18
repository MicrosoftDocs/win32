---
Description: 'Retrieves or sets the minimum number of nodes that the task requires to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '434058a0-426f-4ee3-b226-d4e8280f5235'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MinimumNumberOfNodes property'
---

# ISchedulerTask::MinimumNumberOfNodes property

Retrieves or sets the minimum number of nodes that the task requires to run.

This property is read/write.

## Syntax


```C++
HRESULT put_MinimumNumberOfNodes(
  [in]  long minNodes
);

HRESULT get_MinimumNumberOfNodes(
  [out] long *pMinNodes
);
```



## Property value

The minimum number of nodes. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Node.

This property tells the scheduler that the task requires at least *n* nodes to run (the scheduler will not allocate less than this number of nodes for the task).

The value must be less than or equal to:

-   The value of the [**MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md) task property.
-   The value of the [**MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md) job property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md)
</dt> </dl>

 

 




