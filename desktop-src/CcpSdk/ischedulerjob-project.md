---
Description: 'Retrieves or sets the project name to associate with the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '44f0d95e-d1fd-4b25-bc10-14d10ca6dc2a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Project property'
---

# ISchedulerJob::Project property

Retrieves or sets the project name to associate with the job.

This property is read/write.

## Syntax


```C++
HRESULT put_Project(
  [in]  BSTR project
);

HRESULT get_Project(
  [out] BSTR *pProject
);
```



## Property value

The project name. The name is limited to 80 Unicode characters.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

The name can be used for accounting purposes.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> </dl>

 

 




