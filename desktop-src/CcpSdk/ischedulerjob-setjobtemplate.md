---
Description: 'Sets the job template to use for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '4d381994-5ecc-45a2-93a3-b9c51c614758'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SetJobTemplate method'
---

# ISchedulerJob::SetJobTemplate method

Sets the job template to use for the job.

## Syntax


```C++
HRESULT SetJobTemplate(
  [in] BSTR name
);
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The name of the template to use for this job.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) property.

## Remarks

To get the template specified for the job, access the [**ISchedulerJob::JobTemplate**](ischedulerjob-jobtemplate.md) property. To get a list of available templates, access the [**IScheduler::GetJobTemplateList**](ischeduler-getjobtemplatelist.md) scheduler property.

HPC maintains the following three property values for each property:

-   The value set by the user
-   The template value if specified by the template
-   A default value

If the user sets the property value, the user-defined value is used. If not, the template value is used. If the user and template do not specify a value, the default property value is used.

For those properties that are defined in both the new and old template, the default values and template values defined in the new template override the values for the same properties defined in the old template. All property values changed by the user remain unchanged. The default values for any properties defined in the old template that are not also defined in the new template are retained. The method does not validate the job's property values against the new template until the scheduler tries to run the job.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob.JobTemplate**](ischedulerjob-jobtemplate.md)
</dt> </dl>

 

 




