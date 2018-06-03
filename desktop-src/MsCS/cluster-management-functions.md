---
title: Failover Cluster Management Functions
description: The failover cluster management functions manage cluster objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1b3a3b23-39db-47b7-b4a8-17fc1ee45df6
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- failover cluster object management functions Failover Cluster ,failover cluster management functions
- failover cluster management functions Failover Cluster
- failover clusters Failover Cluster ,management functions
- cluster object management functions Failover Cluster ,cluster management functions
- cluster management functions Failover Cluster
- clusters Failover Cluster ,management functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Failover Cluster Management Functions

The failover cluster management functions manage [cluster objects](cluster-objects.md).

## In this section

<dl> <dt>

[*CloseCluster*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster)
</dt> <dd>

Closes a cluster handle.

</dd> <dt>

[*CloseClusterNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_close_cluster_notify_port)
</dt> <dd>

Closes a notification port established through [*CreateClusterNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port).

</dd> <dt>

[*ClusterCloseEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_close_enum)
</dt> <dd>

Closes a cluster enumeration handle originally opened by [*ClusterOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum).

</dd> <dt>

[*ClusterCloseEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_close_enum_ex)
</dt> <dd>

Closes a handle to an enumeration that was opened by the [*ClusterOpenEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum_ex) function.

</dd> <dt>

[*ClusterEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum)
</dt> <dd>

Enumerates the [cluster objects](cluster-objects.md) in a [cluster](https://www.bing.com/search?q=cluster), returning the name of one object with each call.

</dd> <dt>

[*ClusterEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_enum_ex)
</dt> <dd>

Enumerates the objects in a cluster, and then gets the name and properties of the cluster object.

</dd> <dt>

[*ClusterGetEnumCount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_get_enum_count)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [cluster](https://www.bing.com/search?q=cluster) enumeration handle.

</dd> <dt>

[*ClusterGetEnumCountEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_get_enum_count_ex)
</dt> <dd>

Returns the number of cluster objects that are associated with a cluster enumeration handle.

</dd> <dt>

[*ClusterOpenEnum*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum)
</dt> <dd>

Opens an enumerator for iterating through [cluster objects](cluster-objects.md) in a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*ClusterOpenEnumEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum_ex)
</dt> <dd>

Opens a handle to a cluster in order to iterate through its objects.

</dd> <dt>

[*ClusterSetupProgressCallback*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_setup_progress_callback)
</dt> <dd>

Callback function that receives regular updates on the progression of the setup of the cluster.

</dd> <dt>

[*ClusterUpgradeFunctionalLevel*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_upgrade)
</dt> <dd>

Initiates a rolling upgrade of the operating system on a cluster. **PCLUSAPI\_CLUSTER\_UPGRADE** defines a pointer to this function.

</dd> <dt>

[*ClusterUpgradeProgressCallback*](/previous-versions/windows/desktop/api/clusapi/nc-clusapi-pcluster_upgrade_progress_callback)
</dt> <dd>

Retrieves status information for a rolling upgrade of the operating system on a cluster. **PCLUSTER\_UPGRADE\_PROGRESS\_CALLBACK** type defines a pointer to this function.

</dd> <dt>

[*CreateCluster*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster)
</dt> <dd>

Creates and starts a cluster.

</dd> <dt>

[*CreateClusterCNOless*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_cnoless)
</dt> <dd>

Creates a cluster without [cluster name](network-name.md) and [IP Address](ip-address.md) resources. The allows you to create clusters that are domain joined but not managed by Active Directory, and clusters that are not members of a domain. **PCLUSAPI\_CREATE\_CLUSTER\_CNOLESS** defines a pointer to this function.

</dd> <dt>

[*CreateClusterNameAccount*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_name_account)
</dt> <dd>

Creates a [cluster name](network-name.md) resource and then uses it add a cluster to a domain, even if the machines that host the cluster aren't members of the domain.

</dd> <dt>

[*CreateClusterNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port)
</dt> <dd>

Creates or modifies a notification port. For information on notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*CreateClusterNotifyPortV2*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port_v2)
</dt> <dd>

Creates or modifies a notification port. For information about notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*DestroyCluster*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_destroy_cluster)
</dt> <dd>

Removes a cluster.

</dd> <dt>

[*GetClusterInformation*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_information)
</dt> <dd>

Retrieves a [cluster's](https://www.bing.com/search?q=cluster's) name and version.

</dd> <dt>

[*GetClusterNotify*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify)
</dt> <dd>

information relating to the next notification event that is stored for a notification port.

</dd> <dt>

[*GetClusterNotifyV2*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify_v2)
</dt> <dd>

Retrieves information about the next notification event for a notification port.

</dd> <dt>

[*GetClusterQuorumResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_quorum_resource)
</dt> <dd>

Returns the name of a cluster's [quorum resource](quorum-resource.md).

</dd> <dt>

[*GetNotifyEventHandle*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_notify_event_handle_v2)
</dt> <dd>

Retrieves a handle to a notification event.

</dd> <dt>

[*OpenCluster*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster)
</dt> <dd>

Opens a connection to a [cluster](https://www.bing.com/search?q=cluster) and returns a handle to it.

</dd> <dt>

[*OpenClusterEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_open_cluster_ex)
</dt> <dd>

Opens a connection to a [cluster](https://www.bing.com/search?q=cluster) and returns a handle to it.

</dd> <dt>

[*RegisterClusterNotify*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_register_cluster_notify)
</dt> <dd>

Adds an event type to the list of events stored for a notification port.

</dd> <dt>

[*RegisterClusterNotifyV2*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_register_cluster_notify_v2)
</dt> <dd>

Registers an event type with a notification port by adding the notification key to the event type.

</dd> <dt>

[*SetClusterName*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_setclustername)
</dt> <dd>

Sets the name for a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*SetClusterQuorumResource*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_quorum_resource)
</dt> <dd>

Establishes a [resource](resources.md) as the [quorum resource](quorum-resource.md) for a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[*SetClusterServiceAccountPassword*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password)
</dt> <dd>

Changes the password for the Cluster service user account on all available cluster nodes.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




