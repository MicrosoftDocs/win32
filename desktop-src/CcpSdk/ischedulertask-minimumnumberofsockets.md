---
Description: 'Retrieves or sets the minimum number of sockets that the task requires to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '58ac11c6-8843-45c7-984f-78c4e7c62ab2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MinimumNumberOfSockets property'
---

# ISchedulerTask::MinimumNumberOfSockets property

Retrieves or sets the minimum number of sockets that the task requires to run.

This property is read/write.

## Syntax


```C++
HRESULT put_MinimumNumberOfSockets(
  [in]  long minSockets
);

HRESULT get_MinimumNumberOfSockets(
  [out] long *pMinSockets
);
```



## Property value

The minimum number of sockets. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Socket.

This property tells the scheduler that the task requires at least *n* sockets to run (the scheduler will not allocate less than this number of sockets for the task).

The value must be less than or equal to:

-   The value of the [**MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md) task property.
-   The value of the [**MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md) job property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.MaximumNumberOfSockets**](ischedulertask-maximumnumberofsockets.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfNodes**](ischedulertask-minimumnumberofnodes.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfCores**](ischedulertask-minimumnumberofcores.md)
</dt> </dl>

 

 




