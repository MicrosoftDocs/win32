---
Description: 'Retrieves or sets a value indicating whether child tasks should be marked as failed if the current task fails.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'A3376B08-3AA3-4DA3-8A23-7ADCFDC40F61'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::FailDependentTasks property'
---

# ISchedulerJob::FailDependentTasks property

Retrieves or sets a value indicating whether child tasks should be marked as failed if the current task fails.

This property is read/write.

## Syntax


```C++
HRESULT put_FailDependentTasks(
  [in]  VARIANT_BOOL value
);

HRESULT get_FailDependentTasks(
  [out] VARIANT_BOOL *pValue
);
```



## Property value

Set to VARIANT\_TRUE true if child tasks should be marked as failed if the current task fails; otherwise, VARIANT\_FALSE.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Requirements



|                         |                                                                                                             |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Pack 2012 and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>      |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




