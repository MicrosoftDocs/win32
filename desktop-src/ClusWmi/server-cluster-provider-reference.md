---
title: Failover Cluster Provider Reference
description: Allows you to manage failover clusters through WMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '00427606-dd8b-4450-9d93-d44f236d067c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Failover Cluster APIs Failover Cluster , provider reference"]
---

# Failover Cluster Provider Reference

The WMI provider for failover clusters (defined in ClusWmi.mof) allows you to manage failover clusters through Windows Management Instrumentation (WMI). This documentation assumes you are familiar with the concept of WMI and have experience writing WMI scripts and applications.

## In this section

<dl> <dt>

[**CIM\_Cluster**](cim-cluster.md)
</dt> <dd>

A class derived from ComputerSystem that 'is made up of' two or more ComputerSystems which operate together as an atomic, functional whole to increase the performance, resources and/or RAS (Reliability, Availability and Serviceability) of the component ComputerSystems, related to some aspects of these ComputerSystems.

</dd> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> <dd>

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

</dd> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dd>

A generic association used to establish 'part of' relationships between Managed System Elements. For example, the SystemComponent association defines parts of a System.

</dd> <dt>

[**CIM\_ComponentCS**](cim-componentcs.md)
</dt> <dd>

A ComputerSystem can aggregate another ComputerSystem. This association can be used to model MPP Systems with workstation frontends, an I2O subsystem embedded in a UnitaryComputerSystem, or a System that splits functionality between two processors, potentially running different OperatingSystems.

</dd> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> <dd>

A class derived from System that is a special collection of ManagedSystemElements. This collection provides compute capabilities and serves as aggregation point to associate one or more of the following elements: FileSystem, OperatingSystem, Processor and Memory (Volatile and/or NonVolatile Storage).

</dd> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dd>

CIM\_Dependency is a generic association used to establish dependency relationships between objects.

</dd> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dd>

CIM\_HostedService is an association between a Service and the System on which the functionality resides.

</dd> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dd>

An abstraction or emulation of a hardware entity, that may or may not be Realized in physical hardware.

</dd> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> <dd>

CIM\_LogicalElement is a base class for all the components of a System that represent abstract system components, such as Files, Processes, or system capabilities in the form of Logical Devices.

</dd> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dd>

CIM\_ManagedSystemElement is the base class for the System Element hierarchy. Membership Criteria: Any distinguishable component of a System is a candidate for inclusion in this class. Examples: software components, such as files; and devices, such as disk drives and controllers, and physical components such as chips and cards.

</dd> <dt>

[**CIM\_ParticipatingCS**](cim-participatingcs.md)
</dt> <dd>

A Cluster is composed of two or more ComputerSystems, operating together. A ComputerSystem may participate in multiple Clusters.

</dd> <dt>

[**CIM\_Service**](cim-service.md)
</dt> <dd>

A CIM\_Service is a Logical Element that contains the information necessary to represent and manage the functionality provided by a Device and/or SoftwareFeature. A Service is a general-purpose object to configure and manage the implementation of functionality. It is not the functionality itself.

</dd> <dt>

[**CIM\_System**](cim-system.md)
</dt> <dd>

A CIM\_System is a LogicalElement that aggregates an enumerable set of Managed System Elements. The aggregation operates as a functional whole. Within any particular subclass of System, there is a well-defined list of Managed System Element classes whose instances must be aggregated.

</dd> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dd>

CIM\_SystemComponent is a specialization of the CIM\_Component association that establishes 'part of' relationships between a System and the Managed System Elements of which it is composed.

</dd> <dt>

[**CIM\_SystemDevice**](cim-systemdevice.md)
</dt> <dd>

LogicalDevices may be aggregated by a System. This relationship is made explicit by the SystemDevice association.

</dd> <dt>

[**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md)
</dt> <dd>

A class derived from ComputerSystem that represents a Desktop, Mobile, NetPC, Server or other type of a single node Computer System.

</dd> <dt>

[**MSCluster\_AvailableDisk**](mscluster-availabledisk.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents an available disk.

</dd> <dt>

[**MSCluster\_AvailableDiskPartition**](mscluster-availablediskpartition.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents an available disk partition.

</dd> <dt>

[**MSCluster\_AvailableDiskToPartition**](mscluster-availabledisktopartition.md)
</dt> <dd>

Represents a list of the partitions on the available disk.

</dd> <dt>

[**MSCluster\_AvailableStoragePool**](mscluster-availablestoragepool.md)
</dt> <dd>

Describes the available storage pool.

The following syntax is simplified from MOF code and includes all inherited properties.

</dd> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> <dd>

a dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_ClusterDisk**](mscluster-clusterdisk.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk.

</dd> <dt>

[**MSCluster\_ClusterDiskPartition**](mscluster-clusterdiskpartition.md)
</dt> <dd>

The base class which provides the common properties for cluster disk partitions.

</dd> <dt>

[**MSCluster\_ClusterSharedVolume**](mscluster-clustersharedvolume.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a cluster shared volume

</dd> <dt>

[**MSCluster\_ClusterSharedVolumeToNode**](mscluster-clustersharedvolumetonode.md)
</dt> <dd>

A cluster shared volume has a node hosting the resource. This lists the cluster node hosting cluster shared volume resource.

</dd> <dt>

[**MSCluster\_ClusterSharedVolumeToPartition**](mscluster-clustersharedvolumetopartition.md)
</dt> <dd>

A cluster shared volume has a partition. This lists the cluster shared volume partition information.

</dd> <dt>

[**MSCluster\_ClusterSharedVolumeToResource**](mscluster-clustersharedvolumetoresource.md)
</dt> <dd>

A cluster shared volume has a resource associated with it. This lists the cluster resource which is the cluster shared volume.

</dd> <dt>

[**MSCluster\_ClusterToAvailableDisk**](mscluster-clustertoavailabledisk.md)
</dt> <dd>

Represents a list of the available disks contained in a cluster.

</dd> <dt>

[**MSCluster\_ClusterToClusterSharedVolume**](mscluster-clustertoclustersharedvolume.md)
</dt> <dd>

Represents a list of the available cluster shared volumes contained in a cluster.

</dd> <dt>

[**MSCluster\_ClusterToNetwork**](mscluster-clustertonetwork.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the networks the cluster uses for communication.

</dd> <dt>

[**MSCluster\_ClusterToNetworkInterface**](mscluster-clustertonetworkinterface.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the network interfaces the cluster has installed on the nodes it manages.

</dd> <dt>

[**MSCluster\_ClusterToNode**](mscluster-clustertonode.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that provides access to the nodes in a cluster.

</dd> <dt>

[**MSCluster\_ClusterToQuorumResource**](mscluster-clustertoquorumresource.md)
</dt> <dd>

A dynamic association[WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [quorum resource](https://msdn.microsoft.com/library/aa371819) of a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_ClusterToResource**](mscluster-clustertoresource.md)
</dt> <dd>

A dynamic association[WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [resources](https://msdn.microsoft.com/library/aa372152) in a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_ClusterToResourceGroup**](mscluster-clustertoresourcegroup.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that provides access to the groups in a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_ClusterToResourceType**](mscluster-clustertoresourcetype.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [groups](https://msdn.microsoft.com/library/aa369645) in the [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_ClusterUtilities**](mscluster-clusterutilities.md)
</dt> <dd>

Verifies whether a node is configured to support clustering.

</dd> <dt>

[**MSCluster\_Disk**](mscluster-disk.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk.

</dd> <dt>

[**MSCluster\_DiskPartition**](mscluster-diskpartition.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a disk partition.

</dd> <dt>

[**MSCluster\_DiskToDiskPartition**](mscluster-disktodiskpartition.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that represents a list of the disk partitions on a disk

</dd> <dt>

[**MSCluster\_Event**](mscluster-event.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a cluster event.

</dd> <dt>

[**MSCluster\_EventClusterCallback**](mscluster-eventclustercallback.md)
</dt> <dd>

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

</dd> <dt>

[**MSCluster\_EventGroupStateChange**](mscluster-eventgroupstatechange.md)
</dt> <dd>

Represents a [group](https://msdn.microsoft.com/library/aa369645) state change event.

</dd> <dt>

[**MSCluster\_EventObjectAdd**](mscluster-eventobjectadd.md)
</dt> <dd>

Represents an add object event. An add object event is generated when a cluster object is added to a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_EventObjectRemove**](mscluster-eventobjectremove.md)
</dt> <dd>

The [**MSCluster\_EventObjectRemove**](mscluster-eventobjectremove.md) class is a [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a remove object event. A remove object event is generated when a cluster object is removed from a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly).

</dd> <dt>

[**MSCluster\_EventPropertyChange**](mscluster-eventpropertychange.md)
</dt> <dd>

A [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a property change event. A property change event is generated when a cluster object property is changed.

</dd> <dt>

[**MSCluster\_EventRegistryChange**](mscluster-eventregistrychange.md)
</dt> <dd>

TBD

The following syntax is simplified from MOF code and includes all inherited properties.

</dd> <dt>

[**MSCluster\_EventResourceStateChange**](mscluster-eventresourcestatechange.md)
</dt> <dd>

A [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a resource state change event.

</dd> <dt>

[**MSCluster\_EventStateChange**](mscluster-eventstatechange.md)
</dt> <dd>

Represents a state change event. A state change event is generated when the state of a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) changes.

</dd> <dt>

[**MSCluster\_ExtendedStatus**](mscluster-extendedstatus.md)
</dt> <dd>

Contains the error type.

</dd> <dt>

[**MSCluster\_LogicalElement**](mscluster-logicalelement.md)
</dt> <dd>

A superclass for cluster objects that provide the **Flags** and **Characteristics** properties.

</dd> <dt>

[**MSCluster\_Network**](mscluster-network.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents cluster [networks](https://msdn.microsoft.com/library/aa371501).

</dd> <dt>

[**MSCluster\_NetworkInterface**](mscluster-networkinterface.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [network interface](https://msdn.microsoft.com/library/aa371519).

</dd> <dt>

[**MSCluster\_NetworkToNetworkInterface**](mscluster-networktonetworkinterface.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the network interfaces connected to a network.

</dd> <dt>

[**MSCluster\_Node**](mscluster-node.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [node](https://msdn.microsoft.com/library/aa371745).

</dd> <dt>

[**MSCluster\_NodeToActiveGroup**](mscluster-nodetoactivegroup.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [groups](https://msdn.microsoft.com/library/aa369645) active on a [node](https://msdn.microsoft.com/library/aa371745).

</dd> <dt>

[**MSCluster\_NodeToActiveResource**](mscluster-nodetoactiveresource.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [resources](https://msdn.microsoft.com/library/aa372152) active on a [node](https://msdn.microsoft.com/library/aa371745).

</dd> <dt>

[**MSCluster\_NodeToHostedService**](mscluster-nodetohostedservice.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a service managed by the [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) as a [resource](https://msdn.microsoft.com/library/aa372152).

</dd> <dt>

[**MSCluster\_NodeToNetworkInterface**](mscluster-nodetonetworkinterface.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [network interfaces](https://msdn.microsoft.com/library/aa371519) connected to a [node](https://msdn.microsoft.com/library/aa371745).

</dd> <dt>

[**MSCluster\_Property**](mscluster-property.md)
</dt> <dd>

An abstract [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that is a superclass for properties of cluster objects.

</dd> <dt>

[**MSCluster\_Resource**](mscluster-resource.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [resource](https://msdn.microsoft.com/library/aa372152).

</dd> <dt>

[**MSCluster\_ResourceGroup**](mscluster-resourcegroup.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [cluster](https://msdn.microsoft.com/library/aa369336#-wolf-cluster-gly) [group](https://msdn.microsoft.com/library/aa369645).

</dd> <dt>

[**MSCluster\_ResourceGroupToPreferredNode**](mscluster-resourcegrouptopreferrednode.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a list of the resource [groups](https://msdn.microsoft.com/library/aa369645) and their preferred [nodes](https://msdn.microsoft.com/library/aa371745) list.

</dd> <dt>

[**MSCluster\_ResourceGroupToResource**](mscluster-resourcegrouptoresource.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the resources in a group.

</dd> <dt>

[**MSCluster\_ResourceToDependentResource**](mscluster-resourcetodependentresource.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the dependencies of a resource.

</dd> <dt>

[**MSCluster\_ResourceToDisk**](mscluster-resourcetodisk.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that associates an instance of the [**MSCluster\_Resource**](mscluster-resource.md) class representing a disk resource to an instance of the [**MSCluster\_Disk**](mscluster-disk.md) class.

</dd> <dt>

[**MSCluster\_ResourceToDiskPartition**](mscluster-resourcetodiskpartition.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa371764#mscs-n---z-22-gly) that associates an instance of the [**MSCluster\_Resource**](mscluster-resource.md) class representing a disk resource to an instance of the [**MSCluster\_DiskPartition**](mscluster-diskpartition.md) class.

</dd> <dt>

[**MSCluster\_ResourceToPossibleOwner**](mscluster-resourcetopossibleowner.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a list of the resources and their possible owner nodes.

</dd> <dt>

[**MSCluster\_ResourceType**](mscluster-resourcetype.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents a [resource type](https://msdn.microsoft.com/library/aa372279).

</dd> <dt>

[**MSCluster\_ResourceTypeToPossibleOwner**](mscluster-resourcetypetopossibleowner.md)
</dt> <dd>

Lists nodes which are capable of hosting the particular resource type.

</dd> <dt>

[**MSCluster\_ResourceTypeToResource**](mscluster-resourcetypetoresource.md)
</dt> <dd>

A dynamic association [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents resources of a particular type.

</dd> <dt>

[**MSCluster\_Service**](mscluster-service.md)
</dt> <dd>

A dynamic [WMI class](https://msdn.microsoft.com/library/aa373136#-wolf-wmi-class-gly) that represents the [Cluster service](https://msdn.microsoft.com/library/aa369163).

</dd> <dt>

[**MSCluster\_ValidationStatus**](mscluster-validationstatus.md)
</dt> <dd>

Provides methods for generating the validation report file name as well as retrieving the result of the cluster or node validation.

</dd> </dl>

 

 




