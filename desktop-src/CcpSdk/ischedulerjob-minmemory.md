---
Description: 'Retrieves or sets the minimum amount of memory that a node must have for the job to run on it.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f285cb26-c05f-4bd1-9a4c-a0e3d11130b5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::MinMemory property'
---

# ISchedulerJob::MinMemory property

Retrieves or sets the minimum amount of memory that a node must have for the job to run on it.

This property is read/write.

## Syntax


```C++
HRESULT put_MinMemory(
  [in]  long memory
);

HRESULT get_MinMemory(
  [out] long *pMemory
);
```



## Property value

The minimum amount of memory, in megabytes, that a node must have for the job to run on it. The default value is 1 MB.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

This property is not used in the scheduling process unless set by the user.

If you set this property to 1,000, the scheduler will not schedule the job on nodes that have less than 1 GB of RAM.

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

[**ISchedulerJob.MinCoresPerNode**](ischedulerjob-mincorespernode.md)
</dt> </dl>

 

 




