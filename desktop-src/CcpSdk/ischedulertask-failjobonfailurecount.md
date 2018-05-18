---
Description: 'Retrieves or sets the number of subtasks of a critical parametric sweep or service task that must fail before the job and its tasks and subtask should stop running and the task and job should be marked as failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '64EFF813-2E32-4F04-9E2F-17018D74CF6F'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::FailJobOnFailureCount property'
---

# ISchedulerTask::FailJobOnFailureCount property

Retrieves or sets the number of subtasks of a critical parametric sweep or service task that must fail before the job and its tasks and subtask should stop running and the task and job should be marked as failed.

This property is read/write.

## Syntax


```C++
HRESULT put_FailJobOnFailureCount(
  [in]  long value
);

HRESULT get_FailJobOnFailureCount(
  [out] long *pValue
);
```



## Property value

Indicates the number of subtasks of a critical parametric sweep or service task that must fail before the job and its tasks and subtask should stop running and the task and job should be marked as failed.

## Error codes

If the method succeeds, the return value is **S\_OK**. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulerjob-errormessage.md) task property.

## Remarks

You can specify a value from 1 through 1,000,000. If you specify more subtasks than the critical task contains, the job and its tasks and subtasks run to completion no matter how many subtasks fail.

If you specify a value greater than 1 for the **FailJobOnFailureCount** property for a task that is not a parametric sweep or service task, an error occurs.

If you specify a value for the **FailJobOnFailureCount** property, but also specify **VARIANT\_FALSE** for the [**FailJobOnFailure**](ischedulertask-failjobonfailure.md) property, **FailJobOnFailureCount** is set to 0. If you specify a value for **FailJobOnFailureCount**, and do not specify a value for **FailJobOnFailure**, **FailJobOnFailure** is automatically set to **VARIANT\_TRUE**.

## Requirements



|                         |                                                                                                                                            |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | This property was introduced in Windows HPC Server 2008 R2 with Service Pack 1 (SP1) and is not supported in previous versions.<br/> |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl>                                     |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**FailJobOnFailure**](ischedulertask-failjobonfailure.md)
</dt> </dl>

 

 




