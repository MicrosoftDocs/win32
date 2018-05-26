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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Management Functions

The failover cluster management functions manage [cluster objects](cluster-objects.md).

## In this section

<dl> <dt>

[*CloseCluster*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster?branch=master)
</dt> <dd>

Closes a cluster handle.

</dd> <dt>

[*CloseClusterNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_close_cluster_notify_port?branch=master)
</dt> <dd>

Closes a notification port established through [*CreateClusterNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port?branch=master).

</dd> <dt>

[*ClusterCloseEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_close_enum?branch=master)
</dt> <dd>

Closes a cluster enumeration handle originally opened by [*ClusterOpenEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum?branch=master).

</dd> <dt>

[*ClusterCloseEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_close_enum_ex?branch=master)
</dt> <dd>

Closes a handle to an enumeration that was opened by the [*ClusterOpenEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum_ex?branch=master) function.

</dd> <dt>

[*ClusterEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_enum?branch=master)
</dt> <dd>

Enumerates the [cluster objects](cluster-objects.md) in a [cluster](c-gly.md#-wolf-cluster-gly), returning the name of one object with each call.

</dd> <dt>

[*ClusterEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_enum_ex?branch=master)
</dt> <dd>

Enumerates the objects in a cluster, and then gets the name and properties of the cluster object.

</dd> <dt>

[*ClusterGetEnumCount*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_get_enum_count?branch=master)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [cluster](c-gly.md#-wolf-cluster-gly) enumeration handle.

</dd> <dt>

[*ClusterGetEnumCountEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_get_enum_count_ex?branch=master)
</dt> <dd>

Returns the number of cluster objects that are associated with a cluster enumeration handle.

</dd> <dt>

[*ClusterOpenEnum*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum?branch=master)
</dt> <dd>

Opens an enumerator for iterating through [cluster objects](cluster-objects.md) in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*ClusterOpenEnumEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_open_enum_ex?branch=master)
</dt> <dd>

Opens a handle to a cluster in order to iterate through its objects.

</dd> <dt>

[*ClusterSetupProgressCallback*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_setup_progress_callback?branch=master)
</dt> <dd>

Callback function that receives regular updates on the progression of the setup of the cluster.

</dd> <dt>

[*ClusterUpgradeFunctionalLevel*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_upgrade?branch=master)
</dt> <dd>

Initiates a rolling upgrade of the operating system on a cluster. **PCLUSAPI\_CLUSTER\_UPGRADE** defines a pointer to this function.

</dd> <dt>

[*ClusterUpgradeProgressCallback*](/windows/previous-versions/clusapi/nc-clusapi-pcluster_upgrade_progress_callback?branch=master)
</dt> <dd>

Retrieves status information for a rolling upgrade of the operating system on a cluster. **PCLUSTER\_UPGRADE\_PROGRESS\_CALLBACK** type defines a pointer to this function.

</dd> <dt>

[*CreateCluster*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster?branch=master)
</dt> <dd>

Creates and starts a cluster.

</dd> <dt>

[*CreateClusterCNOless*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_cnoless?branch=master)
</dt> <dd>

Creates a cluster without [cluster name](network-name.md) and [IP Address](ip-address.md) resources. The allows you to create clusters that are domain joined but not managed by Active Directory, and clusters that are not members of a domain. **PCLUSAPI\_CREATE\_CLUSTER\_CNOLESS** defines a pointer to this function.

</dd> <dt>

[*CreateClusterNameAccount*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_name_account?branch=master)
</dt> <dd>

Creates a [cluster name](network-name.md) resource and then uses it add a cluster to a domain, even if the machines that host the cluster aren't members of the domain.

</dd> <dt>

[*CreateClusterNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port?branch=master)
</dt> <dd>

Creates or modifies a notification port. For information on notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*CreateClusterNotifyPortV2*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port_v2?branch=master)
</dt> <dd>

Creates or modifies a notification port. For information about notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*DestroyCluster*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_destroy_cluster?branch=master)
</dt> <dd>

Removes a cluster.

</dd> <dt>

[*GetClusterInformation*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_information?branch=master)
</dt> <dd>

Retrieves a [cluster's](c-gly.md#-wolf-cluster-gly) name and version.

</dd> <dt>

[*GetClusterNotify*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify?branch=master)
</dt> <dd>

information relating to the next notification event that is stored for a notification port.

</dd> <dt>

[*GetClusterNotifyV2*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_notify_v2?branch=master)
</dt> <dd>

Retrieves information about the next notification event for a notification port.

</dd> <dt>

[*GetClusterQuorumResource*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_cluster_quorum_resource?branch=master)
</dt> <dd>

Returns the name of a cluster's [quorum resource](quorum-resource.md).

</dd> <dt>

[*GetNotifyEventHandle*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_get_notify_event_handle_v2?branch=master)
</dt> <dd>

Retrieves a handle to a notification event.

</dd> <dt>

[*OpenCluster*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster?branch=master)
</dt> <dd>

Opens a connection to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to it.

</dd> <dt>

[*OpenClusterEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_open_cluster_ex?branch=master)
</dt> <dd>

Opens a connection to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to it.

</dd> <dt>

[*RegisterClusterNotify*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_register_cluster_notify?branch=master)
</dt> <dd>

Adds an event type to the list of events stored for a notification port.

</dd> <dt>

[*RegisterClusterNotifyV2*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_register_cluster_notify_v2?branch=master)
</dt> <dd>

Registers an event type with a notification port by adding the notification key to the event type.

</dd> <dt>

[*SetClusterName*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_setclustername?branch=master)
</dt> <dd>

Sets the name for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*SetClusterQuorumResource*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_quorum_resource?branch=master)
</dt> <dd>

Establishes a [resource](resources.md) as the [quorum resource](quorum-resource.md) for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*SetClusterServiceAccountPassword*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password?branch=master)
</dt> <dd>

Changes the password for the Cluster service user account on all available cluster nodes.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




