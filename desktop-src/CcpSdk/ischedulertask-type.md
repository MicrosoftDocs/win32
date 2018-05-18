---
Description: 'Gets or sets a task type that defines how to run the command for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '37661E08-7C52-43DC-9360-7AF6B2E21C57'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerTask::Type property'
---

# ISchedulerTask::Type property

Gets or sets a task type that defines how to run the command for the task.

This property is read/write.

## Syntax


```C++
HRESULT put_Type(
  [in]          TaskType pRetVal
);

HRESULT get_Type(
  [out, retval] TaskType *pRetVal
);
```



## Property value

The task type that defines how to run the command for the task. For possible values, see the [**TaskType**](tasktype.md) enumeration. The default value is **TaskType\_Basic**.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerTask**](ischedulertask.md)
</dt> <dt>

[**TaskType**](tasktype.md)
</dt> </dl>

 

 




