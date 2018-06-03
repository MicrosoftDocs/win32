---
title: ClusNetInterface.State property
description: State of a network interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3bc6bec3-bfe4-4ab4-8ad3-c42eba6d7cba
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- State property Failover Cluster
- State property Failover Cluster , ClusNetInterface object
- ClusNetInterface object Failover Cluster , State property
topic_type:
- apiref
api_name:
- ClusNetInterface.State
api_location:
- MsClus.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ClusNetInterface.State property

\[The **State** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns information about the state of a [network interface](network-interfaces.md).

This property is read-only.

## Syntax


```VB
ClusNetInterface.State
```



## Property value

**Long** representing the network interface's state with one of the following values enumerated by the [**CLUSTER\_NETINTERFACE\_STATE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_netinterface_state) enumeration.

<dt>

<span id="ClusterNetInterfaceStateUnknown"></span><span id="clusternetinterfacestateunknown"></span><span id="CLUSTERNETINTERFACESTATEUNKNOWN"></span>

<span id="ClusterNetInterfaceStateUnknown"></span><span id="clusternetinterfacestateunknown"></span><span id="CLUSTERNETINTERFACESTATEUNKNOWN"></span>**ClusterNetInterfaceStateUnknown** (-1)


</dt> <dd>

The **State** property has failed; the state of the network interface is unknown.

</dd> <dt>

<span id="ClusterNetInterfaceUnavailable"></span><span id="clusternetinterfaceunavailable"></span><span id="CLUSTERNETINTERFACEUNAVAILABLE"></span>

<span id="ClusterNetInterfaceUnavailable"></span><span id="clusternetinterfaceunavailable"></span><span id="CLUSTERNETINTERFACEUNAVAILABLE"></span>**ClusterNetInterfaceUnavailable** (0)


</dt> <dd>

The node that owns the network interface is down.

</dd> <dt>

<span id="ClusterNetInterfaceFailed"></span><span id="clusternetinterfacefailed"></span><span id="CLUSTERNETINTERFACEFAILED"></span>

<span id="ClusterNetInterfaceFailed"></span><span id="clusternetinterfacefailed"></span><span id="CLUSTERNETINTERFACEFAILED"></span>**ClusterNetInterfaceFailed** (1)


</dt> <dd>

The network interface cannot communicate with any other network interface.

</dd> <dt>

<span id="ClusterNetInterfaceUnreachable"></span><span id="clusternetinterfaceunreachable"></span><span id="CLUSTERNETINTERFACEUNREACHABLE"></span>

<span id="ClusterNetInterfaceUnreachable"></span><span id="clusternetinterfaceunreachable"></span><span id="CLUSTERNETINTERFACEUNREACHABLE"></span>**ClusterNetInterfaceUnreachable** (2)


</dt> <dd>

The network interface cannot communicate with at least one other network interface whose state is not **ClusterNetInterfaceFailed** or **ClusterNetInterfaceUnavailable**.

</dd> <dt>

<span id="ClusterNetInterfaceUp"></span><span id="clusternetinterfaceup"></span><span id="CLUSTERNETINTERFACEUP"></span>

<span id="ClusterNetInterfaceUp"></span><span id="clusternetinterfaceup"></span><span id="CLUSTERNETINTERFACEUP"></span>**ClusterNetInterfaceUp** (3)


</dt> <dd>

The network interface can communicate with all other network interfaces whose state is not **ClusterNetInterfaceFailed** or **ClusterNetInterfaceUnavailable**.

</dd> </dl>

## Remarks

For information on making constants defined by the Cluster Automation Server type library (MsClus.tlb) available to scripts, see [Creating a Cluster Automation Server Script](creating-a-cluster-automation-server-script.md).

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusNetInterface is defined as F2E606EE-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusNetInterface**](clusnetinterface-object.md)
</dt> <dt>

[**CLUSTER\_NETINTERFACE\_STATE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_netinterface_state)
</dt> <dt>

[**GetClusterNetInterfaceState**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface_state)
</dt> </dl>

 

 





