---
Description: 'Retrieves or sets the maximum amount of memory that a node may have for the job to run on it.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fe5632d6-39a9-4b2e-8a25-9f68dc1f716a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MaxMemory property'
---

# ISchedulerJob::MaxMemory property

Retrieves or sets the maximum amount of memory that a node may have for the job to run on it.

This property is read/write.

## Syntax


```C++
HRESULT put_MaxMemory(
  [in]  long memory
);

HRESULT get_MaxMemory(
  [out] long *pMemory
);
```



## Property value

The maximum amount of memory, in megabytes, that a node may have for the job to run on it. The default value is INT\_MAX.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

This property is not used in the scheduling process unless set by the user.

If you set this property to 1,000, the scheduler will not schedule the job on nodes that have more than 1 GB of RAM.

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

[**ISchedulerJob.MinMemory**](ischedulerjob-minmemory.md)
</dt> </dl>

 

 




