---
Description: 'Determines whether nodes are exclusively allocated to the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ea70c922-60b3-4a07-94ab-920e432a98f5'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::IsExclusive property'
---

# ISchedulerJob::IsExclusive property

Determines whether nodes are exclusively allocated to the job.

This property is read/write.

## Syntax


```C++
HRESULT put_IsExclusive(
  [in]  VARIANT_BOOL isExclusive
);

HRESULT get_IsExclusive(
  [out] VARIANT_BOOL *pIsExclusive
);
```



## Property value

Set to VARIANT\_TRUE if the nodes are exclusively allocated to the job; otherwise, VARIANT\_FALSE.

The Default job template sets the default value to VARIANT\_FALSE.

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

[**ISchedulerJob.RequestedNodes**](ischedulerjob-requestednodes.md)
</dt> </dl>

 

 




