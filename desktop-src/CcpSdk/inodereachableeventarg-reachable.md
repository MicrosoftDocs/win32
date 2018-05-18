---
Description: 'Gets whether the HPC Node Manager Service on the node that the NodeId property identifies became reachable or unreachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '22F1AF91-DD7F-4EF0-AB95-10F1DF4ACBB9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INodeReachableEventArg::Reachable property'
---

# INodeReachableEventArg::Reachable property

Gets whether the HPC Node Manager Service on the node that the NodeId property identifies became reachable or unreachable.

This property is read-only.

## Syntax


```C++
HRESULT get_Reachable(
  [out, retval] long *pRetVal
);
```



## Property value

Gets whether the HPC Node Manager Service on the node that the NodeId property identifies became reachable or unreachable.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities with Service Pack 1 (SP1).<br/>                                |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INodeReachableEventArg**](inodereachableeventarg.md)
</dt> </dl>

 

 




