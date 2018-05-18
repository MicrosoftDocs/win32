---
title: Cluster Registry Access Functions
description: Cluster registry access functions are called by Resource DLLs to directly access and update keys in the cluster database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2bb0650f-ef9c-40bb-ae90-229bfa23838e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# Cluster Registry Access Functions

Cluster registry access functions are called by [Resource DLLs](resource-dlls.md) to directly access and update keys in the [cluster database](cluster-database.md).

> [!Note]  
> These functions should primarily be used by resource DLLs, so [*Cluster-aware applications*](c-gly.md#-wolf-cluster-aware-application-gly) should avoid these functions whenever possible. For more information, see [standard order of preference](standard-order-of-preference.md).

 

## In this section

<dl> <dt>

[*ClusterRegBatchAddCommand*](clusterregbatchaddcommand.md)
</dt> <dd>

Adds a command to a batch that will be executed on a cluster registry key.

</dd> <dt>

[*ClusterRegBatchCloseNotification*](clusterregbatchclosenotification.md)
</dt> <dd>

Frees the memory associated with the batch notification.

</dd> <dt>

[*ClusterRegBatchReadCommand*](clusterregbatchreadcommand.md)
</dt> <dd>

Reads a command from a batch notification.

</dd> <dt>

[*ClusterRegCloseBatch*](clusterregclosebatch.md)
</dt> <dd>

Executes or ignores the batch created by the [*ClusterRegCreateBatch*](clusterregcreatebatch.md) function.

</dd> <dt>

[**ClusterRegCloseBatchEx**](clusterregclosebatchex.md)
</dt> <dd>

Executes or ignores the batch created by the [**ClusterRegCreateBatch**](clusterregcreatebatch.md) function.

</dd> <dt>

[*ClusterRegCloseBatchNotifyPort*](clusterregclosebatchnotifyport.md)
</dt> <dd>

Closes a subscription to a batch notification port created by the [*ClusterRegCreateBatchNotifyPort*](clusterregcreatebatchnotifyport.md) function.

</dd> <dt>

[**ClusterRegCloseKey**](clusterregclosekey.md)
</dt> <dd>

Releases the handle of a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegCloseReadBatch*](clusterregclosereadbatch.md)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[*ClusterRegCloseReadBatchEx*](clusterregclosereadbatchex.md)
</dt> <dd>

Executes a read batch and returns results from the read batch executions.

</dd> <dt>

[**ClusterRegCloseReadBatchReply**](clusterregclosereadbatchreply.md)
</dt> <dd>

Closes a read batch result handle and frees the memory associated with it.

</dd> <dt>

[**ClusterRegCreateBatch**](clusterregcreatebatch.md)
</dt> <dd>

Creates a batch that will execute commands on a cluster registry key.

</dd> <dt>

[*ClusterRegCreateBatchNotifyPort*](clusterregcreatebatchnotifyport.md)
</dt> <dd>

Creates a subscription to a batch notification port.

</dd> <dt>

[**ClusterRegCreateKey**](clusterregcreatekey.md)
</dt> <dd>

Creates a specified [cluster database](cluster-database.md) key. If the key already exists in the database, [**ClusterRegCreateKey**](clusterregcreatekey.md) opens it without making changes.

</dd> <dt>

[**ClusterRegCreateReadBatch**](clusterregcreatereadbatch.md)
</dt> <dd>

Creates a handle to the read batch that executes read commands on the cluster registry key.

</dd> <dt>

[**ClusterRegDeleteKey**](clusterregdeletekey.md)
</dt> <dd>

Deletes a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegDeleteValue**](clusterregdeletevalue.md)
</dt> <dd>

Removes a named value from a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumKey**](clusterregenumkey.md)
</dt> <dd>

Enumerates the subkeys of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegEnumValue**](clusterregenumvalue.md)
</dt> <dd>

Enumerates the values of an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegGetBatchNotification**](clusterreggetbatchnotification.md)
</dt> <dd>

Fetches the batch notification.

</dd> <dt>

[**ClusterRegGetKeySecurity**](clusterreggetkeysecurity.md)
</dt> <dd>

Returns a copy of the security descriptor protecting the specified [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegOpenKey**](clusterregopenkey.md)
</dt> <dd>

Opens an existing [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryInfoKey**](clusterregqueryinfokey.md)
</dt> <dd>

Returns information about a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegQueryValue**](clusterregqueryvalue.md)
</dt> <dd>

Returns the name, type, and data components associated with a value for an open [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegReadBatchAddCommand**](clusterregreadbatchaddcommand.md)
</dt> <dd>

Adds a read command to a batch that executes on a cluster registry key.

</dd> <dt>

[**ClusterRegReadBatchReplyNextCommand**](clusterregreadbatchreplynextcommand.md)
</dt> <dd>

Reads the next command from a read batch result.

</dd> <dt>

[**ClusterRegSetKeySecurity**](clusterregsetkeysecurity.md)
</dt> <dd>

Sets the security attributes for a [cluster database](cluster-database.md) key.

</dd> <dt>

[**ClusterRegSetValue**](clusterregsetvalue.md)
</dt> <dd>

Sets a value for a [cluster database](cluster-database.md) key.

</dd> <dt>

[*ClusterRegSyncDatabase*](clusterregsyncdatabase.md)
</dt> <dd>

Synchronizes the [Cluster Database](cluster-database.md) with a cluster.

</dd> <dt>

[*ClusterSetAccountAccess*](clustersetaccountaccess.md)
</dt> <dd>

Updates an account access list (ACL) for a cluster.

</dd> <dt>

[**GetClusterGroupKey**](getclustergroupkey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [group](groups.md).

</dd> <dt>

[**GetClusterKey**](getclusterkey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**GetClusterNetInterfaceKey**](getclusternetinterfacekey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network interface](network-interfaces.md) object.

</dd> <dt>

[**GetClusterNetworkKey**](getclusternetworkkey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [network](networks.md).

</dd> <dt>

[**GetClusterNodeKey**](getclusternodekey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [node](nodes.md).

</dd> <dt>

[**GetClusterResourceKey**](getclusterresourcekey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource](resources.md).

</dd> <dt>

[**GetClusterResourceTypeKey**](getclusterresourcetypekey.md)
</dt> <dd>

Opens the root of the [cluster database](cluster-database.md) subtree for a [resource type](resource-types.md).

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Database Access Functions](cluster-database-access-functions.md)
</dt> <dt>

[Creating Resource Types](creating-resource-types.md)
</dt> </dl>

 

 




