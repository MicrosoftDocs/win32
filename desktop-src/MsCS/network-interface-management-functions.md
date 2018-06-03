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
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Network Interface Management Functions

The network interface management functions manage [network interfaces](network-interfaces.md).

## In this section

<dl> <dt>

[*CloseClusterNetInterface*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_net_interface)
</dt> <dd>

Closes a [network interface](network-interfaces.md) handle.

</dd> <dt>

[**ClusterNetInterfaceCloseEnum**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfacecloseenum)
</dt> <dd>

Closes a network interface enumeration handle.

</dd> <dt>

[**ClusterNetInterfaceEnum**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfaceenum)
</dt> <dd>

Enumerates the [network interfaces](network-interfaces.md) installed on a cluster, returning one name with each call.

</dd> <dt>

[**ClusterNetInterfaceOpenEnum**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusternetinterfaceopenenum)
</dt> <dd>

Opens an enumerator for iterating through the installed [network interfaces](network-interfaces.md).

</dd> <dt>

[*GetClusterFromNetInterface*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_from_net_interface)
</dt> <dd>

Returns a handle to the [cluster](https://www.bing.com/search?q=cluster) associated with a [network interface](network-interfaces.md).

</dd> <dt>

[*GetClusterNetInterface*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface)
</dt> <dd>

Returns the name of a [node's](nodes.md) interface to a [network](networks.md) in a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*GetClusterNetInterfaceState*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_net_interface_state)
</dt> <dd>

Returns the current state of a [network interface](network-interfaces.md).

</dd> <dt>

[*OpenClusterNetInterface*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_net_interface)
</dt> <dd>

Opens a handle to a [network interface](network-interfaces.md).

</dd> <dt>

[*OpenClusterNetInterfaceEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_netinterface_ex)
</dt> <dd>

Opens a handle to a [network interface](network-interfaces.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




