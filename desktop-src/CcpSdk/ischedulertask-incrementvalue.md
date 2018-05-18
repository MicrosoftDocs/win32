---
Description: 'Retrieves or sets the number by which to increment the instance value for a parametric task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f0d8465e-805a-4dd7-aa98-d4844b05b7f6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::IncrementValue property'
---

# ISchedulerTask::IncrementValue property

Retrieves or sets the number by which to increment the instance value for a parametric task.

This property is read/write.

## Syntax


```C++
HRESULT put_IncrementValue(
  [in]  long value
);

HRESULT get_IncrementValue(
  [out] long *pValue
);
```



## Property value

The increment value used to calculate the next instance value. The default is 1.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The parametric instance value is incremented by the increment value until the instance value exceeds the specified ending value.

This property has meaning only if the [**IsParametric**](ischedulertask-isparametric.md) property is VARIANT\_TRUE.

## Examples

For an example, see [Creating a Parametric Sweep Task](creating-parametric-sweep-task.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.EndValue**](ischedulertask-endvalue.md)
</dt> <dt>

[**ISchedulerTask.IsParametric**](ischedulertask-isparametric.md)
</dt> <dt>

[**ISchedulerTask.StartValue**](ischedulertask-startvalue.md)
</dt> </dl>

 

 




