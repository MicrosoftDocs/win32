---
Description: 'Retrieves the date and time that the task started running.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd514de9a-1741-40b3-aa29-ab9839a6cb5b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::StartTime property'
---

# ISchedulerTask::StartTime property

Retrieves the date and time that the task started running.

This property is read-only.

## Syntax


```C++
HRESULT get_StartTime(
  [out] DATE *pStartTime
);
```



## Property value

The task start time. The value is in Coordinated Universal Time.

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

[**ISchedulerTask.CreateTime**](ischedulertask-createtime.md)
</dt> <dt>

[**ISchedulerTask.EndTime**](ischedulertask-endtime.md)
</dt> <dt>

[**ISchedulerTask.StartTime**](ischedulertask-starttime.md)
</dt> <dt>

[**ISchedulerTask.SubmitTime**](ischedulertask-submittime.md)
</dt> </dl>

 

 




