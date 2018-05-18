---
Description: 'Retrieves the output from the command.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c55b51a4-5a5a-46ea-aa96-e1b09da8dc77'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::Output property'
---

# ISchedulerTask::Output property

Retrieves the output from the command.

This property is read-only.

## Syntax


```C++
HRESULT get_Output(
  [out] BSTR *pOutput
);
```



## Property value

The command output.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

The string includes the output from standard out and standard error. Only the first 4 kilobytes of the output are available. If you expect more than 4 kilobytes of output, set the [**StdErrFilePath**](ischedulertask-stderrfilepath.md) and [**StdOutFilePath**](ischedulertask-stdoutfilepath.md) task properties. If you specify paths for both stderr and stdout, this property will be empty.

## Examples

For an example, see [Implementing the Event Handlers for Job Events in C++](implementing-the-event-handlers-for-job-events-in-c--.md).

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**ISchedulerTask.StdErrFilePath**](ischedulertask-stderrfilepath.md)
</dt> <dt>

[**ISchedulerTask.StdOutFilePath**](ischedulertask-stdoutfilepath.md)
</dt> </dl>

 

 




