---
Description: 'Retrieves the date and time when the task was created.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '599921bc-2d25-4c64-815b-1dbccb6d1c9e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::CreateTime property'
---

# ISchedulerTask::CreateTime property

Retrieves the date and time when the task was created.

This property is read-only.

## Syntax


```C++
HRESULT get_CreateTime(
  [out] DATE *pTime
);
```



## Property value

The task creation time. The value is in Coordinated Universal Time.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.ChangeTime**](ischedulertask-changetime.md)
</dt> <dt>

[**ISchedulerTask.EndTime**](ischedulertask-endtime.md)
</dt> <dt>

[**ISchedulerTask.StartTime**](ischedulertask-starttime.md)
</dt> <dt>

[**ISchedulerTask.SubmitTime**](ischedulertask-submittime.md)
</dt> </dl>

 

 




