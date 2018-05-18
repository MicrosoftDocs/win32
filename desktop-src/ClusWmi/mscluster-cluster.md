---
title: MSCluster\_Cluster class
description: A dynamic WMI class that represents a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '13a88f6b-1ec9-464d-adcf-a8b17341552d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["MSCluster_Cluster class", "MSCluster_Cluster class, described"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster
- MSCluster_Cluster.Caption
- MSCluster_Cluster.InstallDate
- MSCluster_Cluster.Status
- MSCluster_Cluster.CreationClassName
- MSCluster_Cluster.PrimaryOwnerContact
- MSCluster_Cluster.PrimaryOwnerName
- MSCluster_Cluster.Roles
- MSCluster_Cluster.NameFormat
- MSCluster_Cluster.OtherIdentifyingInfo
- MSCluster_Cluster.IdentifyingDescriptions
- MSCluster_Cluster.Dedicated
- MSCluster_Cluster.MaxNumberOfNodes
- MSCluster_Cluster.Name
- MSCluster_Cluster.Fqdn
- MSCluster_Cluster.Description
- MSCluster_Cluster.QuorumLogFileSize
- MSCluster_Cluster.Security
- MSCluster_Cluster.NetworkInterfaceAdminExtensions
- MSCluster_Cluster.NetworkAdminExtensions
- MSCluster_Cluster.ResourceTypeAdminExtensions
- MSCluster_Cluster.ResourceAdminExtensions
- MSCluster_Cluster.NodeAdminExtensions
- MSCluster_Cluster.GroupAdminExtensions
- MSCluster_Cluster.AdminExtensions
- MSCluster_Cluster.MaintenanceFile
- MSCluster_Cluster.QuorumType
- MSCluster_Cluster.QuorumPath
- MSCluster_Cluster.QuorumTypeValue
- MSCluster_Cluster.NetworkPriorities
- MSCluster_Cluster.DefaultNetworkRole
- MSCluster_Cluster.Security_Descriptor
- MSCluster_Cluster.QuorumArbitrationTimeMax
- MSCluster_Cluster.QuorumArbitrationTimeMin
- MSCluster_Cluster.DisableGroupPreferredOwnerRandomization
- MSCluster_Cluster.ResourceDllDeadlockPeriod
- MSCluster_Cluster.ClusSvcHangTimeout
- MSCluster_Cluster.ClusSvcRegroupOpeningTimeout
- MSCluster_Cluster.PlumbAllCrossSubnetRoutes
- MSCluster_Cluster.ClusSvcRegroupStageTimeout
- MSCluster_Cluster.ClusSvcRegroupPruningTimeout
- MSCluster_Cluster.ClusSvcRegroupTickInMilliseconds
- MSCluster_Cluster.ClusterLogSize
- MSCluster_Cluster.ClusterLogLevel
- MSCluster_Cluster.LogResourceControls
- MSCluster_Cluster.HangRecoveryAction
- MSCluster_Cluster.SameSubnetDelay
- MSCluster_Cluster.CrossSubnetDelay
- MSCluster_Cluster.CrossSiteDelay
- MSCluster_Cluster.SameSubnetThreshold
- MSCluster_Cluster.CrossSubnetThreshold
- MSCluster_Cluster.CrossSiteThreshold
- MSCluster_Cluster.BackupInProgress
- MSCluster_Cluster.RequestReplyTimeout
- MSCluster_Cluster.PrivateProperties
- MSCluster_Cluster.WitnessRestartInterval
- MSCluster_Cluster.SecurityLevel
- MSCluster_Cluster.WitnessDatabaseWriteTimeout
- MSCluster_Cluster.AddEvictDelay
- MSCluster_Cluster.FixQuorum
- MSCluster_Cluster.PreventQuorum
- MSCluster_Cluster.IgnorePersistentStateOnStartup
- MSCluster_Cluster.SharedVolumesRoot
- MSCluster_Cluster.WitnessDynamicWeight
- MSCluster_Cluster.AdminAccessPoint
- MSCluster_Cluster.ClusterFunctionalLevel
- MSCluster_Cluster.ClusterUpgradeVersion
- MSCluster_Cluster.ResiliencyLevel
- MSCluster_Cluster.ResiliencyDefaultPeriod
- MSCluster_Cluster.GroupDependencyTimeout
- MSCluster_Cluster.GracePeriodEnabled
- MSCluster_Cluster.GracePeriodTimeout
- MSCluster_Cluster.QuarantineDuration
- MSCluster_Cluster.AutoAssignedNodeSite
- MSCluster_Cluster.PreferredSite
- MSCluster_Cluster.PlacementOptions
- MSCluster_Cluster.QuarantineThreshold
- MSCluster_Cluster.AutoAssignNodeSite
- MSCluster_Cluster.AutoBalancerLevel
- MSCluster_Cluster.AutoBalancerMode
- MSCluster_Cluster.EnableSharedVolumes
- MSCluster_Cluster.BlockCacheSize
- MSCluster_Cluster.ClusterEnforcedAntiAffinity
- MSCluster_Cluster.SharedVolumeVssWriterOperationTimeout
- MSCluster_Cluster.UseClientAccessNetworksForSharedVolumes
- MSCluster_Cluster.SharedVolumeCompatibleFilters
- MSCluster_Cluster.SharedVolumeIncompatibleFilters
- MSCluster_Cluster.ClusterGroupWaitDelay
- MSCluster_Cluster.MinimumPreemptorPriority
- MSCluster_Cluster.MinimumNeverPreemptPriority
- MSCluster_Cluster.ShutdownTimeoutInMinutes
- MSCluster_Cluster.RootMemoryReserved
- MSCluster_Cluster.SharedVolumeSecurityDescriptor
- MSCluster_Cluster.RouteHistoryLength
- MSCluster_Cluster.DumpPolicy
- MSCluster_Cluster.DynamicQuorumEnabled
- MSCluster_Cluster.RecentEventsResetTime
- MSCluster_Cluster.DrainOnShutdown
- MSCluster_Cluster.DatabaseReadWriteMode
- MSCluster_Cluster.NetftIPSecEnabled
- MSCluster_Cluster.CsvBalancer
- MSCluster_Cluster.MessageBufferLength
- MSCluster_Cluster.S2DEnabled
- MSCluster_Cluster.S2DBusTypes
- MSCluster_Cluster.S2DOptimizations
- MSCluster_Cluster.S2DIOLatencyThreshold
- MSCluster_Cluster.S2DCacheDesiredState
- MSCluster_Cluster.S2DCacheDeviceModel
- MSCluster_Cluster.S2DCacheMetadataReserveBytes
- MSCluster_Cluster.S2DCachePageSizeKBytes
- MSCluster_Cluster.S2DCacheFlashReservePercent
- MSCluster_Cluster.S2DCacheBehavior
- MSCluster_Cluster.LowerQuorumPriorityNodeId
- MSCluster_Cluster.VirtualStorageArrayNotificationInterval
- MSCluster_Cluster.VirtualStorageArrayIOLatencyThreshold
- MSCluster_Cluster.VirtualStorageArrayStorageOptFlags
- MSCluster_Cluster.VirtualStorageArrayStorageBusTypes
- MSCluster_Cluster.VirtualStorageArrayEnabled
api_location:
- ClusWMI.dll
api_type:
- DllExport
---

# MSCluster\_Cluster class

The **MSCluster\_Cluster** class is a dynamic [*WMI class*](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [*cluster*](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

The following syntax is simplified from MOF code in MOF order and includes all inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("MS_CLUSTER_PROVIDER"), UUID("{9EB9A2F9-0751-4dcf-AB59-F8341D0F60B2}"), AMENDMENT]
class MSCluster_Cluster : CIM_Cluster
{
  string             Caption;
  datetime           InstallDate;
  string             Status;
  string             CreationClassName;
  string             PrimaryOwnerContact;
  string             PrimaryOwnerName;
  string             Roles[];
  string             NameFormat;
  string             OtherIdentifyingInfo[];
  string             IdentifyingDescriptions[];
  uint16             Dedicated[];
  uint32             MaxNumberOfNodes;
  string             Name;
  string             Fqdn;
  string             Description;
  uint32             QuorumLogFileSize;
  uint8              Security[];
  string             NetworkInterfaceAdminExtensions[];
  string             NetworkAdminExtensions[];
  string             ResourceTypeAdminExtensions[];
  string             ResourceAdminExtensions[];
  string             NodeAdminExtensions[];
  string             GroupAdminExtensions[];
  string             AdminExtensions[];
  string             MaintenanceFile;
  string             QuorumType;
  string             QuorumPath;
  uint32             QuorumTypeValue;
  string             NetworkPriorities[];
  uint32             DefaultNetworkRole;
  uint8              Security_Descriptor[];
  uint32             QuorumArbitrationTimeMax;
  uint32             QuorumArbitrationTimeMin;
  uint32             DisableGroupPreferredOwnerRandomization;
  uint32             ResourceDllDeadlockPeriod;
  uint32             ClusSvcHangTimeout;
  uint32             ClusSvcRegroupOpeningTimeout;
  uint32             PlumbAllCrossSubnetRoutes;
  uint32             ClusSvcRegroupStageTimeout;
  uint32             ClusSvcRegroupPruningTimeout;
  uint32             ClusSvcRegroupTickInMilliseconds;
  uint32             ClusterLogSize;
  uint32             ClusterLogLevel;
  uint32             LogResourceControls;
  uint32             HangRecoveryAction;
  uint32             SameSubnetDelay;
  uint32             CrossSubnetDelay;
  uint32             CrossSiteDelay;
  uint32             SameSubnetThreshold;
  uint32             CrossSubnetThreshold;
  uint32             CrossSiteThreshold;
  uint32             BackupInProgress;
  uint32             RequestReplyTimeout;
  MSCluster_Property PrivateProperties;
  uint32             WitnessRestartInterval;
  uint32             SecurityLevel;
  uint32             WitnessDatabaseWriteTimeout;
  uint32             AddEvictDelay = 60;
  uint32             FixQuorum = 0;
  uint32             PreventQuorum;
  uint32             IgnorePersistentStateOnStartup = 0;
  string             SharedVolumesRoot;
  uint32             WitnessDynamicWeight;
  uint32             AdminAccessPoint;
  uint32             ClusterFunctionalLevel;
  uint32             ClusterUpgradeVersion;
  uint32             ResiliencyLevel;
  uint32             ResiliencyDefaultPeriod;
  uint32             GroupDependencyTimeout;
  uint32             GracePeriodEnabled;
  uint32             GracePeriodTimeout;
  uint32             QuarantineDuration;
  uint32             AutoAssignedNodeSite;
  string             PreferredSite;
  uint32             PlacementOptions;
  uint32             QuarantineThreshold;
  uint32             AutoAssignNodeSite;
  uint32             AutoBalancerLevel;
  uint32             AutoBalancerMode;
  uint32             EnableSharedVolumes;
  uint32             BlockCacheSize;
  uint32             ClusterEnforcedAntiAffinity;
  uint32             SharedVolumeVssWriterOperationTimeout;
  uint32             UseClientAccessNetworksForSharedVolumes;
  string             SharedVolumeCompatibleFilters[];
  string             SharedVolumeIncompatibleFilters[];
  uint32             ClusterGroupWaitDelay;
  uint32             MinimumPreemptorPriority;
  uint32             MinimumNeverPreemptPriority;
  uint32             ShutdownTimeoutInMinutes;
  uint32             RootMemoryReserved;
  uint8              SharedVolumeSecurityDescriptor[];
  uint32             RouteHistoryLength;
  uint64             DumpPolicy;
  uint32             DynamicQuorumEnabled;
  string             RecentEventsResetTime;
  uint32             DrainOnShutdown;
  uint32             DatabaseReadWriteMode;
  uint32             NetftIPSecEnabled;
  uint32             CsvBalancer;
  uint32             MessageBufferLength;
  uint32             S2DEnabled;
  uint32             S2DBusTypes;
  uint32             S2DOptimizations;
  uint32             S2DIOLatencyThreshold;
  uint32             S2DCacheDesiredState;
  string             S2DCacheDeviceModel[];
  uint64             S2DCacheMetadataReserveBytes;
  uint32             S2DCachePageSizeKBytes;
  uint32             S2DCacheFlashReservePercent;
  uint64             S2DCacheBehavior;
  uint32             LowerQuorumPriorityNodeId;
  uint32             VirtualStorageArrayNotificationInterval;
  uint32             VirtualStorageArrayIOLatencyThreshold;
  uint32             VirtualStorageArrayStorageOptFlags;
  uint32             VirtualStorageArrayStorageBusTypes;
  uint32             VirtualStorageArrayEnabled;
};
```

## Members

The **MSCluster\_Cluster** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSCluster\_Cluster** class has these methods.



| Method                                                                                                     | Description                                                                                                                                                                                                                      |
|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddClusterNameAccount**](mscluster-cluster-addclusternameaccount.md)                                   | Creates a cluster name account in Active Directory Domain Services.<br/>                                                                                                                                                   |
| [**AddNode**](mscluster-cluster-addnode.md)                                                               | Adds a node to a cluster.<br/>                                                                                                                                                                                             |
| [**AddResourceToClusterSharedVolumes**](mscluster-cluster-addresourcetoclustersharedvolumes.md)           | Adds storage to Cluster Shared Volumes.<br/> **Windows Server 2008:** This method is not supported before Windows Server 2008 R2.<br/> <br/>                                                                   |
| [**AddVirtualMachine**](mscluster-cluster-addvirtualmachine.md)                                           | Adds an existing virtual machine to the cluster.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>                                  |
| [**CreateCluster**](mscluster-cluster-createcluster.md)                                                   | Creates a cluster.<br/>                                                                                                                                                                                                    |
| [**DestroyCluster**](mscluster-cluster-destroycluster.md)                                                 | Removes the cluster.<br/>                                                                                                                                                                                                  |
| [**EvictNode**](mscluster-cluster-evictnode.md)                                                           | Removes a specified node from the cluster.<br/>                                                                                                                                                                            |
| [**ExecuteClusterControl**](mscluster-cluster-executeclustercontrol.md)                                   | Executes a control code on the cluster.<br/>                                                                                                                                                                               |
| [**ForceCleanup**](mscluster-cluster-forcecleanup.md)                                                     | Forces a node to be cleaned up.<br/>                                                                                                                                                                                       |
| [**GenerateValidationStatus**](mscluster-cluster-generatevalidationstatus.md)                             | Creates an [**MSCluster\_ValidationStatus**](mscluster-validationstatus.md) object bound to the cluster.<br/> **Windows Server 2008:** This method is not supported before Windows Server 2008 R2.<br/> <br/> |
| [**GetNodeClusterState**](mscluster-cluster-getnodeclusterstate.md)                                       | Determines whether the Cluster service is installed and running on a node.<br/>                                                                                                                                            |
| [**RemoveResourceFromClusterSharedVolumes**](mscluster-cluster-removeresourcefromclustersharedvolumes.md) | Removes storage from Cluster Shared Volumes.<br/> **Windows Server 2008:** This method is not supported before Windows Server 2008 R2.<br/> <br/>                                                              |
| [**Rename**](mscluster-cluster-rename.md)                                                                 | Renames the cluster.<br/>                                                                                                                                                                                                  |
| [**SetDiskQuorum**](mscluster-cluster-setdiskquorum.md)                                                   | Sets the quorum behavior to not be a majority and to use the passed-in disk as the quorum resource.<br/>                                                                                                                   |
| [**SetMajorityQuorum**](mscluster-cluster-setmajorityquorum.md)                                           | Sets the quorom to a majority quorum and uses the passed-in resource as the quorum witness resource.<br/>                                                                                                                  |
| [**SetNodeMajorityQuorum**](mscluster-cluster-setnodemajorityquorum.md)                                   | Sets the cluster to not have a node majority quorum.<br/>                                                                                                                                                                  |
| [**VerifyPath**](mscluster-cluster-verifypath.md)                                                         | Verifies if the path is valid cluster storage for the resource group.<br/> **Windows Server 2008 R2 and Windows Server 2008:** This method is not supported before Windows Server 2012.<br/> <br/>             |



 

### Properties

The **MSCluster\_Cluster** class has these properties.

<dl> <dt>

**AddEvictDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the cluster's [**AddEvictDelay**](https://msdn.microsoft.com/library/ee342504) property, which is the number a seconds that a new node is delayed after an eviction of another node.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

<dt>

60
</dt> <dd>

Default

</dd> <dt>

0–600
</dt> <dd>

Valid range.

</dd> </dl>

</dd> <dt>

**AdminAccessPoint**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of the cluster administrative access point.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**AdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**AutoAssignedNodeSite**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines whether or not the cluster will attempt to automatically assign nodes to sites based on networks and Active Directory Site information.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**AutoAssignNodeSite**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines whether or not the cluster will attempt to automatically assign nodes to sites based on networks and Active Directory Site information

</dd> <dt>

**AutoBalancerLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines the level of aggressiveness of AutoBalancer.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**AutoBalancerMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Determines whether or not the auto balancer is enabled.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**BackupInProgress**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether a backup is in progress.

</dd> <dt>

**BlockCacheSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

CSV BlockCache Size in MB.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

**Windows Server 2008 R2:  **

This property is named **SharedVolumeBlockCacheSizeInMB** in Windows Server 2008 R2.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

A short textual description (one-line string) of the cluster.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ClusSvcHangTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Controls how long the cluster network driver waits between Failover Cluster Service heartbeats before it determines that the Failover Cluster Service has stopped responding.

</dd> <dt>

**ClusSvcRegroupOpeningTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Controls how long a node will wait on other nodes in the opening stage before deciding that they failed.

</dd> <dt>

**ClusSvcRegroupPruningTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is not supported.

**Windows Server 2008 R2 and Windows Server 2008:  **

Controls how long the membership leader will wait to reach full connectivity between cluster nodes.

</dd> <dt>

**ClusSvcRegroupStageTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Controls how long a node will wait on other nodes in a membership stage before deciding that they failed.

</dd> <dt>

**ClusSvcRegroupTickInMilliseconds**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Controls how frequently the membership algorithm is sending periodic membership messages.

</dd> <dt>

**ClusterEnforcedAntiAffinity**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables or disables hard enforcement of group anti-affinity classes.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

The possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**ClusterFunctionalLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The functional level the cluster is currently running in.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**ClusterGroupWaitDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum time in seconds that a group waits for its preferred node to come online during cluster startup before coming online on a different node.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**ClusterLogLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the level of cluster logging.

</dd> <dt>

**ClusterLogSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the maximum size of the cluster log files on each of the nodes.

</dd> <dt>

**ClusterUpgradeVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the upgrade version the cluster is currently running in.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_KEY**](https://msdn.microsoft.com/library/aa393651), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**CrossSiteDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how long the cluster network driver waits in milliseconds between sending Cluster Service heartbeats across sites.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**CrossSiteThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how many Cluster Service heartbeats can be missed across sites before it determines that Cluster Service has stopped responding.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**CrossSubnetDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how long the cluster network driver waits in milliseconds between sending Cluster Service heartbeats across subnets.

</dd> <dt>

**CrossSubnetThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how many Cluster Service heartbeats can be missed across subnets before it determines that Cluster Service has stopped responding.

</dd> <dt>

**CsvBalancer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether automatic balancing for CSV is enabled."

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**DatabaseReadWriteMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Sets the database read and write mode.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**Dedicated**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the cluster is a special-purpose cluster.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

<dt>

<span id="Not_Dedicated"></span><span id="not_dedicated"></span><span id="NOT_DEDICATED"></span>

**Not Dedicated** (0)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (1)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (2)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (3)


</dt> <dd></dd> <dt>

<span id="Router"></span><span id="router"></span><span id="ROUTER"></span>

**Router** (4)


</dt> <dd></dd> <dt>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>

**Switch** (5)


</dt> <dd></dd> <dt>

<span id="Layer_3_Switch"></span><span id="layer_3_switch"></span><span id="LAYER_3_SWITCH"></span>

**Layer 3 Switch** (6)


</dt> <dd></dd> <dt>

<span id="Central_Office_Switch"></span><span id="central_office_switch"></span><span id="CENTRAL_OFFICE_SWITCH"></span>

**Central Office Switch** (7)


</dt> <dd></dd> <dt>

<span id="Hub"></span><span id="hub"></span><span id="HUB"></span>

**Hub** (8)


</dt> <dd></dd> <dt>

<span id="Access_Server"></span><span id="access_server"></span><span id="ACCESS_SERVER"></span>

**Access Server** (9)


</dt> <dd></dd> <dt>

<span id="Firewall"></span><span id="firewall"></span><span id="FIREWALL"></span>

**Firewall** (10)


</dt> <dd></dd> <dt>

<span id="Print"></span><span id="print"></span><span id="PRINT"></span>

**Print** (11)


</dt> <dd></dd> <dt>

<span id="I_O"></span><span id="i_o"></span>

**I/O** (12)


</dt> <dd></dd> <dt>

<span id="Web_Caching"></span><span id="web_caching"></span><span id="WEB_CACHING"></span>

**Web Caching** (13)


</dt> <dd></dd> </dl>

</dd> <dt>

**DefaultNetworkRole**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the cluster's [**DefaultNetworkRole**](https://msdn.microsoft.com/library/aa369047) property.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Description)
</dt> </dl>

Provides access to the cluster's [**Description**](https://msdn.microsoft.com/library/aa369049) property.

</dd> <dt>

**DisableGroupPreferredOwnerRandomization**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is not supported.

</dd> <dt>

**DrainOnShutdown**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether to drain the node when cluster service is being stopped.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**DumpPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the cluster dump collection policy.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**DynamicQuorumEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Allows cluster service to adjust node weights as needed to increase availability.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**EnableSharedVolumes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables or disables cluster shared volumes on this cluster.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

The possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (1)


</dt> <dd></dd> </dl>

</dd> <dt>

**FixQuorum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Provides access to the cluster's [**FixQuorum**](https://msdn.microsoft.com/library/ee342505) property, which specifies if the cluster is in a fix quorum state.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

<dt>

0
</dt> <dd>

The cluster is not in a fix quorum state. This is the default value.

</dd> <dt>

1
</dt> <dd>

The cluster is in a fix quorum state.

</dd> </dl>

</dd> <dt>

**Fqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The fully qualified domain name of the cluster.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**GracePeriodEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the node grace period feature of this cluster is enabled.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (1)


</dt> <dd></dd> </dl>

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**GracePeriodTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The grace period timeout in milliseconds.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**GroupAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**GroupDependencyTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The timeout after which a group will be brought online despite unsatisfied dependencies

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**HangRecoveryAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the action to take if the user-mode processes have stopped responding.

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).OtherIdentifyingInfo")
</dt> </dl>

An array of free-form strings providing explanations and details behind the entries in the **OtherIdentifyingInfo** array. Note, each entry of this array is related to the entry in **OtherIdentifyingInfo** that is located at the same index.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

</dd> <dt>

**IgnorePersistentStateOnStartup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the cluster's [**IgnorePersistentStateOnStartup**](https://msdn.microsoft.com/library/ee342506) property, which specifies whether the cluster will bring online groups that were online when the cluster was shut down.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2, and is read-only until Windows Server 2016.

<dt>

0
</dt> <dd>

On startup groups that were online when the cluster was shut down will be brought online. This is the default value.

</dd> <dt>

1
</dt> <dd>

On startup all groups will remain offline.

</dd> </dl>

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

A datetime value indicating when the cluster was installed. A lack of a value does not indicate that the cluster is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**LogResourceControls**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the logging of resource controls.

</dd> <dt>

**LowerQuorumPriorityNodeId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the Node ID that has a lower priority when voting for quorum is performed. If the quorum vote is split 50/50%, the specified node's vote would be ignored to break the tie. If this is not set then the cluster will pick a node at random to break the tie.

> [!Note]  
> The **LowerQuorumPriorityNodeId** property is available for use in Windows Server 2012 R2. It may be altered or unavailable in subsequent versions of Windows Server.

 

</dd> <dt>

**MaintenanceFile**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**MaxNumberOfNodes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates the maximum number of nodes that may participate in the Cluster. If unlimited, enter 0.

This property is inherited from [**CIM\_Cluster**](cim-cluster.md).

</dd> <dt>

**MessageBufferLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum unacknowledged message count for GEM.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**MinimumNeverPreemptPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Groups with this priority or higher cannot be preempted.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**MinimumPreemptorPriority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Minimum priority a cluster group must have to be able to preempt another group.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Name)
</dt> </dl>

Specifies the name of the cluster.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies how the system name is generated.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

<dt>



 ("Other")


</dt> <dd></dd> <dt>



 ("IP")


</dt> <dd></dd> <dt>



 ("Dial")


</dt> <dd></dd> <dt>



 ("HID")


</dt> <dd></dd> <dt>



 ("NWA")


</dt> <dd></dd> <dt>



 ("HWA")


</dt> <dd></dd> <dt>



 ("X25")


</dt> <dd></dd> <dt>



 ("ISDN")


</dt> <dd></dd> <dt>



 ("IPX")


</dt> <dd></dd> <dt>



 ("DCC")


</dt> <dd></dd> <dt>



 ("ICD")


</dt> <dd></dd> <dt>



 ("E.164")


</dt> <dd></dd> <dt>



 ("SNA")


</dt> <dd></dd> <dt>



 ("OID/OSI")


</dt> <dd></dd> </dl>

</dd> <dt>

**NetftIPSecEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether IPSec is enabled for cluster internal traffic.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**NetworkAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**NetworkInterfaceAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**NetworkPriorities**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Arraytype**](https://msdn.microsoft.com/library/aa393650) ("Ordered")
</dt> </dl>

This property is obsolete.

</dd> <dt>

**NodeAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("[**CIM\_ComputerSystem**](cim-computersystem.md).IdentifyingDescriptions")
</dt> </dl>

Captures additional data, beyond System Name information, that could be used to identify a cluster.

This property is inherited from [**CIM\_ComputerSystem**](cim-computersystem.md).

</dd> <dt>

**PlacementOptions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Various option flags to modify default placement behavior.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**PlumbAllCrossSubnetRoutes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Plumbs all possible cross subnet routes to all nodes.

</dd> <dt>

**PreferredSite**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the site whose nodes will be given preference during regroup and node weight adjustment.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**PreventQuorum**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether the cluster will ignore group persistent state on startup.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**PrimaryOwnerContact**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.3")
</dt> </dl>

A string that provides information on how the primary system owner can be reached (e.g. phone number, email address, ...).

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**PrimaryOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|General Information\|001.4")
</dt> </dl>

The name of the primary system owner.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**PrivateProperties**
</dt> <dd> <dl> <dt>

Data type: **[**MSCluster\_Property**](mscluster-property.md)**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls private properties of the cluster.

</dd> <dt>

**QuarantineDuration**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The quarantine period timeout in milliseconds.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**QuarantineThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of node failures before it will be quarantined.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**QuorumArbitrationTimeMax**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the maximum time necessary to decide the Quorum owner node.

</dd> <dt>

**QuorumArbitrationTimeMin**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the minimum time necessary to decide the Quorum owner node.

</dd> <dt>

**QuorumLogFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**QuorumPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maintains quorum files.

</dd> <dt>

**QuorumType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the current quorum type.

The following are the possible values:

"Majority"

"No Majority"

</dd> <dt>

**QuorumTypeValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Get the current quorum type value.

Possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (-1)


</dt> <dd></dd> <dt>

<span id="Node"></span><span id="node"></span><span id="NODE"></span>

**Node** (1)


</dt> <dd></dd> <dt>

<span id="FileShareWitness"></span><span id="filesharewitness"></span><span id="FILESHAREWITNESS"></span>

**FileShareWitness** (2)


</dt> <dd></dd> <dt>

<span id="Storage"></span><span id="storage"></span><span id="STORAGE"></span>

**Storage** (3)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (4)


</dt> <dd></dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**RecentEventsResetTime**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Allows cluster to reset the last events displayed to clients.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**RequestReplyTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the request reply time-out period.

</dd> <dt>

**ResiliencyDefaultPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The default resiliency period, in seconds, for the cluster.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**ResiliencyLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (2)
</dt> </dl>

The resiliency level for the cluster.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**ResourceAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**ResourceDllDeadlockPeriod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is obsolete.

</dd> <dt>

**ResourceTypeAdminExtensions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**Roles**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array (bag) of strings that specify the roles this cluster plays in the IT-environment.

This property is inherited from [**CIM\_System**](cim-system.md).

</dd> <dt>

**RootMemoryReserved**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the amount of memory reserved for the parent partition on all cluster nodes.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**RouteHistoryLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The history length for routes to help finding network issues.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**S2DBusTypes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Bus types for storage spaces direct.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**S2DCacheBehavior**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Flags that affect the behavior of the storage spaces direct mode cache.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**S2DCacheDesiredState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Desired state of the storage spaces direct cache.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**S2DCacheDeviceModel**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Use this property to override the default selection of physical disks to be used for S2D cache.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**S2DCacheFlashReservePercent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Percentage of allocated flash space to utilize when caching.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**S2DCacheMetadataReserveBytes**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Bytes to reserve on flash devices for metadata.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This method is not supported before Windows Server 2016.

</dd> <dt>

**S2DCachePageSizeKBytes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Page size in KB used by S2D cache.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**S2DEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether direct attached storage (DAS) is enabled.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**S2DIOLatencyThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The I/O latency threshold for storage spaces direct.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**S2DOptimizations**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Optimization flags for storage spaces direct.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2016.

</dd> <dt>

**SameSubnetDelay**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how long the cluster network driver waits in milliseconds between sending Cluster Service heartbeats on the same subnet.

</dd> <dt>

**SameSubnetThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls how many Cluster Service heartbeats can be missed on the same subnet before it determines that Cluster Service has stopped responding.

</dd> <dt>

**Security**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

This property is obsolete.

</dd> <dt>

**Security\_Descriptor**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Provides access to the cluster's [**Security Descriptor**](https://msdn.microsoft.com/library/aa369055) property.

</dd> <dt>

**SecurityLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the level of security that should apply to intracluster messages.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is read-only before Windows Server 2012.

The following are the possible values.

<dt>

<span id="Clear_Text"></span><span id="clear_text"></span><span id="CLEAR_TEXT"></span>

**Clear Text** (0)


</dt> <dd></dd> <dt>

<span id="Sign"></span><span id="sign"></span><span id="SIGN"></span>

**Sign** (1)


</dt> <dd></dd> <dt>

<span id="Encrypt"></span><span id="encrypt"></span><span id="ENCRYPT"></span>

**Encrypt** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**SharedVolumeCompatibleFilters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Certain classes of filter drivers may be flagged as incompatible with the direct I/O mode of shared volumes. This property is used to override cluster service determination of filters as incompatible. Compatible filter driver names are specified without the .sys extension.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**SharedVolumeIncompatibleFilters**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Certain classes of filter drivers may be incompatible with the direct I/O mode of shared volumes. This property is used to add filters to be deemed as incompatible for direct I/O. Incompatible filter driver names are specified without the .sys extension.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**SharedVolumeSecurityDescriptor**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls access to the CSV Meta Data Server volume for the user mode applications.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**SharedVolumesRoot**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Root directory from which the cluster shared volumes are linked.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

</dd> <dt>

**SharedVolumeVssWriterOperationTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

CSV VSS Writer operation timeout in seconds.

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**ShutdownTimeoutInMinutes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The maximum time in minutes allowed for cluster resources to come offline during cluster service shutdown.

**Windows Server 2008:  **

This property is not supported before Windows Server 2008 R2.

This property can have the following values.

Range: 0–1440

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (10)
</dt> </dl>

A string indicating the current status of the cluster. Various operational and non-operational statuses are defined. Operational statuses are "OK", "Degraded", "Stressed" and "Pred Fail". "Stressed" indicates that the Element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, etc. The condition "Pred Fail" (failure predicted) indicates that an Element is functioning properly but predicting a failure in the near future. An example is a SMART-enabled hard drive. Non-operational statuses can also be specified. These are "Error", "NonRecover", "Starting", "Stopping" and "Service". "NonRecover" indicates that a non-recoverable error has occurred. "Service" describes an Element being configured, maintained or cleaned, or otherwise administered. This status could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative task. Not all such work is on-line, yet the Element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> <dt>



 ("Stressed")


</dt> <dd></dd> <dt>



 ("NonRecover")


</dt> <dd></dd> </dl>

</dd> <dt>

**UseClientAccessNetworksForSharedVolumes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Whether the use of client access networks for cluster shared volumes feature of this cluster is enabled.

Possible values are.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (1)


</dt> <dd></dd> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>**Auto** (2)


</dt> <dd>

**Windows Server 2012 R2 and Windows Server 2012:  **

This value is not supported before Windows Server 2016.

</dd> </dl>

**Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012.

</dd> <dt>

**VirtualStorageArrayEnabled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is only supported in Windows Server 2012 R2.

</dd> <dt>

**VirtualStorageArrayIOLatencyThreshold**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is only supported in Windows Server 2012 R2.

</dd> <dt>

**VirtualStorageArrayNotificationInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is only supported in Windows Server 2012 R2.

</dd> <dt>

**VirtualStorageArrayStorageBusTypes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is only supported in Windows Server 2012 R2.

</dd> <dt>

**VirtualStorageArrayStorageOptFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Not supported.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is only supported in Windows Server 2012 R2.

</dd> <dt>

**WitnessDatabaseWriteTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the maximum time in seconds that a cluster database write to a witness can take before the write is abandoned.

</dd> <dt>

**WitnessDynamicWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The weight of the configured witness.

**Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This property is not supported before Windows Server 2012 R2.

</dd> <dt>

**WitnessRestartInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the witness restart interval.

</dd> </dl>

## Remarks

The **MSCluster\_Cluster** class is derived from the **CIM\_Cluster** class.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Cluster**](cim-cluster.md)
</dt> <dt>

[Failover Cluster Provider Reference](server-cluster-provider-reference.md)
</dt> </dl>

 

 





