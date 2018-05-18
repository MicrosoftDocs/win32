---
Description: 'Retrieves or sets the path from which the server redirects standard input.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f00f0652-c0c7-4663-b6a5-66253e298993'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::StdInFilePath property'
---

# ISchedulerTask::StdInFilePath property

Retrieves or sets the path from which the server redirects standard input.

This property is read/write.

## Syntax


```C++
HRESULT put_StdInFilePath(
  [in]  BSTR path
);

HRESULT get_StdInFilePath(
  [out] BSTR *pPath
);
```



## Property value

The full path to the file from which standard input is redirected.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

For parametric tasks (see the [**IsParametric**](ischedulertask-isparametric.md) property), the Scheduler replaces all occurrences of an asterisk (\*) found in the file path with the instance value.

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

 

 




