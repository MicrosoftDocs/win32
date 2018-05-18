---
Description: 'Defines the state of the node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1f2ec2ce-fec4-41c5-810f-27a0553044bc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeState enumeration
---

# NodeState enumeration

Defines the state of the node.

## Syntax


```C++
typedef enum  { 
  NodeState_Offline   = 1,
  NodeState_Draining  = 2,
  NodeState_Online    = 4,
  NodeState_ALL       = 7
} NodeState;
```



## Constants

<dl> <dt>

<span id="NodeState_Offline"></span><span id="nodestate_offline"></span><span id="NODESTATE_OFFLINE"></span>**NodeState\_Offline**
</dt> <dd>

The node is offline.

</dd> <dt>

<span id="NodeState_Draining"></span><span id="nodestate_draining"></span><span id="NODESTATE_DRAINING"></span>**NodeState\_Draining**
</dt> <dd>

The scheduler is in the process of removing jobs from the node.

</dd> <dt>

<span id="NodeState_Online"></span><span id="nodestate_online"></span><span id="NODESTATE_ONLINE"></span>**NodeState\_Online**
</dt> <dd>

The node is online and ready to run jobs.

</dd> <dt>

<span id="NodeState_ALL"></span><span id="nodestate_all"></span><span id="NODESTATE_ALL"></span>**NodeState\_ALL**
</dt> <dd>

Indicates a node in any state.

</dd> </dl>

## Requirements



|                         |                                                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities, HPC Pack 2008 Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Scheduler.Properties.tlb</dt> </dl> |



## See also

<dl> <dt>

[HPC Enumerations](hpc-enumerations.md)
</dt> <dt>

[**ISchedulerNode.State**](ischedulernode-state.md)
</dt> </dl>

 

 




