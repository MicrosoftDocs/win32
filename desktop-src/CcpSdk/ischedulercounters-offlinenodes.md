---
Description: 'Retrieves the number of nodes that are offline.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '69c8f520-ba2c-434d-b42d-559fc76e9105'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerCounters::OfflineNodes property'
---

# ISchedulerCounters::OfflineNodes property

Retrieves the number of nodes that are offline.

This property is read-only.

## Syntax


```C++
HRESULT get_OfflineNodes(
  [out] long *pOfflineNodes
);
```



## Property value

The number of nodes that are offline.

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

 

 




