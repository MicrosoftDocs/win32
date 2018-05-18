---
Description: 'Retrieves or sets the display name of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '88e9e170-c81e-4f57-ac61-cb03e9037ce9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Name property'
---

# ISchedulerJob::Name property

Retrieves or sets the display name of the job.

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

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




