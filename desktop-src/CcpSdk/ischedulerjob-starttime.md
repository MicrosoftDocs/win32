---
Description: 'Retrieves the date and time that the job started running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f1250d9d-d609-4bb7-a052-04a8020030e9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::StartTime property'
---

# ISchedulerJob::StartTime property

Retrieves the date and time that the job started running.

This property is read-only.

## Syntax


```C++
HRESULT get_StartTime(
  [out] DATE *pStartTime
);
```



## Property value

The job start time. The value is in Coordinated Universal Time.

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

[**ISchedulerJob.ChangeTime**](ischedulerjob-changetime.md)
</dt> <dt>

[**ISchedulerJob.CreateTime**](ischedulerjob-createtime.md)
</dt> <dt>

[**ISchedulerJob.EndTime**](ischedulerjob-endtime.md)
</dt> <dt>

[**ISchedulerJob.SubmitTime**](ischedulerjob-submittime.md)
</dt> </dl>

 

 




