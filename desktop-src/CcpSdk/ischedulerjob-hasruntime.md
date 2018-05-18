---
Description: 'Determines whether the Runtime job property is set.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9db60565-52fb-4e48-a053-d3b80a1e659d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::HasRuntime property'
---

# ISchedulerJob::HasRuntime property

Determines whether the [**Runtime**](ischedulerjob-runtime.md) job property is set.

This property is read-only.

## Syntax


```C++
HRESULT get_HasRuntime(
  [out] VARIANT_BOOL *pHasRuntimeLimit
);
```



## Property value

Is VARIANT\_TRUE if the run-time limit is set; otherwise, VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.Runtime**](ischedulerjob-runtime.md)
</dt> </dl>

 

 




