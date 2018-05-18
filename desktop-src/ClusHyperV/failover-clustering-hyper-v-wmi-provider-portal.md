---
title: Failover Clustering Hyper-V WMI Provider
description: The Failover Clustering Hyper-V WMI provider exposes the following classes.In this sectionCIM\_ActiveConnectionDefines a connection that is currently turned on and configured to provide communication between two CIM\_ServiceAccessPoint objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4e5ef7ab-10bb-4528-820d-83d68321e19c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-hyperv'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Failover Clustering Hyper-V WMI Provider

## Purpose

The Failover Clustering Hyper-V WMI provider exposes the following classes.

## In this section

<dl> <dt>

[**CIM\_ActiveConnection**](cim-activeconnection.md)
</dt> <dd>

Defines a connection that is currently turned on and configured to provide communication between two **CIM\_ServiceAccessPoint** objects. **CIM\_ActiveConnection** is used when the connection is not treated as a **CIM\_ManagedElement** object. Service access points that are connected by an active connection are typically at the same networking or application layer.

</dd> <dt>

[**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
</dt> <dd>

Represents an association between a job and the **CIM\_ManagedElement** objects that may be affected by its execution. It may not be feasible for the job to describe all of the affected elements. The main purpose of this association is to provide information when a job requires exclusive use of the affected managed elements or when describing the side effects that may result.

</dd> <dt>

[**CIM\_AggregationMetricDefinition**](cim-aggregationmetricdefinition.md)
</dt> <dd>

Represents the definition of a metric that is derived from another metric value. A **CIM\_AggregationMetricDefinition** object should be associated with the **CIM\_ManagedElement** objects to which it applies.

</dd> <dt>

[**CIM\_AggregationMetricValue**](cim-aggregationmetricvalue.md)
</dt> <dd>

Represents the instance value of a metric defined by an instance of **CIM\_AggregationMetricDefinition**.

</dd> <dt>

[**CIM\_AlertIndication**](cim-alertindication.md)
</dt> <dd>

A concrete superclass for CIM alert notifications. **CIM\_AlertIndication** is a specialized type of **CIM\_Indication** class that contains information about the severity, cause, recommended actions, and other data for a real world event. This event and its data may or may not be modeled in the CIM class hierarchy.

</dd> <dt>

[**CIM\_AllocationCapabilities**](cim-allocationcapabilities.md)
</dt> <dd>

Represents the resource allocation settings of a managed element for a specific resource type.

</dd> <dt>

[**CIM\_BasedOn**](cim-basedon.md)
</dt> <dd>

Represents an association between a higher level **CIM\_StorageExtent** object and a lower level **CIM\_StorageExtent** object. For example a [**CIM\_ProtectedSpaceExtent**](https://msdn.microsoft.com/library/aa387988) object is a part of a [**CIM\_PhysicalExtent**](https://msdn.microsoft.com/library/aa387964) object.

</dd> <dt>

[**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md)
</dt> <dd>

Represents a metric definition that contains the meta data for a **CIM\_MetricInstance** object.

</dd> <dt>

[**CIM\_BaseMetricValue**](cim-basemetricvalue.md)
</dt> <dd>

Represents the instance value of a metric.

</dd> <dt>

[**CIM\_BindsTo**](cim-bindsto.md)
</dt> <dd>

Represents an association where a [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) object requests protocol services from a [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object.

</dd> <dt>

[**CIM\_BindsToLANEndpoint**](cim-bindstolanendpoint.md)
</dt> <dd>

Represents an association where a [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md) or [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md) object depends on an underlying [**CIM\_LANEndpoint**](cim-lanendpoint.md) object on the same system.

</dd> <dt>

[**CIM\_BIOSElement**](cim-bioselement.md)
</dt> <dd>

Represents the low-level software that is loaded into non-volatile storage and used to start up and configure a computer system ([**CIM\_ComputerSystem**](cim-computersystem.md)).

</dd> <dt>

[**CIM\_Capabilities**](cim-capabilities.md)
</dt> <dd>

An abstract class for subclasses that describes the abilities of an associated managed element, and the potential of the abilities.

</dd> <dt>

[**CIM\_CDROMDrive**](cim-cdromdrive.md)
</dt> <dd>

Represents the capabilities and management of a CD ROM drive.

</dd> <dt>

[**CIM\_CollectedMSEs**](cim-collectedmses.md)
</dt> <dd>

Represents a generic association between a collection of managed system elements and the members of the collection.

</dd> <dt>

[**CIM\_Collection**](cim-collection.md)
</dt> <dd>

A superclass for classes that represent a collection of [**CIM\_ManagedElement**](cim-managedelement.md) objects and the subclasses of managed elements.

</dd> <dt>

[**CIM\_CollectionOfMSEs**](cim-collectionofmses.md)
</dt> <dd>

An abstract class for subclasses that represent a collection of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects. These collections allow managed system elements to be grouped for identification purposes and to simplify the association of settings and configurations.

</dd> <dt>

[**CIM\_Component**](cim-component.md)
</dt> <dd>

Represents a generic association between a parent managed element and a child managed element where the child represents a component or part of the parent.

</dd> <dt>

[**CIM\_ComponentCS**](cim-componentcs.md)
</dt> <dd>

Represents an association where a computer system contains and aggregates another computer system.

</dd> <dt>

[**CIM\_ComputerSystem**](cim-computersystem.md)
</dt> <dd>

Represents a collection that provides computing capabilities and consists of [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) objects.

</dd> <dt>

[**CIM\_ConcreteComponent**](cim-concretecomponent.md)
</dt> <dd>

Represents a generic association used to establish the parts of a relationship between managed elements.

</dd> <dt>

[**CIM\_ConcreteDependency**](cim-concretedependency.md)
</dt> <dd>

Represents a generic association in which a managed element depends on another. **CIM\_ConcreteDependency** subclasses [**CIM\_Dependency**](cim-dependency.md) to provide a concrete class version of **CIM\_Dependency**.

</dd> <dt>

[**CIM\_ConcreteIdentity**](cim-concreteidentity.md)
</dt> <dd>

Represents an association between two managed elements that represent different aspects of the same underlying entity.

</dd> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> <dd>

A concrete version of the [**CIM\_Job**](cim-job.md) class. This class represent a generic instantiable unit of work to run, such as a batch or a print job.

</dd> <dt>

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dd>

Represents a relationship between a controller and a logical device that is managed by the controller.

</dd> <dt>

[**CIM\_Controller**](cim-controller.md)
</dt> <dd>

A superclass for miscellaneous control-related devices that provide a classic bus master interface. The controller class is an abstraction for devices with a single protocol stack, and exist to control communications (data, control, and reset) to downstream devices.

</dd> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dd>

Represents a generic association used to establish dependency relationships between managed elements.

</dd> <dt>

[**CIM\_DesktopMonitor**](cim-desktopmonitor.md)
</dt> <dd>

Represents a CRT desktop monitor.

</dd> <dt>

[**CIM\_DeviceConnection**](cim-deviceconnection.md)
</dt> <dd>

A relationship that indicates that two or more devices are connected together.

</dd> <dt>

[**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
</dt> <dd>

Represents an association between a service access point (SAP) and a logical device that implements it.

</dd> <dt>

[**CIM\_DiskDrive**](cim-diskdrive.md)
</dt> <dd>

Represents a disk drive.

</dd> <dt>

[**CIM\_DisketteDrive**](cim-diskettedrive.md)
</dt> <dd>

Represents a diskette drive.

</dd> <dt>

[**CIM\_Display**](cim-display.md)
</dt> <dd>

A superclass for classes that represent display devices.

</dd> <dt>

[**CIM\_DisplayController**](cim-displaycontroller.md)
</dt> <dd>

Represents a display controller.

</dd> <dt>

[**CIM\_DVDDrive**](cim-dvddrive.md)
</dt> <dd>

Represents a DVD drive.

</dd> <dt>

[**CIM\_DynamicForwardingEntry**](cim-dynamicforwardingentry.md)
</dt> <dd>

Represents an entry in the forwarding database associated with the [**CIM\_TransparentBridgingService**](cim-transparentbridgingservice.md) class.

</dd> <dt>

[**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md)
</dt> <dd>

Represents an association in which a [**CIM\_LogicalElement**](cim-logicalelement.md) object represents a resource allocated from a [**CIM\_ResourcePool**](cim-resourcepool.md) object.

</dd> <dt>

[**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
</dt> <dd>

Represents an association between a managed element and its capabilities.

</dd> <dt>

[**CIM\_ElementConformsToProfile**](cim-elementconformstoprofile.md)
</dt> <dd>

Represents an association in which a managed element conforms to the standard of a registered profile. This association usually applies to a higher level instance, such as a system, namespace, or service. When applied to a higher level instance, all constituent parts MUST behave appropriately in support of the ManagedElement's conformance to the named RegisteredProfile.

</dd> <dt>

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dd>

Represents an association between a managed element and its associated setting data. This association also describes whether this is a default or current setting.

</dd> <dt>

[**CIM\_ElementView**](cim-elementview.md)
</dt> <dd>

Represents and association between a view, and an instance that represents the normalized view of a managed resource.

</dd> <dt>

[**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md)
</dt> <dd>

Represents a logical element that can be enabled and disabled.

</dd> <dt>

[**CIM\_EnabledLogicalElementCapabilities**](cim-enabledlogicalelementcapabilities.md)
</dt> <dd>

Describes the restrictions on the properties of an associated [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md) object.

</dd> <dt>

[**CIM\_Error**](cim-error.md)
</dt> <dd>

The **CIM\_Error** class contains information about the failure of a CIM operation.

</dd> <dt>

[**CIM\_EthernetPort**](cim-ethernetport.md)
</dt> <dd>

Represents an ethernet port.

</dd> <dt>

[**CIM\_EthernetPortAllocationSettingData**](cim-ethernetportallocationsettingdata.md)
</dt> <dd>

Represents settings for the allocation of the ethernet port, in addition to the settings provided by the [**CIM\_EthernetPort**](cim-ethernetport.md) class. These settings are used to provide information specific to the resource itself.

</dd> <dt>

[**CIM\_FCPort**](cim-fcport.md)
</dt> <dd>

Represents the capabilities and management of a fibre channel (FC) port device.

</dd> <dt>

[**CIM\_ForwardingService**](cim-forwardingservice.md)
</dt> <dd>

Represents a forwarding service for network traffic. The service processes packets received protocol endpoints by discarding them, or sending the packets to other protocol endpoints.

</dd> <dt>

[**CIM\_ForwardsAmong**](cim-forwardsamong.md)
</dt> <dd>

Represents an association in which protocol endpoints depend on a forwarding service to forward data.

</dd> <dt>

[**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md)
</dt> <dd>

Represents an association between a service access point (SAP) and the system that hosts it. A system can host multiple access points. If the implementation of the SAP is modeled, it must be implemented by a device or software feature that is part of the system that hosts the SAP.

</dd> <dt>

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dd>

Represents an association where a managed element is hosted by another.

</dd> <dt>

[**CIM\_HostedResourcePool**](cim-hostedresourcepool.md)
</dt> <dd>

Represents an association between a system and a resource pool that is a component of the system.

</dd> <dt>

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dd>

Represents an association between a service and the system that hosts the service. A System can host many services, however this class does not represent services hosted across multiple systems.

</dd> <dt>

[**CIM\_IDEController**](cim-idecontroller.md)
</dt> <dd>

Describes the capabilities and management of an IDE controller.

</dd> <dt>

[**CIM\_Indication**](cim-indication.md)
</dt> <dd>

[**CIM\_Indication**](cim-indication.md) is the abstract base class for all notifications about changes in schema objects, and schema object data, events detected by providers and instrumentation. Subclasses of **CIM\_Indication** represent specific types of notifications.

</dd> <dt>

[**CIM\_Job**](cim-job.md)
</dt> <dd>

A logical element that represents a unit of work to execute, such as a script or a print job. A job is distinct from a process because a job can be scheduled or queued, and its execution is not limited to a single system.

</dd> <dt>

[**CIM\_LANEndpoint**](cim-lanendpoint.md)
</dt> <dd>

A communication endpoint that can connect to a LAN to send and receive data frames. LAN endpoints include ethernet, token Ring, and FDDI interfaces.

</dd> <dt>

[**CIM\_LastAppliedSnapshot**](cim-lastappliedsnapshot.md)
</dt> <dd>

Represents an association between a computer system and its most recently applied virtual system snapshot.

</dd> <dt>

[**CIM\_LogicalDevice**](cim-logicaldevice.md)
</dt> <dd>

An abstraction or emulation of a hardware entity that may or may not be based on physical hardware.

</dd> <dt>

[**CIM\_LogicalDisk**](cim-logicaldisk.md)
</dt> <dd>

Represents a contiguous range of logical blocks that is identifiable by a file system through the disk's **DeviceID** (key) field. For example, in a Windows environment, the **DeviceID** field contains a drive letter; in a UNIX environment, it contains the access path; and in a NetWare environment, it contains the volume name.

</dd> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> <dd>

**CIM\_LogicalElement** is a base class for all components of a System that represent abstract system components, such as files, processes, and logical devices.

</dd> <dt>

[**CIM\_LogicalIdentity**](cim-logicalidentity.md)
</dt> <dd>

Represents a generic association between two managed elements that represent different aspects of the same underlying entity.

</dd> <dt>

[**CIM\_LogicalPort**](cim-logicalport.md)
</dt> <dd>

The abstraction of a port or connection point of a device.

</dd> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dd>

The **CIM\_ManagedElement** class is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

</dd> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dd>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md) is the base class for the system element hierarchy. Any component of a system can potentially be represented by this class or its subclasses.

</dd> <dt>

[**CIM\_MediaAccessDevice**](cim-mediaaccessdevice.md)
</dt> <dd>

Represents a device that can use media to store and retrieve data.

</dd> <dt>

[**CIM\_MediaPresent**](cim-mediapresent.md)
</dt> <dd>

Represents a relationship in which a storage extent must be accessed through a media access device.

</dd> <dt>

[**CIM\_MemberOfCollection**](cim-memberofcollection.md)
</dt> <dd>

Represents a relationship in which a managed element is a member of and is aggregated by a collection.

</dd> <dt>

[**CIM\_Memory**](cim-memory.md)
</dt> <dd>

Represents the capabilities and management of memory-related logical devices.

</dd> <dt>

[**CIM\_MetricDefForME**](cim-metricdefforme.md)
</dt> <dd>

Represents an association in which a [**CIM\_BaseMetricDefinition**](cim-basemetricdefinition.md) object defines metrics for a managed element.

</dd> <dt>

[**CIM\_MetricForME**](cim-metricforme.md)
</dt> <dd>

Represents an association in which a metric values are collected for a managed element.

</dd> <dt>

[**CIM\_MetricInstance**](cim-metricinstance.md)
</dt> <dd>

Represents an association between an instance of a metric value and a metric definition.

</dd> <dt>

[**CIM\_MetricService**](cim-metricservice.md)
</dt> <dd>

Manages metrics for managed elements.

</dd> <dt>

[**CIM\_MetricServiceCapabilities**](cim-metricservicecapabilities.md)
</dt> <dd>

Describes the capabilities of a [**CIM\_MetricService**](cim-metricservice.md) object.

</dd> <dt>

[**CIM\_MostCurrentSnapshotInBranch**](cim-mostcurrentsnapshotinbranch.md)
</dt> <dd>

Represents an association between a virtual system and the most current snapshot of the system. This association can only exist if the virtual system was create using a snapshot or if a snapshot was created from the virtual system.

</dd> <dt>

[**CIM\_NetworkPort**](cim-networkport.md)
</dt> <dd>

A logical representation of a network port on a network device.

</dd> <dt>

[**CIM\_NetworkService**](cim-networkservice.md)
</dt> <dd>

This class is deprecated. Instead, we recommend deriving from the [**CIM\_Service**](cim-service.md) class.

</dd> <dt>

[**CIM\_OwningJobElement**](cim-owningjobelement.md)
</dt> <dd>

Represents an association between a job and the managed element that created the job. Since a job might move between systems, and the managed element might not exist for the entire duration of the job, in some cases, this association might not be possible or might only exist for a portion of the existence of the job.

</dd> <dt>

[**CIM\_PointingDevice**](cim-pointingdevice.md)
</dt> <dd>

Represents a device used to point to regions of a display.

</dd> <dt>

[**CIM\_PortOnDevice**](cim-portondevice.md)
</dt> <dd>

Represents an association between a port or connection point and a device.

</dd> <dt>

[**CIM\_ProcessIndication**](cim-processindication.md)
</dt> <dd>

[**CIM\_ProcessIndication**](cim-processindication.md) is an abstract superclass for specialized indication classes, that address specific changes and alerts published by providers and instrumentation.

</dd> <dt>

[**CIM\_Processor**](cim-processor.md)
</dt> <dd>

Represents the capabilities and management of a processor.

</dd> <dt>

[**CIM\_ProtocolController**](cim-protocolcontroller.md)
</dt> <dd>

Represents a group of controllers that control the operation and function of devices that initiate protocols.

</dd> <dt>

[**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md)
</dt> <dd>

Represents an association between a logical device and a protocol controller that is connected to the device.

</dd> <dt>

[**CIM\_ProtocolControllerForUnit**](cim-protocolcontrollerforunit.md)
</dt> <dd>

Represents an association between a protocol controller and an exposed logical unit.

</dd> <dt>

[**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md)
</dt> <dd>

A communication point used to send and receive data between systems, computer interfaces, and logical networks.

</dd> <dt>

[**CIM\_RedundancySet**](cim-redundancyset.md)
</dt> <dd>

A collection of managed elements that provides redundancy.

</dd> <dt>

[**CIM\_ResourceAllocationFromPool**](cim-resourceallocationfrompool.md)
</dt> <dd>

Represents an association in which a [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instance is allocated from a resource pool.

</dd> <dt>

[**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md)
</dt> <dd>

Represents settings for an allocated resource that are outside the scope of the CIM class typically used to represent the resource itself. These settings include information specific to the allocation that may not be visible to the consumer of the resource.

</dd> <dt>

[**CIM\_ResourcePool**](cim-resourcepool.md)
</dt> <dd>

Represents a resource pool, which is a logical entity provided by the host system to allocate and assign resources.

</dd> <dt>

[**CIM\_ResourcePoolConfigurationCapabilities**](cim-resourcepoolconfigurationcapabilities.md)
</dt> <dd>

Manages the capabilities of the [**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md) instance for a [**CIM\_ResourcePool**](cim-resourcepool.md) object.

</dd> <dt>

[**CIM\_ResourcePoolConfigurationService**](cim-resourcepoolconfigurationservice.md)
</dt> <dd>

Manages the configuration of resource pools by using jobs.

</dd> <dt>

[**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
</dt> <dd>

Represents an association between two service access points (SAP), in which one SAP is dependant on the other to utilize or connect with a service. For example, to print on a network printer, local print access points must utilize underlying network-related SAPs to send the print request.

</dd> <dt>

[**CIM\_SCSIProtocolController**](cim-scsiprotocolcontroller.md)
</dt> <dd>

Represents a protocol controller that manages a SCSI interface.

</dd> <dt>

[**CIM\_SerialController**](cim-serialcontroller.md)
</dt> <dd>

Describes the capabilities and management of a serial controller.

</dd> <dt>

[**CIM\_Service**](cim-service.md)
</dt> <dd>

Represents a logical element that contains information to represent and manage the functionality provided by a device or software feature. A service is a general-purpose object to configure and manage the implementation of functionality; it is not the functionality itself.

</dd> <dt>

[**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)
</dt> <dd>

Represents a service access point (SAP), which is able to utilize or invoke a service. SAPs indicate that a service is available for other entities to use.

</dd> <dt>

[**CIM\_ServiceAffectsElement**](cim-serviceaffectselement.md)
</dt> <dd>

Represents an association between a service and a managed element that might be affected by its execution.

</dd> <dt>

[**CIM\_ServiceComponent**](cim-servicecomponent.md)
</dt> <dd>

Represents an association in which a service is a component of a parent service, which together, form a higher-level service.

</dd> <dt>

[**CIM\_ServiceSAPDependency**](cim-servicesapdependency.md)
</dt> <dd>

Represents an association between a service and a service access point (SAP) that provides the service with functionality.

</dd> <dt>

[**CIM\_SettingData**](cim-settingdata.md)
</dt> <dd>

Represents configuration and operational parameters for [**CIM\_ManagedElement**](cim-managedelement.md) instances.

</dd> <dt>

[**CIM\_SettingsDefineCapabilities**](cim-settingsdefinecapabilities.md)
</dt> <dd>

Represents an association between properties of a [**CIM\_SettingData**](cim-settingdata.md) instance and a [**CIM\_Capabilities**](cim-capabilities.md) instance.

</dd> <dt>

[**CIM\_SettingsDefineState**](cim-settingsdefinestate.md)
</dt> <dd>

Associates settings data with a managed element.

</dd> <dt>

[**CIM\_SnapshotOfVirtualSystem**](cim-snapshotofvirtualsystem.md)
</dt> <dd>

Associates a virtual system a snapshot of the virtual system.

</dd> <dt>

[**CIM\_SoftwareElement**](cim-softwareelement.md)
</dt> <dd>

Represents an individually manageable or deployable part of a **CIM\_SoftwareFeature**.

</dd> <dt>

[**CIM\_StorageAllocationSettingData**](cim-storageallocationsettingdata.md)
</dt> <dd>

Represents settings for the allocation of virtual storage.

</dd> <dt>

[**CIM\_StorageExtent**](cim-storageextent.md)
</dt> <dd>

Describes the capabilities and management of media that stores data and allows retrieval of the data. This super class is used to represent software and hardware RAID components, or a raw logical extent of physical media.

</dd> <dt>

[**CIM\_SwitchesAmong**](cim-switchesamong.md)
</dt> <dd>

Represents a switch service, which switches frames between switch ports.

</dd> <dt>

[**CIM\_SwitchPort**](cim-switchport.md)
</dt> <dd>

Represents a switch port that sends and receives data frames.

</dd> <dt>

[**CIM\_SwitchPortDynamicForwarding**](cim-switchportdynamicforwarding.md)
</dt> <dd>

Represents an association in which an entry of a forwarding database applies to a switch port.

</dd> <dt>

[**CIM\_SwitchService**](cim-switchservice.md)
</dt> <dd>

Represents a switch service.

</dd> <dt>

[**CIM\_SwitchServiceTransparentBridging**](cim-switchservicetransparentbridging.md)
</dt> <dd>

Represents an association in which a bridge service is a component of a switch service.

</dd> <dt>

[**CIM\_System**](cim-system.md)
</dt> <dd>

Represents a set of components that function as a single high-level entity.

</dd> <dt>

[**CIM\_SystemBIOS**](cim-systembios.md)
</dt> <dd>

Associates a BIOS with a computer system.

</dd> <dt>

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dd>

Represents an association between a system and one of the elements that compose it.

</dd> <dt>

[**CIM\_SystemDevice**](cim-systemdevice.md)
</dt> <dd>

Associates a system with a logical device that is a component of the system.

</dd> <dt>

[**CIM\_SystemSpecificCollection**](cim-systemspecificcollection.md)
</dt> <dd>

Represents the a generic collection that is contained by a system.

</dd> <dt>

[**CIM\_TapeDrive**](cim-tapedrive.md)
</dt> <dd>

Represents the capabilities and management of a tape drive.

</dd> <dt>

[**CIM\_TPM**](cim-tpm.md)
</dt> <dd>

Describes a Trusted Platform Module (TPM) device.

</dd> <dt>

[**CIM\_TransparentBridgingDynamicForwarding**](cim-transparentbridgingdynamicforwarding.md)
</dt> <dd>

Associates a transparent bridging service with an entry of its forwarding database.

</dd> <dt>

[**CIM\_TransparentBridgingService**](cim-transparentbridgingservice.md)
</dt> <dd>

Represents the transparent bridging aspect of a [**CIM\_SwitchService**](cim-switchservice.md) object.

</dd> <dt>

[**CIM\_USBDevice**](cim-usbdevice.md)
</dt> <dd>

The management characteristics of a USB device.

</dd> <dt>

[**CIM\_UserDevice**](cim-userdevice.md)
</dt> <dd>

Represents a logical device that allows a user to input, view or hear data on the computer system.

</dd> <dt>

[**CIM\_VideoHead**](cim-videohead.md)
</dt> <dd>

Represents one head of a [**CIM\_DisplayController**](cim-displaycontroller.md) object.

</dd> <dt>

[**CIM\_VideoHeadOnController**](cim-videoheadoncontroller.md)
</dt> <dd>

Associates a video head with the video adapter that contains it.

</dd> <dt>

[**CIM\_View**](cim-view.md)
</dt> <dd>

The [**CIM\_View**](cim-view.md) class is an superclass for classes that provide de-normalized, aggregate representations of managed resources.

</dd> <dt>

[**CIM\_VirtualEthernetSwitchSettingData**](cim-virtualethernetswitchsettingdata.md)
</dt> <dd>

Describes settings data for a virtual ethernet switch.

</dd> <dt>

[**CIM\_VirtualSystemManagementCapabilities**](cim-virtualsystemmanagementcapabilities.md)
</dt> <dd>

Represents the capabilities of a [**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md) object.

</dd> <dt>

[**CIM\_VirtualSystemManagementService**](cim-virtualsystemmanagementservice.md)
</dt> <dd>

Represents a service that manages virtual systems.

</dd> <dt>

[**CIM\_VirtualSystemMigrationCapabilities**](cim-virtualsystemmigrationcapabilities.md)
</dt> <dd>

Represents the capabilities of a [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) object.

</dd> <dt>

[**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md)
</dt> <dd>

Represents a service that controls the migration of virtual systems between host systems. This class also verifies whether a pending migration is likely to succeed.

</dd> <dt>

[**CIM\_VirtualSystemMigrationSettingData**](cim-virtualsystemmigrationsettingdata.md)
</dt> <dd>

Defines the settings for virtual system migration that is managed by an instance of the [**CIM\_VirtualSystemMigrationService**](cim-virtualsystemmigrationservice.md) class.

</dd> <dt>

[**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md)
</dt> <dd>

Describes the virtual aspects of a virtual system through a set of virtualization specific properties. **CIM\_VirtualSystemSettingData** is also used as the top level class of virtual system configurations.

</dd> <dt>

[**CIM\_VirtualSystemSettingDataComponent**](cim-virtualsystemsettingdatacomponent.md)
</dt> <dd>

Represents a portion of a relationship between a [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) instance and a set of [**CIM\_ResourceAllocationSettingData**](cim-resourceallocationsettingdata.md) instances.

</dd> <dt>

[**CIM\_VirtualSystemSnapshotService**](cim-virtualsystemsnapshotservice.md)
</dt> <dd>

Represents a service that can create, apply, and delete snapshots of virtual systems.

</dd> <dt>

[**CIM\_VLANEndpoint**](cim-vlanendpoint.md)
</dt> <dd>

An endpoint on a switch or end station that is assigned to a VLAN, or accepts traffic from one or more VLANs.

</dd> <dt>

[**CIM\_VLANEndpointSettingData**](cim-vlanendpointsettingdata.md)
</dt> <dd>

Represents configuration data for a VLAN endpoint.

</dd> <dt>

[**CIM\_WiFiEndpoint**](cim-wifiendpoint.md)
</dt> <dd>

Represents a wireless communication endpoint, which can send and receive data frames when its associated interface device is connected with an IEEE 802.11 wireless LAN.

</dd> <dt>

[**CIM\_WiFiPort**](cim-wifiport.md)
</dt> <dd>

Represents a wireless local area network communications device that conforms to the IEEE 802.11 series of specifications.

</dd> <dt>

[**Msvm\_AffectedJobElement**](msvm-affectedjobelement.md)
</dt> <dd>

Represents an association between a job and the managed element that can be affected by the job's execution.

</dd> <dt>

[**Msvm\_ClusterV2ElementConformsToProfile**](msvm-clusterv2elementconformstoprofile.md)
</dt> <dd>

Defines the registered profile to which the referenced computer system conforms.

The following syntax is simplified from MOF code and includes all inherited properties.

</dd> <dt>

[**Msvm\_CollectedCollections**](msvm-collectedcollections.md)
</dt> <dd>

Associates a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object with contained [**Msvm\_ComputerSystem**](msvm-computersystem.md) objects.

</dd> <dt>

[**Msvm\_CollectedReferencePoints**](msvm-collectedreferencepoints.md)
</dt> <dd>

Associates a [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md) object with the contained [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md) objects.

</dd> <dt>

[**Msvm\_CollectedSnapshots**](msvm-collectedsnapshots.md)
</dt> <dd>

Associates an [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) object with contained [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) objects.

</dd> <dt>

[**Msvm\_CollectedVirtualSystems**](msvm-collectedvirtualsystems.md)
</dt> <dd>

Associates a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object with contained [**Msvm\_ComputerSystem**](msvm-computersystem.md) objects.

</dd> <dt>

[**Msvm\_CollectionManagementService**](msvm-collectionmanagementservice.md)
</dt> <dd>

Manages [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) objects on a Hyper-V host.

</dd> <dt>

[**Msvm\_CollectionRecoveryPoint**](msvm-collectionrecoverypoint.md)
</dt> <dd>

Represents a recovery point of a collection.

</dd> <dt>

[**Msvm\_CollectionReferencePointExportJob**](msvm-collectionreferencepointexportjob.md)
</dt> <dd>

Represents a collection reference point export operation job.

</dd> <dt>

[**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md)
</dt> <dd>

Represents export setting data to pass to the **ExportReferencePoint** method of [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md) class.

</dd> <dt>

[**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
</dt> <dd>

Represents a service that manages reference points of virtual system collections.

</dd> <dt>

[**Msvm\_CollectionReferencePointSettingData**](msvm-collectionreferencepointsettingdata.md)
</dt> <dd>

Retrieves information for the [**CreateReferencePoint**](msvm-collectionreferencepointservice-createreferencepoint.md) method of the [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md) class.

</dd> <dt>

[**Msvm\_CollectionReplicationService**](msvm-collectionreplicationservice.md)
</dt> <dd>

Manages the replication service for collection of virtual machines.

</dd> <dt>

[**Msvm\_CollectionReplicationSettingData**](msvm-collectionreplicationsettingdata.md)
</dt> <dd>

The class that represents configured settings for a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object.

</dd> <dt>

[**Msvm\_CollectionReplicationStatistics**](msvm-collectionreplicationstatistics.md)
</dt> <dd>

Provides replication statistics for a virtual system collection.

</dd> <dt>

[**Msvm\_CollectionSettingData**](msvm-collectionsettingdata.md)
</dt> <dd>

Represents the configured settings for an [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object.

</dd> <dt>

[**Msvm\_CollectionSnapshotExportSettingData**](msvm-collectionsnapshotexportsettingdata.md)
</dt> <dd>

The export setting data to pass to the [**ExportSnapshot**](msvm-collectionsnapshotservice-exportsnapshot.md) method of the [**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md) class.

</dd> <dt>

[**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
</dt> <dd>

Represents a service that manages snapshots of virtual machine collections.

</dd> <dt>

[**Msvm\_ComponentCS**](msvm-componentcs.md)
</dt> <dd>

Represents an aggregation relationship between an instance of [**Msvm\_ComputerSystem**](msvm-computersystem.md), and an instance of **Msvm\_ComputerSystem**.

</dd> <dt>

[**Msvm\_ComputerSystem**](msvm-computersystem.md)
</dt> <dd>

Represents a hosting computer system or virtual computer system.

</dd> <dt>

[**Msvm\_ComputerSystemSummaryInformation**](msvm-computersystemsummaryinformation.md)
</dt> <dd>

Associates a hosting computer system or a virtual machine with summary information.

</dd> <dt>

[**Msvm\_ConcreteIdentity**](msvm-concreteidentity.md)
</dt> <dd>

An association between two managed elements that represent different aspects of the same underlying entity.

</dd> <dt>

[**Msvm\_ConcreteJob**](msvm-concretejob.md)
</dt> <dd>

Represents an instantiable unit of work used in Hyper-V to track the progress of asynchronous operations.

</dd> <dt>

[**Msvm\_ElementConformsToProfile**](msvm-elementconformstoprofile.md)
</dt> <dd>

Defines the registered profile to which the referenced computer system conforms.

</dd> <dt>

[**Msvm\_ElementSettingData**](msvm-elementsettingdata.md)
</dt> <dd>

Associates a managed element with its configuration data.

</dd> <dt>

[**Msvm\_Error**](msvm-error.md)
</dt> <dd>

Represents information about the failure of a CIM operation for Hyper-V.

</dd> <dt>

[**Msvm\_FailoverIndication**](msvm-failoverindication.md)
</dt> <dd>

Represents information about a failover.

</dd> <dt>

[**Msvm\_HostedDependency**](msvm-hosteddependency.md)
</dt> <dd>

Associates a virtual computer system instance with the computer system object that represents the physical hosting system.

</dd> <dt>

[**Msvm\_HostedService**](msvm-hostedservice.md)
</dt> <dd>

Associates a service with its hosting computer system.

</dd> <dt>

[**Msvm\_ManagementCollection**](msvm-managementcollection.md)
</dt> <dd>

Represents a collection of collections.

</dd> <dt>

[**Msvm\_MemberOfCollection**](msvm-memberofcollection.md)
</dt> <dd>

Represents an association in which a collection aggregates its members.

</dd> <dt>

[**Msvm\_MigrationJob**](msvm-migrationjob.md)
</dt> <dd>

Represents a job that monitors a storage or virtual machine migration operation by the virtual system migration service.

</dd> <dt>

[**Msvm\_MostCurrentSnapshotInBranch**](msvm-mostcurrentsnapshotinbranch.md)
</dt> <dd>

Associates a virtual machine and the most current virtual machine snapshot in the virtual machine's branch of dependent snapshots.

</dd> <dt>

[**Msvm\_OwningJobElement**](msvm-owningjobelement.md)
</dt> <dd>

Associates a [**Msvm\_ConcreteJob**](msvm-concretejob.md) instance with the [**Msvm\_Service**](msvm-serviceaffectselement.md) object that created the job.

</dd> <dt>

[**Msvm\_ParentChildSettingData**](msvm-parentchildsettingdata.md)
</dt> <dd>

Represents an association between a virtual machine and the most recent snapshot of the virtual machine.

</dd> <dt>

[**Msvm\_RecoveryPointOfVirtualSystemCollection**](msvm-recoverypointofvirtualsystemcollection.md)
</dt> <dd>

Associates the [**Msvm\_CollectionRecoveryPoint**](msvm-collectionrecoverypoint.md) to the corresponding [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

</dd> <dt>

[**Msvm\_RedundancySet**](msvm-redundancyset.md)
</dt> <dd>

Represents a collection of managed elements that provide redundancy.

</dd> <dt>

[**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md)
</dt> <dd>

Represents a collection of virtual machine reference points.

</dd> <dt>

[**Msvm\_ReferencePointOfVirtualSystemCollection**](msvm-referencepointofvirtualsystemcollection.md)
</dt> <dd>

Associates a [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md) instance with [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

</dd> <dt>

[**Msvm\_ReferencedProfile**](msvm-referencedprofile.md)
</dt> <dd>

Used to associate an instance [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375) with an instance of **CIM\_RegisteredProfile** of another profile that references the dependent profile as a related profile.

</dd> <dt>

[**Msvm\_RegisteredProfile**](msvm-registeredprofile.md)
</dt> <dd>

Used to advertise implementation conformance to a profile.

</dd> <dt>

[**Msvm\_ReplicaCollectionDependency**](msvm-replicacollectiondependency.md)
</dt> <dd>

An association between an instance of [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md) that represents the replica collection and an instance of **CIM\_CollectionOfMSEs** that represents the test replica collection.

</dd> <dt>

[**Msvm\_ServiceAffectsElement**](msvm-serviceaffectselement.md)
</dt> <dd>

Associates an instance of a virtual machine with the management service that controls its state.

</dd> <dt>

[**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md)
</dt> <dd>

Associates a virtual machine and its devices with settings data.

</dd> <dt>

[**Msvm\_SharedDiskSetReplicationRelationship**](msvm-shareddisksetreplicationrelationship.md)
</dt> <dd>

Represents the replication relationship for the shared disks set of a collection.

</dd> <dt>

[**Msvm\_SharedDiskSetReplicationRelationshipOfVirtualSystemCollection**](msvm-shareddisksetreplicationrelationshipofvirtualsystemcollection.md)
</dt> <dd>

Associates the [**Msvm\_SharedDiskSetReplicationRelationship**](msvm-shareddisksetreplicationrelationship.md) to the corresponding [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) objects.

</dd> <dt>

[**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md)
</dt> <dd>

Represents a collection of virtual machine snapshots.

</dd> <dt>

[**Msvm\_SnapshotOfVirtualSystem**](msvm-snapshotofvirtualsystem.md)
</dt> <dd>

Associates an instance of the [**CIM\_ComputerSystem**](cim-computersystem.md) class that represents a virtual machine, and an instance of the [**CIM\_VirtualSystemSettingData**](cim-virtualsystemsettingdata.md) class that represents a snapshot of the virtual machine.

</dd> <dt>

[**Msvm\_SnapshotOfVirtualSystemCollection**](msvm-snapshotofvirtualsystemcollection.md)
</dt> <dd>

Associates a [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) object with a [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md) object.

</dd> <dt>

[**Msvm\_SummaryInformation**](msvm-summaryinformation.md)
</dt> <dd>

Used in the [**GetSummaryInformation**](msvm-virtualsystemmanagementservice-getsummaryinformation.md) method in the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class to quickly retrieve common information related to a virtual system or snapshot.

</dd> <dt>

[**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md)
</dt> <dd>

Retrieves summary information about a virtual machine or snapshot for the [**GetSummaryInformation**](msvm-virtualsystemmanagementservice-getsummaryinformation.md) method of the [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class.

</dd> <dt>

[**Msvm\_VirtualMachineToDisks**](msvm-virtualmachinetodisks.md)
</dt> <dd>

Setting data to be passed as an array to the [**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md) class.

</dd> <dt>

[**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md)
</dt> <dd>

Represents a collection of virtual machines.

</dd> <dt>

[**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md)
</dt> <dd>

Represents the virtualization service that manages virtual machines on a single host system.

</dd> <dt>

[**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md)
</dt> <dd>

Represents the settings for the virtualization service present on a single host system.

</dd> <dt>

[**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md)
</dt> <dd>

Represents the virtual system migration service. The service migrates virtual machines and virtual machine storage from one virtualization platform to another.

</dd> <dt>

[**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md)
</dt> <dd>

Represents a reference point for a virtual machine.

</dd> <dt>

[**Msvm\_VirtualSystemReferencePointExportSettingData**](msvm-virtualsystemreferencepointexportsettingdata.md)
</dt> <dd>

Provides additional information for the [**ExportReferencePoint**](msvm-collectionreferencepointservice-exportreferencepoint.md) method of the [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md) class.

</dd> <dt>

[**Msvm\_VirtualSystemReferencePointSettingData**](msvm-virtualsystemreferencepointsettingdata.md)
</dt> <dd>

Retrieves additional information for the [**CreateReferencePoint**](msvm-collectionreferencepointservice-createreferencepoint.md) method of the [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md) class.

</dd> <dt>

[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)
</dt> <dd>

Represents the virtualization-specific settings for a virtual machine.

</dd> <dt>

[**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md)
</dt> <dd>

Represents a service that manages snapshots of virtual machines.

</dd> <dt>

[**Msvm\_VirtualSystemSnapshotSettingData**](msvm-virtualsystemsnapshotsettingdata.md)
</dt> <dd>

Retrieves additional information for the [**CreateSnapshot**](msvm-virtualsystemsnapshotservice-createsnapshot.md) method of the [**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md) class.

</dd> </dl>

 

 




