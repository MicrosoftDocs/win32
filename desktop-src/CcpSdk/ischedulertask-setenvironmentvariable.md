---
Description: 'Sets a task-specific environment variable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '287cc000-68a8-4e8e-9632-623cff4e60e0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::SetEnvironmentVariable method'
---

# ISchedulerTask::SetEnvironmentVariable method

Sets a task-specific environment variable.

## Syntax


```C++
HRESULT SetEnvironmentVariable(
  [in] BSTR name,
  [in] BSTR value
);
```



## Parameters

<dl> <dt>

*name* \[in\]
</dt> <dd>

The name of the variable.

</dd> <dt>

*value* \[in\]
</dt> <dd>

The string value of the variable. If **NULL** or an empty string, the variable is deleted.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The length of all environment variables specified for the task is limited to 2,048 Unicode characters.

The environment variables that are made available to the task include variables set using this method, those set using the [**IScheduler::SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md) method, and the HPC-defined environment variables.

To retrieve variables from inside your task, call the Win32 function [**GetEnvironmentVariable**](https://msdn.microsoft.com/library/windows/desktop/ms683188).

To set cluster-wide environment variables, call the [**IScheduler::SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler::SetEnvironmentVariable**](ischeduler-setenvironmentvariable.md)
</dt> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.EnvironmentVariables**](ischedulertask-environmentvariables.md)
</dt> </dl>

 

 




