---
title: Failover Cluster Enumerations
description: This section contains the enumerations of the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 546071de-1067-4b47-b862-668be976e563
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Failover Cluster Enumerations

This section contains the enumerations of the Failover Cluster API.

## In this section

<dl> <dt>

[**CLCTL\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clctl_codes?branch=master)
</dt> <dd>

enumerates the possible operations that a control code will perform.

</dd> <dt>

[**CLUS\_CHARACTERISTICS**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_characteristics?branch=master)
</dt> <dd>

Enumerates characteristics of resource types and resources.

</dd> <dt>

[**CLUS\_FLAGS**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_flags?branch=master)
</dt> <dd>

Identifies the resource or group as a [core resource](core-resources.md).

</dd> <dt>

[**CLUS\_GROUP\_START\_SETTING**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_group_start_setting?branch=master)
</dt> <dd>

Enumerates the start settings for a cluster group.

</dd> <dt>

[**CLUS\_RESSUBCLASS**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_ressubclass?branch=master)
</dt> <dd>

Identifies a resource subclass that manages a shared resource.

</dd> <dt>

[**CLUS\_RESSUBCLASS\_NETWORK**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_ressubclass_network?branch=master)
</dt> <dd>

Identifies a resource subclass that manages an IP address provider.

</dd> <dt>

[**CLUS\_RESSUBCLASS\_STORAGE**](/windows/previous-versions/ClusAPI/ne-clusapi-clus_ressubclass_storage?branch=master)
</dt> <dd>

Identifies a resource subclass that manages a shared bus.

</dd> <dt>

[**CLUSCTL\_CLUSTER\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_cluster_codes?branch=master)
</dt> <dd>

Enumerates cluster [control codes](about-control-codes.md) used by the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function.

</dd> <dt>

[**CLUSCTL\_GROUP\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_group_codes?branch=master)
</dt> <dd>

Enumerates [group](groups.md)[control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_GROUPSET\_CODES**](/windows/previous-versions/msclus/ne-clusapi-clusctl_groupset_codes?branch=master)
</dt> <dd>

Enumerates groupset [control codes](about-control-codes.md) used by the [**ClusterGroupSetControl**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_groupset_control?branch=master) function.

</dd> <dt>

[**CLUSCTL\_NETINTERFACE\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_netinterface_codes?branch=master)
</dt> <dd>

Enumerates Network Interface [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_NETWORK\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_network_codes?branch=master)
</dt> <dd>

Enumerates [network](networks.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_NODE\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_node_codes?branch=master)
</dt> <dd>

Enumerates [node](nodes.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_RESOURCE\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_resource_codes?branch=master)
</dt> <dd>

Enumerates [resource](resources.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_RESOURCE\_TYPE\_CODES**](/windows/previous-versions/ClusAPI/ne-clusapi-clusctl_resource_type_codes?branch=master)
</dt> <dd>

Enumerates [resource type](resource-types.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSGROUP\_TYPE**](/windows/previous-versions/ClusApi/ne-clusapi-clusgroup_type?branch=master)
</dt> <dd>

Specifies the type of cluster group to create.

</dd> <dt>

[**CLUSPROP\_IPADDR\_ENABLENETBIOS**](/windows/previous-versions/ClusAPI/ne-clusapi-clusprop_ipaddr_enablenetbios?branch=master)
</dt> <dd>

When used with the [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) structure, enables or disables the functionality of the [**EnableNetBIOS**](ip-addresses-enablenetbios.md) property of [IP Address](ip-address.md) [resources](resources.md).

</dd> <dt>

[**CLUSPROP\_PIFLAGS**](/windows/previous-versions/ClusAPI/ne-clusapi-clusprop_piflags?branch=master)
</dt> <dd>

Represents disk partition information. The enumeration flags identify certain properties of a disk partition, which is a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[**CLUSTER\_CHANGE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change?branch=master)
</dt> <dd>

Describes the type of notification returned.

</dd> <dt>

[**CLUSTER\_CHANGE\_CLUSTER\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_cluster_v2?branch=master)
</dt> <dd>

Defines the list of notifications that are generated for a cluster.

</dd> <dt>

[**CLUSTER\_CHANGE\_GROUP\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_group_v2?branch=master)
</dt> <dd>

Defines the list of notifications that are generated for a group.

</dd> <dt>

[**CLUSTER\_CHANGE\_GROUPSET\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_groupset_v2?branch=master)
</dt> <dd>

Defines the list of notifications that are generated for a groupset.

</dd> <dt>

[**CLUSTER\_CHANGE\_NETINTERFACE\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_netinterface_v2?branch=master)
</dt> <dd>

Defines the set of notifications that are generated for a cluster network interface.

</dd> <dt>

[**CLUSTER\_CHANGE\_NETWORK\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_network_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for a cluster network.

</dd> <dt>

[**CLUSTER\_CHANGE\_NODE\_UPGRADE\_PHASE\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_node_upgrade_phase_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for the upgrade of a cluster node.

</dd> <dt>

[**CLUSTER\_CHANGE\_NODE\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_node_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for a cluster node.

</dd> <dt>

[**CLUSTER\_CHANGE\_QUORUM\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_quorum_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for quorum-specific information.

</dd> <dt>

[**CLUSTER\_CHANGE\_REGISTRY\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_registry_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for a registry key.

</dd> <dt>

[**CLUSTER\_CHANGE\_RESOURCE\_TYPE\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_resource_type_v2?branch=master)
</dt> <dd>

Defines the set of notifications that are generated for a resource type.

</dd> <dt>

[**CLUSTER\_CHANGE\_RESOURCE\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_resource_v2?branch=master)
</dt> <dd>

Defines the list of notifications that are generated for a resource.

</dd> <dt>

[**CLUSTER\_CHANGE\_SHARED\_VOLUME\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_shared_volume_v2?branch=master)
</dt> <dd>

Defines the notifications that are generated for a cluster shared volume.

</dd> <dt>

[**CLUSTER\_CHANGE\_SPACEPORT\_V2**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_change_spaceport_v2?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_CONTROL\_OBJECT**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_control_object?branch=master)
</dt> <dd>

The 8-bit object component of a control code that indicates the type of cluster object to which the control code applies. For more information, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSTER\_CSV\_VOLUME\_FAULT\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_csv_volume_fault_state?branch=master)
</dt> <dd>

Defines the various fault states for a cluster shared volume (CSV).

</dd> <dt>

[**CLUSTER\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_enum?branch=master)
</dt> <dd>

Describes the type of cluster objects being enumerated.

</dd> <dt>

[**CLUSTER\_GROUP\_AUTOFAILBACK\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_group_autofailback_type?branch=master)
</dt> <dd>

Used by the [**AutoFailbackType**](groups-autofailbacktype.md) group [common property](common-properties.md) to specify whether the group should be failed back to the [node](nodes.md) identified as its preferred owner when that node comes back online following a [failover](failover.md).

</dd> <dt>

[**CLUSTER\_GROUP\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_group_enum?branch=master)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterGroupEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_enum?branch=master) and [**ClusterGroupOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_group_open_enum?branch=master) functions.

</dd> <dt>

[**CLUSTER\_GROUP\_PRIORITY**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_group_priority?branch=master)
</dt> <dd>

Specifies the priority level of a group.

</dd> <dt>

[**CLUSTER\_GROUP\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_group_state?branch=master)
</dt> <dd>

Enumerates the possible states of a [group](groups.md).

</dd> <dt>

[**CLUSTER\_MGMT\_POINT\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_mgmt_point_type?branch=master)
</dt> <dd>

Specifies the type of the management point for the cluster.

</dd> <dt>

[**CLUSTER\_NETINTERFACE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_netinterface_state?branch=master)
</dt> <dd>

Enumerates the possible values of the state of a [network interface](network-interfaces.md).

</dd> <dt>

[**CLUSTER\_NETWORK\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_network_enum?branch=master)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterNetworkEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_network_enum?branch=master) and [**ClusterNetworkOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_network_open_enum?branch=master) functions.

</dd> <dt>

[**CLUSTER\_NETWORK\_ROLE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_network_role?branch=master)
</dt> <dd>

Describes the role a [network](networks.md) plays in the [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**CLUSTER\_NETWORK\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_network_state?branch=master)
</dt> <dd>

Enumerates the possible values of the state of a [network](networks.md).

</dd> <dt>

[**CLUSTER\_NODE\_DRAIN\_STATUS**](/windows/previous-versions/ClusApi/ne-clusapi-cluster_node_drain_status?branch=master)
</dt> <dd>

Enumerates the possible values of the status of a node drain.

</dd> <dt>

[**CLUSTER\_NODE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_node_enum?branch=master)
</dt> <dd>

Describes the types of cluster objects that are enumerated by the [**ClusterNodeEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_enum?branch=master) and [**ClusterNodeOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_node_open_enum?branch=master) functions.

</dd> <dt>

[**CLUSTER\_NODE\_RESUME\_FAILBACK\_TYPE**](/windows/previous-versions/ClusApi/ne-clusapi-cluster_node_resume_failback_type?branch=master)
</dt> <dd>

Specifies the failback type to use when a cluster node in a paused state is resumed by the [**ResumeClusterNodeEx**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_resume_cluster_node_ex?branch=master) function.

</dd> <dt>

[**CLUSTER\_NODE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_node_state?branch=master)
</dt> <dd>

Describes the state of a cluster node.

</dd> <dt>

[**CLUSTER\_NODE\_STATUS**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_node_status?branch=master)
</dt> <dd>

Describes the status of a cluster node.

</dd> <dt>

[**CLUSTER\_NOTIFICATIONS\_VERSION**](/windows/previous-versions/ClusApi/ne-clusapi-cluster_notifications_version?branch=master)
</dt> <dd>

Defines the various versions of cluster notification enumerations.

</dd> <dt>

[**CLUSTER\_OBJECT\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_object_type?branch=master)
</dt> <dd>

Defines the type of object for which a notification is requested or generated.

</dd> <dt>

[**CLUSTER\_PROPERTY\_FORMAT**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_format?branch=master)
</dt> <dd>

Specifies the data type of a property value in a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_PROPERTY\_SYNTAX**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_syntax?branch=master)
</dt> <dd>

Provides the possible values for the syntax structures in a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_PROPERTY\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_property_type?branch=master)
</dt> <dd>

defines the property types that are supported by a cluster [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_QUORUM\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_quorum_type?branch=master)
</dt> <dd>

The type of quorum resource to be created.

</dd> <dt>

[**CLUSTER\_QUORUM\_VALUE**](/windows/previous-versions/msclus/ne-clusapi-cluster_quorum_value?branch=master)
</dt> <dd>

Enumerates values returned by the [**ClusterControl**](/windows/previous-versions/ClusAPI/nf-clusapi-clustercontrol?branch=master) function with the [CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN](clusctl-cluster-check-voter-down.md) or the [CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT](clusctl-cluster-check-voter-evict.md) control codes.

</dd> <dt>

[**CLUSTER\_REG\_COMMAND**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_reg_command?branch=master)
</dt> <dd>

Enumerates the possible cluster registry commands that a local node will perform when attempting to join a cluster.

</dd> <dt>

[**CLUSTER\_RESOURCE\_APPLICATION\_STATE**](/windows/previous-versions/Resapi/ne-resapi-cluster_resource_application_state?branch=master)
</dt> <dd>

Enumerates resource application states.

</dd> <dt>

[**CLUSTER\_RESOURCE\_CLASS**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_class?branch=master)
</dt> <dd>

Defines the class of a resource.

</dd> <dt>

[**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_create_flags?branch=master)
</dt> <dd>

Determines which resource monitor a given resource will be assigned to.

</dd> <dt>

[**CLUSTER\_RESOURCE\_EMBEDDED\_FAILURE\_ACTION**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_embedded_failure_action?branch=master)
</dt> <dd>

Specifies the various actions that can be performed when a resource has an embedded failure.

</dd> <dt>

[**CLUSTER\_RESOURCE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_enum?branch=master)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterResourceEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_enum?branch=master) or [**ClusterResourceOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_open_enum?branch=master) functions.

</dd> <dt>

[**CLUSTER\_RESOURCE\_RESTART\_ACTION**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_restart_action?branch=master)
</dt> <dd>

Used by the [**RestartAction**](resources-restartaction.md) [resource common property](resource-common-properties.md) to specify the action to be taken by the [cluster service](cluster-service.md) if the [resource fails](resource-failure.md).

</dd> <dt>

[**CLUSTER\_RESOURCE\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state?branch=master)
</dt> <dd>

Describes the operational condition of a resource.

</dd> <dt>

[**CLUSTER\_RESOURCE\_STATE\_CHANGE\_REASON**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_state_change_reason?branch=master)
</dt> <dd>

Used by the [**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](/windows/previous-versions/ClusAPI/ns-clusapi-_clusctl_resource_state_change_reason_struct?branch=master) and [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control codes to describe the reason for a resource state change.

</dd> <dt>

[**CLUSTER\_RESOURCE\_TYPE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_resource_type_enum?branch=master)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterResourceTypeEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_enum?branch=master) and [**ClusterResourceTypeOpenEnum**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_cluster_resource_type_open_enum?branch=master) functions.

</dd> <dt>

[**CLUSTER\_ROLE**](/windows/previous-versions/ResApi/ne-resapi-_cluster_role?branch=master)
</dt> <dd>

Contains the names of the standard cluster roles.

</dd> <dt>

[**CLUSTER\_ROLE\_STATE**](/windows/previous-versions/ResApi/ne-resapi-_cluster_role_state?branch=master)
</dt> <dd>

Defines the potential return values for the [**ResUtilGetClusterRoleState**](/windows/previous-versions/ResApi/nf-resapi-resutilgetclusterrolestate?branch=master) function.

</dd> <dt>

[**CLUSTER\_SET\_PASSWORD\_FLAGS**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dd>

Enumerates flags for the [**SetClusterServiceAccountPassword**](/windows/previous-versions/ClusAPI/nc-clusapi-pclusapi_set_cluster_service_account_password?branch=master) function that describe how the password update is to be applied to the cluster.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_setup_phase?branch=master)
</dt> <dd>

Used by the [*ClusterSetupProgressCallback*](/windows/previous-versions/ClusAPI/nc-clusapi-pcluster_setup_progress_callback?branch=master) function to identify the current phase of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE\_SEVERITY**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_setup_phase_severity?branch=master)
</dt> <dd>

Describes the severity of the current phase of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE\_TYPE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_setup_phase_type?branch=master)
</dt> <dd>

Describes the progress of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_BACKUP\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_shared_volume_backup_state?branch=master)
</dt> <dd>

Describes the CSV backup state

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_SNAPSHOT\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-cluster_shared_volume_snapshot_state?branch=master)
</dt> <dd>

Specifies the various snapshot states for a shared volume.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_shared_volume_state?branch=master)
</dt> <dd>

Defines the states of a cluster shared volume.

</dd> <dt>

[**CLUSTER\_UPGRADE\_PHASE**](/windows/previous-versions/ClusAPI/ne-clusapi-_cluster_upgrade_phase?branch=master)
</dt> <dd>

Describes the state of a rolling upgrade of the operating system on a cluster. This enumeration is used by the [*ClusterUpgradeProgressCallback*](/windows/previous-versions/clusapi/nc-clusapi-pcluster_upgrade_progress_callback?branch=master) callback function.

</dd> <dt>

[**FAILURE\_TYPE**](/windows/previous-versions/ResApi/ne-resapi-_failure_type?branch=master)
</dt> <dd>

Defines the failure types for cluster resources.

</dd> <dt>

[**FILESHARE\_CHANGE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-_fileshare_change_enum?branch=master)
</dt> <dd>

Contains the possible change events that are used by the [**FILESHARE\_CHANGE**](/windows/previous-versions/ClusAPI/ns-clusapi-_fileshare_change?branch=master) structure to describe an entry in a file share event notification list.

</dd> <dt>

[**LOG\_LEVEL**](/windows/previous-versions/ResApi/ne-resapi-log_level?branch=master)
</dt> <dd>

Represents the severity of the log event passed to the [*LogEvent*](/windows/previous-versions/ResApi/nc-resapi-plog_event_routine?branch=master) callback function.

</dd> <dt>

[**MAINTENANCE\_MODE\_TYPE\_ENUM**](/windows/previous-versions/ClusAPI/ne-clusapi-_maintenance_mode_type_enum?branch=master)
</dt> <dd>

Defines the possible states that a storage class resource can be placed in when marked for maintenance.

</dd> <dt>

[**NODE\_CLUSTER\_STATE**](/windows/previous-versions/ClusAPI/ne-clusapi-node_cluster_state?branch=master)
</dt> <dd>

Indicates the state of the cluster.

</dd> <dt>

[**PLACEMENT\_OPTIONS**](/windows/previous-versions/clusapi/ne-clusapi-placement_options?branch=master)
</dt> <dd>

Defines options for placing the cluster.

</dd> <dt>

[**RESDLL\_CONTEXT\_OPERATION\_TYPE**](/windows/previous-versions/ResApi/ne-resapi-resdll_context_operation_type?branch=master)
</dt> <dd>

Specifies the various types of context operations for the [**GET\_OPERATION\_CONTEXT\_PARAMS**](/windows/previous-versions/ResApi/ns-resapi-get_operation_context_params?branch=master) structure.

</dd> <dt>

[**RESOURCE\_EXIT\_STATE**](/windows/previous-versions/ResApi/ne-resapi-_resource_exit_state?branch=master)
</dt> <dd>

Enumerates the possible exit states of a [resource](resources.md).

</dd> <dt>

[**RESOURCE\_MONITOR\_STATE**](/windows/previous-versions/ResApi/ne-resapi-resource_monitor_state?branch=master)
</dt> <dd>

TBD

</dd> <dt>

[**SR\_DISK\_REPLICATION\_ELIGIBLE**](/windows/previous-versions/ClusAPI/ne-clusapi-_sr_disk_replication_eligible?branch=master)
</dt> <dd>

Specifies the various reasons a disk on a cluster node can be eligible or ineligible for replication.

</dd> <dt>

[**SR\_REPLICATED\_DISK\_TYPE**](/windows/previous-versions/ResApi/ne-clusapi-_sr_replicated_disk_type?branch=master)
</dt> <dd>

Specifies the replicated disk types for the [**SR\_RESOURCE\_TYPE\_REPLICATED\_DISK**](/windows/previous-versions/ClusAPI/ns-clusapi-_sr_resource_type_replicated_disk?branch=master) structure.

</dd> <dt>

[**VM\_RESDLL\_CONTEXT**](/windows/previous-versions/ResApi/ne-resapi-vm_resdll_context?branch=master)
</dt> <dd>

Contains actions for a virtual machine to perform.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster API Reference](server-cluster-api-reference.md)
</dt> </dl>

 

 




