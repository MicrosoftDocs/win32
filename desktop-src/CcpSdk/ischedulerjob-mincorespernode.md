---
Description: 'Retrieves or sets the minimum number of cores that a node must have for the job to run on it.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fce24ce8-8b2b-4a48-bebd-25db83bca517'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MinCoresPerNode property'
---

# ISchedulerJob::MinCoresPerNode property

Retrieves or sets the minimum number of cores that a node must have for the job to run on it.

This property is read/write.

## Syntax


```C++
HRESULT put_MinCoresPerNode(
  [in]  long maxCores
);

HRESULT get_MinCoresPerNode(
  [out] long *pMaxCores
);
```



## Property value

The minimum number of cores. The default value is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

This property is not used in the scheduling process unless set by the user.

If you set this property to 2, the scheduler will not schedule the job on nodes that have less than two cores.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.MaxCoresPerNode**](ischedulerjob-maxcorespernode.md)
</dt> <dt>

[**ISchedulerJob.MinimumNumberOfCores**](ischedulerjob-minimumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MinMemory**](ischedulerjob-minmemory.md)
</dt> </dl>

 

 




