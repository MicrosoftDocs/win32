---
Description: 'Retrieves or sets the estimate of the maximum amount of memory the job will consume.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F5810513-75A1-41F6-A060-18A4E24EA551'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::EstimatedProcessMemory property'
---

# ISchedulerJob::EstimatedProcessMemory property

Retrieves or sets the estimate of the maximum amount of memory the job will consume.

This property is read/write.

## Syntax


```C++
HRESULT put_EstimatedProcessMemory(
  [in]  long value
);

HRESULT get_EstimatedProcessMemory(
  [out] long *pValue
);
```



## Property value

The estimated number of megabytes of memory the job will require.

## Error codes

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

The **EstimatedProcessMemory** property is used by the job scheduler to assign jobs to nodes with sufficient memory to execute the job.

## Requirements



|                         |                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Server 2008 R2 with Service Pack 1 (SP1) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                                     |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




