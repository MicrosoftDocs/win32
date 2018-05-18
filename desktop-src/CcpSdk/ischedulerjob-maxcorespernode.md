---
Description: 'Retrieves or sets the maximum number of cores that a node can have for the job to run on it.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bedb3070-552f-496a-a217-0f94e55c1e17'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MaxCoresPerNode property'
---

# ISchedulerJob::MaxCoresPerNode property

Retrieves or sets the maximum number of cores that a node can have for the job to run on it.

This property is read/write.

## Syntax


```C++
HRESULT put_MaxCoresPerNode(
  [in]  long maxCores
);

HRESULT get_MaxCoresPerNode(
  [out] long *pMaxCores
);
```



## Property value

The maximum number of cores. The default value is INT\_MAX.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

This property is not used in the scheduling process unless set by the user.

If you set this property to 2, the scheduler will not schedule the job on nodes that have more than two cores.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.MaxMemory**](ischedulerjob-maxmemory.md)
</dt> <dt>

[**ISchedulerJob.MaximumNumberOfCores**](ischedulerjob-maximumnumberofcores.md)
</dt> <dt>

[**ISchedulerJob.MinCoresPerNode**](ischedulerjob-mincorespernode.md)
</dt> </dl>

 

 




