---
Description: 'Determines whether cores, nodes, or sockets are used to allocate resources for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3eea7a99-e119-4c7a-bbbe-6de1266cac91'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::UnitType property'
---

# ISchedulerJob::UnitType property

Determines whether cores, nodes, or sockets are used to allocate resources for the job.

This property is read/write.

## Syntax


```C++
HRESULT put_UnitType(
  [in]  JobUnitType type
);

HRESULT get_UnitType(
  [out] JobUnitType *pType
);
```



## Property value

The unit type. For possible values, see the [**JobUnitType**](jobunittype.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The Default job template sets the default value to JobUnitType\_Core.

The resource units that you specify should be based on the threading model that the service uses. Specify Core if the service is linked to non-thread safe libraries. Specify Node if the service is multithreaded. Specify Socket if the service is single-threaded and memory-bus intensive.

If the unit type is JobUnitType\_Core, use the [**ISchedulerJob::MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md) and [**ISchedulerJob::MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md) properties to specify the required hardware for the job.

If the unit type is JobUnitType\_Socket, use the [**ISchedulerJob::MaximumNumberOfSockets**](ischedulerjob-maximumnumberofsockets.md) and [**ISchedulerJob::MinimumNumberOfSockets**](ischedulerjob-minimumnumberofsockets.md) properties to specify the required hardware for the job.

If the unit type is JobUnitType\_Node, use the [**ISchedulerJob::MaximumNumberOfNodes**](ischedulerjob-maximumnumberofnodes.md) and [**ISchedulerJob::MinimumNumberOfNodes**](ischedulerjob-minimumnumberofnodes.md) properties to specify the required hardware for the job.

The maximum and minimum values are used unless the [**ISchedulerJob::AutoCalculateMax**](ischedulerjob-autocalculatemax.md) and [**ISchedulerJob::AutoCalculateMin**](ischedulerjob-autocalculatemin.md) properties are set to VARIANT\_TRUE, respectively.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




