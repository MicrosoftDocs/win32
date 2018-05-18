---
Description: 'Retrieves the last time that the user or server changed a property of the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2999cc1c-00b0-4818-bfab-86e271b2839f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::ChangeTime property'
---

# ISchedulerTask::ChangeTime property

Retrieves the last time that the user or server changed a property of the task.

This property is read-only.

## Syntax


```C++
HRESULT get_ChangeTime(
  [out] DATE *pTime
);
```



## Property value

The date and time that the task was last touched. The value is in Coordinated Universal Time.

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

[**ISchedulerTask.EndTime**](ischedulertask-endtime.md)
</dt> <dt>

[**ISchedulerTask.CreateTime**](ischedulertask-createtime.md)
</dt> <dt>

[**ISchedulerTask.StartTime**](ischedulertask-starttime.md)
</dt> <dt>

[**ISchedulerTask.SubmitTime**](ischedulertask-submittime.md)
</dt> </dl>

 

 




