---
Description: 'Sets a cluster-wide environment variable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9949532e-bbbd-4e64-a888-b54d84a36d55'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::SetEnvironmentVariable method'
---

# IScheduler::SetEnvironmentVariable method

Sets a cluster-wide environment variable.

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

The value of the variable.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The sum of all environment variables is limited to 2,048 Unicode characters.

You can use this method to add, delete, or update an environment variable. To delete a variable, set the *value* parameter to **NULL**. You cannot delete or update an HPC-defined variable. If you try to delete or update an HPC-defined variable (for example, CCP\_CLUSTER\_NAME), the operation is ignored.

The method uses a case-insensitive comparison to find the environment variable. If the variable is not found, the method adds the variable. If the variable is found, the method updates its value unless the value is empty or **NULL**, in which case the method deletes the variable.

To set environment variables for a task, call the [**ISchedulerTask::SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md) method.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**IScheduler.EnvironmentVariables**](ischeduler-environmentvariables.md)
</dt> <dt>

[**ISchedulerTask::SetEnvironmentVariable**](ischedulertask-setenvironmentvariable.md)
</dt> </dl>

 

 




