---
title: Cluster Registry Access Functions
description: Cluster registry access functions are called by Resource DLLs to directly access and update keys in the cluster database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2bb0650f-ef9c-40bb-ae90-229bfa23838e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Cluster Registry Access Functions

Cluster registry access functions are called by [Resource DLLs](resource-dlls.md) to directly access and update keys in the [cluster database](cluster-database.md).

> [!Note]  
> These functions should primarily be used by resource DLLs, so [*Cluster-aware applications*](https://www.bing.com/search?q=*Cluster-aware applications*) should avoid these functions whenever possible. For more information, see [standard order of preference](standard-order-of-preference.md).

 

## In this section

<dl> <dt>

[*ClusterRegBatchAddCommand*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_batch_add_command)
</dt> <dd>

Adds a command to a batch that will be executed on a cluster registry key.

</dd> <dt>

[*ClusterRegBatchCloseNotification*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_batch_close_notification)
</dt> <dd>

Frees the memory associated with the batch notification.

</dd> <dt>

[*ClusterRegBatchReadCommand*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_get_batch_notification)
</dt> <dd>

Reads a command from a batch notification.

</dd> <dt>

[*ClusterRegCloseBatch*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_batch)
</dt> <dd>

Executes or ignores the batch created by the [*ClusterRegCreateBatch*](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatebatch) function.

</dd> <dt>

[**ClusterRegCloseBatchEx**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregclosebatchex)
</dt> <dd>

Executes or ignores the batch created by the [**ClusterRegCreateBatch**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatebatch) function.

</dd> <dt>

[*ClusterRegCloseBatchNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_batch_notify_port)
</dt> <dd>

Closes a subscription to a batch notification port created by the [*ClusterRegCreateBatchNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_create_batch_notify_port) function.

</dd> <dt>

[**ClusterRegCloseKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregclosekey)
</dt> <dd>

Releases the handle of a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegCloseReadBatch*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_read_batch)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[*ClusterRegCloseReadBatchEx*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_read_batch_ex)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[**ClusterRegCloseReadBatchReply**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregclosereadbatchreply)
</dt> <dd>

Closes a read batch result handle and frees the memory associated with it.

</dd> <dt>

[**ClusterRegCreateBatch**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatebatch)
</dt> <dd>

Creates a batch that will execute commands on a cluster registry key.

</dd> <dt>

[*ClusterRegCreateBatchNotifyPort*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_create_batch_notify_port)
</dt> <dd>

Creates a subscription to a batch notification port.

</dd> <dt>

[**ClusterRegCreateKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatekey)
</dt> <dd>

Creates a specified [cluster database](cluster-database.md) key. If the key already exists in the database, [**ClusterRegCreateKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatekey) opens it without making changes.

</dd> <dt>

[**ClusterRegCreateReadBatch**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatereadbatch)
</dt> <dd>

Creates a handle to the read batch that executes read commands on the cluster registry key.

</dd> <dt>

[**ClusterRegDeleteKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregdeletekey)
</dt> <dd>

Deletes a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegDeleteValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregdeletevalue)
</dt> <dd>

Removes a named value from a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregenumkey)
</dt> <dd>

Enumerates the subkeys of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregenumvalue)
</dt> <dd>

Enumerates the values of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegGetBatchNotification**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterreggetbatchnotification)
</dt> <dd>

Fetches the batch notification.

</dd> <dt>

[**ClusterRegGetKeySecurity**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterreggetkeysecurity)
</dt> <dd>

Returns a copy of the security descriptor protecting the specified [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegOpenKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregopenkey)
</dt> <dd>

Opens an existing [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryInfoKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregqueryinfokey)
</dt> <dd>

Returns information about a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregqueryvalue)
</dt> <dd>

Returns the name, type, and data components associated with a value for an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegReadBatchAddCommand**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregreadbatchaddcommand)
</dt> <dd>

Adds a read command to a batch that executes on a cluster registry key.

</dd> <dt>

[**ClusterRegReadBatchReplyNextCommand**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregreadbatchreplynextcommand)
</dt> <dd>

Reads the next command from a read batch result.

</dd> <dt>

[**ClusterRegSetKeySecurity**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregsetkeysecurity)
</dt> <dd>

Sets the security attributes for a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegSetValue**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregsetvalue)
</dt> <dd>

Sets a value for a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegSyncDatabase*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_cluster_reg_sync_database)
</dt> <dd>

Synchronizes the [Cluster Database](cluster-database.md) with a cluster.

</dd> <dt>

[*ClusterSetAccountAccess*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_set_account_access)
</dt> <dd>

Updates an account access list (ACL) for a cluster.

</dd> <dt>

[**GetClusterGroupKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclustergroupkey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [group](groups.md).

</dd> <dt>

[**GetClusterKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusterkey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [cluster](https://www.bing.com/search?q=cluster).

</dd> <dt>

[**GetClusterNetInterfaceKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusternetinterfacekey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network interface](network-interfaces.md) object.

</dd> <dt>

[**GetClusterNetworkKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusternetworkkey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network](networks.md).

</dd> <dt>

[**GetClusterNodeKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusternodekey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [node](nodes.md).

</dd> <dt>

[**GetClusterResourceKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusterresourcekey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource](resources.md).

</dd> <dt>

[**GetClusterResourceTypeKey**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-getclusterresourcetypekey)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource type](resource-types.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Database Access Functions](cluster-database-access-functions.md)
</dt> <dt>

[Creating Resource Types](creating-resource-types.md)
</dt> </dl>

 

 




