---
Description: 'Sets the dependent tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ce8aa776-d40a-4a61-a320-224a605b45a1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ITask::put\_Depend method'
---

# ITask::put\_Depend method

Sets the dependent tasks.

## Syntax


```C++
HRESULT put_Depend(
  [in] BSTR Val
);
```



## Parameters

<dl> <dt>

*Val* \[in\]
</dt> <dd>

A comma-separated list of task names.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Remarks

Typically, you use dependencies to break a large task into smaller subtasks. For example, if task A needs to finish before task B, which needs to finish before task C, then task B depends on A and task C depends on B. Task B will not run until A finishes, fails, or is canceled.

The method checks for circular dependencies.

The dependency is ignored if the task is specified in a [command](icluster-executecommand.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ITask**](itask.md)
</dt> <dt>

[**ITask::get\_Depend**](itask-get-depend.md)
</dt> </dl>

 

 




