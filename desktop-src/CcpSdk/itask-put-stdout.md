---
Description: 'Redirects standard output to the specified file.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'abeece55-2c5c-4335-b0ce-71cd9c432455'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_Stdout method'
---

# ITask::put\_Stdout method

Redirects standard output to the specified file.

## Syntax


```C++
HRESULT put_Stdout(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

The path to the file to which standard output is redirected.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

You must specify a file to capture output to stdout; otherwise, the output is lost. If the file exists, it is overwritten. Specify a separate file for each task. If you use the same file, the task could fail if the file is currently locked by another task. The path must exist on each node on which the task runs. If the path contains long file names, enclose the path in quotation marks.

The output file is ignored for tasks run as [commands](icluster-executecommand.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_Stdout**](itask-get-stdout.md)
</dt> <dt>

[**ITask::put\_Stderr**](itask-put-stderr.md)
</dt> <dt>

[**ITask::put\_Stdin**](itask-put-stdin.md)
</dt> </dl>

 

 




