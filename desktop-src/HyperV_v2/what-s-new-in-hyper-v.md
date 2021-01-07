---
description: Version 2 of the Hyper-V WMI provider is all new for Windows 8 and Windows Server 2012.
ms.assetid: A91ACF7A-AFE6-45B6-960C-C4AAA0083735
title: Whats new in Hyper-V WMI provider
ms.topic: article
ms.date: 05/31/2018
---

# What's new in Hyper-V WMI provider

Version 2 of the Hyper-V WMI provider is all new for Windows 8 and Windows Server 2012.

## Windows 10, version 1709

New classes:

-   [**Msvm\_Battery**](msvm-battery.md)
-   [**Msvm\_BatterySettingData**](msvm-batterysettingdata.md)
-   [**Msvm\_PersistentMemoryController**](msvm-persistentmemorycontroller.md)

New properties:

-   [**Msvm\_CollectionReferencePointExportJob**](msvm-collectionreferencepointexportjob.md): **ExportedGuestStateFilePaths**
-   [**Msvm\_EthernetSwitchHardwareOffloadData**](msvm-ethernetswitchhardwareoffloaddata.md): **DefaultQueueVrssIndependentHostSpreading**, **DefaultQueueVrssExcludePrimaryProcessor**, **DefaultQueueVrssQueueSchedulingMode**, and **DefaultQueueVrssMinQueuePairs**
-   [**Msvm\_EthernetSwitchHardwareOffloadSettingData**](msvm-ethernetswitchhardwareoffloadsettingdata.md): **DefaultQueueVrssIndependentHostSpreading**, **DefaultQueueVrssExcludePrimaryProcessor**, **DefaultQueueVrssQueueSchedulingMode**, **DefaultQueueVrssMinQueuePairs**,
-   [**Msvm\_EthernetSwitchPortOffloadData**](msvm-ethernetswitchportoffloaddata.md): **VrssVmbusChannelAffinityPolicy**, **VrssIndependentHostSpreading**, **VrssExcludePrimaryProcessor**, **VrssQueueSchedulingModes**, and **VrssMinQueuePairs**
-   [**Msvm\_VirtualHardDiskSettingData**](msvm-virtualharddisksettingdata.md): **DataAlignment**, **PmemAddressAbstractionType**, and **IsPmemCompatible**
-   [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md): **DisableDifferentialOfIgnoredStorage**, and **ExcludedVirtualHardDisks**
-   [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md): **HypervisorRootSchedulerEnabled**
-   [**Msvm\_VirtualSystemMigrationSettingData**](msvm-virtualsystemmigrationsettingdata.md): **CPUCappingMagnitude**, and **CancelIfBlackoutThresholdExceeded**
-   [**Msvm\_VirtualSystemReferencePointExportJob**](msvm-virtualsystemreferencepointexportjob.md): **ExportedGuestStateFilePath**
-   [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md): **Architecture**, **AutomaticSnapshotsEnabled**, **IsAutomaticSnapshot**, **GuestStateFile**, and **GuestStateDataRoot**

## Windows 10, version 1703

New classes:

-   [**Msvm\_AssignableDeviceDismountSettingData**](msvm-assignabledevicedismountsettingdata.md)
-   [**Msvm\_AssignableDeviceService**](msvm-assignabledeviceservice.md)
-   [**Msvm\_CollectionReferencePointExportJob**](msvm-collectionreferencepointexportjob.md)
-   [**Msvm\_EthernetSwitchHardwareOffloadSettingData**](msvm-ethernetswitchhardwareoffloadsettingdata.md)
-   [**Msvm\_EthernetSwitchPortMigrationQosSettingData**](msvm-ethernetswitchportmigrationqossettingdata.md)
-   [**Msvm\_EthernetSwitchPortRdmaSettingData**](msvm-ethernetswitchportrdmasettingdata.md)
-   [**Msvm\_EthernetSwitchPortTeamMappingSettingData**](msvm-ethernetswitchportteammappingsettingdata.md)
-   [**Msvm\_GpuPartition**](msvm-gpupartition.md)
-   [**Msvm\_GpuPartitionSettingData**](msvm-gpupartitionsettingdata.md)
-   [**Msvm\_NetworkConnectionDiagnosticInformation**](msvm-networkconnectiondiagnosticinformation.md)
-   [**Msvm\_NetworkConnectionDiagnosticSettingData**](msvm-networkconnectiondiagnosticsettingdata.md)
-   [**Msvm\_PartitionableGpu**](msvm-partitionablegpu.md)
-   [**Msvm\_PciExpress**](msvm-pciexpress.md)
-   [**Msvm\_PciExpressSettingData**](msvm-pciexpresssettingdata.md)
-   [**Msvm\_SecurityElement**](msvm-securityelement.md)
-   [**Msvm\_SecurityService**](msvm-securityservice.md)
-   [**Msvm\_SecuritySettingData**](msvm-securitysettingdata.md)
-   [**Msvm\_StorageSettingData**](msvm-storagesettingdata.md)
-   [**Msvm\_SummaryInformationBase**](msvm-summaryinformationbase.md)
-   [**Msvm\_SystemComponentSettingData**](msvm-systemcomponentsettingdata.md)
-   [**Msvm\_VirtualSystemReferencePointExportJob**](msvm-virtualsystemreferencepointexportjob.md)
-   [**Msvm\_VirtualSystemReferencePointSettingData**](msvm-virtualsystemreferencepointsettingdata.md)

Classes removed:

-   [**Msvm\_TPMSettingData**](msvm-tpmsettingdata.md)

New methods:

-   [**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md) class: [**ApplySnapshot**](msvm-collectionsnapshotservice-applysnapshot.md)
-   [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md) class: [**AddSystemComponentSetting**](msvm-virtualsystemmanagementservice-addsystemcomponentsettings.md), [**DiagnoseNetworkConnection**](msvm-virtualsystemmanagementservice-diagnosenetworkconnection.md), [**ModifySystemComponentSettings**](msvm-virtualsystemmanagementservice-modifysystemcomponentsettings.md), and [**RemoveSystemComponentSettings**](msvm-virtualsystemmanagementservice-removesystemcomponentsettings.md)
-   [**Msvm\_VirtualSystemReferencePointService**](msvm-virtualsystemreferencepointservice.md) class: [**ImportReferencePointMetadata**](msvm-virtualsystemreferencepointservice-importreferencepointmetadata.md)

New properties:

-   [**Msvm\_EthernetSwitchHardwareOffloadData**](msvm-ethernetswitchhardwareoffloaddata.md): **DefaultQueueVmmqQueuePairs**, **DefaultQueueVmmqEnabled** and **DefaultQueueVrssEnabled**
-   [**Msvm\_EthernetSwitchPortOffloadData**](msvm-ethernetswitchportoffloaddata.md): **VmmqQueuePairs**, **VmmqEnabled**, and **VrssEnabled**
-   [**Msvm\_EthernetSwitchPortOffloadSettingData**](msvm-ethernetswitchportoffloadsettingdata.md): **VmmqQueuePairs**, **VmmqEnabled** and **VrssEnabled**
-   [**Msvm\_GuestClusterInformation**](msvm-guestclusterinformation.md): **LastResourceMoveTime**
-   [**Msvm\_KvpExchangeComponentSettingData**](msvm-kvpexchangecomponentsettingdata.md): **DisableHostKVPItems**
-   [**Msvm\_MemorySettingData**](msvm-memorysettingdata.md): **SgxSize** and **SgxEnabled**
-   [**Msvm\_Physical3dGraphicsProcessor**](msvm-physical3dgraphicsprocessor.md): **CompatibleForVirtualization** and **DriverModelVersion**
-   [**Msvm\_ProcessorSettingData**](msvm-processorsettingdata.md): **HwThreadsPerCoreCpuGroupId**, **HideHypervisorPresent**, and **ExposeVirtualizationExtensions**
-   [**Msvm\_SettingsDefineCapabilities**](msvm-settingsdefinecapabilities.md): **SupportStatement**
-   [**Msvm\_StorageAllocationSettingData**](msvm-storageallocationsettingdata.md): **WriteHardeningMethod**
-   [**Msvm\_SummaryInformation**](msvm-summaryinformation.md): **Shielded**
-   [**Msvm\_SyntheticEthernetPortSettingData**](msvm-syntheticethernetportsettingdata.md): **AllowPacketDirect**
-   [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md): **LastApplyConsistencyLevel**, **LastApplyVirtualMachineIds**, **LastApplyTime**, **FailedOverReplicationType**, **ReplicationMode**, and **ReplicationState**
-   [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md): **ExportForLiveMigration**
-   [**Msvm\_VirtualSystemMigrationSettingData**](msvm-virtualsystemmigrationsettingdata.md): **AvoidRemovingVHDs**, and **AllowOverwriteExistingFile**
-   [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md): **HighMmioGapSize**
-   [**Msvm\_VirtualSystemSnapshotSettingData**](msvm-virtualsystemsnapshotsettingdata.md): **GuestBackupType**

Removed properties:

-   [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md): **ParentPackage**

## Windows 10

New classes:

-   [**CIM\_CollectedMSEs**](cim-collectedmses.md)
-   [**CIM\_Collection**](cim-collection.md)
-   [**CIM\_CollectionOfMSEs**](cim-collectionofmses.md)
-   [**CIM\_ElementView**](cim-elementview.md)
-   [**CIM\_MemberOfCollection**](cim-memberofcollection.md)
-   [**CIM\_TPM**](cim-tpm.md)
-   [**CIM\_View**](cim-view.md)
-   [**Msvm\_CollectedCollections**](msvm-collectedcollections.md)
-   [**Msvm\_CollectedReferencePoints**](msvm-collectedreferencepoints.md)
-   [**Msvm\_CollectedSnapshots**](msvm-collectedsnapshots.md)
-   [**Msvm\_CollectedVirtualSystems**](msvm-collectedvirtualsystems.md)
-   [**Msvm\_CollectionManagementService**](msvm-collectionmanagementservice.md)
-   [**Msvm\_CollectionReferencePointExportSettingData**](msvm-collectionreferencepointexportsettingdata.md)
-   [**Msvm\_CollectionReferencePointService**](msvm-collectionreferencepointservice.md)
-   [**Msvm\_CollectionReferencePointSettingData**](msvm-collectionreferencepointsettingdata.md)
-   [**Msvm\_CollectionSettingData**](msvm-collectionsettingdata.md)
-   [**Msvm\_CollectionSnapshotExportSettingData**](msvm-collectionsnapshotexportsettingdata.md)
-   [**Msvm\_CollectionSnapshotService**](msvm-collectionsnapshotservice.md)
-   [**Msvm\_ComputerSystemSummaryInformation**](msvm-computersystemsummaryinformation.md)
-   [**Msvm\_EthernetSwitchPortVfpSettingData**](msvm-ethernetswitchportvfpsettingdata.md)
-   [**Msvm\_GuestClusterInformation**](msvm-guestclusterinformation.md)
-   [**Msvm\_GuestCommunicationService**](msvm-guestcommunicationservice.md)
-   [**Msvm\_GuestCommunicationServiceSettingData**](msvm-guestcommunicationservicesettingdata.md)
-   [**Msvm\_GuestServiceInterfaceSettingDataComponent**](msvm-guestserviceinterfacesettingdatacomponent.md)
-   [**Msvm\_ManagementCollection**](msvm-managementcollection.md)
-   [**Msvm\_MoveUnmanagedVhd**](msvm-moveunmanagedvhd.md)
-   [**Msvm\_ReferencePointCollection**](msvm-referencepointcollection.md)
-   [**Msvm\_ReferencePointOfVirtualSystem**](msvm-referencepointofvirtualsystem.md)
-   [**Msvm\_ReferencePointOfVirtualSystemCollection**](msvm-referencepointofvirtualsystemcollection.md)
-   [**Msvm\_ResourceDependentOnResource**](msvm-resourcedependentonresource.md)
-   [**Msvm\_SerialPortSettingData**](msvm-serialportsettingdata.md)
-   [**Msvm\_ServiceOfVssComponent**](msvm-serviceofvsscomponent.md)
-   [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md)
-   [**Msvm\_SnapshotOfVirtualSystemCollection**](msvm-snapshotofvirtualsystemcollection.md)
-   [**Msvm\_StandaloneV2ElementConformsToProfile**](msvm-standalonev2elementconformstoprofile.md)
-   [**Msvm\_SyntheticDisplayControllerSettingData**](msvm-syntheticdisplaycontrollersettingdata.md)
-   [**Msvm\_SyntheticKeyboard**](msvm-synthetickeyboard.md)
-   [**Msvm\_TPM**](msvm-tpm.md)
-   [**Msvm\_TPMSettingData**](msvm-tpmsettingdata.md)
-   [**Msvm\_VHDSetInformation**](msvm-vhdsetinformation.md)
-   [**Msvm\_VHDSnapshotInformation**](msvm-vhdsnapshotinformation.md)
-   [**Msvm\_VirtualEthernetSwitchNicTeamingMember**](msvm-virtualethernetswitchnicteamingmember.md)
-   [**Msvm\_VirtualEthernetSwitchNicTeamingSettingData**](msvm-virtualethernetswitchnicteamingsettingdata.md)
-   [**Msvm\_VirtualMachineToDisks**](msvm-virtualmachinetodisks.md)
-   [**Msvm\_VirtualSystemCollection**](msvm-virtualsystemcollection.md)
-   [**Msvm\_VirtualSystemReferencePoint**](msvm-virtualsystemreferencepoint.md)
-   [**Msvm\_VirtualSystemReferencePointExportSettingData**](msvm-virtualsystemreferencepointexportsettingdata.md)
-   [**Msvm\_VirtualSystemReferencePointService**](msvm-virtualsystemreferencepointservice.md)
-   [**Msvm\_VirtualSystemReferencePointSettingData**](msvm-virtualsystemreferencepointsettingdata.md)
-   [**Msvm\_VirtualSystemSnapshotSettingData**](msvm-virtualsystemsnapshotsettingdata.md)
-   [**Msvm\_VssService**](msvm-vssservice.md)

Removed class:

-   [**Msvm\_ResourcePoolComponent**](msvm-resourcepoolcomponent.md)
-   [**Msvm\_ResourcePoolRegistration**](msvm-resourcepoolregistration.md)
-   [**Msvm\_ResourcePoolSettingData**](msvm-resourcepoolsettingdata.md)
-   [**Msvm\_VirtualizationComponent**](msvm-virtualizationcomponent.md)
-   [**Msvm\_VirtualizationComponentRegistration**](msvm-virtualizationcomponentregistration.md)

New properties:

-   [**Msvm\_BootSourceSettingData**](msvm-bootsourcesettingdata.md): **OptionalData**
-   [**Msvm\_EthernetPortAllocationSettingData**](msvm-ethernetportallocationsettingdata.md): **LastKnownSwitchName**, and **CompartmentGuid**
-   [**Msvm\_EthernetSwitchHardwareOffloadData**](msvm-ethernetswitchhardwareoffloaddata.md): **PacketDirectInUse**
-   [**Msvm\_EthernetSwitchPortOffloadSettingData**](msvm-ethernetswitchportoffloadsettingdata.md): **PacketDirectModerationInterval**, **PacketDirectModerationCount**, **PacketDirectNumProcs**,
-   [**Msvm\_EthernetSwitchPortSecuritySettingData**](msvm-ethernetswitchportsecuritysettingdata.md): **EnableFixSpeed10G**, and **Reserved**
-   [**Msvm\_GuestServiceInterfaceComponentSettingData**](msvm-guestserviceinterfacecomponentsettingdata.md): **DefaultEnabledStatePolicy**
-   [**Msvm\_ProcessorSettingData**](msvm-processorsettingdata.md): **EnableHostResourceProtection**
-   [**Msvm\_StorageAllocationSettingData**](msvm-storageallocationsettingdata.md): **StorageQoSPolicyID**, **CachingMode**, and **SnapshotId**
-   [**Msvm\_SummaryInformation**](msvm-summaryinformation.md): **InstanceID**, **Version**, **ThumbnailImageHeight**, **ThumbnailImageWidth**, and **HostComputerSystemName**
-   [**Msvm\_Synthetic3DDisplayControllerSettingData**](msvm-synthetic3ddisplaycontrollersettingdata.md): **VRAMSizeBytes**
-   [**Msvm\_VirtualEthernetSwitchSettingData**](msvm-virtualethernetswitchsettingdata.md): **TeamingEnabled**, and **PacketDirectEnabled**
-   [**Msvm\_VirtualHardDiskSettingData**](msvm-virtualharddisksettingdata.md): **ParentTimestamp**, and **ParentIdentifier**
-   [**Msvm\_VirtualHardDiskState**](msvm-virtualharddiskstate.md): **Timestamp**
-   [**Msvm\_VirtualSystemExportSettingData**](msvm-virtualsystemexportsettingdata.md): **BackupIntent**, and **DifferentialBackupBase**
-   [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md): **DefaultVirtualHardDiskCachingMode**
-   [**Msvm\_VirtualSystemMigrationSettingData**](msvm-virtualsystemmigrationsettingdata.md): **RemoveSourceUnmanagedVhds**, and **UnmanagedVhds**
-   [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md): **UserSnapshotType**, **GuestControlledCacheTypes**, **LockOnDisconnect**, **ParentPackage**, **AutomaticCriticalErrorActionTimeout**, **AutomaticCriticalErrorAction**, **ConsoleMode**, and **SecureBootTemplateId**

New methods:

-   [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class: [**ConvertVirtualHardDiskToVHDSet**](msvm-imagemanagementservice-convertvirtualharddisktovhdset.md), [**DeleteVHDSnapshot**](msvm-imagemanagementservice-deletevhdsnapshot.md), [**FindMountedStorageImageInstance**](msvm-imagemanagementservice-findmountedstorageimageinstance.md), [**GetVHDSetInformation**](msvm-imagemanagementservice-getvhdsetinformation.md), [**GetVHDSnapshotInformation**](msvm-imagemanagementservice-getvhdsnapshotinformation.md), [**GetVirtualDiskChanges**](msvm-imagemanagementservice-getvirtualdiskchanges.md), [**OptimizeVHDSet**](msvm-imagemanagementservice-optimizevhdset.md), and [**SetVHDSnapshotInformation**](msvm-imagemanagementservice-setvhdsnapshotinformation.md)
-   [**Msvm\_ShutdownComponent**](msvm-shutdowncomponent.md) class: [**InitiateReboot**](msvm-shutdowncomponent-initiatereboot.md)
-   [**Msvm\_VirtualSystemManagementService**](msvm-virtualsystemmanagementservice.md): [**AddBootSourceSettings**](msvm-virtualsystemmanagementservice-addbootsourcesettings.md), [**AddGuestServiceSettings**](msvm-virtualsystemmanagementservice-addguestservicesettings.md), [**DefinePlannedSystem**](msvm-virtualsystemmanagementservice-defineplannedsystem.md), [**ModifyGuestServiceSettings**](msvm-virtualsystemmanagementservice-modifyguestservicesettings.md), [**RemoveBootSourceSettings**](msvm-virtualsystemmanagementservice-removebootsourcesettings.md), [**RemoveGuesServiceSettings**](msvm-virtualsystemmanagementservice-removeguestservicesettings.md), [**SetInitialMachineConfigurationData**](msvm-virtualsystemmanagementservice-setinitialmachineconfigurationdata.md), and [**UpgradeSystemVersion**](msvm-virtualsystemmanagementservice-upgradesystemversion.md)
-   [**Msvm\_VirtualSystemSnapshotService**](msvm-virtualsystemsnapshotservice.md) class: [**ConvertToReferencePoint**](msvm-virtualsystemsnapshotservice-converttoreferencepoint.md)

## Windows 8.1 and Windows Server 2012 R2

Windows 8.1 and Windows Server 2012 R2 include new functionality for version 2 of the Hyper-V WMI provider.

-   The **IOPSAllocationUnits**, **IOPSLimit**, **IOPSReservation**, and **PersistentReservationsSupported** properties have been added to the [**Msvm\_StorageAllocationSettingData**](msvm-storageallocationsettingdata.md) class.
-   The **VirtualDiskId** property has been added to the [**Msvm\_VirtualHardDiskSettingData**](msvm-virtualharddisksettingdata.md) class.
-   Info about storage QoS has been added to the **OperationalStatus** property of the [**Msvm\_LogicalDisk**](msvm-logicaldisk.md) and [**Msvm\_ResourcePool**](msvm-resourcepool.md) classes.
-   [**Msvm\_StorageAlert**](msvm-storagealert.md) class
-   The **ClusterMonitored** property has been added to the [**Msvm\_EmulatedEthernetPortSettingData**](msvm-emulatedethernetportsettingdata.md) and [**Msvm\_SyntheticEthernetPortSettingData**](msvm-syntheticethernetportsettingdata.md) classes.
-   The **EnableCompression** and **EnableSmbTransport** properties have been added to the [**Msvm\_VirtualSystemMigrationServiceSettingData**](msvm-virtualsystemmigrationservicesettingdata.md) class.
-   The **EnableCompression** property has been added to the [**Msvm\_VirtualSystemMigrationSettingData**](msvm-virtualsystemmigrationsettingdata.md) class. The **TransportType** property includes info about live migration.
-   [**Msvm\_CopyFileToGuestJob**](msvm-copyfiletoguestjob.md) class
-   [**Msvm\_CopyFileToGuestSettingData**](msvm-copyfiletoguestsettingdata.md) class
-   [**Msvm\_GuestFileService**](msvm-guestfileservice.md) class
-   [**Msvm\_GuestService**](msvm-guestservice.md) class
-   [**Msvm\_GuestServiceInterfaceComponent**](msvm-guestserviceinterfacecomponent.md) class
-   [**Msvm\_GuestServiceInterfaceComponentSettingData**](msvm-guestserviceinterfacecomponentsettingdata.md) class
-   [**Msvm\_RegisteredGuestService**](msvm-registeredguestservice.md) class
-   The **EnhancedSessionModeEnabled** property has been added to the [**Msvm\_VirtualSystemManagementServiceSettingData**](msvm-virtualsystemmanagementservicesettingdata.md) class.
-   The **EnhancedModeState** property and the [**InjectNonMaskableInterrupt**](injectnonmaskableinterrupt-msvm-computersystem.md) method have been added to the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class.
-   The **BootSourceOrder**, **LowMmioGapSize**, **NetworkBootPreferredProtocol**, **PauseAfterBootFailure** , **SecureBootEnabled**, and **VirtualSystemSubType** properties have been added to the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class.
-   [**Msvm\_BootSourceSettingData**](msvm-bootsourcesettingdata.md) class
-   [**Msvm\_BootSourceComponent**](msvm-bootsourcecomponent.md) class
-   [**Msvm\_LogicalIdentity**](msvm-logicalidentity.md) class
-   [**Msvm\_CompatibilityVector**](msvm-compatibilityvector.md) class
-   The [**GetSystemCompatibilityVectors**](getsystemcompatibilityvectors-msvm-virtualsystemmigrationservice.md) method has been added to the [**Msvm\_VirtualSystemMigrationService**](msvm-virtualsystemmigrationservice.md) class.
-   The **ReplicationStateEx**, **ReplicationHealthEx**, **EnhancedSessionModeState**, **VirtualSwitchNames** , and **VirtualSystemSubType** properties have been added to the [**Msvm\_SummaryInformation**](msvm-summaryinformation.md) class. The **ReplicationState** and **ReplicationHealth** properties are deprecated and replaced by the **ReplicationStateEx** and **ReplicationHealthEx** properties.
-   The **PnpDevicePath** property has been added to the [**Msvm\_MountedStorageImage**](msvm-mountedstorageimage.md) class.
-   The **AllowedHashAlgorithms** and **TrustedIssuerCertificateHashes** properties have been added to the [**Msvm\_TerminalServiceSettingData**](msvm-terminalservicesettingdata.md) class.

Windows 8.1 and Windows Server 2012 R2 include new functionality for virtual machine replication and failover recovery.

-   [**Msvm\_ReplicationProvider**](msvm-replicationprovider.md) class
-   [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) class
-   The [**ChangeReplicationModeToPrimary**](changereplicationmodetoprimary-msvm-replicationservice.md), [**GetReplicationStatisticsEx**](getreplicationstatisticsex-msvm-replicationservice.md), [**InitiateFailback**](initiatefailback-msvm-replicationservice.md), [**RemoveReplicationRelationshipEx**](removereplicationrelationshipex-msvm-replicationservice.md), and [**ResetReplicationStatisticsEx**](resetreplicationstatisticsex-msvm-replicationservice.md) methods have been added to the [**Msvm\_ReplicationService**](msvm-replicationservice.md) class. The **GetReplicationStatisticsEx**, **RemoveReplicationRelationshipEx**, and **ResetReplicationStatisticsEx** methods replace the [**GetReplicationStatistics**](getreplicationstatistics-msvm-replicationservice.md), [**RemoveReplicationRelationship**](removereplicationrelationship-msvm-replicationservice.md), and [**ResetReplicationStatistics**](resetreplicationstatistics-msvm-replicationservice.md) methods.
-   The [**Msvm\_SystemReplicationRelationship**](msvm-systemreplicationrelationship.md) class shows an association between a virtual machine and many replication relationship.
-   The **AdditionalSettings** and **ReplicationProvider** properties have been added to the [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) class.
-   Info about host-to-host provider has been added to the [**CreateReplicationRelationship**](createreplicationrelationship-msvm-replicationservice.md) and [**ModifyReplicationSettings**](modifyreplicationsettings-msvm-replicationservice.md) methods of the [**Msvm\_ReplicationService**](msvm-replicationservice.md) class.
-   The [**RequestReplicationStateChangeEx**](msvm-requestreplicationstatechangeex-computersystem.md) method has been added to the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class and replaces the [**RequestReplicationStateChange**](msvm-computersystem-requestreplicationstatechange.md) method. The **InstanceID** property can now indicate extended replication. For more info about extended replication, see [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md).
-   [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) and [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) instances have a 1:1 relationship that you can represent with a [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md) association.

    | [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md) property name | Value                                                                                                |
    |-----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
    | **ManagedElement**                                                          | Represents the [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) object          |
    | **SettingData**                                                             | Represents the associated [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) object |

    

     

-   [**Msvm\_ReplicationSettingData**](msvm-replicationsettingdata.md) can differentiate between setting instances for replication relationship based on the **InstanceId** or **ReplicationRelationship** property. Therefore, these methods that deal with single relationship didn't change their signature:

    -   [**Msvm\_ReplicationService::CreateReplicationRelationship**](createreplicationrelationship-msvm-replicationservice.md)
    -   [**Msvm\_ReplicationService::ModifyReplicationSettings**](modifyreplicationsettings-msvm-replicationservice.md)
    -   [**Msvm\_ReplicationService::Resync**](resynchronize-msvm-replicationservice.md)
    -   [**Msvm\_ReplicationService::StartReplication**](startreplication-msvm-replicationservice.md)

-   Although you can use [**GetReplicationStatistics**](getreplicationstatistics-msvm-replicationservice.md), [**RemoveReplicationRelationship**](removereplicationrelationship-msvm-replicationservice.md), and [**RequestReplicationStateChange**](msvm-computersystem-requestreplicationstatechange.md) always for the primary relationship, we recommend that you instead use [**GetReplicationStatisticsEx**](getreplicationstatisticsex-msvm-replicationservice.md), [**RemoveReplicationRelationshipEx**](removereplicationrelationshipex-msvm-replicationservice.md), and [**RequestReplicationStateChangeEx**](msvm-requestreplicationstatechangeex-computersystem.md) because they can process primary and extended replication relationship. For more info about extended replication, see [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md).
-   Although these properties of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class continue to indicate the status for primary replication relationship, instead use these properties of a [**Msvm\_ReplicationRelationship**](msvm-replicationrelationship.md) object to determine the current status for primary and extended replication relationship.

    | Property name                                | Type        |
    |----------------------------------------------|-------------|
    | **ReplicationState**                         | Uint16 (RO) |
    | **ReplicationHealth**                        | Uint16 (RO) |
    | **LastReplicationTime**                      | DateTime    |
    | **FailedOverReplicationType**                | Uint16      |
    | **LastApplicationConsistentReplicationTime** | DateTime    |
    | **LastReplicationType**                      | Uint16      |

    

     

 

 



