---
Description: 'Retrieves or sets the minimum number of cores that the task requires to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dbf5c829-0b97-4e83-b573-a779bfb029b3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MinimumNumberOfCores property'
---

# ISchedulerTask::MinimumNumberOfCores property

Retrieves or sets the minimum number of cores that the task requires to run.

This property is read/write.

## Syntax


```C++
HRESULT put_MinimumNumberOfCores(
  [in]  long minCores
);

HRESULT get_MinimumNumberOfCores(
  [out] long *pMinCores
);
```



## Property value

The minimum number of cores. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Core.

This property tells the scheduler that the task requires at least *n* cores to run (the scheduler will not allocate less than this number of cores for the task).

The value must be less than or equal to:

-   The value of the [**MaximumNumberOfCores**](ischedulertask-maximumnumberofcores.md) task property.
-   The value of the [**MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md) job property.

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

[**ISchedulerTask.MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md)
</dt> </dl>

 

 




