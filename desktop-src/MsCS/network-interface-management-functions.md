---
title: Network Interface Management Functions
description: The network interface management functions manage network interfaces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 63602522-6425-4c3f-b80f-32ee2c3d6469
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster object management functions Failover Cluster ,network interface management functions
- failover cluster object management functions Failover Cluster ,network interface management functions
- network interface management functions Failover Cluster
- network interfaces Failover Cluster ,management functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Network Interface Management Functions

The network interface management functions manage [network interfaces](network-interfaces.md).

## In this section

<dl> <dt>

[*CloseClusterNetInterface*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_net_interface?branch=master)
</dt> <dd>

Closes a [network interface](network-interfaces.md) handle.

</dd> <dt>

[**ClusterNetInterfaceCloseEnum**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfacecloseenum?branch=master)
</dt> <dd>

Closes a network interface enumeration handle.

</dd> <dt>

[**ClusterNetInterfaceEnum**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfaceenum?branch=master)
</dt> <dd>

Enumerates the [network interfaces](network-interfaces.md) installed on a cluster, returning one name with each call.

</dd> <dt>

[**ClusterNetInterfaceOpenEnum**](/windows/previous-versions/ClusAPI/nf-clusapi-clusternetinterfaceopenenum?branch=master)
</dt> <dd>

Opens an enumerator for iterating through the installed [network interfaces](network-interfaces.md).

</dd> <dt>

[*GetClusterFromNetInterface*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_net_interface?branch=master)
</dt> <dd>

Returns a handle to the [cluster](c-gly.md#-wolf-cluster-gly) associated with a [network interface](network-interfaces.md).

</dd> <dt>

[*GetClusterNetInterface*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface?branch=master)
</dt> <dd>

Returns the name of a [node's](nodes.md) interface to a [network](networks.md) in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*GetClusterNetInterfaceState*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface_state?branch=master)
</dt> <dd>

Returns the current state of a [network interface](network-interfaces.md).

</dd> <dt>

[*OpenClusterNetInterface*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_net_interface?branch=master)
</dt> <dd>

Opens a handle to a [network interface](network-interfaces.md).

</dd> <dt>

[*OpenClusterNetInterfaceEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_netinterface_ex?branch=master)
</dt> <dd>

Opens a handle to a [network interface](network-interfaces.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




