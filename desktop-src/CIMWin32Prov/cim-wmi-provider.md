---
description: These WMI classes are declared in CimWin32.mof.
ms.assetid: 53122499-1CC0-4B48-AEA1-B70B7BBC3A99
ms.tgt_platform: multiple
title: CIM WMI Provider
ms.topic: article
ms.date: 05/31/2018
---

# CIM WMI Provider

These WMI classes are declared in CimWin32.mof.

## In this section

<dl> <dt>

[**CIM\_Action**](cim-action.md)
</dt> <dd>

A [**CIM\_Action**](cim-action.md) class is an operation that is part of a process to either create a software element in its next state or to eliminate the software element in the current state.

</dd> <dt>

[**CIM\_ActionSequence**](cim-actionsequence.md)
</dt> <dd>

The [**CIM\_ActionSequence**](cim-actionsequence.md) association defines a series of operations that transition the software element (referenced by the [**CIM\_SoftwareElementActions**](cim-softwareelementactions.md) association) to its next state, or removes the software element from its current state.

</dd> <dt>

[**CIM\_ActsAsSpare**](cim-actsasspare.md)
</dt> <dd>

The [**CIM\_ActsAsSpare**](cim-actsasspare.md) association indicates which elements can be spares or replace other aggregated elements. A spare can operate in "hot-standby" mode as specified on an element-by-element basis.

</dd> <dt>

[**CIM\_AdjacentSlots**](cim-adjacentslots.md)
</dt> <dd>

The [**CIM\_AdjacentSlots**](cim-adjacentslots.md) association describes the layout of slots on a hosting board or adapter card. Information, such as the distance between the slots and whether they are "shared" (if one is populated, then the other slot cannot be used), is conveyed as association properties.

</dd> <dt>

[**CIM\_AggregatePExtent**](cim-aggregatepextent.md)
</dt> <dd>

The [**CIM\_AggregatePExtent**](cim-aggregatepextent.md) class provides summary information about addressable logical blocks, which are in the same storage redundancy group and located on the same physical media.

</dd> <dt>

[**CIM\_AggregatePSExtent**](cim-aggregatepsextent.md)
</dt> <dd>

The [**CIM\_AggregatePSExtent**](cim-aggregatepsextent.md) class defines the number of addressable logical blocks on a single storage device, excluding logical blocks mapped as check data. If volume sets are defined, the logical blocks are contained within a single volume set. This is an alternative grouping for [**CIM\_ProtectedSpaceExtent**](cim-protectedspaceextent.md), when only summary information is needed or when automatic configuration is used.

</dd> <dt>

[**CIM\_AggregateRedundancyComponent**](cim-aggregateredundancycomponent.md)
</dt> <dd>

The [**CIM\_AggregateRedundancyComponent**](cim-aggregateredundancycomponent.md) class describes the aggregate physical extent in a storage redundancy group.

</dd> <dt>

[**CIM\_AlarmDevice**](cim-alarmdevice.md)
</dt> <dd>

The [**CIM\_AlarmDevice**](cim-alarmdevice.md) class is an alarm device that emits audible or visible indications related to a problem situation.

</dd> <dt>

[**CIM\_AllocatedResource**](cim-allocatedresource.md)
</dt> <dd>

The [**CIM\_AllocatedResource**](cim-allocatedresource.md) class represents an association between logical devices and system resources and indicates that the resource is assigned to the device.

</dd> <dt>

[**CIM\_ApplicationSystem**](cim-applicationsystem.md)
</dt> <dd>

The [**CIM\_ApplicationSystem**](cim-applicationsystem.md) class represents an application or software system that supports a particular business function that can be managed as an independent unit. Such a system can be decomposed into its functional components using the [**CIM\_SoftwareFeature**](cim-softwarefeature.md) class. The software features for a particular application or software system are located using the [**CIM\_ApplicationSystemSoftwareFeature**](cim-applicationsystemsoftwarefeature.md) association.

</dd> <dt>

[**CIM\_ApplicationSystemSoftwareFeature**](cim-applicationsystemsoftwarefeature.md)
</dt> <dd>

The [**CIM\_ApplicationSystemSoftwareFeature**](cim-applicationsystemsoftwarefeature.md) class represents an association that identifies the software features that make up a particular application system. The software features can be included in different products.

</dd> <dt>

[**CIM\_AssociatedAlarm**](cim-associatedalarm.md)
</dt> <dd>

The [**CIM\_AssociatedAlarm**](cim-associatedalarm.md) dependency associates an alarm with a logical device.

</dd> <dt>

[**CIM\_AssociatedBattery**](cim-associatedbattery.md)
</dt> <dd>

The [**CIM\_AssociatedBattery**](cim-associatedbattery.md) dependency associates a battery with a logical device. Use this association to model individual batteries that make up an uninterruptible power supply (UPS).

</dd> <dt>

[**CIM\_AssociatedCooling**](cim-associatedcooling.md)
</dt> <dd>

The [**CIM\_AssociatedCooling**](cim-associatedcooling.md) association indicates when fans or other cooling devices are specific to a device (versus providing enclosure or cabinet cooling).

</dd> <dt>

[**CIM\_AssociatedMemory**](cim-associatedmemory.md)
</dt> <dd>

The [**CIM\_AssociateMemory**](cim-associatedmemory.md) class associates installed or associated memory, such as cache memory with a logical device.

</dd> <dt>

[**CIM\_AssociatedProcessorMemory**](cim-associatedprocessormemory.md)
</dt> <dd>

The [**CIM\_AssociatedProcessorMemory**](cim-associatedprocessormemory.md) class associates the processor and system memory, or a processor's cache.

</dd> <dt>

[**CIM\_AssociatedSensor**](cim-associatedsensor.md)
</dt> <dd>

The [**CIM\_AssociatedSensor**](cim-associatedsensor.md) class associates an installed sensor with a logical device. The sensor measures critical input and output properties, and can be included with the device or installed nearby.

</dd> <dt>

[**CIM\_AssociatedSupplyCurrentSensor**](cim-associatedsupplycurrentsensor.md)
</dt> <dd>

The [**CIM\_AssociatedSupplyCurrentSensor**](cim-associatedsupplycurrentsensor.md) class associates a power supply with a current (amperage) sensor that monitors its input frequency.

</dd> <dt>

[**CIM\_AssociatedSupplyVoltageSensor**](cim-associatedsupplyvoltagesensor.md)
</dt> <dd>

Associates a power supply with a voltage sensor that monitors its input voltage.

</dd> <dt>

[**CIM\_BasedOn**](cim-basedon.md)
</dt> <dd>

The [**CIM\_BasedOn**](cim-basedon.md) class represents an association that describes how storage extents can be assembled from lower-level extents. For example, physical extents include protected space extents. Thus, volume sets are assembled from one or more physical or protected space extents. Cache memory can be defined independently and realized in a physical element, or it can be based on volatile or non-volatile storage extents.

</dd> <dt>

[**CIM\_Battery**](cim-battery.md)
</dt> <dd>

The [**CIM\_Battery**](cim-battery.md) class represents the capabilities and management of the battery logical device. This class applies to batteries in laptop systems and other internal and external batteries.

</dd> <dt>

[**CIM\_BinarySensor**](cim-binarysensor.md)
</dt> <dd>

The [**CIM\_BinarySensor**](cim-binarysensor.md) class provides a Boolean output. The **CurrentState** and **PossibleStates** properties were added for sensoring, thus making the **CIM\_BinarySensor** subclass no longer necessary, although, it is retained for backward compatibility. A binary sensor can be created by instantiating a sensor with two possible states.

</dd> <dt>

[**CIM\_BIOSElement**](cim-bioselement.md)
</dt> <dd>

The [**CIM\_BIOSElement**](cim-bioselement.md) class represents the low-level software that is loaded into non-volatile storage and used to start and configure a computer system.

</dd> <dt>

[**CIM\_BIOSFeature**](cim-biosfeature.md)
</dt> <dd>

represents the capabilities of the low-level software that is used to start and configure a computer system.

</dd> <dt>

[**CIM\_BIOSFeatureBIOSElements**](cim-biosfeaturebioselements.md)
</dt> <dd>

The [**CIM\_BIOSFeatureBIOSElements**](cim-biosfeaturebioselements.md) class associates a BIOS feature and its aggregated BIOS elements.

</dd> <dt>

[**CIM\_BIOSLoadedInNV**](cim-biosloadedinnv.md)
</dt> <dd>

The [**CIM\_BIOSLoadedInNV**](cim-biosloadedinnv.md) class associates a BIOS element and the non-volatile storage in which it is loaded.

</dd> <dt>

[**CIM\_BootOSFromFS**](cim-bootosfromfs.md)
</dt> <dd>

The [**CIM\_BootOSFromFS**](cim-bootosfromfs.md) class associates the operating system and the file systems from which the operating system is loaded. The association is many-to-many; a distributed operating system can depend on several file systems to load correctly and completely.

</dd> <dt>

[**CIM\_BootSAP**](cim-bootsap.md)
</dt> <dd>

The [**CIM\_BootSAP**](cim-bootsap.md) class represents the access points of a boot service.

</dd> <dt>

[**CIM\_BootService**](cim-bootservice.md)
</dt> <dd>

The [**CIM\_BootService**](cim-bootservice.md) class represents the functionality provided by a device or software, or by a network, to load an operating system on a unitary computer system.

</dd> <dt>

[**CIM\_BootServiceAccessBySAP**](cim-bootserviceaccessbysap.md)
</dt> <dd>

The [**CIM\_BootServiceAccessBySAP**](cim-bootserviceaccessbysap.md) class associates a boot service and its access points.

</dd> <dt>

[**CIM\_CacheMemory**](cim-cachememory.md)
</dt> <dd>

The [**CIM\_CacheMemory**](cim-cachememory.md) class defines the capabilities and management of cache memory.

</dd> <dt>

[**CIM\_Card**](cim-card.md)
</dt> <dd>

The [**CIM\_Card**](cim-card.md) class represents a type of physical container that can be plugged into another card or hosting board, or is itself a hosting board/motherboard in a chassis. This class includes any package that is capable of carrying signals and providing a mounting point for physical components, such as chips or other physical packages, such as other cards.

</dd> <dt>

[**CIM\_CardInSlot**](cim-cardinslot.md)
</dt> <dd>

The [**CIM\_CardInSlot**](cim-cardinslot.md) class associates an adapter card with the container into which it is inserted.

</dd> <dt>

[**CIM\_CardOnCard**](cim-cardoncard.md)
</dt> <dd>

The [**CIM\_CardOnCard**](cim-cardoncard.md) association describes relationships about cards that can be plugged into motherboards/baseboards, daughtercards of an adapter, or cards that support special card-like modules.

</dd> <dt>

[**CIM\_CDROMDrive**](cim-cdromdrive.md)
</dt> <dd>

The [**CIM\_CDROMDrive**](cim-cdromdrive.md) class represents a CD-ROM drive on the computer.

</dd> <dt>

[**CIM\_Chassis**](cim-chassis.md)
</dt> <dd>

The [**CIM\_Chassis**](cim-chassis.md) class represents the physical elements that enclose other elements and provide definable functionality, such as a desktop, processing node, UPS, disk or tape storage, or a combination of these.

</dd> <dt>

[**CIM\_ChassisInRack**](cim-chassisinrack.md)
</dt> <dd>

The [**CIM\_ChassisInRack**](cim-chassisinrack.md) association represents the "containing" relationship between a rack and a chassis that it contains.

</dd> <dt>

[**CIM\_Check**](cim-check.md)
</dt> <dd>

The [**CIM\_Check**](cim-check.md) class represents a condition or characteristic that is expected to be true in an environment defined or scoped by an instance of a [**CIM\_ComputerSystem**](cim-computersystem.md) class. The checks associated with a particular software element are organized into one of two groups using the **Phase** property of the [**CIM\_SoftwareElementChecks**](cim-softwareelementchecks.md) association.

</dd> <dt>

[**CIM\_Chip**](cim-chip.md)
</dt> <dd>

The [**CIM\_Chip**](cim-chip.md) class represents the type of integrated circuit hardware, including ASICs, processors, memory chips, and so on.

</dd> <dt>

[**CIM\_ClusteringSAP**](cim-clusteringsap.md)
</dt> <dd>

The [**CIM\_ClusteringSAP**](cim-clusteringsap.md) class represents the access points of a clustering service.

</dd> <dt>

[**CIM\_ClusteringService**](cim-clusteringservice.md)
</dt> <dd>

The [**CIM\_ClusteringService**](cim-clusteringservice.md) class represents the functionality provided by a cluster. For example, failover functionality can be modeled as a service of a failover cluster.

</dd> <dt>

[**CIM\_ClusterServiceAccessBySAP**](cim-clusterserviceaccessbysap.md)
</dt> <dd>

The [**CIM\_ClusterServiceAccessBySAP**](cim-clusterserviceaccessbysap.md) class represents the relationship between a clustering service and its access points.

</dd> <dt>

[**CIM\_CollectedCollections**](cim-collectedcollections.md)
</dt> <dd>

The [**CIM\_CollectedCollections**](cim-collectedcollections.md) class is an aggregation association that represents a collection of Managed System Elements (MSE) contained in a collection of MSEs.

</dd> <dt>

[**CIM\_CollectedMSEs**](cim-collectedmses.md)
</dt> <dd>

The [**CIM\_CollectedMSEs**](cim-collectedmses.md) association class represents the members of the grouping object, a [**CollectionOfMSEs**](cim-collectionofmses.md) class.

</dd> <dt>

[**CIM\_CollectionOfMSEs**](cim-collectionofmses.md)
</dt> <dd>

The [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) object allows the grouping of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects for the purpose of associating settings and configurations. It is abstract to require further definition and semantic refinement in subclasses.

</dd> <dt>

[**CIM\_CollectionOfSensors**](cim-collectionofsensors.md)
</dt> <dd>

The [**CIM\_CollectionOfSensors**](cim-collectionofsensors.md) association represents the binary sensors that make up the multistate sensor.

</dd> <dt>

[**CIM\_CollectionSetting**](cim-collectionsetting.md)
</dt> <dd>

The [**CIM\_CollectionSetting**](cim-collectionsetting.md) class represents the association between a [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) and the setting class defined for them.

</dd> <dt>

[**CIM\_CompatibleProduct**](cim-compatibleproduct.md)
</dt> <dd>

The [**CIM\_CompatibleProduct**](cim-compatibleproduct.md) class represents an association between products that indicates whether two referenced products are interoperable, such as whether they can be installed together, or whether one can be the physical container for the other, and so on.

</dd> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dd>

The [**CIM\_Component**](cim-component.md) association represents the parts of a relationship between MSEs.

</dd> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> <dd>

A [**CIM\_ComputerSystem**](cim-computersystem.md) class represents a special collection of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) instances. This collection provides computer capabilities and serves as an aggregation point to associate one or more of the following elements: file system, operating system, processor and memory (volatile and non-volatile storage). This class is derived from [**CIM\_System**](cim-system.md).

</dd> <dt>

[**CIM\_ComputerSystemDMA**](cim-computersystemdma.md)
</dt> <dd>

The [**CIM\_ComputerSystemDMA**](cim-computersystemdma.md) class represents an association between a computer system and its available direct memory access (DMA) channels.

</dd> <dt>

[**CIM\_ComputerSystemIRQ**](cim-computersystemirq.md)
</dt> <dd>

The [**CIM\_ComputerSystemIRQ**](cim-computersystemirq.md) class represents an association between a computer system and its available interrupt request lines (IRQs).

</dd> <dt>

[**CIM\_ComputerSystemMappedIO**](cim-computersystemmappedio.md)
</dt> <dd>

The [**CIM\_ComputerSystemMappedIO**](cim-computersystemmappedio.md) class represents an association between a computer system and its available memory-mapped I/O ports.

</dd> <dt>

[**CIM\_ComputerSystemPackage**](cim-computersystempackage.md)
</dt> <dd>

The [**CIM\_ComputerSystemPackage**](cim-computersystempackage.md) class represents an association that explicitly defines the relationship between unitary computer systems and one or more physical packages. The association is similar to the way that logical devices are realized by physical elements.

</dd> <dt>

[**CIM\_ComputerSystemResource**](cim-computersystemresource.md)
</dt> <dd>

The [**CIM\_ComputerSystemResource**](cim-computersystemresource.md) class represents an association between a computer system and its available system resources.

</dd> <dt>

[**CIM\_Configuration**](cim-configuration.md)
</dt> <dd>

The [**CIM\_Configuration**](cim-configuration.md) object allows the grouping of parameter sets (defined in [**CIM\_Setting**](cim-setting.md) objects) and dependencies for one or more managed system elements.

</dd> <dt>

[**CIM\_ConnectedTo**](cim-connectedto.md)
</dt> <dd>

The [**CIM\_ConnectedTo**](cim-connectedto.md) class represents an association that indicates that two or more physical connectors are connected.

</dd> <dt>

[**CIM\_ConnectorOnPackage**](cim-connectoronpackage.md)
</dt> <dd>

The [**CIM\_ConnectorOnPackage**](cim-connectoronpackage.md) class represents an association that makes explicit the containment relationship between connectors and packages. Physical packages contain connectors as well as other physical elements.

</dd> <dt>

[**CIM\_Container**](cim-container.md)
</dt> <dd>

The [**CIM\_Container**](cim-container.md) class represents an association between a contained and a containing physical element. A containing object must be a physical package.

</dd> <dt>

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dd>

The [**CIM\_ControlledBy**](cim-controlledby.md) relationship indicates which devices are commanded by, or accessed through, the controller logical device.

</dd> <dt>

[**CIM\_Controller**](cim-controller.md)
</dt> <dd>

The [**CIM\_Controller**](cim-controller.md) class is a parent class for grouping miscellaneous control-related devices. Examples of controllers are SCSI controllers, USB controllers, and serial controllers.

</dd> <dt>

[**CIM\_CoolingDevice**](cim-coolingdevice.md)
</dt> <dd>

The [**CIM\_CoolingDevice**](cim-coolingdevice.md) class represents the capabilities and management of cooling devices.

</dd> <dt>

[**CIM\_CopyFileAction**](cim-copyfileaction.md)
</dt> <dd>

The [**CIM\_CopyFileAction**](cim-copyfileaction.md) class represents moving or copying files from a computer system to a new location.

</dd> <dt>

[**CIM\_CreateDirectoryAction**](cim-createdirectoryaction.md)
</dt> <dd>

The [**CIM\_CreateDirectoryAction**](cim-createdirectoryaction.md) class creates empty directories for software elements to be installed locally.

</dd> <dt>

[**CIM\_CurrentSensor**](cim-currentsensor.md)
</dt> <dd>

The [**CIM\_CurrentSensor**](cim-currentsensor.md) class exists for backward compatibility to earlier CIM schema definitions.

</dd> <dt>

[**CIM\_DataFile**](cim-datafile.md)
</dt> <dd>

The [**CIM\_DataFile**](cim-datafile.md) class represents a named collection of data or executable code. Only instances of files on local fixed disks will be returned

</dd> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dd>

The [**CIM\_Dependency**](cim-dependency.md) class represents an association that establishes dependency relationships between objects.

</dd> <dt>

[**CIM\_DependencyContext**](cim-dependencycontext.md)
</dt> <dd>

The [**CIM\_DependencyContext**](cim-dependencycontext.md) relationship associates a [**CIM\_Dependency**](cim-dependency.md) class with one or more [**CIM\_Configuration**](cim-configuration.md) objects. For example, a computer system's dependencies can change based on the network to which the system is attached.

</dd> <dt>

[**CIM\_DesktopMonitor**](cim-desktopmonitor.md)
</dt> <dd>

The [**CIM\_DesktopMonitor**](cim-desktopmonitor.md) class represents the capabilities and management of the desktop monitor (CRT) logical device.

</dd> <dt>

[**CIM\_DeviceAccessedByFile**](cim-deviceaccessedbyfile.md)
</dt> <dd>

The [**CIM\_DeviceAccessedByFile**](cim-deviceaccessedbyfile.md) association class specifies the logical device accessed by using the referenced [**CIM\_DeviceFile**](cim-devicefile.md) class.

</dd> <dt>

[**CIM\_DeviceConnection**](cim-deviceconnection.md)
</dt> <dd>

The [**CIM\_DeviceConnection**](cim-deviceconnection.md) association class represents two or more connected devices.

</dd> <dt>

[**CIM\_DeviceErrorCounts**](cim-deviceerrorcounts.md)
</dt> <dd>

The [**CIM\_DeviceErrorCounts**](cim-deviceerrorcounts.md) class is a statistical class that contains error-related counters for a logical device. The types of errors are defined by CCITT (Rec X.733) and ISO (IEC 10164-4).

</dd> <dt>

[**CIM\_DeviceFile**](cim-devicefile.md)
</dt> <dd>

The [**CIM\_DeviceFile**](cim-devicefile.md) class represents a type of logical file, which represents a device. This convention is useful for operating systems that manage devices using a byte stream I/O model. The logical device that is associated with this file is specified using the [**CIM\_DeviceAccessedByFile**](cim-deviceaccessedbyfile.md) relationship.

</dd> <dt>

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> <dd>

The [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md) class represents an association between a service access point (SAP) and how it is implemented. When many logical devices are associated with one SAP, the elements operate in conjunction to provide the access point. If different implementations of a SAP exist, each implementation results in individual instantiations of the SAP object.

</dd> <dt>

[**CIM\_DeviceServiceImplementation**](cim-deviceserviceimplementation.md)
</dt> <dd>

The [**CIM\_DeviceServiceImplementation**](cim-deviceserviceimplementation.md) class represents an association between a service and how it is implemented. When multiple devices are associated with one service, the elements operate in conjunction to provide the service. If different implementations of a service exist, each implementation results in individual instantiations of the service object.

</dd> <dt>

[**CIM\_DeviceSoftware**](cim-devicesoftware.md)
</dt> <dd>

The [**CIM\_DeviceSoftware**](cim-devicesoftware.md) relationship identifies software that is associated with a device, such as drivers, configuration or application software, or firmware.

</dd> <dt>

[**CIM\_Directory**](cim-directory.md)
</dt> <dd>

The [**CIM\_Directory**](cim-directory.md) class represents a file type that logically groups the data files that it contains and provides path information for the grouped files.

</dd> <dt>

[**CIM\_DirectoryAction**](cim-directoryaction.md)
</dt> <dd>

The [**CIM\_DirectoryAction**](cim-directoryaction.md) abstract class manages directories. Directory creation is handled by the [**CIM\_CreateDirectoryAction**](cim-createdirectoryaction.md) class and directory removal is handled by the [**CIM\_RemoveDirectoryAction**](cim-removedirectoryaction.md) class.

</dd> <dt>

[**CIM\_DirectoryContainsFile**](cim-directorycontainsfile.md)
</dt> <dd>

The [**CIM\_DirectoryContainsFile**](cim-directorycontainsfile.md) class represents an association between a directory and files contained within that directory.

</dd> <dt>

[**CIM\_DirectorySpecification**](cim-directoryspecification.md)
</dt> <dd>

The [**CIM\_DirectorySpecification**](cim-directoryspecification.md) class captures the major directory structure of a software element. This class is used to organize the files of a software element into manageable units that can be relocated on a computer system.

</dd> <dt>

[**CIM\_DirectorySpecificationFile**](cim-directoryspecificationfile.md)
</dt> <dd>

The [**CIM\_DirectorySpecificationFile**](cim-directoryspecificationfile.md) association represents the directory that contains the file specified by referencing the [**CIM\_DirectorySpecification**](cim-directoryspecification.md) class.

</dd> <dt>

[**CIM\_DiscreteSensor**](cim-discretesensor.md)
</dt> <dd>

The [**CIM\_DiscreteSensor**](cim-discretesensor.md) class has a set of legal string values that it can report. The values are enumerated in the sensor's **PossibleValues** property. A discrete sensor always has a current reading that corresponds to one of the enumerated values.

</dd> <dt>

[**CIM\_DiskDrive**](cim-diskdrive.md)
</dt> <dd>

The [**CIM\_DiskDrive**](cim-diskdrive.md) class represents a physical disk drive as seen by the operating system. The disk drive features correspond to the logical and management characteristics of the drive, and in some cases, may not reflect the physical characteristics of the device. An interface to a physical drive is a member of this class. However, an object based on another logical device is not a member of this class.

</dd> <dt>

[**CIM\_DisketteDrive**](cim-diskettedrive.md)
</dt> <dd>

The [**CIM\_DisketteDrive**](cim-diskettedrive.md) class represents the capabilities and management of a diskette drive.

</dd> <dt>

[**CIM\_DiskPartition**](cim-diskpartition.md)
</dt> <dd>

The [**CIM\_DiskPartition**](cim-diskpartition.md) class represents a contiguous range of logical blocks that is identifiable by the operating system by way of the partition's type and subtype fields. Disk partitions should be directly realized by physical media (indicated by the [**CIM\_RealizesDiskPartition**](cim-realizesdiskpartition.md) association) or built on storage volumes.

</dd> <dt>

[**CIM\_DiskSpaceCheck**](cim-diskspacecheck.md)
</dt> <dd>

The [**CIM\_DiskSpaceCheck**](cim-diskspacecheck.md) class checks the system's amount of available disk space and specifies it in the **AvailableDiskSpace** property. Details are compared with the value in the **AvailableSpace** property of the [**CIM\_FileSystem**](cim-filesystem.md) object that is associated with the [**CIM\_ComputerSystem**](cim-computersystem.md) object, which describes the system environment. When the value of the **AvailableSpace** property is greater than or equal to the value specified in the **AvailableDiskSpace** property, the condition is satisfied.

</dd> <dt>

[**CIM\_Display**](cim-display.md)
</dt> <dd>

The [**CIM\_Display**](cim-display.md) class is a parent class for grouping miscellaneous display devices.

</dd> <dt>

[**CIM\_DMA**](cim-dma.md)
</dt> <dd>

The [**CIM\_DMA**](cim-dma.md) class represents computer architecture direct memory access (DMA).

</dd> <dt>

[**CIM\_Docked**](cim-docked.md)
</dt> <dd>

The [**CIM\_Docked**](cim-docked.md) association represents the relationship between two chassis. For example, a laptop (a type of chassis) can be docked in a docking station (another type of chassis). This typical relationship is explicitly described.

</dd> <dt>

[**CIM\_ElementCapacity**](cim-elementcapacity.md)
</dt> <dd>

The [**CIM\_ElementCapacity**](cim-elementcapacity.md) class associates a [**CIM\_PhysicalCapacity**](cim-physicalcapacity.md) object with one or more physical elements. It associates a description of the minimum and maximum hardware requirements (or capabilities) to the physical elements being described.

</dd> <dt>

[**CIM\_ElementConfiguration**](cim-elementconfiguration.md)
</dt> <dd>

The [**CIM\_ElementConfiguration**](cim-elementconfiguration.md) association relates a [**CIM\_Configuration**](cim-configuration.md) object to one or more managed system elements. The **CIM\_Configuration** object represents a certain behavior, or a desired functional state for the associated [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

[**CIM\_ElementSetting**](cim-elementsetting.md)
</dt> <dd>

The [**CIM\_ElementSetting**](cim-elementsetting.md) class represents the association between managed system elements and the setting class defined for them.

</dd> <dt>

[**CIM\_ElementsLinked**](cim-elementslinked.md)
</dt> <dd>

The [**CIM\_ElementsLinked**](cim-elementslinked.md) association represents physical elements that are cabled together by a physical link.

</dd> <dt>

[**CIM\_ErrorCountersForDevice**](cim-errorcountersfordevice.md)
</dt> <dd>

The [**CIM\_ErrorCountersForDevice**](cim-errorcountersfordevice.md) class associates the [**CIM\_DeviceErrorCounts**](cim-deviceerrorcounts.md) class to the logical device to which it applies.

</dd> <dt>

[**CIM\_ExecuteProgram**](cim-executeprogram.md)
</dt> <dd>

The [**CIM\_ExecuteProgram**](cim-executeprogram.md) class represents files that can be executed on the system where the software element is installed.

</dd> <dt>

[**CIM\_Export**](cim-export.md)
</dt> <dd>

The [**CIM\_Export**](cim-export.md) class represents an association between a local file system and its directories, which indicate that the specified directories are available for mount. When exporting an entire file system, the directory should reference the topmost directory of the file system.

</dd> <dt>

[**CIM\_ExtraCapacityGroup**](cim-extracapacitygroup.md)
</dt> <dd>

The [**CIM\_ExtraCapacityGroup**](cim-extracapacitygroup.md) class is derived from a redundancy group that indicates the aggregated elements have more capacity or capability than is needed. An example of this type of redundancy is the installation of N+1 power supplies or fans in a system.

</dd> <dt>

[**CIM\_Fan**](cim-fan.md)
</dt> <dd>

The [**CIM\_Fan**](cim-fan.md) class represents the capabilities and management of a fan cooling device.

</dd> <dt>

[**CIM\_FileAction**](cim-fileaction.md)
</dt> <dd>

The [**CIM\_FileAction**](cim-fileaction.md) class allows the author to locate files that already exist on a user's computer, and then move or copy those files to a new location.

</dd> <dt>

[**CIM\_FileSpecification**](cim-filespecification.md)
</dt> <dd>

The [**CIM\_FileSpecification**](cim-filespecification.md) class represents a file that is either on or off of the system. The file is located in the directory identified by the [**CIM\_DirectorySpecificationFile**](cim-directoryspecificationfile.md) association. The [**Invoke**](invoke-method-in-class-cim-filespecification.md) method uses the information to check for the file's existence. Note that properties with a **Null** value are not checked.

</dd> <dt>

[**CIM\_FileStorage**](cim-filestorage.md)
</dt> <dd>

The [**CIM\_FileStorage**](cim-filestorage.md) association links the file system and the logical files addressed through the file system.

</dd> <dt>

[**CIM\_FileSystem**](cim-filesystem.md)
</dt> <dd>

The [**CIM\_FileSystem**](cim-filesystem.md) class represents a file or data set local to a computer system or remotely mounted from a file server.

</dd> <dt>

[**CIM\_FlatPanel**](cim-flatpanel.md)
</dt> <dd>

The [**CIM\_FlatPanel**](cim-flatpanel.md) class represents the capabilities and management of the flat panel logical device.

</dd> <dt>

[**CIM\_FromDirectoryAction**](cim-fromdirectoryaction.md)
</dt> <dd>

The [**CIM\_FromDirectoryAction**](cim-fromdirectoryaction.md) association identifies the source directory for the file action. When this association is used, the assumption is that the source directory was created by a previous action. This association cannot exist with a [**CIM\_FromDirectorySpecification**](cim-fromdirectoryspecification.md) association; a file action can only involve a single source directory.

</dd> <dt>

[**CIM\_FromDirectorySpecification**](cim-fromdirectoryspecification.md)
</dt> <dd>

The [**CIM\_FromDirectorySpecification**](cim-fromdirectoryspecification.md) association identifies the source directory for the file action. When this association is used, the assumption is that the source directory already exists. This association cannot exist with a [**CIM\_FromDirectoryAction**](cim-fromdirectoryaction.md) association; a file action can only involve a single source directory.

</dd> <dt>

[**CIM\_FRU**](cim-fru.md)
</dt> <dd>

The [**CIM\_FRU**](cim-fru.md) class represents a vendor-defined collection of products and physical elements that are associated with a field replaceable unit (FRU) to support, maintain, or upgrade a product at the customer's location.

</dd> <dt>

[**CIM\_FRUIncludesProduct**](cim-fruincludesproduct.md)
</dt> <dd>

The [**CIM\_FRUIncludesProduct**](cim-fruincludesproduct.md) class indicates that a field replaceable unit (FRU) may be composed of other products.

</dd> <dt>

[**CIM\_FRUPhysicalElements**](cim-fruphysicalelements.md)
</dt> <dd>

The [**CIM\_FRUPhysicalElements**](cim-fruphysicalelements.md) class represents the physical elements that make up a field replaceable unit (FRU).

</dd> <dt>

[**CIM\_HeatPipe**](cim-heatpipe.md)
</dt> <dd>

The [**CIM\_HeatPipe**](cim-heatpipe.md) class represents the capabilities and management of a heat pipe cooling device.

</dd> <dt>

[**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md)
</dt> <dd>

The [**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md) class represents an association between a service access point (SAP) and the system on which it is provided. Each system may host many SAPs.

</dd> <dt>

[**CIM\_HostedBootSAP**](cim-hostedbootsap.md)
</dt> <dd>

The [**CIM\_HostedBootSAP**](cim-hostedbootsap.md) class defines the hosting unitary computer system for a [**CIM\_BootSAP**](cim-bootsap.md) class. Since this relationship is subclassed from [**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md), it inherits the scoping/naming scheme defined for [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md), where an access point defers to its hosting system. In this case, **CIM\_BootSAP** must defer to its hosting [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md) class.

</dd> <dt>

[**CIM\_HostedBootService**](cim-hostedbootservice.md)
</dt> <dd>

The [**CIM\_HostedBootService**](cim-hostedbootservice.md) class associates a hosting system and a boot service. Since this relationship is subclassed from [**CIM\_HostedService**](cim-hostedservice.md), it inherits the scoping/naming scheme defined for service, where a service defers to its hosting system.

</dd> <dt>

[**CIM\_HostedFileSystem**](cim-hostedfilesystem.md)
</dt> <dd>

The [**CIM\_HostedFileSystem**](cim-hostedfilesystem.md) association represents a link between the computer system and the file system hosted on the computer system.

</dd> <dt>

[**CIM\_HostedJobDestination**](cim-hostedjobdestination.md)
</dt> <dd>

The [**CIM\_HostedJobDestination**](cim-hostedjobdestination.md) class represents an association between a job destination and the system on which it resides. A system may host many job queues. Job destinations defer to the hosting system.

</dd> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dd>

The [**CIM\_HostedService**](cim-hostedservice.md) class represents an association between a service and the system on which the functionality resides. A system may host many services, which defer to the hosting system. The model does not represent services hosted across multiple systems.

</dd> <dt>

[**CIM\_InfraredController**](cim-infraredcontroller.md)
</dt> <dd>

The [**CIM\_InfraredController**](cim-infraredcontroller.md) class represents the capabilities and management of an infrared controller.

</dd> <dt>

[**CIM\_InstalledOS**](cim-installedos.md)
</dt> <dd>

The [**CIM\_InstalledOS**](cim-installedos.md) association class represents a link between the computer system and the installed operating system. An operating system is installed when it is in a computer system's storage extent (for example, copied to a disk drive or downloaded to memory).

</dd> <dt>

[**CIM\_InstalledSoftwareElement**](cim-installedsoftwareelement.md)
</dt> <dd>

The [**CIM\_InstalledSoftwareElement**](cim-installedsoftwareelement.md) class associates a computer system with an installed software element.

</dd> <dt>

[**CIM\_IRQ**](cim-irq.md)
</dt> <dd>

The [**CIM\_IRQ**](cim-irq.md) class represents an Intel architecture interrupt request line (IRQ).

</dd> <dt>

[**CIM\_Job**](cim-job.md)
</dt> <dd>

The [**CIM\_Job**](cim-job.md) class represents a unit of work for a system, such as a print job. A job is distinct from a process because a job can be scheduled.

</dd> <dt>

[**CIM\_JobDestination**](cim-jobdestination.md)
</dt> <dd>

The [**CIM\_JobDestination**](cim-jobdestination.md) class represents where a job is submitted for processing. It can refer to a queue that contains zero or more jobs, such as a print queue containing print jobs. Job destinations are hosted on systems, similar to the way in which services are hosted on systems.

</dd> <dt>

[**CIM\_JobDestinationJobs**](cim-jobdestinationjobs.md)
</dt> <dd>

The [**CIM\_JobDestinationJobs**](cim-jobdestinationjobs.md) association describes where a job is submitted for processing (that is, to which job destination).

</dd> <dt>

[**CIM\_Keyboard**](cim-keyboard.md)
</dt> <dd>

The [**CIM\_Keyboard**](cim-keyboard.md) class represents the capabilities and management of the keyboard logical device.

</dd> <dt>

[**CIM\_LinkHasConnector**](cim-linkhasconnector.md)
</dt> <dd>

The [**CIM\_LinkHasConnector**](cim-linkhasconnector.md) class associates cables and links used as physical connectors, which connect the physical elements. This association explicitly defines the relationship of connectors for [**CIM\_PhysicalLink**](cim-physicallink.md).

</dd> <dt>

[**CIM\_LocalFileSystem**](cim-localfilesystem.md)
</dt> <dd>

The [**CIM\_LocalFileSystem**](cim-localfilesystem.md) class represents the file store controlled by a computer system through local means (for example, direct device-driver access). The file store can be managed directly by the computer system, without the need for another computer to act as a file server. For a clustered file system, however, the file system is local and, therefore, defers to the cluster.

</dd> <dt>

[**CIM\_Location**](cim-location.md)
</dt> <dd>

The [**CIM\_Location**](cim-location.md) class represents the position and address of a physical element.

</dd> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dd>

The [**CIM\_LogicalDevice**](cim-logicaldevice.md) class represents a hardware entity that may or may not be realized in physical hardware.

</dd> <dt>

[**CIM\_LogicalDisk**](cim-logicaldisk.md)
</dt> <dd>

The [**CIM\_LogicalDisk**](cim-logicaldisk.md) class represents a contiguous range of logical blocks that is identifiable by a file system through the disk's **DeviceID** (key) field. For example, in a Windows environment, the **DeviceID** field contains a drive letter; in a UNIX environment, it contains the access path; and in a NetWare environment, it contains the volume name.

</dd> <dt>

[**CIM\_LogicalDiskBasedOnPartition**](cim-logicaldiskbasedonpartition.md)
</dt> <dd>

The [**CIM\_LogicalDiskBasedOnPartition**](cim-logicaldiskbasedonpartition.md) class associates a logical disk with the disk partition on which it resides.

</dd> <dt>

[**CIM\_LogicalDiskBasedOnVolumeSet**](cim-logicaldiskbasedonvolumeset.md)
</dt> <dd>

The [**CIM\_LogicalDiskBasedOnVolumeSet**](cim-logicaldiskbasedonvolumeset.md) association relates logical disks with the volume on which they are found. Logical disks can be based on a single volume (for example, exposed by a software volume manager) or a disk partition.

</dd> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> <dd>

The [**CIM\_LogicalElement**](cim-logicalelement.md) class is the base class for all system components that represent abstract system components, such as profiles, processes, or system capabilities, in the form of logical devices.

</dd> <dt>

[**CIM\_LogicalFile**](cim-logicalfile.md)
</dt> <dd>

The [**CIM\_LogicalFile**](cim-logicalfile.md) class represents a named collection of data, which can be executable code, that is located in a file system on a storage extent.

</dd> <dt>

[**CIM\_LogicalIdentity**](cim-logicalidentity.md)
</dt> <dd>

The [**CIM\_LogicalIdentity**](cim-logicalidentity.md) class is an abstract and generic association that indicates that two logical elements represent different aspects of the same underlying entity.

</dd> <dt>

[**CIM\_MagnetoOpticalDrive**](cim-magnetoopticaldrive.md)
</dt> <dd>

The [**CIM\_MagnetoOpticalDrive**](cim-magnetoopticaldrive.md) class represents the capabilities and management of a magneto-optical drive, a subtype of the media access device.

</dd> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dd>

The [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) class is the base class for the system element hierarchy. Any distinguishable system component is a candidate for inclusion in this class.

</dd> <dt>

[**CIM\_ManagementController**](cim-managementcontroller.md)
</dt> <dd>

The [**CIM\_ManagementController**](cim-managementcontroller.md) class relates to the capabilities and management of a management controller.

</dd> <dt>

[**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md)
</dt> <dd>

The [**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md) class represents the ability to access one or more media, and then use the media to store and retrieve data.

</dd> <dt>

[**CIM\_MediaPresent**](cim-mediapresent.md)
</dt> <dd>

The [**CIM\_MediaPresent**](cim-mediapresent.md) association describes a relationship where a storage extent must be accessed through a media access device.

</dd> <dt>

[**CIM\_Memory**](cim-memory.md)
</dt> <dd>

The [**CIM\_Memory**](cim-memory.md) class represents the capabilities and management of memory-related logical devices.

</dd> <dt>

[**CIM\_MemoryCapacity**](cim-memorycapacity.md)
</dt> <dd>

The [**CIM\_MemoryCapacity**](cim-memorycapacity.md) class represents memory that can be installed on a physical element and its minimum and maximum configurations. Information on memory that is currently installed and an element's minimum and maximum requirements is located in instances of the [**CIM\_PhysicalMemory**](cim-physicalmemory.md) class.

</dd> <dt>

[**CIM\_MemoryCheck**](cim-memorycheck.md)
</dt> <dd>

The [**CIM\_MemoryCheck**](cim-memorycheck.md) class specifies a condition for the minimum amount of memory that must be available on a system.

</dd> <dt>

[**CIM\_MemoryMappedIO**](cim-memorymappedio.md)
</dt> <dd>

The [**CIM\_MemoryMappedIO**](cim-memorymappedio.md) class represents computer architecture memory-mapped I/O. This class addresses memory and port I/O resources.

</dd> <dt>

[**CIM\_MemoryOnCard**](cim-memoryoncard.md)
</dt> <dd>

The [**CIM\_MemoryOnCard**](cim-memoryoncard.md) class associates physical memory located on hosting boards, adapter cards, and so on. This association explicitly defines the relationship of memory to cards.

</dd> <dt>

[**CIM\_MemoryWithMedia**](cim-memorywithmedia.md)
</dt> <dd>

The [**CIM\_MemoryWithMedia**](cim-memorywithmedia.md) class associates physical memory with a physical media and its cartridge. The memory provides media identification and stores user-specific data.

</dd> <dt>

[**CIM\_ModifySettingAction**](cim-modifysettingaction.md)
</dt> <dd>

The [**CIM\_ModifySettingAction**](cim-modifysettingaction.md) class represents the information for modifying a specific setting file, for a specific entry, with a specific value.

</dd> <dt>

[**CIM\_MonitorResolution**](cim-monitorresolution.md)
</dt> <dd>

The [**CIM\_MonitorResolution**](cim-monitorresolution.md) class represents the relationship between horizontal and vertical resolutions and the refresh rate and scan mode for a desktop monitor. Values are specified in the video controller object.

</dd> <dt>

[**CIM\_MonitorSetting**](cim-monitorsetting.md)
</dt> <dd>

The [**CIM\_MonitorSetting**](cim-monitorsetting.md) class associates the monitor resolution with the desktop monitor to which it applies.

</dd> <dt>

[**CIM\_Mount**](cim-mount.md)
</dt> <dd>

The [**CIM\_Mount**](cim-mount.md) class represents an association between a file system and a directory to which it is attached.

</dd> <dt>

[**CIM\_MultiStateSensor**](cim-multistatesensor.md)
</dt> <dd>

The [**CIM\_MultiStateSensor**](cim-multistatesensor.md) class represents a multi-member set of binary sensors where each binary sensor reports a Boolean result.

</dd> <dt>

[**CIM\_NetworkAdapter**](cim-networkadapter.md)
</dt> <dd>

The [**CIM\_NetworkAdapter**](cim-networkadapter.md) class is an abstract class that defines general networking hardware concepts (for example, permanent address or speed of operation). The information is conveyed using the [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md) association.

</dd> <dt>

[**CIM\_NFS**](cim-nfs.md)
</dt> <dd>

The [**CIM\_NFS**](cim-nfs.md) class represents a remote file system that is mounted, using the network file system (NFS) protocol, from a computer system.

</dd> <dt>

[**CIM\_NonVolatileStorage**](cim-nonvolatilestorage.md)
</dt> <dd>

The [**CIM\_NonVolatileStorage**](cim-nonvolatilestorage.md) class represents the capabilities and management of non-volatile storage. Nonvolatile memory natively includes flash and ROM storage.

</dd> <dt>

[**CIM\_NumericSensor**](cim-numericsensor.md)
</dt> <dd>

The [**CIM\_NumericSensor**](cim-numericsensor.md) class represents a numeric sensor that returns numeric readings and optionally supports thresholds settings.

</dd> <dt>

[**CIM\_OperatingSystem**](cim-operatingsystem.md)
</dt> <dd>

The [**CIM\_OperatingSystem**](cim-operatingsystem.md) class represents a computer operating system, which is made up of software and firmware that make a computer system's hardware usable.

</dd> <dt>

[**CIM\_OperatingSystemSoftwareFeature**](cim-operatingsystemsoftwarefeature.md)
</dt> <dd>

The [**CIM\_OperatingSystemSoftwareFeature**](cim-operatingsystemsoftwarefeature.md) class represents the software features that make up the operating system.

</dd> <dt>

[**CIM\_OSProcess**](cim-osprocess.md)
</dt> <dd>

The [**CIM\_OSProcess**](cim-osprocess.md) class associates the operating system and one or more processes running in the context of the operating system.

</dd> <dt>

[**CIM\_OSVersionCheck**](cim-osversioncheck.md)
</dt> <dd>

The [**CIM\_OSVersionCheck**](cim-osversioncheck.md) class specifies the versions of the operating system that can support a software element.

</dd> <dt>

[**CIM\_PackageAlarm**](cim-packagealarm.md)
</dt> <dd>

The [**CIM\_PackageAlarm**](/windows/desktop/SecCrypto/extendedproperties-newenum) association represents the relationship in which an alarm device is installed as part of a package. The installation indicates issues with the package's environment—its security state or its overall health.

</dd> <dt>

[**CIM\_PackageCooling**](cim-packagecooling.md)
</dt> <dd>

The [**CIM\_PackageCooling**](cim-packagecooling.md) association represents the relationship in which a cooling device is installed in a package, such as a chassis or rack, to assist with the package's cooling.

</dd> <dt>

[**CIM\_PackagedComponent**](cim-packagedcomponent.md)
</dt> <dd>

The [**CIM\_PackagedComponent**](cim-packagedcomponent.md) association represents an explicit relationship in which a component is typically contained by a physical package, such as a chassis or card.

</dd> <dt>

[**CIM\_PackageInChassis**](cim-packageinchassis.md)
</dt> <dd>

The [**CIM\_PackageInChassis**](cim-packageinchassis.md) association represents the relationship in which a chassis can contain other packages, such as other chassis and cards.

</dd> <dt>

[**CIM\_PackageInSlot**](cim-packageinslot.md)
</dt> <dd>

The [**CIM\_PackageInSlot**](cim-packageinslot.md) association represents the relationship between device cards and the chassis in which they are mounted.

</dd> <dt>

[**CIM\_PackageTempSensor**](cim-packagetempsensor.md)
</dt> <dd>

The [**CIM\_PackageTempSensor**](cim-packagetempsensor.md) association represents the relationship in which a temperature sensor is often installed in a package, such as a chassis or a rack, to monitor the package's environment.

</dd> <dt>

[**CIM\_ParallelController**](cim-parallelcontroller.md)
</dt> <dd>

The [**CIM\_ParallelController**](cim-parallelcontroller.md) association relates to the capabilities and management of the parallel port logical device.

</dd> <dt>

[**CIM\_ParticipatesInSet**](cim-participatesinset.md)
</dt> <dd>

The [**CIM\_ParticipatesInSet**](cim-participatesinset.md) class identifies physical elements that should be replaced together.

</dd> <dt>

[**CIM\_PCIController**](cim-pcicontroller.md)
</dt> <dd>

The [**CIM\_PCIController**](cim-pcicontroller.md) class represents the properties and management of a PCI controller. The properties in this class and its subclasses are defined in the various PCI specifications published by the PCI SIG.

</dd> <dt>

[**CIM\_PCMCIAController**](cim-pcmciacontroller.md)
</dt> <dd>

The [**CIM\_PCMCIAController**](cim-pcmciacontroller.md) class represents the capabilities and management of a Personal Computer Memory Card International Association (PCMCIA) controller.

</dd> <dt>

[**CIM\_PCVideoController**](cim-pcvideocontroller.md)
</dt> <dd>

The [**CIM\_PCVideoController**](cim-pcvideocontroller.md) represents the capabilities and management of a personal computer video controller, a subtype of a video controller.

</dd> <dt>

[**CIM\_PExtentRedundancyComponent**](cim-pextentredundancycomponent.md)
</dt> <dd>

The [**CIM\_PExtentRedundancyComponent**](cim-pextentredundancycomponent.md) class represents the physical extents that participate in a storage redundancy group.

</dd> <dt>

[**CIM\_PhysicalCapacity**](cim-physicalcapacity.md)
</dt> <dd>

The [**CIM\_PhysicalCapacity**](cim-physicalcapacity.md) class is an abstract class that represents a physical element's minimum and maximum requirements and its ability to support different types of hardware. For example, minimum and maximum memory requirements can be modeled as a subclass of **CIM\_PhysicalCapacity**.

</dd> <dt>

[**CIM\_PhysicalComponent**](cim-physicalcomponent.md)
</dt> <dd>

The [**CIM\_PhysicalComponent**](cim-physicalcomponent.md) class represents a low-level or basic component within a package. A physical element that is not a link, connector, or package is a descendant (or member) of this class.

</dd> <dt>

[**CIM\_PhysicalConnector**](cim-physicalconnector.md)
</dt> <dd>

The [**CIM\_PhysicalConnector**](cim-physicalconnector.md) class represents any physical element that is used to connect to other elements. Any object that can connect and transmit signals or power between two or more physical elements is a descendant (or member) of this class.

</dd> <dt>

[**CIM\_PhysicalElement**](cim-physicalelement.md)
</dt> <dd>

The [**CIM\_PhysicalElement**](cim-physicalelement.md) subclasses define any component of a system that has a distinct physical identity. Instances of this class can be defined in terms of labels that can be physically attached to the object.

</dd> <dt>

[**CIM\_PhysicalElementLocation**](cim-physicalelementlocation.md)
</dt> <dd>

The [**CIM\_PhysicalElementLocation**](cim-physicalelementlocation.md) class associates a physical element with a [**CIM\_Location**](cim-location.md) object for inventory or replacement purposes.

</dd> <dt>

[**CIM\_PhysicalExtent**](cim-physicalextent.md)
</dt> <dd>

The [**CIM\_PhysicalExtent**](cim-physicalextent.md) class represents an SCC RAID implementation. It defines the consecutive addressable block addresses on a single storage device that are treated as a single storage extent in the same [**CIM\_StorageRedundancyGroup**](cim-storageredundancygroup.md) class. An alternative, when automatic configuration is used, is to instantiate or extend the [**CIM\_AggregatePExtent**](cim-aggregatepextent.md) class.

</dd> <dt>

[**CIM\_PhysicalFrame**](cim-physicalframe.md)
</dt> <dd>

The [**CIM\_PhysicalFrame**](cim-physicalframe.md) class is a parent class of rack, chassis, and other frame enclosures as they are defined in extension classes. Properties such as **VisibleAlarm** and **AudibleAlarm**, and data related to security breaches are included in this parent class.

</dd> <dt>

[**CIM\_PhysicalLink**](cim-physicallink.md)
</dt> <dd>

The [**CIM\_PhysicalLink**](cim-physicallink.md) class represents the cabling of physical elements.

</dd> <dt>

[**CIM\_PhysicalMedia**](cim-physicalmedia.md)
</dt> <dd>

The [**CIM\_PhysicalMedia**](cim-physicalmedia.md) class represents types of documentation and storage medium, such as tapes, CD ROMs, and so on.

</dd> <dt>

[**CIM\_PhysicalMemory**](cim-physicalmemory.md)
</dt> <dd>

The [**CIM\_PhysicalMemory**](cim-physicalmemory.md) class represents low-level memory devices, such as SIMMS, DIMMs, raw memory chips, and so on.

</dd> <dt>

[**CIM\_PhysicalPackage**](cim-physicalpackage.md)
</dt> <dd>

The [**CIM\_PhysicalPackage**](cim-physicalpackage.md) class represents physical elements that contain or host other components. Examples are a rack enclosure or an adapter card.

</dd> <dt>

[**CIM\_PointingDevice**](cim-pointingdevice.md)
</dt> <dd>

The [**CIM\_PointingDevice**](cim-pointingdevice.md) class represents a device that points to regions on the display. Any device that manipulates a pointer, or points to regions on a visual display, is a member of this class. For example, a mouse, stylus, touch pad, or tablet.

</dd> <dt>

[**CIM\_POTSModem**](cim-potsmodem.md)
</dt> <dd>

The [**CIM\_POTSModem**](cim-potsmodem.md) class represents a device that translates binary data into wave modulations for sound-based transmission by connecting to the Plain Old Telephone System (POTS) network.

</dd> <dt>

[**CIM\_PowerSupply**](cim-powersupply.md)
</dt> <dd>

The [**CIM\_PowerSupply**](cim-powersupply.md) class represents the capabilities and management of the power supply logical device.

</dd> <dt>

[**CIM\_Printer**](cim-printer.md)
</dt> <dd>

The [**CIM\_Printer**](cim-printer.md) class represents the capabilities and management of the printer logical device.

</dd> <dt>

[**CIM\_Process**](cim-process.md)
</dt> <dd>

The [**CIM\_Process**](cim-process.md) class represents a single instance of a running program. A user typically sees a process as an application or task.

</dd> <dt>

[**CIM\_ProcessExecutable**](cim-processexecutable.md)
</dt> <dd>

The [**CIM\_ProcessExecutable**](cim-processexecutable.md) class represents a link between a process and data file, and indicates that the file participates in the execution of the process.

</dd> <dt>

[**CIM\_Processor**](cim-processor.md)
</dt> <dd>

The [**CIM\_Processor**](cim-processor.md) class represents the capabilities and management of the processor logical device.

</dd> <dt>

[**CIM\_ProcessThread**](cim-processthread.md)
</dt> <dd>

The [**CIM\_ProcessThread**](cim-processthread.md) class represents a link between a process and the threads running in the context of the process.

</dd> <dt>

[**CIM\_Product**](cim-product.md)
</dt> <dd>

The [**CIM\_Product**](cim-product.md) class is a concrete class that represents a collection of physical elements, software features and, other products, acquired as a unit. Acquisition implies an agreement between the supplier and consumer, which can have implications on product licensing, support, and warranty.

</dd> <dt>

[**CIM\_ProductFRU**](cim-productfru.md)
</dt> <dd>

The [**CIM\_ProductFRU**](cim-productfru.md) class represents an association between the product and a field replaceable unit (FRU), which provides information about product components that have been, or are being replaced.

</dd> <dt>

[**CIM\_ProductParentChild**](cim-productparentchild.md)
</dt> <dd>

The [**CIM\_ProductParentChild**](cim-productparentchild.md) association defines a parent-child hierarchy among products. For example, a product can come bundled with other products.

</dd> <dt>

[**CIM\_ProductPhysicalElements**](cim-productphysicalelements.md)
</dt> <dd>

The [**CIM\_ProductPhysicalElements**](cim-productphysicalelements.md) class represents the physical elements that make up a product.

</dd> <dt>

[**CIM\_ProductProductDependency**](cim-productproductdependency.md)
</dt> <dd>

The [**CIM\_ProductProductDependency**](cim-productproductdependency.md) class represents an association between two products, which indicates that one must be installed or absent for the other to function. This is conceptually equivalent to the [**CIM\_ServiceServiceDependency**](cim-serviceservicedependency.md) association.

</dd> <dt>

[**CIM\_ProductSoftwareFeatures**](cim-productsoftwarefeatures.md)
</dt> <dd>

The [**CIM\_ProductSoftwareFeatures**](cim-productsoftwarefeatures.md) association identifies the software features for a particular product.

</dd> <dt>

[**CIM\_ProductSupport**](cim-productsupport.md)
</dt> <dd>

The [**CIM\_ProductSupport**](cim-productsupport.md) class represents an association between product and support access that conveys how support is obtained for the product. Various types of support are available for a product; the same support object can provide assistance for multiple products.

</dd> <dt>

[**CIM\_ProtectedSpaceExtent**](cim-protectedspaceextent.md)
</dt> <dd>

The [**CIM\_ProtectedSpaceExtent**](cim-protectedspaceextent.md) class represents addressable logical-block addresses, which are treated as a single storage extent, but are located on a single physical extent.

</dd> <dt>

[**CIM\_PSExtentBasedOnPExtent**](cim-psextentbasedonpextent.md)
</dt> <dd>

The [**CIM\_PSExtentBasedOnPExtent**](cim-psextentbasedonpextent.md) class associates protected space extents that are based on a physical extent.

</dd> <dt>

[**CIM\_Rack**](cim-rack.md)
</dt> <dd>

The [**CIM\_Rack**](cim-rack.md) class represents a rack (a physical frame or enclosure) in which chassis are stored. Typically, a rack represents the enclosure; all functioning components are packaged in the chassis.

</dd> <dt>

[**CIM\_Realizes**](cim-realizes.md)
</dt> <dd>

The [**CIM\_Realizes**](cim-realizes.md) class represents the association that defines the mapping between a logical device and the physical component that implements the device.

</dd> <dt>

[**CIM\_RealizesAggregatePExtent**](cim-realizesaggregatepextent.md)
</dt> <dd>

The [**CIM\_RealizesAggregatePExtent**](cim-realizesaggregatepextent.md) association represents the relationship in which the [**CIM\_AggregatePExtent**](cim-aggregatepextent.md) class is realized on a physical media.

</dd> <dt>

[**CIM\_RealizesDiskPartition**](cim-realizesdiskpartition.md)
</dt> <dd>

The [**CIM\_RealizesDiskPartition**](cim-realizesdiskpartition.md) class represents a disk partition on a physical media that models the creation of partitions on a raw SCSI or IDE drive.

</dd> <dt>

[**CIM\_RealizesPExtent**](cim-realizespextent.md)
</dt> <dd>

The [**CIM\_RealizesPExtent**](cim-realizespextent.md) association represents the relationship in which physical extents are realized on a physical media. In addition, the starting address of the physical extent on the physical media is specified.

</dd> <dt>

[**CIM\_RebootAction**](cim-rebootaction.md)
</dt> <dd>

The [**CIM\_RebootAction**](cim-rebootaction.md) class causes a system reboot where the software element is installed.

</dd> <dt>

[**CIM\_RedundancyComponent**](cim-redundancycomponent.md)
</dt> <dd>

The [**CIM\_RedundancyComponent**](cim-redundancycomponent.md) class associates a redundancy group composed of managed system elements and indicates that, together, the elements provide redundancy. All elements aggregated in a redundancy group should be instantiations of the same object class.

</dd> <dt>

[**CIM\_RedundancyGroup**](cim-redundancygroup.md)
</dt> <dd>

The [**CIM\_RedundancyGroup**](cim-redundancygroup.md) class represents a collection of managed system elements, which indicates that the aggregated components, together, provide redundancy. All elements aggregated in a redundancy group should be instantiations of the same object class.

</dd> <dt>

[**CIM\_Refrigeration**](cim-refrigeration.md)
</dt> <dd>

The [**CIM\_Refrigeration**](cim-refrigeration.md) class represents the capabilities and management of a refrigeration cooling device.

</dd> <dt>

[**CIM\_RelatedStatistics**](cim-relatedstatistics.md)
</dt> <dd>

The [**CIM\_RelatedStatistics**](cim-relatedstatistics.md) association represents hierarchies and dependencies of related [**CIM\_StatisticalInformation**](cim-statisticalinformation.md) classes.

</dd> <dt>

[**CIM\_RemoteFileSystem**](cim-remotefilesystem.md)
</dt> <dd>

The [**CIM\_RemoteFileSystem**](cim-remotefilesystem.md) class represents a remote file system that is accessed by way of a network-related service. In this case, the file store is hosted by a computer, which acts as a file server.

</dd> <dt>

[**CIM\_RemoveDirectoryAction**](cim-removedirectoryaction.md)
</dt> <dd>

The [**CIM\_RemoveDirectoryAction**](cim-removedirectoryaction.md) class removes directories for software elements.

</dd> <dt>

[**CIM\_RemoveFileAction**](cim-removefileaction.md)
</dt> <dd>

The [**CIM\_RemoveFileAction**](cim-removefileaction.md) class uninstalls files.

</dd> <dt>

[**CIM\_ReplacementSet**](cim-replacementset.md)
</dt> <dd>

The [**CIM\_ReplacementSet**](cim-replacementset.md) class aggregates physical elements that must be replaced together. For example, when replacing a memory card, the component memory chips can also be removed and replaced. Or, this association can be used to replace or upgrade a set of memory chips.

</dd> <dt>

[**CIM\_ResidesOnExtent**](cim-residesonextent.md)
</dt> <dd>

The [**CIM\_ResidesOnExtent**](cim-residesonextent.md) class represents an association between a file system and the storage extent where it is located. Typically, a file system resides on a logical disk.

</dd> <dt>

[**CIM\_RunningOS**](cim-runningos.md)
</dt> <dd>

The [**CIM\_RunningOS**](cim-runningos.md) class represents the currently executing operating system. At most, one operating system can execute at any time on a computer system; the computer system may not be currently booted, or its operating system may be unknown.

</dd> <dt>

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> <dd>

The [**CIM\_SAPSAPDependency**](cim-sapsapdependency.md) class is an association between two service access points (SAPs), which indicates that the second SAP is required for the first SAP to connect with its service.

</dd> <dt>

[**CIM\_Scanner**](cim-scanner.md)
</dt> <dd>

The [**CIM\_Scanner**](cim-scanner.md) represents the capabilities and management of the scanner logical device.

</dd> <dt>

[**CIM\_SCSIController**](cim-scsicontroller.md)
</dt> <dd>

The [**CIM\_SCSIController**](cim-scsicontroller.md) class represents the capabilities and management of the SCSI controller logical device.

</dd> <dt>

[**CIM\_SCSIInterface**](cim-scsiinterface.md)
</dt> <dd>

represents a [**CIM\_ControlledBy**](cim-controlledby.md) relationship that indicates which devices are accessed through a SCSI controller and the access characteristics.

</dd> <dt>

[**CIM\_Sensor**](cim-sensor.md)
</dt> <dd>

The [**CIM\_Sensor**](cim-sensor.md) class represents a hardware device that is capable of measuring the characteristics of a physical property (for example, the temperature or voltage characteristics of a unitary computer system).

</dd> <dt>

[**CIM\_SerialController**](cim-serialcontroller.md)
</dt> <dd>

The [**CIM\_SerialController**](cim-serialcontroller.md) class represents the capabilities and management of the serial port logical device.

</dd> <dt>

[**CIM\_SerialInterface**](cim-serialinterface.md)
</dt> <dd>

The [**CIM\_SerialInterface**](cim-serialinterface.md) class represents a [**CIM\_ControlledBy**](cim-controlledby.md) relationship that indicates which devices are accessed through the serial controller and the characteristics of the access.

</dd> <dt>

[**CIM\_Service**](cim-service.md)
</dt> <dd>

The [**CIM\_Service**](cim-service.md) class represents a logical element that contains information to represent and manage the functionality provided by a device or software feature. A service is a general-purpose object to configure and manage the implementation of functionality; it is not the functionality itself.

</dd> <dt>

[**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md)
</dt> <dd>

The [**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md) association class represents the access points for a service. For example, a printer can be accessed by NetWare, Macintosh, or Windows service access points (SAPs), which are potentially hosted on different systems.

</dd> <dt>

[**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)
</dt> <dd>

The [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) class represents the ability to use or invoke a service. Access points represent services that are available for use by other entities.

</dd> <dt>

[**CIM\_ServiceSAPDependency**](cim-servicesapdependency.md)
</dt> <dd>

The [**CIM\_ServiceSAPDependency**](cim-servicesapdependency.md) class represents an association between a service and a service access point (SAP), which indicates that the referenced SAP is used by the service to provide its functionality.

</dd> <dt>

[**CIM\_ServiceServiceDependency**](cim-serviceservicedependency.md)
</dt> <dd>

The [**CIM\_ServiceServiceDependency**](cim-serviceservicedependency.md) class represents an association between two services.

</dd> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dd>

The [**CIM\_Setting**](cim-setting.md) class represents configuration-related and operational parameters for one or more managed system elements.

</dd> <dt>

[**CIM\_SettingCheck**](cim-settingcheck.md)
</dt> <dd>

The [**CIM\_SettingCheck**](cim-settingcheck.md) class specifies information needed to check a particular setting file for a specific entry that contains a value equal to the value specified. All comparisons are assumed to be case insensitive.

</dd> <dt>

[**CIM\_SettingContext**](cim-settingcontext.md)
</dt> <dd>

The [**CIM\_SettingContext**](cim-settingcontext.md) class associates configuration objects with setting objects.

</dd> <dt>

[**CIM\_Slot**](cim-slot.md)
</dt> <dd>

The [**CIM\_Slot**](cim-slot.md) class represents connectors into which packages are inserted.

</dd> <dt>

[**CIM\_SlotInSlot**](cim-slotinslot.md)
</dt> <dd>

The [**CIM\_SlotInSlot**](cim-slotinslot.md) relationship represents the ability of a special adapter to extend the existing slot structure to enable otherwise incompatible cards to be plugged into a frame or hosting board.

</dd> <dt>

[**CIM\_SoftwareElement**](cim-softwareelement.md)
</dt> <dd>

The [**CIM\_SoftwareElement**](cim-softwareelement.md) class decomposes a [**CIM\_SoftwareFeature**](cim-softwarefeature.md) object into a set of individually manageable or deployable parts for a particular platform. A software element's platform is uniquely identified by its underlying hardware architecture and operating system.

</dd> <dt>

[**CIM\_SoftwareElementActions**](cim-softwareelementactions.md)
</dt> <dd>

The [**CIM\_SoftwareElementActions**](cim-softwareelementactions.md) association identifies the actions for a software element.

</dd> <dt>

[**CIM\_SoftwareElementChecks**](cim-softwareelementchecks.md)
</dt> <dd>

The [**CIM\_SoftwareElementChecks**](cim-softwareelementchecks.md) association class relates a software element with condition or location information that a feature may require.

</dd> <dt>

[**CIM\_SoftwareElementVersionCheck**](cim-softwareelementversioncheck.md)
</dt> <dd>

The [**CIM\_SoftwareElementVersionCheck**](cim-softwareelementversioncheck.md) class represents a type of software element that must exist in the environment.

</dd> <dt>

[**CIM\_SoftwareFeature**](cim-softwarefeature.md)
</dt> <dd>

The [**CIM\_SoftwareFeature**](cim-softwarefeature.md) class represents a particular function or capability of a product or application system.

</dd> <dt>

[**CIM\_SoftwareFeatureSAPImplementation**](cim-softwarefeaturesapimplementation.md)
</dt> <dd>

The [**CIM\_SoftwareFeatureSAPImplementation**](cim-softwarefeaturesapimplementation.md) class represents an association between a service access point (SAP) and how it is implemented in software.

</dd> <dt>

[**CIM\_SoftwareFeatureServiceImplementation**](cim-softwarefeatureserviceimplementation.md)
</dt> <dd>

The [**CIM\_SoftwareFeatureServiceImplementation**](cim-softwarefeatureserviceimplementation.md) class represents an association between a service and how it is implemented in software.

</dd> <dt>

[**CIM\_SoftwareFeatureSoftwareElements**](cim-softwarefeaturesoftwareelements.md)
</dt> <dd>

The [**CIM\_SoftwareFeatureSoftwareElements**](cim-softwarefeaturesoftwareelements.md) association identifies the software elements that make up a specific software feature.

</dd> <dt>

[**CIM\_SpareGroup**](cim-sparegroup.md)
</dt> <dd>

The [**CIM\_SpareGroup**](cim-sparegroup.md) class is derived from the [**CIM\_RedundancyGroup**](cim-redundancygroup.md) class and indicates that one or more of the aggregated elements can be spared.

</dd> <dt>

[**CIM\_StatisticalInformation**](cim-statisticalinformation.md)
</dt> <dd>

The [**CIM\_StatisticalInformation**](cim-statisticalinformation.md) class is a root class for the arbitrary collection of statistical data or metrics applicable to one or more managed system elements.

</dd> <dt>

[**CIM\_Statistics**](cim-statistics.md)
</dt> <dd>

The [**CIM\_Statistics**](cim-statistics.md) class represents an association that relates managed system elements to the statistical groups that apply to them.

</dd> <dt>

[**CIM\_StorageDefect**](cim-storagedefect.md)
</dt> <dd>

The [**CIM\_StorageDefect**](cim-storagedefect.md) aggregation collects the storage errors for a storage extent.

</dd> <dt>

[**CIM\_StorageError**](cim-storageerror.md)
</dt> <dd>

The [**CIM\_StorageError**](cim-storageerror.md) class represents blocks of media or memory space that are mapped out-of-use due to errors. The key of the class is the **StartingAddress** property of the bytes in error.

</dd> <dt>

[**CIM\_StorageExtent**](cim-storageextent.md)
</dt> <dd>

The [**CIM\_StorageExtent**](cim-storageextent.md) class represents the capabilities and management of the various media that exist to store data and allow data retrieval. This parent class can represent the various components of RAID (hardware or software) or a raw logical extent on top of physical media.

</dd> <dt>

[**CIM\_StorageRedundancyGroup**](cim-storageredundancygroup.md)
</dt> <dd>

The [**CIM\_StorageRedundancyGroup**](cim-storageredundancygroup.md) class represents mass storage-related redundancy information.

</dd> <dt>

[**CIM\_SupportAccess**](cim-supportaccess.md)
</dt> <dd>

The [**CIM\_SupportAccess**](cim-supportaccess.md) class defines how to obtain assistance for a product.

</dd> <dt>

[**CIM\_SwapSpaceCheck**](cim-swapspacecheck.md)
</dt> <dd>

The [**CIM\_SwapSpaceCheck**](cim-swapspacecheck.md) class specifies the amount of swap space that must be available on the system.

</dd> <dt>

[**CIM\_System**](cim-system.md)
</dt> <dd>

The [**CIM\_System**](cim-system.md) class aggregates an enumerable set of managed system elements. The aggregation operates as a functional whole. Within any particular subclass of the system, there is a well-defined list of managed system element classes whose instances must be aggregated.

</dd> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dd>

a Common Information Model (CIM) association class that establishes relationships between a system and the managed system elements of which it is composed.

</dd> <dt>

[**CIM\_SystemDevice**](cim-systemdevice.md)
</dt> <dd>

The [**CIM\_SystemDevice**](cim-systemdevice.md) association represents an explicit relationship in which logical devices can be aggregated by a system.

</dd> <dt>

[**CIM\_SystemResource**](cim-systemresource.md)
</dt> <dd>

The [**CIM\_SystemResource**](cim-systemresource.md) class represents an entity managed by BIOS, or an operating system that is available for use by software and logical devices.

</dd> <dt>

[**CIM\_Tachometer**](cim-tachometer.md)
</dt> <dd>

The [**CIM\_Tachometer**](cim-tachometer.md) class exists for backward compatibility with earlier CIM schema definitions.

</dd> <dt>

[**CIM\_TapeDrive**](cim-tapedrive.md)
</dt> <dd>

The [**CIM\_TapeDrive**](cim-tapedrive.md) class represents a tape drive on the system. Tape drives are primarily distinguished in that they can only be accessed sequentially.

</dd> <dt>

[**CIM\_TemperatureSensor**](cim-temperaturesensor.md)
</dt> <dd>

The [**CIM\_TemperatureSensor**](cim-temperaturesensor.md) class exists for backward compatibility with earlier CIM schema definitions.

</dd> <dt>

[**CIM\_Thread**](cim-thread.md)
</dt> <dd>

The [**CIM\_Thread**](cim-thread.md) class represents the ability to execute units of a process or task, in parallel. A process can have many threads, each of which is weak to the process.

</dd> <dt>

[**CIM\_ToDirectoryAction**](cim-todirectoryaction.md)
</dt> <dd>

The [**CIM\_ToDirectoryAction**](cim-todirectoryaction.md) association identifies the target directory for the file action.

</dd> <dt>

[**CIM\_ToDirectorySpecification**](cim-todirectoryspecification.md)
</dt> <dd>

The [**CIM\_ToDirectorySpecification**](cim-todirectoryspecification.md) association identifies the target directory for the file action.

</dd> <dt>

[**CIM\_UninterruptiblePowerSupply**](cim-uninterruptiblepowersupply.md)
</dt> <dd>

The [**CIM\_UninterruptiblePowerSupply**](cim-uninterruptiblepowersupply.md) class represents the capabilities and management of an uninterruptible power supply (UPS).

</dd> <dt>

[**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md)
</dt> <dd>

The [**CIM\_UnitaryComputerSystem**](cim-unitarycomputersystem.md) class represents a desktop, mobile, network computer, server, or other type of single-node computer system.

</dd> <dt>

[**CIM\_USBController**](cim-usbcontroller.md)
</dt> <dd>

The [**CIM\_USBController**](cim-usbcontroller.md) class represents the capabilities and management of a USB controller.

</dd> <dt>

[**CIM\_USBControllerHasHub**](cim-usbcontrollerhashub.md)
</dt> <dd>

The [**CIM\_USBControllerHasHub**](cim-usbcontrollerhashub.md) class defines the hubs that are downstream of the USB controller.

</dd> <dt>

[**CIM\_USBDevice**](cim-usbdevice.md)
</dt> <dd>

The [**CIM\_USBDevice**](cim-usbdevice.md) class represents the management characteristics of a USB device.

</dd> <dt>

[**CIM\_USBHub**](cim-usbhub.md)
</dt> <dd>

The [**CIM\_USBHub**](cim-usbhub.md) class represents the capabilities and management of a USB hub.

</dd> <dt>

[**CIM\_UserDevice**](cim-userdevice.md)
</dt> <dd>

The [**CIM\_UserDevice**](cim-userdevice.md) class is a parent class from which other classes, such as [**CIM\_Keyboard**](cim-keyboard.md) or [**CIM\_DesktopMonitor**](cim-desktopmonitor.md), descend. User devices are logical devices that allow a computer system's user to input, view, or hear data.

</dd> <dt>

[**CIM\_VersionCompatibilityCheck**](cim-versioncompatibilitycheck.md)
</dt> <dd>

The [**CIM\_VersionCompatibilityCheck**](cim-versioncompatibilitycheck.md) class specifies whether it is permissible to create the next state of a software element.

</dd> <dt>

[**CIM\_VideoBIOSElement**](cim-videobioselement.md)
</dt> <dd>

The [**CIM\_VideoBIOSElement**](cim-videobioselement.md) class represents the low-level software that is loaded into non-volatile storage and used to configure and access a computer system's video controller and display.

</dd> <dt>

[**CIM\_VideoBIOSFeature**](cim-videobiosfeature.md)
</dt> <dd>

The [**CIM\_VideoBIOSFeature**](cim-videobiosfeature.md) class represents the capabilities of the low-level software used to configure and access a computer system's video controller and display.

</dd> <dt>

[**CIM\_VideoBIOSFeatureVideoBIOSElements**](cim-videobiosfeaturevideobioselements.md)
</dt> <dd>

The [**CIM\_VideoBIOSFeatureVideoBIOSElements**](cim-videobiosfeaturevideobioselements.md) class associates a video BIOS feature and its aggregated video BIOS elements.

</dd> <dt>

[**CIM\_VideoController**](cim-videocontroller.md)
</dt> <dd>

The [**CIM\_VideoController**](cim-videocontroller.md) class represents the capabilities and management of the video controller.

</dd> <dt>

[**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md)
</dt> <dd>

The [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) class represents the various video modes that a video controller can support.

</dd> <dt>

[**CIM\_VideoSetting**](cim-videosetting.md)
</dt> <dd>

The [**CIM\_VideoSetting**](cim-videosetting.md) class associates the [**CIM\_VideoControllerResolution**](cim-videocontrollerresolution.md) setting object with the controller to which it applies.

</dd> <dt>

[**CIM\_VolatileStorage**](cim-volatilestorage.md)
</dt> <dd>

The [**CIM\_VolatileStorage**](cim-volatilestorage.md) class represents the capabilities and management of volatile storage.

</dd> <dt>

[**CIM\_VoltageSensor**](cim-voltagesensor.md)
</dt> <dd>

The [**CIM\_VoltageSensor**](cim-voltagesensor.md) class exists for backward compatibility to earlier CIM schema definitions. With additions to the [**CIM\_Sensor**](cim-sensor.md) and [**CIM\_NumericSensor**](cim-numericsensor.md) classes in version 2.2, it is no longer necessary.

</dd> <dt>

[**CIM\_VolumeSet**](cim-volumeset.md)
</dt> <dd>

The [**CIM\_VolumeSet**](cim-volumeset.md) class represents a contiguous range of logical blocks presented to the operating environment for reading and writing user data.

</dd> <dt>

[**CIM\_WORMDrive**](cim-wormdrive.md)
</dt> <dd>

The [**CIM\_WORMDrive**](cim-wormdrive.md) class represents the capabilities and management of a WORM drive, a subtype of the media access device.

</dd> </dl>

 

 
