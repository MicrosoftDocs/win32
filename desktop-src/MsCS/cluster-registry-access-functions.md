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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster Registry Access Functions

Cluster registry access functions are called by [Resource DLLs](resource-dlls.md) to directly access and update keys in the [cluster database](cluster-database.md).

> [!Note]  
> These functions should primarily be used by resource DLLs, so [*Cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) should avoid these functions whenever possible. For more information, see [standard order of preference](standard-order-of-preference.md).

 

## In this section

<dl> <dt>

[*ClusterRegBatchAddCommand*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_batch_add_command?branch=master)
</dt> <dd>

Adds a command to a batch that will be executed on a cluster registry key.

</dd> <dt>

[*ClusterRegBatchCloseNotification*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_batch_close_notification?branch=master)
</dt> <dd>

Frees the memory associated with the batch notification.

</dd> <dt>

[*ClusterRegBatchReadCommand*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_get_batch_notification?branch=master)
</dt> <dd>

Reads a command from a batch notification.

</dd> <dt>

[*ClusterRegCloseBatch*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_close_batch?branch=master)
</dt> <dd>

Executes or ignores the batch created by the [*ClusterRegCreateBatch*](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatebatch?branch=master) function.

</dd> <dt>

[**ClusterRegCloseBatchEx**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregclosebatchex?branch=master)
</dt> <dd>

Executes or ignores the batch created by the [**ClusterRegCreateBatch**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatebatch?branch=master) function.

</dd> <dt>

[*ClusterRegCloseBatchNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_close_batch_notify_port?branch=master)
</dt> <dd>

Closes a subscription to a batch notification port created by the [*ClusterRegCreateBatchNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_create_batch_notify_port?branch=master) function.

</dd> <dt>

[**ClusterRegCloseKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregclosekey?branch=master)
</dt> <dd>

Releases the handle of a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegCloseReadBatch*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_close_read_batch?branch=master)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[*ClusterRegCloseReadBatchEx*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_close_read_batch_ex?branch=master)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[**ClusterRegCloseReadBatchReply**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregclosereadbatchreply?branch=master)
</dt> <dd>

Closes a read batch result handle and frees the memory associated with it.

</dd> <dt>

[**ClusterRegCreateBatch**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatebatch?branch=master)
</dt> <dd>

Creates a batch that will execute commands on a cluster registry key.

</dd> <dt>

[*ClusterRegCreateBatchNotifyPort*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_create_batch_notify_port?branch=master)
</dt> <dd>

Creates a subscription to a batch notification port.

</dd> <dt>

[**ClusterRegCreateKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatekey?branch=master)
</dt> <dd>

Creates a specified [cluster database](cluster-database.md) key. If the key already exists in the database, [**ClusterRegCreateKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatekey?branch=master) opens it without making changes.

</dd> <dt>

[**ClusterRegCreateReadBatch**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregcreatereadbatch?branch=master)
</dt> <dd>

Creates a handle to the read batch that executes read commands on the cluster registry key.

</dd> <dt>

[**ClusterRegDeleteKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregdeletekey?branch=master)
</dt> <dd>

Deletes a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegDeleteValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregdeletevalue?branch=master)
</dt> <dd>

Removes a named value from a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregenumkey?branch=master)
</dt> <dd>

Enumerates the subkeys of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregenumvalue?branch=master)
</dt> <dd>

Enumerates the values of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegGetBatchNotification**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterreggetbatchnotification?branch=master)
</dt> <dd>

Fetches the batch notification.

</dd> <dt>

[**ClusterRegGetKeySecurity**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterreggetkeysecurity?branch=master)
</dt> <dd>

Returns a copy of the security descriptor protecting the specified [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegOpenKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregopenkey?branch=master)
</dt> <dd>

Opens an existing [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryInfoKey**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregqueryinfokey?branch=master)
</dt> <dd>

Returns information about a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregqueryvalue?branch=master)
</dt> <dd>

Returns the name, type, and data components associated with a value for an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegReadBatchAddCommand**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregreadbatchaddcommand?branch=master)
</dt> <dd>

Adds a read command to a batch that executes on a cluster registry key.

</dd> <dt>

[**ClusterRegReadBatchReplyNextCommand**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregreadbatchreplynextcommand?branch=master)
</dt> <dd>

Reads the next command from a read batch result.

</dd> <dt>

[**ClusterRegSetKeySecurity**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregsetkeysecurity?branch=master)
</dt> <dd>

Sets the security attributes for a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegSetValue**](/windows/previous-versions/ClusAPI/nf-clusapi-clusterregsetvalue?branch=master)
</dt> <dd>

Sets a value for a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegSyncDatabase*](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_reg_sync_database?branch=master)
</dt> <dd>

Synchronizes the [Cluster Database](cluster-database.md) with a cluster.

</dd> <dt>

[*ClusterSetAccountAccess*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_set_account_access?branch=master)
</dt> <dd>

Updates an account access list (ACL) for a cluster.

</dd> <dt>

[**GetClusterGroupKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclustergroupkey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [group](groups.md).

</dd> <dt>

[**GetClusterKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusterkey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**GetClusterNetInterfaceKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusternetinterfacekey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network interface](network-interfaces.md) object.

</dd> <dt>

[**GetClusterNetworkKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusternetworkkey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network](networks.md).

</dd> <dt>

[**GetClusterNodeKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusternodekey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [node](nodes.md).

</dd> <dt>

[**GetClusterResourceKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusterresourcekey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource](resources.md).

</dd> <dt>

[**GetClusterResourceTypeKey**](/windows/previous-versions/ClusAPI/nf-clusapi-getclusterresourcetypekey?branch=master)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource type](resource-types.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Database Access Functions](cluster-database-access-functions.md)
</dt> <dt>

[Creating Resource Types](creating-resource-types.md)
</dt> </dl>

 

 




