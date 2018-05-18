---
Description: 'Gets the environment variables that are set for the job and their values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '63C37755-7367-4CAB-AC0E-3202CC6EE3E4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerJob::EnvironmentVariables property'
---

# ISchedulerJob::EnvironmentVariables property

Gets the environment variables that are set for the job and their values.

This property is read-only.

## Syntax


```C++
HRESULT get_EnvironmentVariables(
  [out] INameValueCollection **pRetVal
);
```



## Property value

An [**INameValueCollection**](inamevaluecollection.md) interface that represents a set of paired environment variable names and values.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

Use the [**ISchedulerJob::SetEnvironmentVariable**](ischedulerjob-setenvironmentvariable.md) method to set or unset environment variables for a job.

You cannot add environment variables to the job by adding [**INameValue**](inamevalue.md) items to the [**INameValueCollection**](inamevaluecollection.md) interface that the **ISchedulerJob::EnvironmentVariables** property contains. Use the [**ISchedulerJob::SetEnvironmentVariable**](ischedulerjob-setenvironmentvariable.md) method to add environment variables instead.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerJob**](ischedulerjob.md)
</dt> <dt>

[**ISchedulerJob::SetEnvironmentVariable**](ischedulerjob-setenvironmentvariable.md)
</dt> <dt>

[**ISchedulerTask::EnvironmentVariables**](ischedulertask-environmentvariables.md)
</dt> </dl>

 

 




