---
Description: 'Retrieves or sets the maximum number of sockets that the scheduler may allocate for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2da345e2-b319-4db8-bc24-6008619c9a20'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MaximumNumberOfSockets property'
---

# ISchedulerJob::MaximumNumberOfSockets property

Retrieves or sets the maximum number of sockets that the scheduler may allocate for the job.

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

The maximum number of sockets.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

Set this property if the [**ISchedulerJob::UnitType**](ischedulerjob-unittype.md) job property is JobUnitType\_Socket.

If you set this property, you must set the [**ISchedulerJob::AutoCalculateMax**](ischedulerjob-autocalculatemax.md) property to VARIANT\_FALSE; otherwise, the maximum number of sockets that you specified will be ignored.

The Default job template sets the default value to 1.

This property tells the scheduler that the job requires at most *n* sockets to run (the scheduler will not allocate more than this number of sockets for the job).

The job can run when its minimum resource requirements are met. The scheduler may allocate up to the maximum specified resource limit for the job. The scheduler will allocate more resources to the job or release resources if the [**ISchedulerJob::CanGrow**](ischedulerjob-cangrow.md) or [**ISchedulerJob::CanShrink**](ischedulerjob-canshrink.md) properties are set to VARIANT\_TRUE; otherwise, the job uses the initial allocation for its lifetime.

The property value cannot:

-   Exceed the number of sockets in the cluster or the number of sockets on the nodes that you requested (with the [**ISchedulerJob::RequestedNodes**](ischedulerjob-requestednodes.md) property).
-   Be less than the value of the [**ISchedulerJob::MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md)
</dt> </dl>

 

 




