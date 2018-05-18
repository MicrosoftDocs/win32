---
Description: 'Retrieves the identifier of the parent job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7f87518e-a528-4ccc-83c8-c0207dfee75b'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::ParentJobId property'
---

# ISchedulerTask::ParentJobId property

Retrieves the identifier of the parent job.

This property is read-only.

## Syntax


```C++
HRESULT get_ParentJobId(
  [out] long *pParent
);
```



## Property value

The identifier of the parent job.

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
</dt> <dt>

[**ISchedulerTask.TaskId**](ischedulertask-taskid.md)
</dt> </dl>

 

 




