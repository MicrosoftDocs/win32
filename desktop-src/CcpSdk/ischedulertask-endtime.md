---
Description: 'Retrieves the date and time that the task ended.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '160e9c36-2cf3-4fa2-9438-156ba39e0b59'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::EndTime property'
---

# ISchedulerTask::EndTime property

Retrieves the date and time that the task ended.

This property is read-only.

## Syntax


```C++
HRESULT get_EndTime(
  [out] DATE *pTime
);
```



## Property value

The time the task ended. The value is in Coordinated Universal Time.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The end time indicates when the task finished, failed, or was canceled. The value is zero if the task has not finished, failed, or been canceled. The time is reset if you queue a failed or canceled task again.

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

[**ISchedulerTask.CreateTime**](ischedulertask-createtime.md)
</dt> <dt>

[**ISchedulerTask.StartTime**](ischedulertask-starttime.md)
</dt> <dt>

[**ISchedulerTask.SubmitTime**](ischedulertask-submittime.md)
</dt> </dl>

 

 




