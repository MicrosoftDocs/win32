---
Description: 'Retrieves the total number of node in the cluster that are not reachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '580ab614-de43-44df-bc65-cca437c38f93'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::UnreachableNodes property'
---

# ISchedulerCounters::UnreachableNodes property

Retrieves the total number of node in the cluster that are not reachable.

This property is read-only.

## Syntax


```C++
HRESULT get_UnreachableNodes(
  [out] long *pUnreachableNodes
);
```



## Property value

The total number of node in the cluster that are not reachable.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerCounters**](ischedulercounters.md)
</dt> </dl>

 

 




