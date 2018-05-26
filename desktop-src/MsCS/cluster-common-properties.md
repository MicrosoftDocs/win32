---
title: Cluster Common Properties
description: Cluster common properties are stored in the cluster database and apply to the cluster as a whole.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 49ca52e6-7f35-457b-a00f-d33b5d029fe0
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- cluster properties Failover Cluster
- cluster properties Failover Cluster , common
- properties Failover Cluster ,cluster properties
- properties Failover Cluster ,cluster properties, common
- clusters Failover Cluster ,properties
- clusters Failover Cluster ,properties, common
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Cluster Common Properties

Cluster [common properties](common-properties.md) are stored in the cluster database and apply to the [*cluster*](c-gly.md#-wolf-cluster-gly) as a whole.

## In this section

<dl> <dt>

[**AddEvictDelay**](clusters-addevictdelay.md)
</dt> <dd>

Specifies how many seconds after a node is evicted that the failover cluster service will wait before adding a new node.

</dd> <dt>

[**AdminAccessPoint**](adminaccesspoint.md)
</dt> <dd>

Management point type.

</dd> <dt>

[**AdminExtensions**](clusters-adminextensions.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**AutoBalancerLevel**](clusters-autobalancerlevel.md)
</dt> <dd>

Specifies the auto balancer level.

</dd> <dt>

[**AutoBalancerMode**](clusters-autobalancermode.md)
</dt> <dd>

The auto balancer mode.

</dd> <dt>

[**BackupInProgress**](backupinprogress.md)
</dt> <dd>

Indicates whether or not a Volume Shadow Copy Service Task is currently in progress for a specific volume on the cluster.

</dd> <dt>

[**BlockCacheSize**](blockcachesize.md)
</dt> <dd>

Specifies the cache size of a cluster shared volume (CSV), in megabytes.

</dd> <dt>

[**ClusSvcHangTimeout**](clusters-clussvchangtimeout.md)
</dt> <dd>

Controls the amount of time, in seconds, that the cluster network driver waits between Failover Cluster Service heartbeats before it determines that the Failover Cluster Service has stopped responding.

</dd> <dt>

[**ClusSvcHeartbeatTimeout**](cluster-clussvcheartbeattimeout.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**ClusSvcRegroupOpeningTimeout**](clusters-clussvcregroupopeningtimeout.md)
</dt> <dd>

Controls the amount of time, in seconds, that a node waits on other nodes in the opening stage before deciding that they have failed.

</dd> <dt>

[**ClusSvcRegroupPruningTimeout**](clusters-clussvcregrouppruningtimeout.md)
</dt> <dd>

Controls the amount of time, in seconds, that the membership leader waits to reach full connectivity between cluster nodes.

</dd> <dt>

[**ClusSvcRegroupStageTimeout**](clusters-clussvcregroupstagetimeout.md)
</dt> <dd>

Controls the amount of time, in seconds, that a node waits on other nodes in a membership stage before deciding that they have failed.

</dd> <dt>

[**ClusSvcRegroupTickInMilliseconds**](clusters-clussvcregrouptickinmilliseconds.md)
</dt> <dd>

Controls the interval of time, in milliseconds, that the membership algorithm waits between issuances of periodic membership messages.

</dd> <dt>

[**ClusterEnforcedAntiAffinity**](clusters-clusterenforcedantiaffinity.md)
</dt> <dd>

Prevents multiple cluster groups from running on the same cluster node when they contain the same [**AntiAffinityClassNames**](groups-antiaffinityclassnames.md) property value.

</dd> <dt>

[**ClusterFunctionalLevel**](clusters-clusterfunctionallevel.md)
</dt> <dd>

The major version of the OS on a cluster during a rolling upgrade.

</dd> <dt>

[**ClusterGroupWaitDelay**](clusters-clustergroupwaitdelay.md)
</dt> <dd>

Specifies the maximum time, in seconds, that a group waits for its preferred node to come online during cluster startup before coming online on a different node.

</dd> <dt>

[**ClusterLogLevel**](clusters-clusterloglevel.md)
</dt> <dd>

Controls the level of cluster logging.

</dd> <dt>

[**ClusterLogSize**](clusters-clusterlogsize.md)
</dt> <dd>

Controls the maximum size of the cluster log files on each of the nodes.

</dd> <dt>

[**ClusterUpgradeVersion**](clusters-clusterupgradeversion.md)
</dt> <dt>

[**CrossSiteDelay**](crosssitedelay.md)
</dt> <dd>

Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across sites.

</dd> <dt>

[**CrossSiteThreshold**](crosssitethreshold.md)
</dt> <dd>

Controls how many Cluster Service heartbeats can be missed across sites before it determines that Cluster Service has stopped responding.

</dd> <dt>

[**CrossSubnetDelay**](clusters-crosssubnetdelay.md)
</dt> <dd>

Controls the time interval, in milliseconds, that the cluster network driver waits between sending Cluster Service heartbeats across subnets.

</dd> <dt>

[**CrossSubnetThreshold**](clusters-crosssubnetthreshold.md)
</dt> <dd>

Controls how many Cluster Service heartbeats can be missed across subnets before it determines that Cluster Service has stopped responding.

</dd> <dt>

[**DatabaseReadWriteMode**](databasereadwritemode.md)
</dt> <dd>

Specifies the read/write mode for the cluster database.

</dd> <dt>

[**DefaultNetworkRole**](clusters-defaultnetworkrole.md)
</dt> <dd>

Specifies the [**role**](networks-role.md) that the [cluster](c-gly.md#-wolf-cluster-gly) automatically assigns to any newly discovered or created [network](networks.md).

</dd> <dt>

[**Description**](clusters-description.md)
</dt> <dd>

Stores administrative comments about the [cluster](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the **Description** property.

</dd> <dt>

[**DisableGroupPreferredOwnerRandomization**](cluster-disablegrouppreferredownerrandomization.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**DrainOnShutdown**](drainonshutdown.md)
</dt> <dd>

Specifies whether to enable Node Drain for a cluster.

</dd> <dt>

[**DumpPolicy**](dumppolicy.md)
</dt> <dd>

Dump policy.



| Attribute            | Value                                                        |
|----------------------|--------------------------------------------------------------|
| Data type<br/> | **DWORD** <br/>                                        |
| Access<br/>    | [Read/write](read-write-properties.md) <br/>          |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_ularge_integer?branch=master) |
| Minimum<br/>   | 0<br/>                                                 |
| Maximum<br/>   | 0<br/>                                                 |
| Default<br/>   | **( DWORD\_PTR ) &ClusterDumpPolicyDefaults** <br/>    |



 

</dd> <dt>

[**DynamicQuorum**](clusters-dynamicquorum.md)
</dt> <dd>

Enables the cluster to change the required number of nodes that need to participate in quorum when nodes shut down or crash.

</dd> <dt>

[**EnableEventDeltaGeneration**](cluster-enableeventdeltageneration.md)
</dt> <dd>

Controls whether a time delta event is logged when a set of event log entries are replicated to [nodes](nodes.md) across the entire [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**EnableEventLogReplication**](cluster-enableeventlogreplication.md)
</dt> <dd>

Controls whether the system, application, and security event log entries of all the [node's](nodes.md) are replicated across the entire [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**EnableResourceDllDeadlockDetection**](cluster-enableresourcedlldeadlockdetection.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**EnableSharedVolumes**](clusters-enablesharedvolumes.md)
</dt> <dd>

Not supported. This property cannot be set and always evaluates to **TRUE** (1).

</dd> <dt>

[**FixQuorum**](clusters-fixquorum.md)
</dt> <dd>

Specifies if the cluster is in a fix quorum state.

</dd> <dt>

[**GroupDependencyTimeout**](clusters-groupdependencytimeout.md)
</dt> <dd>

The group dependency timeout, in seconds.

</dd> <dt>

[**HangRecoveryAction**](cluster-hangrecoveryaction.md)
</dt> <dd>

Specifies the recovery action taken by the cluster service in response to a heartbeat countdown timeout.

</dd> <dt>

[**IgnorePersistentStateOnStartup**](clusters-ignorepersistentstateonstartup.md)
</dt> <dd>

Specifies whether the cluster will bring online groups that were online when the cluster was shut down.

</dd> <dt>

[**LogResourceControls**](clusters-logresourcecontrols.md)
</dt> <dd>

Controls the logging of resource controls.

</dd> <dt>

[**MessageBufferLength**](messagebufferlength.md)
</dt> <dd>

Specifies the number of characters in a message buffer.

</dd> <dt>

[**MinimumNeverPreemptPriority**](clusters-minimumneverpreemptpriority.md)
</dt> <dd>

Specifies the lowest priority group that cannot be preempted.

</dd> <dt>

[**MinimumPreemptorPriority**](clusters-minimumpreemptorpriority.md)
</dt> <dd>

Specifies the lowest priority group that can preempt other groups.

</dd> <dt>

[**NetftIPSecEnabled**](netftipsecenabled.md)
</dt> <dd>

Specifies whether Internet Protocol Security (IPSec) encryption is enabled for inter-node cluster communication.

</dd> <dt>

[**PlacementOptions**](clusters-placementoptions.md)
</dt> <dd>

Options for placing the cluster.

</dd> <dt>

[**PlumbAllCrossSubnetRoutes**](clusters-plumballcrosssubnetroutes.md)
</dt> <dd>

Plumbs all possible cross subnet routes to all nodes.

</dd> <dt>

[**PreferredSite**](preferredsite.md)
</dt> <dd>

Specifies the preferred site for a site-aware cluster.

</dd> <dt>

[**PreventQuorum**](clusters-preventquorum.md)
</dt> <dd>

Specifies whether to prevent a cluster node from achieving a quorum.

</dd> <dt>

[**QuarantineDuration**](quarantineduration.md)
</dt> <dd>

Specifies the quarantine duration for a node, in seconds.



| Attribute            | Value                                                 |
|----------------------|-------------------------------------------------------|
| Data type<br/> | **DWORD** <br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md) <br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) <br/> |
| Minimum<br/>   | 0<br/>                                          |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                 |
| Default<br/>   | 0<br/>                                          |



 

</dd> <dt>

[**QuarantineThreshold**](quarantinethreshold.md)
</dt> <dd>

Specifies the quarantine threshold for a node, in minutes.

</dd> <dt>

[**QuorumArbitrationTimeMax**](cluster-quorumarbitrationtimemax.md)
</dt> <dd>

Specifies the maximum number of seconds a [node](nodes.md) is allowed to spend arbitrating for the quorum resource in a [cluster](c-gly.md#-wolf-cluster-gly).

</dd> <dt>

[**QuorumArbitrationTimeMin**](cluster-quorumarbitrationtimemin.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**RequestReplyTimeout**](requestreplytimeout.md)
</dt> <dd>

Describes the length of time a request from a node with a cluster state update will wait for replies from the other healthy nodes before the request times out.

</dd> <dt>

[**ResiliencyDefaultPeriod**](resiliencydefaultperiod.md)
</dt> <dd>

Specifies the default resiliency period, in seconds, for the cluster.



| Attribute            | Value                                                 |
|----------------------|-------------------------------------------------------|
| Data type<br/> | **DWORD** <br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md) <br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) <br/> |
| Minimum<br/>   | 0<br/>                                          |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                 |
| Default<br/>   | 240<br/>                                        |



 

</dd> <dt>

[**ResiliencyLevel**](resiliencylevel.md)
</dt> <dd>

Specifies the resiliency level for the cluster.



| Attribute            | Value                                                 |
|----------------------|-------------------------------------------------------|
| Data type<br/> | **DWORD** <br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md) <br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) <br/> |
| Minimum<br/>   | 1<br/>                                          |
| Maximum<br/>   | 2<br/>                                          |
| Default<br/>   | 1<br/>                                          |



 

</dd> <dt>

[**ResourceDllDeadlockPeriod**](cluster-resourcedlldeadlockperiod.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**ResourceDllDeadlockThreshold**](cluster-resourcedlldeadlockthreshold.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**ResourceDllDeadlockTimeout**](cluster-resourcedlldeadlocktimeout.md)
</dt> <dd>

This property is not supported.

</dd> <dt>

[**RootMemoryReserved**](clusters-rootmemoryreserved.md)
</dt> <dd>

Not supported.

</dd> <dt>

[**RouteHistoryLength**](clusters-routehistorylength.md)
</dt> <dd>

The number of heartbeats to log after a cluster network failure.

</dd> <dt>

[**S2DBusTypes**](dasmodebustypes.md)
</dt> <dd>

Specifies the bus types for Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DCacheBehavior**](dasmodecachebehavior.md)
</dt> <dd>

Specifies the cache behavior for Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DCacheDesiredState**](dasmodecachedesiredstate.md)
</dt> <dd>

Specifies the desired cache state for Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DCacheFlashReservePercent**](dasmodecacheflashreservepercent.md)
</dt> <dd>

The percent of disk space, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DCacheMetadataReserveBytes**](dasmodecachemetadatareservebytes.md)
</dt> <dd>

The amount of disk space, in bytes, to reserve for the cache of a flash drive when using Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DCachePageSizeKBytes**](clusters-s2dcachepagesizekbytes.md)
</dt> <dd>

Page size in KB used by S2D cache.

</dd> <dt>

[**S2DEnabled**](dasmodeenabled.md)
</dt> <dd>

Enables Storage Spaces Direct (2SD).



| Attribute            | Value                                                 |
|----------------------|-------------------------------------------------------|
| Data type<br/> | **DWORD** <br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md) <br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) <br/> |
| Minimum<br/>   | 0<br/>                                          |
| Maximum<br/>   | 1<br/>                                          |
| Default<br/>   | 0<br/>                                          |



 

</dd> <dt>

[**S2DIOLatencyThreshold**](dasmodeiolatencythreshold.md)
</dt> <dd>

Specifies the IO latency threshold for Storage Spaces Direct (2SD).

</dd> <dt>

[**S2DOptimizations**](dasmodeoptimizations.md)
</dt> <dd>

Specifies the optimization flags for Storage Spaces Direct (2SD).

</dd> <dt>

[**SameSubnetDelay**](clusters-samesubnetdelay.md)
</dt> <dd>

Controls the delay, in milliseconds, between netft heartbeats.

</dd> <dt>

[**SameSubnetThreshold**](clusters-samesubnetthreshold.md)
</dt> <dd>

Controls how many heartbeats can be missed on the same subnet before the route is declared as unreachable.

</dd> <dt>

[**Security Descriptor**](clusters-security-descriptor.md)
</dt> <dd>

Stores the [security descriptor](https://msdn.microsoft.com/library/windows/desktop/aa379563) of a [cluster](c-gly.md#-wolf-cluster-gly). The following table summarizes the attributes of the [Security Descriptor](clusters-security-descriptor.md) property.

</dd> <dt>

[**SecurityLevel**](clusters-securitylevel.md)
</dt> <dd>

Controls the level of security that applies to intracluster messages.

</dd> <dt>

[**SharedVolumeBlockCacheSizeInMB**](clusters-sharedvolumeblockcachesizeinmb.md)
</dt> <dd>

Specifies the cache size of a cluster shared volume (CSV), in megabytes.

</dd> <dt>

[**SharedVolumeCompatibleFilters**](clusters-sharedvolumecompatiblefilters.md)
</dt> <dd>

Overrides cluster service determination of filters as incompatible.

</dd> <dt>

[**SharedVolumeIncompatibleFilters**](clusters-sharedvolumeincompatiblefilters.md)
</dt> <dd>

Adds filters to be deemed as incompatible for direct I/O.

</dd> <dt>

[**SharedVolumeSecurityDescriptor**](clusters-sharedvolumesecuritydescriptor.md)
</dt> <dd>

Specifies the security descriptor for a cluster shared volume (CSV).

</dd> <dt>

[**SharedVolumesRoot**](clusters-sharedvolumesroot.md)
</dt> <dd>

Specifies the root directory from which the cluster shared volumes (CSVs) are linked.

</dd> <dt>

[**ShutdownTimeoutInMinutes**](clusters-shutdowntimeoutinminutes.md)
</dt> <dd>

Specifies how many minutes after a system shutdown is initiated that the failover cluster service will wait for resources to go offline.

</dd> <dt>

[**UseClientAccessNetworksForSharedVolumes**](clusters-useclientaccessnetworksforsharedvolumes.md)
</dt> <dd>

Enables or disables the use of client access networks for cluster shared volumes (CSV) used by the cluster.

</dd> <dt>

[**UseNetftForSharedVolumes**](clusters-usenetftforsharedvolumes.md)
</dt> <dd>

Specifies whether to enable Network Fault-Tolerance (NETFT) for cluster shared volumes.

</dd> <dt>

[**WitnessDatabaseWriteTimeout**](clusters-witnessdatabasewritetimeout.md)
</dt> <dd>

Specifies the maximum amount of time, in seconds, that a cluster database write to a witness can take before the write is abandoned.

</dd> <dt>

[**WitnessDynamicWeight**](witnessdynamicweight.md)
</dt> <dd>

Specifies the weight of a file share quorum witness for dynamic quorum.

</dd> <dt>

[**WitnessRestartInterval**](witnessrestartinterval.md)
</dt> <dd>

specifies how long (in minutes) the system will wait before attempting to restart a failed file share witness resource.

</dd> </dl>

## Related topics

<dl> <dt>

[Cluster Object Common Properties](common-properties-ref.md)
</dt> <dt>

[Getting Cluster Information](getting-cluster-information.md)
</dt> </dl>

 

 





