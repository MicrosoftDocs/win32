---
Description: 'Retrieves the date and time that the job ended.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f9923058-e5e5-4009-876e-b208c591e382'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::EndTime property'
---

# ISchedulerJob::EndTime property

Retrieves the date and time that the job ended.

This property is read-only.

## Syntax


```C++
HRESULT get_EndTime(
  [out] DATE *pCreateTime
);
```



## Property value

The job end time. The value is in Coordinated Universal Time.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ISchedulerJob::ErrorMessage**](ischedulerjob-errormessage.md) job property.

## Remarks

The end time indicates when the job finished, failed, or was canceled. The value is zero if the job has not finished, failed, or been canceled. The time is reset if you queue a failed or canceled job again.

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

[**ISchedulerJob.StartTime**](ischedulerjob-starttime.md)
</dt> <dt>

[**ISchedulerJob.SubmitTime**](ischedulerjob-submittime.md)
</dt> </dl>

 

 




