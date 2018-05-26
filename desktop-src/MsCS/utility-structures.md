---
title: Utility Structures
description: The utility structures contain various information for the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 45da8dbc-dd70-4f95-b933-66d8e4340448
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- utility structures Failover Cluster
- structures Failover Cluster ,utility
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Utility Structures

The utility structures contain various information for the Failover Cluster API.

## In this section

<dl> <dt>

[**CLUS\_WORKER**](/windows/previous-versions/ResApi/ns-resapi-clus_worker?branch=master)
</dt> <dd>

Contains information about a worker thread.

</dd> <dt>

[**CLUSCTL\_GROUP\_GET\_LAST\_MOVE\_TIME\_OUTPUT**](/windows/previous-versions/ClusAPI/ns-clusapi-_clusctl_group_get_last_move_time_output?branch=master)
</dt> <dd>

Specifies information about the last time a group was moved to another node.

</dd> <dt>

[**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](/windows/previous-versions/ClusAPI/ns-clusapi-_clusctl_resource_state_change_reason_struct?branch=master)
</dt> <dd>

Sent with the [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control code to provide the reason for a [resource](resources.md) state change.

</dd> <dt>

[**CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX2\_INPUT**](/windows/previous-versions/ClusAPI/ns-clusapi-_clusctl_resource_type_storage_get_available_disks_ex2_input?branch=master)
</dt> <dd>

Represents an input buffer for the [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX2\_INT](clusctl-resource-type-storage-get-available-disks-ex2-int.md) control code.

</dd> <dt>

[**CLUSPROP\_BUFFER\_HELPER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_buffer_helper?branch=master)
</dt> <dd>

Used to build or parse a [property list](property-lists.md) or, a [value list](value-lists.md).

</dd> <dt>

[**CLUSPROP\_LIST**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_list?branch=master)
</dt> <dd>

Accesses the beginning of a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_BATCH\_COMMAND**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_batch_command?branch=master)
</dt> <dd>

Represents the order in which current batch command data is sent to the [**ClusterRegBatchReadCommand**](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_reg_get_batch_notification?branch=master) function.

</dd> <dt>

[**CLUSTER\_CREATE\_GROUP\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_create_group_info?branch=master)
</dt> <dd>

Allows the caller to provide additional properties when creating a new group.

</dd> <dt>

[**CLUSTER\_ENUM\_ITEM**](/windows/previous-versions/ClusApi/ns-clusapi-_cluster_enum_item?branch=master)
</dt> <dd>

Contains the properties of a cluster object. This structure is used to enumerate clusters in the [**ClusterEnumEx**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_enum_ex?branch=master) and [**ClusterNodeEnumEx**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum_ex?branch=master) functions.

</dd> <dt>

[**CLUSTER\_HEALTH\_FAULT**](/windows/previous-versions/Resapi/ns-resapi-_cluster_health_fault?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_HEALTH\_FAULT\_ARRAY**](/windows/previous-versions/Resapi/ns-resapi-_cluster_health_fault_array?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_GROUP\_ENUM\_ITEM**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_group_enum_item?branch=master)
</dt> <dd>

Contains the properties of a cluster group.

</dd> <dt>

[**CLUSTER\_IP\_ENTRY**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_ip_entry?branch=master)
</dt> <dd>

Describes an IP address for a cluster.

</dd> <dt>

[**CLUSTER\_MEMBERSHIP\_INFO**](/windows/previous-versions/ClusApi/ns-clusapi-_cluster_membership_info?branch=master)
</dt> <dd>

Represents membership information for a cluster.

</dd> <dt>

[**CLUSTER\_READ\_BATCH\_COMMAND**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_read_batch_command?branch=master)
</dt> <dd>

Represents a result for a single command in a read batch.

</dd> <dt>

[**CLUSTER\_RESOURCE\_ENUM\_ITEM**](/windows/previous-versions/ClusApi/ns-clusapi-_cluster_resource_enum_item?branch=master)
</dt> <dd>

Represents the properties of a cluster resource. This structure is used to enumerate cluster resources in the [**ClusterResourceEnumEx**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum_ex?branch=master) function.

</dd> <dt>

[**CLUSTER\_SET\_PASSWORD\_STATUS**](/windows/previous-versions/ClusAPI/ns-clusapi-cluster_set_password_status?branch=master)
</dt> <dd>

Used by the [**SetClusterServiceAccountPassword**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password?branch=master) function to return the results of a [Cluster service](cluster-service.md) user account password change for each cluster node.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE\_INFO**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_shared_volume_state_info?branch=master)
</dt> <dd>

Represents information about the state of a Cluster Shared Volume (CSV).

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE\_INFO\_EX**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_shared_volume_state_info_ex?branch=master)
</dt> <dd>

Represents information about the state of a Cluster Shared Volume (CSV).

</dd> <dt>

[**CLUSTER\_VALIDATE\_CSV\_FILENAME**](/windows/previous-versions/ClusApi/ns-clusapi-_cluster_validate_csv_filename?branch=master)
</dt> <dd>

Represents a cluster shared volume (CSV) during a validation operation.

</dd> <dt>

[**CLUSTER\_VALIDATE\_DIRECTORY**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_validate_directory?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_VALIDATE\_NETNAME**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_validate_netname?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_VALIDATE\_PATH**](/windows/previous-versions/ClusAPI/ns-clusapi-_cluster_validate_path?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTERVERSIONINFO**](/windows/previous-versions/ClusAPI/ns-clusapi-clusterversioninfo?branch=master)
</dt> <dd>

Describes information about the version of the [Cluster service](cluster-service.md) installed locally on a [node](nodes.md).

</dd> <dt>

[**CLUSTERVERSIONINFO\_NT4**](/windows/previous-versions/ClusAPI/ns-clusapi-clusterversioninfo_nt4?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CREATE\_CLUSTER\_CONFIG**](/windows/previous-versions/ClusAPI/ns-clusapi-_create_cluster_config?branch=master)
</dt> <dd>

Defines the initial cluster configuration.

</dd> <dt>

[**CREATE\_CLUSTER\_NAME\_ACCOUNT**](/windows/previous-versions/ClusAPI/ns-clusapi-_create_cluster_name_account?branch=master)
</dt> <dd>

Describes a [cluster name](network-name.md) resource and domain credentials used by the [**CreateClusterNameAccount**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_name_account?branch=master) function to add a cluster to a domain. **PCREATE\_CLUSTER\_NAME\_ACCOUNT** defines a pointer to this structure.

</dd> <dt>

[**FILESHARE\_CHANGE**](/windows/previous-versions/ClusAPI/ns-clusapi-_fileshare_change?branch=master)
</dt> <dd>

Describes the format for an entry in an event notification list.

</dd> <dt>

[**FILESHARE\_CHANGE\_LIST**](/windows/previous-versions/ClusAPI/ns-clusapi-_fileshare_change_list?branch=master)
</dt> <dd>

Describes an event notification list for file shares managed by the File Server [resource](resources.md).

</dd> <dt>

[**GROUP\_FAILURE\_INFO**](/windows/previous-versions/ClusApi/ns-clusapi-group_failure_info?branch=master)
</dt> <dd>

Represents information about the [Failover](failover.md) attempts for a group failure.

</dd> <dt>

[**GROUP\_FAILURE\_INFO\_BUFFER**](/windows/previous-versions/ClusApi/ns-clusapi-group_failure_info_buffer?branch=master)
</dt> <dd>

Represents a buffer for a [**GROUP\_FAILURE\_INFO**](/windows/previous-versions/ClusApi/ns-clusapi-group_failure_info?branch=master) structure.

</dd> <dt>

[**NOTIFY\_FILTER\_AND\_TYPE**](/windows/previous-versions/ClusApi/ns-clusapi-_notify_filter_and_type?branch=master)
</dt> <dd>

Represents a filter for a notification port that was created by the [**CreateClusterNotifyPortV2**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_create_cluster_notify_port_v2?branch=master) function. A filter specifies that a notification port accept notifications for the specified type of cluster object during the specified event.

</dd> <dt>

[**RESOURCE\_FAILURE\_INFO**](/windows/previous-versions/ClusApi/ns-clusapi-resource_failure_info?branch=master)
</dt> <dd>

Represents information about the [Failover](failover.md) attempts for a resource. This structure is used by the [**RESOURCE\_FAILURE\_INFO\_BUFFER**](/windows/previous-versions/ClusApi/ns-clusapi-resource_failure_info_buffer?branch=master) structure.

</dd> <dt>

[**RESOURCE\_FAILURE\_INFO\_BUFFER**](/windows/previous-versions/ClusApi/ns-clusapi-resource_failure_info_buffer?branch=master)
</dt> <dd>

Represents a buffer for a resource failure.

</dd> <dt>

[**RESOURCE\_TERMINAL\_FAILURE\_INFO\_BUFFER**](/windows/previous-versions/ClusApi/ns-clusapi-resource_terminal_failure_info_buffer?branch=master)
</dt> <dd>

Represents a buffer for a terminal failure for a resource.

</dd> <dt>

[**RESUTIL\_FILETIME\_DATA**](/windows/previous-versions/ResApi/ns-resapi-resutil_filetime_data?branch=master)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for a FILETIME.

</dd> <dt>

[**RESUTIL\_LARGEINT\_DATA**](/windows/previous-versions/ResApi/ns-resapi-resutil_largeint_data?branch=master)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for a signed large integer.

</dd> <dt>

[**RESUTIL\_PROPERTY\_ITEM**](/windows/previous-versions/ResApi/ns-resapi-resutil_property_item?branch=master)
</dt> <dd>

Contains information about a cluster object property. An array of [**RESUTIL\_PROPERTY\_ITEM**](/windows/previous-versions/ResApi/ns-resapi-resutil_property_item?branch=master) structures forms a [property table](property-tables.md) which can be used in property operations.

</dd> <dt>

[**RESUTIL\_ULARGEINT\_DATA**](/windows/previous-versions/ResApi/ns-resapi-resutil_ulargeint_data?branch=master)
</dt> <dd>

Describes the default, maximum, and minimum values allowed for an unsigned large integer.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster Structures](cluster-structures.md)
</dt> </dl>

 

 




