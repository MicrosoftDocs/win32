---
Description: 'Determines whether the Runtime task property is set.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '131d4870-6880-4df5-bea7-d917bb92dd95'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::HasRuntime property'
---

# ISchedulerTask::HasRuntime property

Determines whether the [**Runtime**](ischedulertask-runtime.md) task property is set.

This property is read-only.

## Syntax


```C++
HRESULT get_HasRuntime(
  [out] VARIANT_BOOL *pHasRuntimeLimit
);
```



## Property value

Is VARIANT\_TRUE if the run-time limit is set; otherwise, VARIANT\_FALSE. The default is VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack Client Utilities<br/>                                                                   |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerJob.Runtime**](ischedulerjob-runtime.md)
</dt> <dt>

[**ISchedulerTask.Runtime**](ischedulertask-runtime.md)
</dt> </dl>

 

 




