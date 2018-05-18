---
title: ClusNode.State property
description: State of a node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c1887055-518a-4177-a618-418c75883d69'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["State property Failover Cluster", "State property Failover Cluster , ClusNode object", "ClusNode object Failover Cluster , State property"]
topic_type:
- apiref
api_name:
- ClusNode.State
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNode.State property

\[The **State** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the state of a [node](nodes.md).

This property is read-only.

## Syntax


```VB
ClusNode.State
```



## Property value

Long that receives one of the following values describes the node's current state, enumerated by the [**CLUSTER\_NODE\_STATE**](cluster-node-state.md) enumeration.

<dt>

<span id="ClusterNodeStateUnknown"></span><span id="clusternodestateunknown"></span><span id="CLUSTERNODESTATEUNKNOWN"></span>

<span id="ClusterNodeStateUnknown"></span><span id="clusternodestateunknown"></span><span id="CLUSTERNODESTATEUNKNOWN"></span>**ClusterNodeStateUnknown** (-1)


</dt> <dd>

The current state of the node is unknown.

</dd> <dt>

<span id="ClusterNodeUp"></span><span id="clusternodeup"></span><span id="CLUSTERNODEUP"></span>

<span id="ClusterNodeUp"></span><span id="clusternodeup"></span><span id="CLUSTERNODEUP"></span>**ClusterNodeUp** (0)


</dt> <dd>

The node is physically plugged in, turned on, booted, and capable of executing programs.

</dd> <dt>

<span id="ClusterNodeDown"></span><span id="clusternodedown"></span><span id="CLUSTERNODEDOWN"></span>

<span id="ClusterNodeDown"></span><span id="clusternodedown"></span><span id="CLUSTERNODEDOWN"></span>**ClusterNodeDown** (1)


</dt> <dd>

The node is turned off or not operational.

</dd> <dt>

<span id="ClusterNodePaused"></span><span id="clusternodepaused"></span><span id="CLUSTERNODEPAUSED"></span>

<span id="ClusterNodePaused"></span><span id="clusternodepaused"></span><span id="CLUSTERNODEPAUSED"></span>**ClusterNodePaused** (2)


</dt> <dd>

The node is running but not participating in cluster operations.

</dd> <dt>

<span id="ClusterNodeJoining"></span><span id="clusternodejoining"></span><span id="CLUSTERNODEJOINING"></span>

<span id="ClusterNodeJoining"></span><span id="clusternodejoining"></span><span id="CLUSTERNODEJOINING"></span>**ClusterNodeJoining** (3)


</dt> <dd>

The node is in the process of joining a [*cluster*](c-gly.md#-wolf-cluster-gly).

</dd> </dl>

## Remarks

The **ClusterNodeDown** state only indicates that a node is inactive; it does not specify the reason for the inactivity. A node can be in the **ClusterNodeDown** state for the following reasons:

-   The node is not running.
-   The [Cluster service](cluster-service.md) on the node is not running.
-   The node cannot communicate with the node controlling the [quorum resource](quorum-resource.md).
-   The node is inactive for any other reason.

When a node is operating as an active member of a cluster but cannot host any resources or groups, it is in the **ClusterNodePaused** state (see the [**PauseClusterNode**](pauseclusternode.md) function). Nodes that are undergoing maintenance are typically placed in this state.

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNode is defined as F2E606F8-2631-11D1-89F1-00A0C90D061E<br/>         |



## See also

<dl> <dt>

[**ClusNode**](clusnode-object.md)
</dt> <dt>

[**CLUSTER\_NODE\_STATE**](cluster-node-state.md)
</dt> </dl>

 

 





