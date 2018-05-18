---
Description: 'Retrieves or sets the command line for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '95daa0db-d1fb-4578-b32b-ed2d1468b04a'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::CommandLine property'
---

# ISchedulerTask::CommandLine property

Retrieves or sets the command line for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_CommandLine(
  [in]  BSTR command
);

HRESULT get_CommandLine(
  [out] BSTR *pCommand
);
```



## Property value

The command to execute. The command is limited to 480 Unicode characters.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The command line is required for all tasks. The command line must include the name of the executable program and any arguments. If the path to the executable program contains long file names, enclose the path in quotation marks.

The executable program must exist under the specified path on each node specified in the [**RequiredNodes**](ischedulertask-requirednodes.md) task property. If you do not specify a list of required nodes, the executable program must exist on each node in the cluster. The same is true if you add the task to a job and the job does not use the [**RequestedNodes**](ischedulerjob-requestednodes.md) job property to limit the nodes on which the task can run.

For parametric tasks (see the [**IsParametric**](ischedulertask-isparametric.md) property), the Scheduler replaces all occurrences of an asterisk (\*) found in the command line with the instance value.

For more information about specifying the command line, see the description for the command line parameter of the Win32 [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) function.

## Examples

For an example, see [Creating and Submitting a Job](creating-and-submitting-a-job.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




