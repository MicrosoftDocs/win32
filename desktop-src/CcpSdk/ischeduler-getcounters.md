---
Description: 'Retrieves counter information for the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b6181075-93bc-4acd-8676-1a572adaa8bf'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IScheduler::GetCounters method'
---

# IScheduler::GetCounters method

Retrieves counter information for the cluster.

## Syntax


```C++
HRESULT GetCounters(
  [out] ISchedulerCounters **pCounters
);
```



## Parameters

<dl> <dt>

*pCounters* \[out\]
</dt> <dd>

An [**ISchedulerCounters**](ischedulercounters.md) interface that contains the counter data.

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

[**IScheduler**](ischeduler.md)
</dt> <dt>

[**ISchedulerJob::GetCounters**](ischedulerjob-getcounters.md)
</dt> <dt>

[**ISchedulerNode::GetCounters**](ischedulernode-getcounters.md)
</dt> <dt>

[**ISchedulerTask::GetCounters**](ischedulertask-getcounters.md)
</dt> </dl>

 

 




