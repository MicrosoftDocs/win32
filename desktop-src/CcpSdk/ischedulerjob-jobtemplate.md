---
Description: 'Retrieves the name of the job template used to initialize the properties of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '519e1273-dbb8-49ff-aa9d-e68da3cedb74'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::JobTemplate property'
---

# ISchedulerJob::JobTemplate property

Retrieves the name of the job template used to initialize the properties of the job.

This property is read-only.

## Syntax


```C++
HRESULT get_JobTemplate(
  [out] BSTR *pTemplate
);
```



## Property value

The name of the job template.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

To specify a new template for the job, call the [**ISchedulerJob::SetJobTemplate**](ischedulerjob-setjobtemplate.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::SetJobTemplate**](ischedulerjob-setjobtemplate.md)
</dt> </dl>

 

 




