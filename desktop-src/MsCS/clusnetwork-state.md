---
title: ClusNetwork.State property
description: State of a network.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'abf1f90f-8044-40cf-b360-f80accb9cc58'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["State property Failover Cluster", "State property Failover Cluster , ClusNetwork object", "ClusNetwork object Failover Cluster , State property"]
topic_type:
- apiref
api_name:
- ClusNetwork.State
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusNetwork.State property

\[The **State** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the state of a [network](networks.md).

This property is read-only.

## Syntax


```VB
ClusNetwork.State
```



## Property value

**Long**that receives a constant representing the network's current state enumerated by the [**CLUSTER\_NETWORK\_STATE**](cluster-network-state.md) enumeration.

<dt>

<span id="ClusterNetworkStateUnknown"></span><span id="clusternetworkstateunknown"></span><span id="CLUSTERNETWORKSTATEUNKNOWN"></span>

<span id="ClusterNetworkStateUnknown"></span><span id="clusternetworkstateunknown"></span><span id="CLUSTERNETWORKSTATEUNKNOWN"></span>**ClusterNetworkStateUnknown** (-1)


</dt> <dd>

The **State** property has failed; the state of the network is unknown.

</dd> <dt>

<span id="ClusterNetworkUnavailable"></span><span id="clusternetworkunavailable"></span><span id="CLUSTERNETWORKUNAVAILABLE"></span>

<span id="ClusterNetworkUnavailable"></span><span id="clusternetworkunavailable"></span><span id="CLUSTERNETWORKUNAVAILABLE"></span>**ClusterNetworkUnavailable** (0)


</dt> <dd>

All of the network interfaces on the network are unavailable, which means that the nodes that own the network interfaces are down.

</dd> <dt>

<span id="ClusterNetworkDown"></span><span id="clusternetworkdown"></span><span id="CLUSTERNETWORKDOWN"></span>

<span id="ClusterNetworkDown"></span><span id="clusternetworkdown"></span><span id="CLUSTERNETWORKDOWN"></span>**ClusterNetworkDown** (1)


</dt> <dd>

The network is not operational; none of the **nodes** on the network can communicate.

</dd> <dt>

<span id="ClusterNetworkPartitioned"></span><span id="clusternetworkpartitioned"></span><span id="CLUSTERNETWORKPARTITIONED"></span>

<span id="ClusterNetworkPartitioned"></span><span id="clusternetworkpartitioned"></span><span id="CLUSTERNETWORKPARTITIONED"></span>**ClusterNetworkPartitioned** (2)


</dt> <dd>

The network is operational, but two or more nodes on the network cannot communicate. Typically a path-specific problem has occurred.

</dd> <dt>

<span id="ClusterNetworkUp"></span><span id="clusternetworkup"></span><span id="CLUSTERNETWORKUP"></span>

<span id="ClusterNetworkUp"></span><span id="clusternetworkup"></span><span id="CLUSTERNETWORKUP"></span>**ClusterNetworkUp** (3)


</dt> <dd>

The network is operational; all of the nodes in the cluster can communicate.

</dd> </dl>

## Remarks

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
| IID<br/>                      | IID\_ISClusNetwork is defined as F2E606F2-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[**GetClusterNetworkState**](getclusternetworkstate.md)
</dt> <dt>

[**ClusNetwork**](clusnetwork-object.md)
</dt> </dl>

 

 





