---
Description: 'Sets the job to the finished state and does not run any additional tasks except node release tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'CF4B212B-64AA-405B-B75C-DA8A19B08627'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::Finish method'
---

# ISchedulerJob::Finish method

Sets the job to the finished state and does not run any additional tasks except node release tasks.

## Syntax


```C++
HRESULT Finish();
```



## Parameters

This method has no parameters.

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

You can use this method to finish jobs that have the [**ISchedulerJob::RunUntilCanceled**](ischedulerjob-rununtilcanceled.md)property set to VARIANT\_TRUE when you have an alternate way of determining that the job is finished.

You can call this method only for jobs that are in the Queued or Running states.

The **ISchedulerJob::Finish** method is essentially equivalent to calling the [**IScheduler::CancelJob**](ischeduler-canceljob.md) method, except that the **ISchedulerJob::Finish** method sets the state of the job to Finished instead of Canceled.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**IScheduler::SubmitJob**](ischeduler-submitjob.md)
</dt> <dt>

[**IScheduler::SubmitJobById**](ischeduler-submitjob-2.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> </dl>

 

 




