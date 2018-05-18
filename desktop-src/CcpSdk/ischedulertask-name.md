---
Description: 'Retrieves or sets the display name of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '8973d11c-8d64-43b1-812a-bb13a08b47ee'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::Name property'
---

# ISchedulerTask::Name property

Retrieves or sets the display name of the task.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR name
);

HRESULT get_Name(
  [out] BSTR *pName
);
```



## Property value

The display name. The name is limited to 80 Unicode characters.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

For parametric tasks (see the [**IsParametric**](ischedulertask-isparametric.md) property), the Scheduler replaces all occurrences of an asterisk (\*) found in the name with the instance value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




