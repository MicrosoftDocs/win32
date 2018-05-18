---
Description: 'Retrieves the time that the job was submitted.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e529493e-f33c-42ce-806e-a1af929017e4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SubmitTime property'
---

# ISchedulerJob::SubmitTime property

Retrieves the time that the job was submitted.

This property is read-only.

## Syntax


```C++
HRESULT get_SubmitTime(
  [out] DATE *pStartTime
);
```



## Property value

The job submit time. The value is in Coordinated Universal Time. The value is zero if the job has not been submitted (see [**IScheduler::SubmitJob**](ischeduler-submitjob.md)).

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

[**ISchedulerJob::ChangeTime**](ischedulerjob-changetime.md)
</dt> <dt>

[**ISchedulerJob::CreateTime**](ischedulerjob-createtime.md)
</dt> <dt>

[**ISchedulerJob::EndTime**](ischedulerjob-endtime.md)
</dt> <dt>

[**ISchedulerJob::StartTime**](ischedulerjob-starttime.md)
</dt> </dl>

 

 




