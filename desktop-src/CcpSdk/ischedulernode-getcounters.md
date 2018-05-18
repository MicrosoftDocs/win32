---
Description: 'Retrieves the counter data for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6670d726-7388-40b8-9771-31b33064698c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNode::GetCounters method'
---

# ISchedulerNode::GetCounters method

Retrieves the counter data for the job.

## Syntax


```C++
HRESULT GetCounters(
  [out] ISchedulerNodeCounters **pCounters
);
```



## Parameters

<dl> <dt>

*pCounters* \[out\]
</dt> <dd>

An [**ISchedulerNodeCounters**](ischedulernodecounters.md) interface that contains the counter data for the node.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> </dl>

 

 




