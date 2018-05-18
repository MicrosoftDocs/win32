---
Description: 'Sets the specified environment variable to the specified value in the context of the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '893CBF38-3971-47F0-ABB9-F36EEC4B82E4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::SetEnvironmentVariable method'
---

# ISchedulerJob::SetEnvironmentVariable method

Sets the specified environment variable to the specified value in the context of the job.

## Syntax


```C++
HRESULT SetEnvironmentVariable(
  [in] BSTR Name,
  [in] BSTR Value
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

A string that specifies the name of the environment variable that you want to set in the context of the job.

</dd> <dt>

*Value* \[in\]
</dt> <dd>

A string that specifies the value to which you want to set the environment variable. To unset an environment variable in the context of a job, specify an empty string.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

If you set or unset an environment variable for a job, that environment variable is also set or unset for each task in the job unless you override that environment variable setting for the task by calling the [**ISchedulerTask::SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerTask::SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md)
</dt> <dt>

[**ISchedulerJob::EnvironmentVariables**](ischedulerjob-environmentvariables.md)
</dt> </dl>

 

 




