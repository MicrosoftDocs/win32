---
title: iSCSI Target Server Provider
description: The iSCSI Target Server provider supports a Windows Management Instrumentation (WMI) interface for managing the Microsoft iSCSI Target Server, such as creating virtual disks, and for presenting them to the client.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a4e741cc-64c0-43e9-bca7-ee66037e3881'
ms.prod: 'windows-server-dev'
ms.technology:
- 'iscsi-target'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# iSCSI Target Server Provider

## Purpose

The iSCSI Target Server provider supports a Windows Management Instrumentation (WMI) interface for managing the Microsoft iSCSI Target Server, such as creating virtual disks, and for presenting them to the client.

## Developer audience

The iSCSI Target Server API is designed for WMI developers who use PowerShell, C#, C/C++, or a scripting language that has an engine in the Windows operating system and supports Microsoft ActiveX Controls. Familiarity with Component Object Model (COM) programming is helpful, but not required.

For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582).

For information on enabling and configuring iSCSI Target, see [Introduction of iSCSI Target in Windows Server 2012](http://blogs.technet.com/b/filecab/archive/2012/05/21/introduction-of-iscsi-target-in-windows-server-2012.aspx).

For information about the specification implemented by this API, see [RFC 3720](http://tools.ietf.org/html/rfc3720).

For information about related standards, see [Storage Management Initiative Specification (SMI-S)](http://www.snia.org/tech_activities/standards/curr_standards/smi) on the Storage Networking Industry Association (SNIA) website.

## Run-time requirements

The iSCSI Target Server API is included in Windows Server operating systems beginning with Windows Server 2012.

## In this section

-   [**CIM\_AffectedJobElement**](cim-affectedjobelement.md)
-   [**CIM\_AllocatedFromStoragePool**](cim-allocatedfromstoragepool.md)
-   [**CIM\_AuthenticationService**](cim-authenticationservice.md)
-   [**CIM\_AuthorizedPrivilege**](cim-authorizedprivilege.md)
-   [**CIM\_AuthorizedSubject**](cim-authorizedsubject.md)
-   [**CIM\_AuthorizedTarget**](cim-authorizedtarget.md)
-   [**CIM\_BindsTo**](cim-bindsto.md)
-   [**CIM\_Capabilities**](cim-capabilities.md)
-   [**CIM\_CommMechanismForManager**](cim-commmechanismformanager.md)
-   [**CIM\_Component**](cim-component.md)
-   [**CIM\_ComputerSystem**](cim-computersystem.md)
-   [**CIM\_ConcreteDependency**](cim-concretedependency.md)
-   [**CIM\_ControllerConfigurationService**](cim-controllerconfigurationservice.md)
-   [**CIM\_ConcreteJob**](cim-concretejob.md)
-   [**CIM\_Dependency**](cim-dependency.md)
-   [**CIM\_DeviceSAPImplementation**](cim-devicesapimplementation.md)
-   [**CIM\_ElementAllocatedFromPool**](cim-elementallocatedfrompool.md)
-   [**CIM\_ElementCapabilities**](cim-elementcapabilities.md)
-   [**CIM\_ElementConformsToProfile**](cim-elementconformstoprofile.md)
-   [**CIM\_ElementSettingData**](cim-elementsettingdata.md)
-   [**CIM\_ElementSoftwareIdentity**](cim-elementsoftwareidentity.md)
-   [**CIM\_EnabledLogicalElement**](cim-enabledlogicalelement.md)
-   [**CIM\_EndpointOfNetworkPipe**](cim-endpointofnetworkpipe.md)
-   [**CIM\_EthernetPort**](cim-ethernetport.md)
-   [**CIM\_HostedAccessPoint**](cim-hostedaccesspoint.md)
-   [**CIM\_HostedDependency**](cim-hosteddependency.md)
-   [**CIM\_HostedResourcePool**](cim-hostedresourcepool.md)
-   [**CIM\_HostedService**](cim-hostedservice.md)
-   [**CIM\_HostedStoragePool**](cim-hostedstoragepool.md)
-   [**CIM\_Identity**](cim-identity.md)
-   [**CIM\_IdentityManagementService**](cim-identitymanagementservice.md)
-   [**CIM\_IPProtocolEndpoint**](cim-ipprotocolendpoint.md)
-   [**CIM\_iSCSICapabilities**](cim-iscsicapabilities.md)
-   [**CIM\_iSCSIConfigurationCapabilities**](cim-iscsiconfigurationcapabilities.md)
-   [**CIM\_iSCSIConfigurationService**](cim-iscsiconfigurationservice.md)
-   [**CIM\_iSCSIConnection**](cim-iscsiconnection.md)
-   [**CIM\_iSCSIProtocolEndpoint**](cim-iscsiprotocolendpoint.md)
-   [**CIM\_iSCSISession**](cim-iscsisession.md)
-   [**CIM\_iSCSISessionSettings**](cim-iscsisessionsettings.md)
-   [**CIM\_Job**](cim-job.md)
-   [**CIM\_LogicalDevice**](cim-logicaldevice.md)
-   [**CIM\_LogicalElement**](cim-logicalelement.md)
-   [**CIM\_LogicalPort**](cim-logicalport.md)
-   [**CIM\_ManagedElement**](cim-managedelement.md)
-   [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
-   [**CIM\_Namespace**](cim-namespace.md)
-   [**CIM\_NamespaceInManager**](cim-namespaceinmanager.md)
-   [**CIM\_NetworkPipe**](cim-networkpipe.md)
-   [**CIM\_NetworkPipeComposition**](cim-networkpipecomposition.md)
-   [**CIM\_NetworkPort**](cim-networkport.md)
-   [**CIM\_ObjectManager**](cim-objectmanager.md)
-   [**CIM\_ObjectManagerCommunicationMechanism**](cim-objectmanagercommunicationmechanism.md)
-   [**CIM\_Privilege**](cim-privilege.md)
-   [**CIM\_ProtocolController**](cim-protocolcontroller.md)
-   [**CIM\_ProtocolControllerForDevice**](cim-protocolcontrollerfordevice.md)
-   [**CIM\_ProtocolControllerForUnit**](cim-protocolcontrollerforunit.md)
-   [**CIM\_ProtocolControllerMaskingCapabilities**](cim-protocolcontrollermaskingcapabilities.md)
-   [**CIM\_ProtocolEndpoint**](cim-protocolendpoint.md)
-   [**CIM\_RegisteredSubProfile**](cim-registeredsubprofile.md)
-   [**CIM\_ReplicationService**](cim-replicationservice.md)
-   [**CIM\_ReplicationServiceCapabilities**](cim-replicationservicecapabilities.md)
-   [**CIM\_ResourcePool**](cim-resourcepool.md)
-   [**CIM\_SAPAvailableForElement**](cim-sapavailableforelement.md)
-   [**CIM\_SAPSAPDependency**](cim-sapsapdependency.md)
-   [**CIM\_SCSIProtocolController**](cim-scsiprotocolcontroller.md)
-   [**CIM\_SCSIProtocolEndpoint**](cim-scsiprotocolendpoint.md)
-   [**CIM\_SecurityService**](cim-securityservice.md)
-   [**CIM\_Service**](cim-service.md)
-   [**CIM\_ServiceAccessBySAP**](cim-serviceaccessbysap.md)
-   [**CIM\_ServiceAccessPoint**](cim-serviceaccesspoint.md)
-   [**CIM\_SettingAssociatedToCapabilities**](cim-settingassociatedtocapabilities.md)
-   [**CIM\_SettingData**](cim-settingdata.md)
-   [**CIM\_SoftwareIdentity**](cim-softwareidentity.md)
-   [**CIM\_StorageCapabilities**](cim-storagecapabilities.md)
-   [**CIM\_StorageClientSettingData**](cim-storageclientsettingdata.md)
-   [**CIM\_StorageConfigurationCapabilities**](cim-storageconfigurationcapabilities.md)
-   [**CIM\_StorageConfigurationService**](cim-storageconfigurationservice.md)
-   [**CIM\_StorageExtent**](cim-storageextent.md)
-   [**CIM\_StorageHardwareID**](cim-storagehardwareid.md)
-   [**CIM\_StorageHardwareIDManagementService**](cim-storagehardwareidmanagementservice.md)
-   [**CIM\_StoragePool**](cim-storagepool.md)
-   [**CIM\_StorageReplicationCapabilities**](cim-storagereplicationcapabilities.md)
-   [**CIM\_StorageSetting**](cim-storagesetting.md)
-   [**CIM\_StorageSettingsAssociatedToCapabilities**](cim-storagesettingsassociatedtocapabilities.md)
-   [**CIM\_StorageSynchronized**](cim-storagesynchronized.md)
-   [**CIM\_StorageVolume**](cim-storagevolume.md)
-   [**CIM\_SubProfileRequiresProfile**](cim-subprofilerequiresprofile.md)
-   [**CIM\_Synchronized**](cim-synchronized.md)
-   [**CIM\_System**](cim-system.md)
-   [**CIM\_SystemComponent**](cim-systemcomponent.md)
-   [**CIM\_SystemDevice**](cim-systemdevice.md)
-   [**CIM\_TCPProtocolEndpoint**](cim-tcpprotocolendpoint.md)
-   [**CIM\_WBEMService**](cim-wbemservice.md)
-   [**MSFTSM\_CommMechanismForManager**](msftsm-commmechanismformanager.md)
-   [**MSFTSM\_ComputerSystem**](msftsm-computersystem.md)
-   [**MSFTSM\_ElementConformsToProfile**](msftsm-elementconformstoprofile.md)
-   [**MSFTSM\_ElementConformsToProfileEx**](msftsm-elementconformstoprofileex.md)
-   [**MSFTSM\_ElementSoftwareIdentity**](msftsm-elementsoftwareidentity.md)
-   [**MSFTSM\_HostedAccessPoint**](msftsm-hostedaccesspoint.md)
-   [**MSFTSM\_HostedService**](msftsm-hostedservice.md)
-   [**MSFTSM\_Namespace**](msftsm-namespace.md)
-   [**MSFTSM\_NamespaceInManager**](msftsm-namespaceinmanager.md)
-   [**MSFTSM\_ObjectManager**](msftsm-objectmanager.md)
-   [**MSFTSM\_ReferencedProfile**](msftsm-referencedprofile.md)
-   [**MSFTSM\_RegisteredProfile**](msftsm-registeredprofile.md)
-   [**MSFTSM\_RegisteredSubProfile**](msftsm-registeredsubprofile.md)
-   [**MSFTSM\_SoftwareIdentity**](msftsm-softwareidentity.md)
-   [**MSFTSM\_SubProfileRequiresProfile**](msftsm-subprofilerequiresprofile.md)
-   [**MSFTSM\_System**](msftsm-system.md)
-   [**MSFTSM\_WSManCommunicationMechanism**](msftsm-wsmancommunicationmechanism.md)
-   [**MSFTSMNET\_DeviceSAPImplementation**](msftsmnet-devicesapimplementation.md)
-   [**MSFTSMNET\_EthernetPort**](msftsmnet-ethernetport.md)
-   [**MSFTSMNET\_HostedAccessPoint**](msftsmnet-hostedaccesspoint.md)
-   [**MSFTSMNET\_IPProtocolEndpoint**](msftsmnet-ipprotocolendpoint.md)
-   [**MSFTSMNET\_SystemDevice**](msftsmnet-systemdevice.md)
-   [**MSISCSITARGET\_AffectedJobElement**](msiscsitarget-affectedjobelement.md)
-   [**MSISCSITARGET\_AllocatedFromStoragePool**](msiscsitarget-allocatedfromstoragepool.md)
-   [**MSISCSITARGET\_AuthorizedPrivilege**](msiscsitarget-authorizedprivilege.md)
-   [**MSISCSITARGET\_AuthorizedSubject**](msiscsitarget-authorizedsubject.md)
-   [**MSISCSITARGET\_AuthorizedTarget**](msiscsitarget-authorizedtarget.md)
-   [**MSISCSITARGET\_BindsTo**](msiscsitarget-bindsto.md)
-   [**MSISCSITARGET\_ConcreteDependency**](msiscsitarget-concretedependency.md)
-   [**MSISCSITARGET\_ConcreteJob**](msiscsitarget-concretejob.md)
-   [**MSISCSITARGET\_ControllerConfigurationService**](msiscsitarget-controllerconfigurationservice.md)
-   [**MSISCSITARGET\_DeviceSAPImplementation**](msiscsitarget-devicesapimplementation.md)
-   [**MSISCSITARGET\_ElementCapabilities**](msiscsitarget-elementcapabilities.md)
-   [**MSISCSITARGET\_ElementSettingData**](msiscsitarget-elementsettingdata.md)
-   [**MSISCSITARGET\_EndpointOfNetworkPipe**](msiscsitarget-endpointofnetworkpipe.md)
-   [**MSISCSITARGET\_HostedAccessPoint**](msiscsitarget-hostedaccesspoint.md)
-   [**MSISCSITARGET\_HostedService**](msiscsitarget-hostedservice.md)
-   [**MSISCSITARGET\_HostedStoragePool**](msiscsitarget-hostedstoragepool.md)
-   [**MSISCSITARGET\_iSCSICapabilities**](msiscsitarget-iscsicapabilities.md)
-   [**MSISCSITARGET\_iSCSIConfigurationCapabilities**](msiscsitarget-iscsiconfigurationcapabilities.md)
-   [**MSISCSITARGET\_iSCSIConfigurationService**](msiscsitarget-iscsiconfigurationservice.md)
-   [**MSISCSITARGET\_iSCSIConnection**](msiscsitarget-iscsiconnection.md)
-   [**MSISCSITARGET\_iSCSIProtocolEndpoint**](msiscsitarget-iscsiprotocolendpoint.md)
-   [**MSISCSITARGET\_iSCSISession**](msiscsitarget-iscsisession.md)
-   [**MSISCSITARGET\_iSCSISessionSettings**](msiscsitarget-iscsisessionsettings.md)
-   [**MSISCSITARGET\_NetworkPipeComposition**](msiscsitarget-networkpipecomposition.md)
-   [**MSISCSITARGET\_ProtocolControllerForUnit**](msiscsitarget-protocolcontrollerforunit.md)
-   [**MSISCSITARGET\_ProtocolControllerMaskingCapabilities**](msiscsitarget-protocolcontrollermaskingcapabilities.md)
-   [**MSISCSITARGET\_ReplicationService**](msiscsitarget-replicationservice.md)
-   [**MSISCSITARGET\_ReplicationServiceCapabilities**](msiscsitarget-replicationservicecapabilities.md)
-   [**MSISCSITARGET\_SAPAvailableForElement**](msiscsitarget-sapavailableforelement.md)
-   [**MSISCSITARGET\_SCSIProtocolController**](msiscsitarget-scsiprotocolcontroller.md)
-   [**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
-   [**MSISCSITARGET\_StorageClientSettingData**](msiscsitarget-storageclientsettingdata.md)
-   [**MSISCSITARGET\_StorageConfigurationCapabilities**](msiscsitarget-storageconfigurationcapabilities.md)
-   [**MSISCSITARGET\_StorageConfigurationService**](msiscsitarget-storageconfigurationservice.md)
-   [**MSISCSITARGET\_StorageHardwareID**](msiscsitarget-storagehardwareid.md)
-   [**MSISCSITARGET\_StorageHardwareIDManagementService**](msiscsitarget-storagehardwareidmanagementservice.md)
-   [**MSISCSITARGET\_StoragePool**](msiscsitarget-storagepool.md)
-   [**MSISCSITARGET\_StorageReplicationCapabilities**](msiscsitarget-storagereplicationcapabilities.md)
-   [**MSISCSITARGET\_StorageSetting**](msiscsitarget-storagesetting.md)
-   [**MSISCSITARGET\_StorageSettingsAssociatedToCapabilities**](msiscsitarget-storagesettingsassociatedtocapabilities.md)
-   [**MSISCSITARGET\_StorageSynchronized**](msiscsitarget-storagesynchronized.md)
-   [**MSISCSITARGET\_StorageVolume**](msiscsitarget-storagevolume.md)
-   [**MSISCSITARGET\_SystemDevice**](msiscsitarget-systemdevice.md)
-   [**MSISCSITARGET\_TCPProtocolEndpoint**](msiscsitarget-tcpprotocolendpoint.md)
-   [**WT\_CachedInitiatorInfo**](wt-cachedinitiatorinfo.md)
-   [**WT\_Connection**](wt-connection.md)
-   [**WT\_Disk**](wt-disk.md)
-   [**WT\_DVMountedPath**](wt-dvmountedpath.md)
-   [**WT\_General**](wt-general.md)
-   [**WT\_Host**](wt-host.md)
-   [**WT\_IDMethod**](wt-idmethod.md)
-   [**WT\_iSCSIStorageProviderIdentity**](wt-iscsistorageprovideridentity.md)
-   [**WT\_iSCSIStorageSubsystem**](wt-iscsistoragesubsystem.md)
-   [**WT\_ISnsServer**](wt-isnsserver.md)
-   [**WT\_LUNMapping**](wt-lunmapping.md)
-   [**WT\_Portal**](wt-portal.md)
-   [**WT\_Session**](wt-session.md)
-   [**WT\_Snapshot**](wt-snapshot.md)
-   [**WT\_VDSLunInformation**](wt-vdsluninformation.md)
-   [**WT\_Volume**](wt-volume.md)
-   [**WT\_VPDIdentificationDescriptor**](wt-vpdidentificationdescriptor.md)

 

 




