---
title: Utility Structures
description: The utility structures contain various information for the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '45da8dbc-dd70-4f95-b933-66d8e4340448'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["utility structures Failover Cluster", "structures Failover Cluster ,utility"]
---

# Utility Structures

The utility structures contain various information for the Failover Cluster API.

## In this section

<dl> <dt>

[**CLUS\_WORKER**](clus-worker.md)
</dt> <dd>

Contains information about a worker thread.

</dd> <dt>

[**CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME\_OUTPUT**](clusctl-group-get-last-move-time-output.md)
</dt> <dd>

Specifies information about the last time a group was moved to another node.

</dd> <dt>

[**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](clusctl-resource-state-change-reason-struct.md)
</dt> <dd>

Sent with the [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control code to provide the reason for a [resource](resources.md) state change.

</dd> <dt>

[**CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX2\_INPUT**](clusctl-resource-type-storage-get-available-disks-ex2-input.md)
</dt> <dd>

Represents an input buffer for the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX2\_INT](clusctl-resource-type-storage-get-available-disks-ex2-int.md) control code.

</dd> <dt>

[**CLUSPROP\_BUFFER\_HELPER**](clusprop-buffer-helper.md)
</dt> <dd>

Used to build or parse a [property list](property-lists.md) or, a [value list](value-lists.md).

</dd> <dt>

[**CLUSPROP\_LIST**](clusprop-list.md)
</dt> <dd>

Accesses the beginning of a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_BATCH\_COMMAND**](cluster-batch-command.md)
</dt> <dd>

Represents the order in which current batch command data is sent to the [**ClusterRegBatchReadCommand**](clusterregbatchreadcommand.md) function.

</dd> <dt>

[**CLUSTER\_CREATE\_GROUP\_INFO**](cluster-create-group-info.md)
</dt> <dd>

Allows the caller to provide additional properties when creating a new group.

</dd> <dt>

[**CLUSTER\_ENUM\_ITEM**](cluster-enum-item.md)
</dt> <dd>

Contains the properties of a cluster object. This structure is used to enumerate clusters in the [**ClusterEnumEx**](clusterenumex.md) and [**ClusterNodeEnumEx**](clusternodeenumex.md) functions.

</dd> <dt>

[**CLUSTER\_HEALTH\_FAULT**](cluster-health-fault.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_HEALTH\_FAULT\_ARRAY**](cluster-health-fault-array.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_GROUP\_ENUM\_ITEM**](cluster-group-enum-item.md)
</dt> <dd>

Contains the properties of a cluster group.

</dd> <dt>

[**CLUSTER\_IP\_ENTRY**](cluster-ip-entry.md)
</dt> <dd>

Describes an IP address for a cluster.

</dd> <dt>

[**CLUSTER\_MEMBERSHIP\_INFO**](cluster-membership-info.md)
</dt> <dd>

Represents membership information for a cluster.

</dd> <dt>

[**CLUSTER\_READ\_BATCH\_COMMAND**](cluster-read-batch-command.md)
</dt> <dd>

Represents a result for a single command in a read batch.

</dd> <dt>

[**CLUSTER\_RESOURCE\_ENUM\_ITEM**](cluster-resource-enum-item.md)
</dt> <dd>

Represents the properties of a cluster resource. This structure is used to enumerate cluster resources in the [**ClusterResourceEnumEx**](clusterresourceenumex.md) function.

</dd> <dt>

[**CLUSTER\_SET\_PASSWORD\_STATUS**](cluster-set-password-status.md)
</dt> <dd>

Used by the [**SetClusterServiceAccountPassword**](setclusterserviceaccountpassword.md) function to return the results of a [Cluster service](cluster-service.md) user account password change for each cluster node.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE\_INFO**](cluster-shared-volume-state-info.md)
</dt> <dd>

Represents information about the state of a Cluster Shared Volume (CSV).

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE\_INFO\_EX**](cluster-shared-volume-state-info-ex.md)
</dt> <dd>

Represents information about the state of a Cluster Shared Volume (CSV).

</dd> <dt>

[**CLUSTER\_VALIDATE\_CSV\_FILENAME**](cluster-validate-csv-filename.md)
</dt> <dd>

Represents a cluster shared volume (CSV) during a validation operation.

</dd> <dt>

[**CLUSTER\_VALIDATE\_DIRECTORY**](cluster-validate-directory.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_VALIDATE\_NETNAME**](cluster-validate-netname.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_VALIDATE\_PATH**](cluster-validate-path.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTERVERSIONINFO**](clusterversioninfo.md)
</dt> <dd>

Describes information about the version of the [Cluster service](cluster-service.md) installed locally on a [node](nodes.md).

</dd> <dt>

[**CLUSTERVERSIONINFO\_NT4**](clusterversioninfo-nt4.md)
</dt> <dd>

TBD

</dd> <dt>

[**CREATE\_CLUSTER\_CONFIG**](create-cluster-config.md)
</dt> <dd>

Defines the initial cluster configuration.

</dd> <dt>

[**CREATE\_CLUSTER\_NAME\_ACCOUNT**](create-cluster-name-account.md)
</dt> <dd>

Describes a [cluster name](network-name.md) resource and domain credentials used by the [**CreateClusterNameAccount**](createclusternameaccount.md) function to add a cluster to a domain. **PCREATE\_CLUSTER\_NAME\_ACCOUNT** defines a pointer to this structure.

</dd> <dt>

[**FILESHARE\_CHANGE**](fileshare-change.md)
</dt> <dd>

Describes the format for an entry in an event notification list.

</dd> <dt>

[**FILESHARE\_CHANGE\_LIST**](fileshare-change-list.md)
</dt> <dd>

Describes an event notification list for file shares managed by the File Server [resource](resources.md).

</dd> <dt>

[**GROUP\_FAILURE\_INFO**](group-failure-info.md)
</dt> <dd>

Represents information about the [Failover](failover.md) attempts for a group failure.

</dd> <dt>

[**GROUP\_FAILURE\_INFO\_BUFFER**](group-failure-info-buffer.md)
</dt> <dd>

Represents a buffer for a [**GROUP\_FAILURE\_INFO**](group-failure-info.md) structure.

</dd> <dt>

[**NOTIFY\_FILTER\_AND\_TYPE**](notify-filter-and-type.md)
</dt> <dd>

Represents a filter for a notification port that was created by the [**CreateClusterNotifyPortV2**](createclusternotifyportv2.md) function. A filter specifies that a notification port accept notifications for the specified type of cluster object during the specified event.

</dd> <dt>

[**RESOURCE\_FAILURE\_INFO**](resource-failure-info.md)
</dt> <dd>

Represents information about the [Failover](failover.md) attempts for a resource. This structure is used by the [**RESOURCE\_FAILURE\_INFO\_BUFFER**](resource-failure-info-buffer.md) structure.

</dd> <dt>

[**RESOURCE\_FAILURE\_INFO\_BUFFER**](resource-failure-info-buffer.md)
</dt> <dd>

Represents a buffer for a resource failure.

</dd> <dt>

[**RESOURCE\_TERMINAL\_FAILURE\_INFO\_BUFFER**](resource-terminal-failure-info-buffer.md)
</dt> <dd>

Represents a buffer for a terminal failure for a resource.

</dd> <dt>

[**RESUTIL\_FILETIME\_DATA**](resutil-filetime-data.md)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for a FILETIME.

</dd> <dt>

[**RESUTIL\_LARGEINT\_DATA**](resutil-largeint-data.md)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for a signed large integer.

</dd> <dt>

[**RESUTIL\_PROPERTY\_ITEM**](resutil-property-item.md)
</dt> <dd>

Contains information about a cluster object property. An array of [**RESUTIL\_PROPERTY\_ITEM**](resutil-property-item.md) structures forms a [property table](property-tables.md) which can be used in property operations.

</dd> <dt>

[**RESUTIL\_ULARGEINT\_DATA**](resutil-ulargeint-data.md)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for an unsigned large integer.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




