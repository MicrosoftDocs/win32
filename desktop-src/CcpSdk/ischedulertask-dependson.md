---
Description: 'Retrieves or sets the dependent tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1e697ce9-1363-4f71-abf5-2ec4bc486c79'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::DependsOn property'
---

# ISchedulerTask::DependsOn property

Retrieves or sets the dependent tasks.

This property is read/write.

## Syntax


```C++
HRESULT get_DependsOn(
  [out] IStringCollection **pDependsOn
);
```



## Property value

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, access the [**ErrorMessage**](ischedulertask-errormessage.md) task property.

## Remarks

Typically, you use dependencies to break a large task into smaller subtasks. For example, if task A needs to finish before task B, which needs to finish before task C, then task B depends on A and task C depends on B. Task B will not run until A finishes, fails, or is canceled.

The server checks for circular dependencies.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> </dl>

 

 




