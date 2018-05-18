---
Description: 'Retrieves the last time that the user or server changed a property of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd2ee240e-4502-4c2b-9c52-3f4ebf08ddcd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::ChangeTime property'
---

# ISchedulerJob::ChangeTime property

Retrieves the last time that the user or server changed a property of the job.

This property is read-only.

## Syntax


```C++
HRESULT get_ChangeTime(
  [out] DATE *pChangeTime
);
```



## Property value

The date and time that the job was last touched. The value is in Coordinated Universal Time.

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

[**ISchedulerJob.CreateTime**](ischedulerjob-createtime.md)
</dt> <dt>

[**ISchedulerJob.EndTime**](ischedulerjob-endtime.md)
</dt> <dt>

[**ISchedulerJob.StartTime**](ischedulerjob-starttime.md)
</dt> <dt>

[**ISchedulerJob.SubmitTime**](ischedulerjob-submittime.md)
</dt> </dl>

 

 




