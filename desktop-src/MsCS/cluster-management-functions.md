---
title: Failover Cluster Management Functions
description: The failover cluster management functions manage cluster objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1b3a3b23-39db-47b7-b4a8-17fc1ee45df6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["failover cluster object management functions Failover Cluster ,failover cluster management functions", "failover cluster management functions Failover Cluster", "failover clusters Failover Cluster ,management functions", "cluster object management functions Failover Cluster ,cluster management functions", "cluster management functions Failover Cluster", "clusters Failover Cluster ,management functions"]
---

# Failover Cluster Management Functions

The failover cluster management functions manage [cluster objects](cluster-objects.md).

## In this section

<dl> <dt>

[*CloseCluster*](closecluster.md)
</dt> <dd>

Closes a cluster handle.

</dd> <dt>

[*CloseClusterNotifyPort*](closeclusternotifyport.md)
</dt> <dd>

Closes a notification port established through [*CreateClusterNotifyPort*](createclusternotifyport.md).

</dd> <dt>

[*ClusterCloseEnum*](clustercloseenum.md)
</dt> <dd>

Closes a cluster enumeration handle originally opened by [*ClusterOpenEnum*](clusteropenenum.md).

</dd> <dt>

[*ClusterCloseEnumEx*](clustercloseenumex.md)
</dt> <dd>

Closes a handle to an enumeration that was opened by the [*ClusterOpenEnumEx*](clusteropenenumex.md) function.

</dd> <dt>

[*ClusterEnum*](clusterenum.md)
</dt> <dd>

Enumerates the [cluster objects](cluster-objects.md) in a [cluster](c-gly.md#-wolf-cluster-gly), returning the name of one object with each call.

</dd> <dt>

[*ClusterEnumEx*](clusterenumex.md)
</dt> <dd>

Enumerates the objects in a cluster, and then gets the name and properties of the cluster object.

</dd> <dt>

[*ClusterGetEnumCount*](clustergetenumcount.md)
</dt> <dd>

Returns the number of [cluster objects](cluster-objects.md) associated with a [cluster](c-gly.md#-wolf-cluster-gly) enumeration handle.

</dd> <dt>

[*ClusterGetEnumCountEx*](clustergetenumcountex.md)
</dt> <dd>

Returns the number of cluster objects that are associated with a cluster enumeration handle.

</dd> <dt>

[*ClusterOpenEnum*](clusteropenenum.md)
</dt> <dd>

Opens an enumerator for iterating through [cluster objects](cluster-objects.md) in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*ClusterOpenEnumEx*](clusteropenenumex.md)
</dt> <dd>

Opens a handle to a cluster in order to iterate through its objects.

</dd> <dt>

[*ClusterSetupProgressCallback*](pcluster-setup-progress-callback.md)
</dt> <dd>

Callback function that receives regular updates on the progression of the setup of the cluster.

</dd> <dt>

[*ClusterUpgradeFunctionalLevel*](clusterupgradefunctionallevel.md)
</dt> <dd>

Initiates a rolling upgrade of the operating system on a cluster. **PCLUSAPI\_CLUSTER\_UPGRADE** defines a pointer to this function.

</dd> <dt>

[*ClusterUpgradeProgressCallback*](clusterupgradeprogresscallback.md)
</dt> <dd>

Retrieves status information for a rolling upgrade of the operating system on a cluster. **PCLUSTER\_UPGRADE\_PROGRESS\_CALLBACK** type defines a pointer to this function.

</dd> <dt>

[*CreateCluster*](createcluster.md)
</dt> <dd>

Creates and starts a cluster.

</dd> <dt>

[*CreateClusterCNOless*](createclustercnoless.md)
</dt> <dd>

Creates a cluster without [cluster name](network-name.md) and [IP Address](ip-address.md) resources. The allows you to create clusters that are domain joined but not managed by Active Directory, and clusters that are not members of a domain. **PCLUSAPI\_CREATE\_CLUSTER\_CNOLESS** defines a pointer to this function.

</dd> <dt>

[*CreateClusterNameAccount*](createclusternameaccount.md)
</dt> <dd>

Creates a [cluster name](network-name.md) resource and then uses it add a cluster to a domain, even if the machines that host the cluster aren't members of the domain.

</dd> <dt>

[*CreateClusterNotifyPort*](createclusternotifyport.md)
</dt> <dd>

Creates or modifies a notification port. For information on notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*CreateClusterNotifyPortV2*](createclusternotifyportv2.md)
</dt> <dd>

Creates or modifies a notification port. For information about notification ports, see [Receiving Cluster Events](receiving-cluster-events.md).

</dd> <dt>

[*DestroyCluster*](destroycluster.md)
</dt> <dd>

Removes a cluster.

</dd> <dt>

[*GetClusterInformation*](getclusterinformation.md)
</dt> <dd>

Retrieves a [cluster's](c-gly.md#-wolf-cluster-gly) name and version.

</dd> <dt>

[*GetClusterNotify*](getclusternotify.md)
</dt> <dd>

information relating to the next notification event that is stored for a notification port.

</dd> <dt>

[*GetClusterNotifyV2*](getclusternotifyv2.md)
</dt> <dd>

Retrieves information about the next notification event for a notification port.

</dd> <dt>

[*GetClusterQuorumResource*](getclusterquorumresource.md)
</dt> <dd>

Returns the name of a cluster's [quorum resource](quorum-resource.md).

</dd> <dt>

[*GetNotifyEventHandle*](getnotifyeventhandle.md)
</dt> <dd>

Retrieves a handle to a notification event.

</dd> <dt>

[*OpenCluster*](opencluster.md)
</dt> <dd>

Opens a connection to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to it.

</dd> <dt>

[*OpenClusterEx*](openclusterex.md)
</dt> <dd>

Opens a connection to a [cluster](c-gly.md#-wolf-cluster-gly) and returns a handle to it.

</dd> <dt>

[*RegisterClusterNotify*](registerclusternotify.md)
</dt> <dd>

Adds an event type to the list of events stored for a notification port.

</dd> <dt>

[*RegisterClusterNotifyV2*](registerclusternotifyv2.md)
</dt> <dd>

Registers an event type with a notification port by adding the notification key to the event type.

</dd> <dt>

[*SetClusterName*](setclustername.md)
</dt> <dd>

Sets the name for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*SetClusterQuorumResource*](setclusterquorumresource.md)
</dt> <dd>

Establishes a [resource](resources.md) as the [quorum resource](quorum-resource.md) for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[*SetClusterServiceAccountPassword*](setclusterserviceaccountpassword.md)
</dt> <dd>

Changes the password for the Cluster service user account on all available cluster nodes.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Object Management Functions](cluster-object-management-functions.md)
</dt> </dl>

 

 




