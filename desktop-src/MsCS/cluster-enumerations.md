---
title: Failover Cluster Enumerations
description: This section contains the enumerations of the Failover Cluster API.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '546071de-1067-4b47-b862-668be976e563'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
---

# Failover Cluster Enumerations

This section contains the enumerations of the Failover Cluster API.

## In this section

<dl> <dt>

[**CLCTL\_CODES**](clctl-codes.md)
</dt> <dd>

enumerates the possible operations that a control code will perform.

</dd> <dt>

[**CLUS\_CHARACTERISTICS**](clus-characteristics.md)
</dt> <dd>

Enumerates characteristics of resource types and resources.

</dd> <dt>

[**CLUS\_FLAGS**](clus-flags.md)
</dt> <dd>

Identifies the resource or group as a [core resource](core-resources.md).

</dd> <dt>

[**CLUS\_GROUP\_START\_SETTING**](clus-group-start-setting.md)
</dt> <dd>

Enumerates the start settings for a cluster group.

</dd> <dt>

[**CLUS\_RESSUBCLASS**](clus-ressubclass.md)
</dt> <dd>

Identifies a resource subclass that manages a shared resource.

</dd> <dt>

[**CLUS\_RESSUBCLASS\_NETWORK**](clus-ressubclass-network.md)
</dt> <dd>

Identifies a resource subclass that manages an IP address provider.

</dd> <dt>

[**CLUS\_RESSUBCLASS\_STORAGE**](clus-ressubclass-storage.md)
</dt> <dd>

Identifies a resource subclass that manages a shared bus.

</dd> <dt>

[**CLUSCTL\_CLUSTER\_CODES**](clusctl-cluster-codes.md)
</dt> <dd>

Enumerates cluster [control codes](about-control-codes.md) used by the [**ClusterControl**](clustercontrol.md) function.

</dd> <dt>

[**CLUSCTL\_GROUP\_CODES**](clusctl-group-codes.md)
</dt> <dd>

Enumerates [group](groups.md)[control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_GROUPSET\_CODES**](clusctl-collection-codes.md)
</dt> <dd>

Enumerates groupset [control codes](about-control-codes.md) used by the [**ClusterGroupSetControl**](clustergroupcollectioncontrol.md) function.

</dd> <dt>

[**CLUSCTL\_NETINTERFACE\_CODES**](clusctl-netinterface-codes.md)
</dt> <dd>

Enumerates Network Interface [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_NETWORK\_CODES**](clusctl-network-codes.md)
</dt> <dd>

Enumerates [network](networks.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_NODE\_CODES**](clusctl-node-codes.md)
</dt> <dd>

Enumerates [node](nodes.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_RESOURCE\_CODES**](clusctl-resource-codes.md)
</dt> <dd>

Enumerates [resource](resources.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSCTL\_RESOURCE\_TYPE\_CODES**](clusctl-resource-type-codes.md)
</dt> <dd>

Enumerates [resource type](resource-types.md) [control codes](about-control-codes.md).

</dd> <dt>

[**CLUSGROUP\_TYPE**](clusgroup-type.md)
</dt> <dd>

Specifies the type of cluster group to create.

</dd> <dt>

[**CLUSPROP\_IPADDR\_ENABLENETBIOS**](clusprop-ipaddr-enablenetbios.md)
</dt> <dd>

When used with the [**CLUSPROP\_DWORD**](clusprop-dword.md) structure, enables or disables the functionality of the [**EnableNetBIOS**](ip-addresses-enablenetbios.md) property of [IP Address](ip-address.md) [resources](resources.md).

</dd> <dt>

[**CLUSPROP\_PIFLAGS**](clusprop-piflags.md)
</dt> <dd>

Represents disk partition information. The enumeration flags identify certain properties of a disk partition, which is a [storage class resource](s-gly.md#-wolf-storage-class-resource-gly).

</dd> <dt>

[**CLUSTER\_CHANGE**](cluster-change.md)
</dt> <dd>

Describes the type of notification returned.

</dd> <dt>

[**CLUSTER\_CHANGE\_CLUSTER\_V2**](cluster-change-cluster-v2.md)
</dt> <dd>

Defines the list of notifications that are generated for a cluster.

</dd> <dt>

[**CLUSTER\_CHANGE\_GROUP\_V2**](cluster-change-group-v2.md)
</dt> <dd>

Defines the list of notifications that are generated for a group.

</dd> <dt>

[**CLUSTER\_CHANGE\_GROUPSET\_V2**](cluster-change-collection-v2.md)
</dt> <dd>

Defines the list of notifications that are generated for a groupset.

</dd> <dt>

[**CLUSTER\_CHANGE\_NETINTERFACE\_V2**](cluster-change-netinterface-v2.md)
</dt> <dd>

Defines the set of notifications that are generated for a cluster network interface.

</dd> <dt>

[**CLUSTER\_CHANGE\_NETWORK\_V2**](cluster-change-network-v2.md)
</dt> <dd>

Defines the notifications that are generated for a cluster network.

</dd> <dt>

[**CLUSTER\_CHANGE\_NODE\_UPGRADE\_PHASE\_V2**](cluster-change-node-upgrade-phase-v2.md)
</dt> <dd>

Defines the notifications that are generated for the upgrade of a cluster node.

</dd> <dt>

[**CLUSTER\_CHANGE\_NODE\_V2**](cluster-change-node-v2.md)
</dt> <dd>

Defines the notifications that are generated for a cluster node.

</dd> <dt>

[**CLUSTER\_CHANGE\_QUORUM\_V2**](cluster-change-quorum-v2.md)
</dt> <dd>

Defines the notifications that are generated for quorum-specific information.

</dd> <dt>

[**CLUSTER\_CHANGE\_REGISTRY\_V2**](cluster-change-registry-v2.md)
</dt> <dd>

Defines the notifications that are generated for a registry key.

</dd> <dt>

[**CLUSTER\_CHANGE\_RESOURCE\_TYPE\_V2**](cluster-change-resource-type-v2.md)
</dt> <dd>

Defines the set of notifications that are generated for a resource type.

</dd> <dt>

[**CLUSTER\_CHANGE\_RESOURCE\_V2**](cluster-change-resource-v2.md)
</dt> <dd>

Defines the list of notifications that are generated for a resource.

</dd> <dt>

[**CLUSTER\_CHANGE\_SHARED\_VOLUME\_V2**](cluster-change-shared-volume-v2.md)
</dt> <dd>

Defines the notifications that are generated for a cluster shared volume.

</dd> <dt>

[**CLUSTER\_CHANGE\_SPACEPORT\_V2**](cluster-change-spaceport-v2.md)
</dt> <dd>

TBD

</dd> <dt>

[**CLUSTER\_CONTROL\_OBJECT**](cluster-control-object.md)
</dt> <dd>

The 8-bit object component of a control code that indicates the type of cluster object to which the control code applies. For more information, see [Control Code Architecture](control-code-architecture.md).

</dd> <dt>

[**CLUSTER\_CSV\_VOLUME\_FAULT\_STATE**](cluster-csv-volume-fault-state.md)
</dt> <dd>

Defines the various fault states for a cluster shared volume (CSV).

</dd> <dt>

[**CLUSTER\_ENUM**](cluster-enum.md)
</dt> <dd>

Describes the type of cluster objects being enumerated.

</dd> <dt>

[**CLUSTER\_GROUP\_AUTOFAILBACK\_TYPE**](cluster-group-autofailback-type.md)
</dt> <dd>

Used by the [**AutoFailbackType**](groups-autofailbacktype.md) group [common property](common-properties.md) to specify whether the group should be failed back to the [node](nodes.md) identified as its preferred owner when that node comes back online following a [failover](failover.md).

</dd> <dt>

[**CLUSTER\_GROUP\_ENUM**](cluster-group-enum.md)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterGroupEnum**](clustergroupenum.md) and [**ClusterGroupOpenEnum**](clustergroupopenenum.md) functions.

</dd> <dt>

[**CLUSTER\_GROUP\_PRIORITY**](cluster-group-priority.md)
</dt> <dd>

Specifies the priority level of a group.

</dd> <dt>

[**CLUSTER\_GROUP\_STATE**](cluster-group-state.md)
</dt> <dd>

Enumerates the possible states of a [group](groups.md).

</dd> <dt>

[**CLUSTER\_MGMT\_POINT\_TYPE**](cluster-mgmt-point-type.md)
</dt> <dd>

Specifies the type of the management point for the cluster.

</dd> <dt>

[**CLUSTER\_NETINTERFACE\_STATE**](cluster-netinterface-state.md)
</dt> <dd>

Enumerates the possible values of the state of a [network interface](network-interfaces.md).

</dd> <dt>

[**CLUSTER\_NETWORK\_ENUM**](cluster-network-enum.md)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterNetworkEnum**](clusternetworkenum.md) and [**ClusterNetworkOpenEnum**](clusternetworkopenenum.md) functions.

</dd> <dt>

[**CLUSTER\_NETWORK\_ROLE**](cluster-network-role.md)
</dt> <dd>

Describes the role a [network](networks.md) plays in the [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**CLUSTER\_NETWORK\_STATE**](cluster-network-state.md)
</dt> <dd>

Enumerates the possible values of the state of a [network](networks.md).

</dd> <dt>

[**CLUSTER\_NODE\_DRAIN\_STATUS**](cluster-node-drain-status.md)
</dt> <dd>

Enumerates the possible values of the status of a node drain.

</dd> <dt>

[**CLUSTER\_NODE\_ENUM**](cluster-node-enum.md)
</dt> <dd>

Describes the types of cluster objects that are enumerated by the [**ClusterNodeEnum**](clusternodeenum.md) and [**ClusterNodeOpenEnum**](clusternodeopenenum.md) functions.

</dd> <dt>

[**CLUSTER\_NODE\_RESUME\_FAILBACK\_TYPE**](cluster-node-resume-failback-type.md)
</dt> <dd>

Specifies the failback type to use when a cluster node in a paused state is resumed by the [**ResumeClusterNodeEx**](resumeclusternodeex.md) function.

</dd> <dt>

[**CLUSTER\_NODE\_STATE**](cluster-node-state.md)
</dt> <dd>

Describes the state of a cluster node.

</dd> <dt>

[**CLUSTER\_NODE\_STATUS**](cluster-node-status.md)
</dt> <dd>

Describes the status of a cluster node.

</dd> <dt>

[**CLUSTER\_NOTIFICATIONS\_VERSION**](cluster-notifications-version.md)
</dt> <dd>

Defines the various versions of cluster notification enumerations.

</dd> <dt>

[**CLUSTER\_OBJECT\_TYPE**](cluster-object-type.md)
</dt> <dd>

Defines the type of object for which a notification is requested or generated.

</dd> <dt>

[**CLUSTER\_PROPERTY\_FORMAT**](cluster-property-format.md)
</dt> <dd>

Specifies the data type of a property value in a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_PROPERTY\_SYNTAX**](cluster-property-syntax.md)
</dt> <dd>

Provides the possible values for the syntax structures in a [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_PROPERTY\_TYPE**](cluster-property-type.md)
</dt> <dd>

defines the property types that are supported by a cluster [property list](property-lists.md).

</dd> <dt>

[**CLUSTER\_QUORUM\_TYPE**](cluster-quorum-type.md)
</dt> <dd>

The type of quorum resource to be created.

</dd> <dt>

[**CLUSTER\_QUORUM\_VALUE**](cluster-quorum-value.md)
</dt> <dd>

Enumerates values returned by the [**ClusterControl**](clustercontrol.md) function with the [CLUSCTL\_CLUSTER\_CHECK\_VOTER\_DOWN](clusctl-cluster-check-voter-down.md) or the [CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT](clusctl-cluster-check-voter-evict.md) control codes.

</dd> <dt>

[**CLUSTER\_REG\_COMMAND**](cluster-reg-command.md)
</dt> <dd>

Enumerates the possible cluster registry commands that a local node will perform when attempting to join a cluster.

</dd> <dt>

[**CLUSTER\_RESOURCE\_APPLICATION\_STATE**](cluster-resource-application-state.md)
</dt> <dd>

Enumerates resource application states.

</dd> <dt>

[**CLUSTER\_RESOURCE\_CLASS**](cluster-resource-class.md)
</dt> <dd>

Defines the class of a resource.

</dd> <dt>

[**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](cluster-resource-create-flags.md)
</dt> <dd>

Determines which resource monitor a given resource will be assigned to.

</dd> <dt>

[**CLUSTER\_RESOURCE\_EMBEDDED\_FAILURE\_ACTION**](cluster-resource-embedded-failure-action.md)
</dt> <dd>

Specifies the various actions that can be performed when a resource has an embedded failure.

</dd> <dt>

[**CLUSTER\_RESOURCE\_ENUM**](cluster-resource-enum.md)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterResourceEnum**](clusterresourceenum.md) or [**ClusterResourceOpenEnum**](clusterresourceopenenum.md) functions.

</dd> <dt>

[**CLUSTER\_RESOURCE\_RESTART\_ACTION**](cluster-resource-restart-action.md)
</dt> <dd>

Used by the [**RestartAction**](resources-restartaction.md) [resource common property](resource-common-properties.md) to specify the action to be taken by the [cluster service](cluster-service.md) if the [resource fails](resource-failure.md).

</dd> <dt>

[**CLUSTER\_RESOURCE\_STATE**](cluster-resource-state.md)
</dt> <dd>

Describes the operational condition of a resource.

</dd> <dt>

[**CLUSTER\_RESOURCE\_STATE\_CHANGE\_REASON**](cluster-resource-state-change-reason.md)
</dt> <dd>

Used by the [**CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON\_STRUCT**](clusctl-resource-state-change-reason-struct.md) and [CLUSCTL\_RESOURCE\_STATE\_CHANGE\_REASON](clusctl-resource-state-change-reason.md) control codes to describe the reason for a resource state change.

</dd> <dt>

[**CLUSTER\_RESOURCE\_TYPE\_ENUM**](cluster-resource-type-enum.md)
</dt> <dd>

Describes the type of cluster object being enumerated by the [**ClusterResourceTypeEnum**](clusterresourcetypeenum.md) and [**ClusterResourceTypeOpenEnum**](clusterresourcetypeopenenum.md) functions.

</dd> <dt>

[**CLUSTER\_ROLE**](cluster-role.md)
</dt> <dd>

Contains the names of the standard cluster roles.

</dd> <dt>

[**CLUSTER\_ROLE\_STATE**](cluster-role-state.md)
</dt> <dd>

Defines the potential return values for the [**ResUtilGetClusterRoleState**](resutilgetclusterrolestate.md) function.

</dd> <dt>

[**CLUSTER\_SET\_PASSWORD\_FLAGS**](cluster-set-password-flags.md)
</dt> <dd>

Enumerates flags for the [**SetClusterServiceAccountPassword**](setclusterserviceaccountpassword.md) function that describe how the password update is to be applied to the cluster.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE**](cluster-setup-phase.md)
</dt> <dd>

Used by the [*ClusterSetupProgressCallback*](pcluster-setup-progress-callback.md) function to identify the current phase of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE\_SEVERITY**](cluster-setup-phase-severity.md)
</dt> <dd>

Describes the severity of the current phase of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SETUP\_PHASE\_TYPE**](cluster-setup-phase-type.md)
</dt> <dd>

Describes the progress of the cluster setup process.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_BACKUP\_STATE**](cluster-shared-volume-backup-state.md)
</dt> <dd>

Describes the CSV backup state

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_SNAPSHOT\_STATE**](cluster-shared-volume-snapshot-state.md)
</dt> <dd>

Specifies the various snapshot states for a shared volume.

</dd> <dt>

[**CLUSTER\_SHARED\_VOLUME\_STATE**](cluster-shared-volume-state.md)
</dt> <dd>

Defines the states of a cluster shared volume.

</dd> <dt>

[**CLUSTER\_UPGRADE\_PHASE**](cluster-upgrade-phase.md)
</dt> <dd>

Describes the state of a rolling upgrade of the operating system on a cluster. This enumeration is used by the [*ClusterUpgradeProgressCallback*](clusterupgradeprogresscallback.md) callback function.

</dd> <dt>

[**FAILURE\_TYPE**](failure-type.md)
</dt> <dd>

Defines the failure types for cluster resources.

</dd> <dt>

[**FILESHARE\_CHANGE\_ENUM**](fileshare-change-enum.md)
</dt> <dd>

Contains the possible change events that are used by the [**FILESHARE\_CHANGE**](fileshare-change.md) structure to describe an entry in a file share event notification list.

</dd> <dt>

[**LOG\_LEVEL**](log-level.md)
</dt> <dd>

Represents the severity of the log event passed to the [*LogEvent*](logevent.md) callback function.

</dd> <dt>

[**MAINTENANCE\_MODE\_TYPE\_ENUM**](maintenance-mode-type-enum.md)
</dt> <dd>

Defines the possible states that a storage class resource can be placed in when marked for maintenance.

</dd> <dt>

[**NODE\_CLUSTER\_STATE**](node-cluster-state.md)
</dt> <dd>

Indicates the state of the cluster.

</dd> <dt>

[**PLACEMENT\_OPTIONS**](placement-options.md)
</dt> <dd>

Defines options for placing the cluster.

</dd> <dt>

[**RESDLL\_CONTEXT\_OPERATION\_TYPE**](resdll-context-operation-type.md)
</dt> <dd>

Specifies the various types of context operations for the [**GET\_OPERATION\_CONTEXT\_PARAMS**](get-operation-context-params.md) structure.

</dd> <dt>

[**RESOURCE\_EXIT\_STATE**](resource-exit-state.md)
</dt> <dd>

Enumerates the possible exit states of a [resource](resources.md).

</dd> <dt>

[**RESOURCE\_MONITOR\_STATE**](resource-monitor-state.md)
</dt> <dd>

TBD

</dd> <dt>

[**SR\_DISK\_REPLICATION\_ELIGIBLE**](sr-disk-replication-eligible.md)
</dt> <dd>

Specifies the various reasons a disk on a cluster node can be eligible or ineligible for replication.

</dd> <dt>

[**SR\_REPLICATED\_DISK\_TYPE**](sr-replicated-disk-type.md)
</dt> <dd>

Specifies the replicated disk types for the [**SR\_RESOURCE\_TYPE\_REPLICATED\_DISK**](sr-resource-type-replicated-disk.md) structure.

</dd> <dt>

[**VM\_RESDLL\_CONTEXT**](vm-resdll-context.md)
</dt> <dd>

Contains actions for a virtual machine to perform.

</dd> </dl>

## Related topics

<dl> <dt>

[Failover Cluster API Reference](server-cluster-api-reference.md)
</dt> </dl>

 

 




