---
Description: 'Receives information when the state of the node changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '04E7CEE7-6635-4099-836D-CEFAAC01D9B0'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ISchedulerNodeEvents::OnNodeState method'
---

# ISchedulerNodeEvents::OnNodeState method

Receives information when the state of the node changes.

## Syntax


```C++
void OnNodeState(
  [in] VARIANT            sender,
  [in] INodeStateEventArg *arg
);
```



## Parameters

<dl> <dt>

*sender* \[in\]
</dt> <dd>

A variant that contains a SchedulerNode object for the node for which the state changed.

</dd> <dt>

*arg* \[in\]
</dt> <dd>

An [**INodeStateEventArg**](inodestateeventarg.md) interface that provides information that is related to the change in the state of the node.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To receive information about changes in the state of a node, you need to implement this method in your application. This method is then called when the state of the node changes.

To get the node, query the **pdispVal** member of the *sender* parameter for the [**ISchedulerNode**](ischedulernode.md) interface. Then, pass the [**INodeStateEventArg::nodeId**](inodestateidcollection-nodeid.md) property to the [**IScheduler::OpenNode**](ischeduler-opennode.md) method.

The dispatch identifier for this method is 0x60020000.

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNodeEvents**](ischedulernodeevents.md)
</dt> <dt>

[**INodeStateEventArg**](inodestateeventarg.md)
</dt> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> </dl>

 

 




