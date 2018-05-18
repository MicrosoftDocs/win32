---
Description: 'Sets the command line for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'afd50341-940f-4970-a5b7-7ac9251a3eb0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_CommandLine method'
---

# ITask::put\_CommandLine method

Sets the command line for the task.

## Syntax


```C++
HRESULT put_CommandLine(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The command line. The command is limited to 480 Unicode characters.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

The command line is required for all tasks. The command line must include the name of the executable program and any arguments. If the path to the executable program contains long file names, enclose the path in quotation marks.

For more information about specifying the command line, see the description for the command line parameter of the Win32 [**CreateProcess**](https://msdn.microsoft.com/library/windows/desktop/ms682425) function.

The executable program must exist under the specified path on each node specified in the [**ITask::put\_RequiredNodes**](itask-put-requirednodes.md) method. If you do not specify a list of required nodes, the executable program must exist on each node in the cluster. The same is true if you add the task to a job and the job does not use the [**IJob::put\_AskedNodes**](ijob-put-askednodes.md) method to limit the nodes on which the task runs.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_CommandLine**](itask-get-commandline.md)
</dt> </dl>

 

 




