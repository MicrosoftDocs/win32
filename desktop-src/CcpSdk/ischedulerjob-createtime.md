---
Description: 'Retrieves the date and time that the job was created.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '563f795d-48c9-4135-987b-b82acd7e5919'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::CreateTime property'
---

# ISchedulerJob::CreateTime property

Retrieves the date and time that the job was created.

This property is read-only.

## Syntax


```C++
HRESULT get_CreateTime(
  [out] DATE *pCreateTime
);
```



## Property value

The job creation time. The value is in Coordinated Universal Time.

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

[**ISchedulerJob.EndTime**](ischedulerjob-endtime.md)
</dt> <dt>

[**ISchedulerJob.StartTime**](ischedulerjob-starttime.md)
</dt> <dt>

[**ISchedulerJob.SubmitTime**](ischedulerjob-submittime.md)
</dt> </dl>

 

 




