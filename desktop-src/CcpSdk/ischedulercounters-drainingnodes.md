---
Description: 'Retrieves the number of nodes that are in the process of removing jobs from the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '53f0efbf-2d7a-4a2e-a8b2-f8e1c9babca3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::DrainingNodes property'
---

# ISchedulerCounters::DrainingNodes property

Retrieves the number of nodes that are in the process of removing jobs from the node.

This property is read-only.

## Syntax


```C++
HRESULT get_DrainingNodes(
  [out] long *pDrainingNodes
);
```



## Property value

Retrieves the number of nodes that are in the process of removing jobs from the node.

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

 

 




