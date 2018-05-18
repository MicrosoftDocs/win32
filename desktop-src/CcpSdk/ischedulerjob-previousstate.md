---
Description: 'Retrieves the previous state of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e86cf879-9c92-4b1c-8cac-402b61578928'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::PreviousState property'
---

# ISchedulerJob::PreviousState property

Retrieves the previous state of the job.

This property is read-only.

## Syntax


```C++
HRESULT get_PreviousState(
  [out] JobState *pPreviousState
);
```



## Property value

The previous state of the job. For possible values, see the [**JobState**](jobstate.md) enumeration.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.State**](ischedulerjob-state.md)
</dt> </dl>

 

 




