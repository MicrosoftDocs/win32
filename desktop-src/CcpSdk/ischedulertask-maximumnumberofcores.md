---
Description: 'Retrieves or sets the maximum number of cores that the scheduler may allocate for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c1a3ca4a-a997-4244-a4f9-c4cac2e5855d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MaximumNumberOfCores property'
---

# ISchedulerTask::MaximumNumberOfCores property

Retrieves or sets the maximum number of cores that the scheduler may allocate for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_MaximumNumberOfCores(
  [in]  long maxCores
);

HRESULT get_MaximumNumberOfCores(
  [out] long *pMaxCores
);
```



## Property value

The maximum number of cores. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Core.

This property tells the scheduler that the task requires at most *n* cores to run (the scheduler will not allocate more than this number of cores for the task).

The value cannot:

-   Exceed the value of the [**MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md) job property.
-   Be less than the value of the [**MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md) task property.

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

[**ISchedulerTask.MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md)
</dt> </dl>

 

 




