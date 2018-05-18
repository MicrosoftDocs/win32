---
Description: 'Retrieves or sets the path to which the server redirects standard output.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5331eeab-520b-4795-b757-4a1dc34e5570'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::StdOutFilePath property'
---

# ISchedulerTask::StdOutFilePath property

Retrieves or sets the path to which the server redirects standard output.

This property is read/write.

## Syntax


```C++
HRESULT put_StdOutFilePath(
  [in]  BSTR path
);

HRESULT get_StdOutFilePath(
  [out] BSTR *pPath
);
```



## Property value

The full path to the file to which standard output is redirected.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

You must specify a file to capture output from stdout; otherwise, the output is lost. If the file exists, it is overwritten. Specify a separate file for each task. If you use the same file, the task could fail if the file is currently locked by another task. The path must exist on each node on which the task runs.

If you do not specify a file for stdout, you can access the [**Output**](ischedulertask-output.md) task property to view the output written to stdout.

For parametric tasks (see the [**IsParametric**](ischedulertask-isparametric.md) property), the Scheduler replaces all occurrences of an asterisk (\*) found in the file path with the instance value.

## Examples

For an example, see [Creating a Parametric Sweep Task](creating-parametric-sweep-task.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.Output**](ischedulertask-output.md)
</dt> <dt>

[**ISchedulerTask.StdErrFilePath**](ischedulertask-stderrfilepath.md)
</dt> <dt>

[**ISchedulerTask.StdInFilePath**](ischedulertask-stdinfilepath.md)
</dt> </dl>

 

 




