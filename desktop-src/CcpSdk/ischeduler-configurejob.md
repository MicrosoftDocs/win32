---
Description: 'Moves the job to the Configuring state.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3c60032d-0c3c-4df3-8560-5ecf1b583f75'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::ConfigureJob method'
---

# IScheduler::ConfigureJob method

Moves the job to the Configuring state.

## Syntax


```C++
HRESULT ConfigureJob(
  [in] long id
);
```



## Parameters

<dl> <dt>

*id* \[in\]
</dt> <dd>

Identifies the job to move to the Configuring state.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

You can move the job to the Configuring state from only the following states (see [**JobState**](jobstate.md)):

-   JobState\_Canceled
-   JobState\_Failed
-   JobState\_Queued
-   JobState\_Submitted

Typically, you would move a job back to the Configuring state if a task failed so that you can fix the task and run the job again. When the job is run again, all tasks in the job run regardless of their prior state.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler::AddJob**](ischeduler-addjob.md)
</dt> <dt>

[**IScheduler::CreateJob**](ischeduler-createjob.md)
</dt> <dt>

[**IScheduler::CancelJob**](ischeduler-canceljob.md)
</dt> <dt>

[**IScheduler::OpenJob**](ischeduler-openjob.md)
</dt> </dl>

 

 




