---
Description: 'Determines whether the job fails when one of the tasks in the job fails.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9ab17b0d-9127-4688-9317-ebd7d2d1841b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::FailOnTaskFailure property'
---

# ISchedulerJob::FailOnTaskFailure property

Determines whether the job fails when one of the tasks in the job fails.

This property is read/write.

## Syntax


```C++
HRESULT put_FailOnTaskFailure(
  [in]  VARIANT_BOOL fail
);

HRESULT get_FailOnTaskFailure(
  [out] VARIANT_BOOL *pFail
);
```



## Property value

Set to VARIANT\_TRUE if you want the job to fail when a task fails; otherwise, VARIANT\_FALSE.

The Default job template sets the default value to VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

By default, all tasks in the job will run. However, in some cases, if a task fails, it is no longer necessary to run the entire job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




