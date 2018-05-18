---
Description: 'Gets the numeric identifier of the node for which the HPC Node Manager Service became reachable or unreachable.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '75C528CE-B423-4491-B416-2C92F8BF75BE'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'INodeReachableEventArg::NodeId property'
---

# INodeReachableEventArg::NodeId property

Gets the numeric identifier of the node for which the HPC Node Manager Service became reachable or unreachable.

This property is read-only.

## Syntax


```C++
HRESULT get_NodeId(
  [out, retval] long *pRetVal
);
```



## Property value

Gets the numeric identifier of the node for which the HPC Node Manager Service became reachable or unreachable.

## Error codes

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error value.

## Remarks

To get information about the node for which the HPC Node Manager Service became reachable or unreachable, use the [**IScheduler::OpenNode**](ischeduler-opennode.md) method and set the *id* parameter set to a value that this property returns to get an [**ISchedulerNode**](ischedulernode.md) interface for the node.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities with Service Pack 1 (SP1).<br/>                                |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**INodeReachableEventArg**](inodereachableeventarg.md)
</dt> </dl>

 

 




