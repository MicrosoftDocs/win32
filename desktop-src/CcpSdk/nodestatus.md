---
Description: 'Defines the node status constants.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '68cbf28e-562b-4e16-9081-6ca96932dfb8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NodeStatus enumeration
---

# NodeStatus enumeration

Defines the node status constants.

## Syntax


```C++
typedef enum  { 
  NodeStatus_Ready        = 0,
  NodeStatus_Paused       = 1,
  NodeStatus_Unreachable  = 2,
  NodeStatus_Pending      = 3
} NodeStatus;
```



## Constants

<dl> <dt>

<span id="NodeStatus_Ready"></span><span id="nodestatus_ready"></span><span id="NODESTATUS_READY"></span>**NodeStatus\_Ready**
</dt> <dd>

The node is ready to run jobs.

</dd> <dt>

<span id="NodeStatus_Paused"></span><span id="nodestatus_paused"></span><span id="NODESTATUS_PAUSED"></span>**NodeStatus\_Paused**
</dt> <dd>

The [**ICluster::PauseNode**](icluster-pausenode.md) method was called. No new jobs or tasks can be started while the node is paused, but existing jobs and tasks can still run. To resume the node, call the [**ICluster::ResumeNode**](icluster-resumenode.md) method.

</dd> <dt>

<span id="NodeStatus_Unreachable"></span><span id="nodestatus_unreachable"></span><span id="NODESTATUS_UNREACHABLE"></span>**NodeStatus\_Unreachable**
</dt> <dd>

Communication with the node has been broken.

</dd> <dt>

<span id="NodeStatus_Pending"></span><span id="nodestatus_pending"></span><span id="NODESTATUS_PENDING"></span>**NodeStatus\_Pending**
</dt> <dd>

Node approval is pending. To approve the node for addition to the cluster, call the [**ICluster::ApproveNode**](icluster-approvenode.md) method.

</dd> </dl>

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[CCP Enumerations](enumeration-types.md)
</dt> <dt>

[**INode::get\_Status**](inode-get-status.md)
</dt> </dl>

 

 




