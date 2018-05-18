---
Description: 'Retrieves or sets the maximum number of sockets that the scheduler may allocate for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2fbb7395-3e7a-45f7-ae1d-64340b9bae06'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::MaximumNumberOfSockets property'
---

# ISchedulerTask::MaximumNumberOfSockets property

Retrieves or sets the maximum number of sockets that the scheduler may allocate for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_MaximumNumberOfSockets(
  [in]  long maxSockets
);

HRESULT get_MaximumNumberOfSockets(
  [out] long *pMaxSockets
);
```



## Property value

The maximum number of sockets. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

Set this property if the [**UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Socket.

This property tells the scheduler that the task requires at most *n* sockets to run (the scheduler will not allocate more than this number of sockets for the task).

The value cannot:

-   Exceed the value of the [**MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md) job property.
-   Be less than the value of the [**MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md) task property.

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

[**ISchedulerTask.MaximumNumberOfNodes**](ischedulertask-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerTask.MinimumNumberOfSockets**](ischedulertask-minimumnumberofsockets.md)
</dt> </dl>

 

 




