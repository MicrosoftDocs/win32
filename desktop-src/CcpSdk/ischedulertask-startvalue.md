---
Description: 'Retrieves or sets the starting instance value for a parametric task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ff68279f-373f-4a60-960d-9d8f99c834fd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::StartValue property'
---

# ISchedulerTask::StartValue property

Retrieves or sets the starting instance value for a parametric task.

This property is read/write.

## Syntax


```C++
HRESULT put_StartValue(
  [in]  long value
);

HRESULT get_StartValue(
  [out] long *pValue
);
```



## Property value

The starting instance value. The value must be greater than zero and must not exceed the value of [**EndValue**](ischedulertask-endvalue.md). The default value is 1.

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

[**ISchedulerTask.IncrementValue**](ischedulertask-incrementvalue.md)
</dt> <dt>

[**ISchedulerTask.IsParametric**](ischedulertask-isparametric.md)
</dt> </dl>

 

 




