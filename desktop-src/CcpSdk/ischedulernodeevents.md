---
Description: 'Defines methods that you implement to receive event notification when the state of a node changes.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '70929CBB-426B-4748-A8C4-AD749D81451A'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ISchedulerNodeEvents interface
---

# ISchedulerNodeEvents interface

Defines methods that you implement to receive event notification when the state of a node changes.

## When to implement

Implement this interface when you want to receive notification when the state of a node changes.

## Members

The **ISchedulerNodeEvents** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ISchedulerNodeEvents** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISchedulerNodeEvents** interface has these methods.



| Method                                                  | Description                                                         |
|:--------------------------------------------------------|:--------------------------------------------------------------------|
| [**OnNodeState**](ischedulernodeevents-onnodestate.md) | Receives information when the state of the node changes.<br/> |



 

## Requirements



|                         |                                                                                                        |
|-------------------------|--------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                           |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ISchedulerNode**](ischedulernode.md)
</dt> <dt>

[**INodeStateEventArg**](inodestateeventarg.md)
</dt> </dl>

 

 




