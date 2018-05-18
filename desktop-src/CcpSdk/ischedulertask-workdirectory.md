---
Description: 'Retrieves or sets the directory in which to start the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9c3379d9-b4f7-4241-90f2-1d3456e56a37'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::WorkDirectory property'
---

# ISchedulerTask::WorkDirectory property

Retrieves or sets the directory in which to start the task.

This property is read/write.

## Syntax


```C++
HRESULT put_WorkDirectory(
  [in]  BSTR dir
);

HRESULT get_WorkDirectory(
  [out] BSTR *pDir
);
```



## Property value

The absolute path to the startup directory.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




