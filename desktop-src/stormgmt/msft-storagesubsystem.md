---
title: MSFT\_StorageSubSystem class
description: Represents a storage array subsystem that exposes virtual disks and/or a computer system that exposes file server capabilities.
ms.assetid: 3fa2f78f-be75-42c0-baba-b08f4959af8c
keywords:
- MSFT_StorageSubSystem class Windows Storage Management API
- MSFT_StorageSubSystem class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystem
- MSFT_StorageSubSystem.FriendlyName
- MSFT_StorageSubSystem.Description
- MSFT_StorageSubSystem.Name
- MSFT_StorageSubSystem.NameFormat
- MSFT_StorageSubSystem.OtherIdentifyingInfo
- MSFT_StorageSubSystem.OtherIdentifyingInfoDescription
- MSFT_StorageSubSystem.HealthStatus
- MSFT_StorageSubSystem.OperationalStatus
- MSFT_StorageSubSystem.OtherOperationalStatusDescription
- MSFT_StorageSubSystem.CurrentCacheLevel
- MSFT_StorageSubSystem.Manufacturer
- MSFT_StorageSubSystem.Model
- MSFT_StorageSubSystem.SerialNumber
- MSFT_StorageSubSystem.FirmwareVersion
- MSFT_StorageSubSystem.Tag
- MSFT_StorageSubSystem.AutomaticClusteringEnabled
- MSFT_StorageSubSystem.PhysicalDisksPerStoragePoolMin
- MSFT_StorageSubSystem.SupportsMirrorLocal
- MSFT_StorageSubSystem.SupportsMirrorRemote
- MSFT_StorageSubSystem.SupportsSnapshotLocal
- MSFT_StorageSubSystem.SupportsSnapshotRemote
- MSFT_StorageSubSystem.SupportsCloneLocal
- MSFT_StorageSubSystem.SupportsCloneRemote
- MSFT_StorageSubSystem.SupportsVirtualDiskCreation
- MSFT_StorageSubSystem.SupportsVirtualDiskModification
- MSFT_StorageSubSystem.SupportsVirtualDiskDeletion
- MSFT_StorageSubSystem.SupportsVirtualDiskCapacityExpansion
- MSFT_StorageSubSystem.SupportsVirtualDiskCapacityReduction
- MSFT_StorageSubSystem.SupportsVirtualDiskRepair
- MSFT_StorageSubSystem.SupportsVolumeCreation
- MSFT_StorageSubSystem.SupportsStoragePoolCreation
- MSFT_StorageSubSystem.SupportsStoragePoolDeletion
- MSFT_StorageSubSystem.SupportsStoragePoolFriendlyNameModification
- MSFT_StorageSubSystem.SupportsStoragePoolAddPhysicalDisk
- MSFT_StorageSubSystem.SupportsStoragePoolRemovePhysicalDisk
- MSFT_StorageSubSystem.SupportsAutomaticStoragePoolSelection
- MSFT_StorageSubSystem.SupportsMultipleResiliencySettingsPerStoragePool
- MSFT_StorageSubSystem.SupportsStorageTierCreation
- MSFT_StorageSubSystem.SupportsStorageTierDeletion
- MSFT_StorageSubSystem.SupportsStorageTierResize
- MSFT_StorageSubSystem.SupportsStorageTierFriendlyNameModification
- MSFT_StorageSubSystem.SupportsStorageTieredVirtualDiskCreation
- MSFT_StorageSubSystem.ReplicasPerSourceSnapshotMax
- MSFT_StorageSubSystem.ReplicasPerSourceCloneMax
- MSFT_StorageSubSystem.ReplicasPerSourceMirrorMax
- MSFT_StorageSubSystem.SupportsMaskingVirtualDiskToHosts
- MSFT_StorageSubSystem.MaskingValidInitiatorIdTypes
- MSFT_StorageSubSystem.MaskingOtherValidInitiatorIdTypes
- MSFT_StorageSubSystem.MaskingPortsPerView
- MSFT_StorageSubSystem.MaskingClientSelectableDeviceNumbers
- MSFT_StorageSubSystem.MaskingOneInitiatorIdPerView
- MSFT_StorageSubSystem.MaskingMapCountMax
- MSFT_StorageSubSystem.DataTieringType
- MSFT_StorageSubSystem.iSCSITargetCreationScheme
- MSFT_StorageSubSystem.NumberOfSlots
- MSFT_StorageSubSystem.SupportedHostType
- MSFT_StorageSubSystem.OtherHostTypeDescription
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageSubSystem class

Represents a storage array subsystem that exposes virtual disks and/or a computer system that exposes file server capabilities.

Storage subsystems expose virtual disks to Windows. Storage subsystems respond to administrative commands through corresponding storage providers.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
class MSFT_StorageSubSystem : MSFT_StorageObject
{
  String  FriendlyName;
  String  Description;
  String  Name;
  UInt16  NameFormat;
  String  OtherIdentifyingInfo[];
  String  OtherIdentifyingInfoDescription[];
  UInt16  HealthStatus;
  UInt16  OperationalStatus[];
  String  OtherOperationalStatusDescription;
  UInt16  CurrentCacheLevel;
  String  Manufacturer;
  String  Model;
  String  SerialNumber;
  String  FirmwareVersion;
  String  Tag;
  Boolean AutomaticClusteringEnabled;
  UInt16  PhysicalDisksPerStoragePoolMin;
  Boolean SupportsMirrorLocal;
  Boolean SupportsMirrorRemote;
  Boolean SupportsSnapshotLocal;
  Boolean SupportsSnapshotRemote;
  Boolean SupportsCloneLocal;
  Boolean SupportsCloneRemote;
  Boolean SupportsVirtualDiskCreation;
  Boolean SupportsVirtualDiskModification;
  Boolean SupportsVirtualDiskDeletion;
  Boolean SupportsVirtualDiskCapacityExpansion;
  Boolean SupportsVirtualDiskCapacityReduction;
  Boolean SupportsVirtualDiskRepair;
  Boolean SupportsVolumeCreation;
  Boolean SupportsStoragePoolCreation;
  Boolean SupportsStoragePoolDeletion;
  Boolean SupportsStoragePoolFriendlyNameModification;
  Boolean SupportsStoragePoolAddPhysicalDisk;
  Boolean SupportsStoragePoolRemovePhysicalDisk;
  Boolean SupportsAutomaticStoragePoolSelection;
  Boolean SupportsMultipleResiliencySettingsPerStoragePool;
  Boolean SupportsStorageTierCreation;
  Boolean SupportsStorageTierDeletion;
  Boolean SupportsStorageTierResize;
  Boolean SupportsStorageTierFriendlyNameModification;
  Boolean SupportsStorageTieredVirtualDiskCreation;
  Uint16  ReplicasPerSourceSnapshotMax;
  Uint16  ReplicasPerSourceCloneMax;
  Uint16  ReplicasPerSourceMirrorMax;
  Boolean SupportsMaskingVirtualDiskToHosts;
  Uint16  MaskingValidInitiatorIdTypes[];
  String  MaskingOtherValidInitiatorIdTypes[];
  Uint16  MaskingPortsPerView;
  Boolean MaskingClientSelectableDeviceNumbers;
  Boolean MaskingOneInitiatorIdPerView;
  Uint16  MaskingMapCountMax;
  Uint16  DataTieringType;
  Uint16  iSCSITargetCreationScheme;
  UInt32  NumberOfSlots;
  UInt16  SupportedHostType[];
  String  OtherHostTypeDescription[];
};
```

## Members

The **MSFT\_StorageSubSystem** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageSubSystem** class has these methods.



| Method                                                                                       | Description                                                                                                              |
|:---------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------|
| [**CreateFileServer**](msft-storagesubsystem-createfileserver.md)                           | **Starting in Windows 10:** Creates a file server on a storage subsystem.<br/>                                     |
| [**CreateMaskingSet**](msft-storagesubsystem-createmaskingset.md)                           | Creates a new masking set.<br/>                                                                                    |
| [**CreateReplicationGroup**](msft-storagesubsystem-createreplicationgroup.md)               | **Starting in Windows 10:** Creates a replication group on a storage subsystem.<br/>                               |
| [**CreateReplicationRelationship**](msft-storagesubsystem-createreplicationrelationship.md) | **Starting in Windows 10:** Creates two replication groups and a replication relationship between them.<br/>       |
| [**CreateStoragePool**](createstoragepool-msft-storagesubsystem.md)                         | Creates a storage pool from available physical disks contained within a common primordial pool.<br/>               |
| [**CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md)                         | Creates a new virtual disk.<br/>                                                                                   |
| [**DeleteReplicationRelationship**](msft-storagesubsystem-deletereplicationrelationship.md) | **Starting in Windows 10:** Deletes a replication relationship between groups.<br/>                                |
| [**Diagnose**](msft-storagesubsystem-diagnose.md)                                           | **Starting in Windows 10:** Performs a diagnostic on the storage subsystem, returning any actionable results.<br/> |
| [**GetDiagnosticInfo**](msft-storagesubsystem-getdiagnosticinfo.md)                         | **Starting in Windows 10:** Gets the diagnostic information of the storage subsystem.<br/>                         |
| [**GetSecurityDescriptor**](msft-storagesubsystem-getsecuritydescriptor.md)                 | Retrieves the security descriptor that controls access to the storage subsystem object instance.<br/>              |
| [**SetAttributes**](msft-storagesubsystem-setattributes.md)                                 | Sets the **SupportsAutomaticObjectClustering** field of the storage subsystem object instance.<br/>                |
| [**SetDescription**](msft-storagesubsystem-setdescription.md)                               | Sets the **Description** property of the storage subsystem object instance.<br/>                                   |
| [**SetSecurityDescriptor**](msft-storagesubsystem-setsecuritydescriptor.md)                 | Sets the security descriptor that controls access to the storage subsystem object instance.<br/>                   |
| [**StartDiagnosticLog**](msft-storagesubsystem-startdiagnosticlog.md)                       | **Starting in Windows 10:** Starts a diagnostic log for the storage subsystem.<br/>                                |
| [**StopDiagnosticLog**](msft-storagesubsystem-stopdiagnosticlog.md)                         | **Starting in Windows 10:** Stops the diagnostic log for the storage subsystem.<br/>                               |



 

### Properties

The **MSFT\_StorageSubSystem** class has these properties.

<dl> <dt>

**AutomaticClusteringEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this subsystem supports automatic object clustering; otherwise, **FALSE**.

</dd> <dt>

**CurrentCacheLevel**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The cache level that has been discovered. This corresponds to the storage provider's *DiscoveryLevel* parameter in the [**Discover**](discover-msft-storageprovider.md) method.



| Value                                                                                                                                                                                                                       | Meaning                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Level_0"></span><span id="level_0"></span><span id="LEVEL_0"></span><dl> <dt>**Level 0**</dt> <dt>0</dt> </dl> | The storage provider and storage subsystem objects have been discovered.<br/>                                                                      |
| <span id="Level_1"></span><span id="level_1"></span><span id="LEVEL_1"></span><dl> <dt>**Level 1**</dt> <dt>1</dt> </dl> | Storage pools, resiliency settings, target ports, target portals, and initiator identifiers belonging to this subsystem have been discovered.<br/> |
| <span id="Level_2"></span><span id="level_2"></span><span id="LEVEL_2"></span><dl> <dt>**Level 2**</dt> <dt>2</dt> </dl> | Virtual disks and masking sets belonging to this subsystem have been discovered.<br/>                                                              |
| <span id="Level_3"></span><span id="level_3"></span><span id="LEVEL_3"></span><dl> <dt>**Level 3**</dt> <dt>3</dt> </dl> | Physical disks belonging to this subsystem have been discovered.<br/>                                                                              |



 

</dd> <dt>

**DataTieringType**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The type of data tiering, if any, that is supported by the storage subsystem.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)
</dt> <dt>

<span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span>**Manual** (2)
</dt> <dt>

<span id="Auto"></span><span id="auto"></span><span id="AUTO"></span>**Auto** (3)
</dt> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable description of the storage subsystem. This field can be used to store extra free-form information, such as notes or details about the subsystem's intended usage.

</dd> <dt>

**FirmwareVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The firmware version of the storage subsystem array.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-settable string containing the name of the storage subsystem. The storage provider is expected to supply an initial value for this field.

</dd> <dt>

**HealthStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The health status of the subsystem.



| Value                                                                                                                                                                                                                                    | Meaning                                                                                                                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Healthy"></span><span id="healthy"></span><span id="HEALTHY"></span><dl> <dt>**Healthy**</dt> <dt>0</dt> </dl>              | The storage subsystem is functioning normally.<br/>                                                                                      |
| <span id="Warning"></span><span id="warning"></span><span id="WARNING"></span><dl> <dt>**Warning**</dt> <dt>1</dt> </dl>              | The storage subsystem is still functioning, but has detected errors or issues that require administrator intervention.<br/>              |
| <span id="Unhealthy_"></span><span id="unhealthy_"></span><span id="UNHEALTHY_"></span><dl> <dt>**Unhealthy** </dt> <dt>2 </dt> </dl> | The storage subsystem is not functioning, due to errors or failures. The subsystem needs immediate attention from an administrator.<br/> |



 

</dd> <dt>

**iSCSITargetCreationScheme**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The iSCSI target creation scheme, if any, that is supported by the storage subsystem.



| Value                                                                                                                                                                                                                                                   | Meaning                                                       |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span><dl> <dt>**Not Applicable**</dt> <dt>0</dt> </dl> | The subsystem is a non-iSCSI subsystem.<br/>            |
| <span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span><dl> <dt>**Not Supported**</dt> <dt>1</dt> </dl>     | The subsystem does not allow creation of a target.<br/> |
| <span id="Manual"></span><span id="manual"></span><span id="MANUAL"></span><dl> <dt>**Manual**</dt> <dt>2</dt> </dl>                                 | The subsystem allows manual creation of a target.<br/>  |
| <span id="Auto"></span><span id="auto"></span><span id="AUTO"></span><dl> <dt>**Auto**</dt> <dt>3</dt> </dl>                                         | The subsystem automatically creates a target.<br/>      |



 

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The name of the company responsible for creating the storage subsystem hardware.

</dd> <dt>

**MaskingClientSelectableDeviceNumbers**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if this storage subsystem allows the client to specify the *DeviceNumber* parameter in methods such as [**MSFT\_StorageSubsystem::CreateMaskingSet**](msft-storagesubsystem-createmaskingset.md) and [**MSFT\_MaskingSet::AddVirtualDisk**](msft-maskingset-addvirtualdisk.md).

</dd> <dt>

**MaskingMapCountMax**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of masking sets that can be a particular virtual disk can be added to. If this property is zero, there is no limit.

</dd> <dt>

**MaskingOneInitiatorIdPerView**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if this storage subsystem allows only one initiator identifier per masking set.

</dd> <dt>

**MaskingOtherValidInitiatorIdTypes**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

If one of the elements in the **MaskingValidInitiatorIdTypes** array is **Other**, this property is an array that contains the other valid [**MSFT\_InitiatorId**](msft-initiatorid.md) types.

</dd> <dt>

**MaskingPortsPerView**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of target ports that can be used for masking a virtual disk. This applies to masking sets and to the [**MSFT\_VirtualDisk.Show**](msft-virtualdisk-show.md) method.



| Value                                                                        | Meaning                                              |
|------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>2</dt> </dl> | There is only one target per view.<br/>        |
| <dl> <dt>3</dt> </dl> | There are multiple target ports per view.<br/> |
| <dl> <dt>4</dt> </dl> | All target ports share the same view.<br/>     |



 

</dd> <dt>

**MaskingValidInitiatorIdTypes**
</dt> <dd> <dl> <dt>

Data type: **Uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array that contains the address formats the storage provider and subsystem can expect when working with initiator identifiers.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Port_WWN"></span><span id="port_wwn"></span><span id="PORT_WWN"></span>**Port WWN** (2)
</dt> <dt>

<span id="Node_WWN"></span><span id="node_wwn"></span><span id="NODE_WWN"></span>**Node WWN** (3)
</dt> <dt>

<span id="Host_Name"></span><span id="host_name"></span><span id="HOST_NAME"></span>**Host Name** (4)
</dt> <dt>

<span id="iSCSI_Name"></span><span id="iscsi_name"></span><span id="ISCSI_NAME"></span>**iSCSI Name** (5)
</dt> <dt>

<span id="Switch_WWN"></span><span id="switch_wwn"></span><span id="SWITCH_WWN"></span>**Switch WWN** (6)
</dt> <dt>

<span id="SAS_Address"></span><span id="sas_address"></span><span id="SAS_ADDRESS"></span>**SAS Address** (7)
</dt> </dl>

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The model number of the storage subsystem array.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

A globally unique, human-readable string used to identify the storage subsystem.

</dd> <dt>

**NameFormat**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The format of the string stored in the **Name** property.

<dl> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="IP"></span><span id="ip"></span>**IP** (2)
</dt> <dt>

<span id="Dial"></span><span id="dial"></span><span id="DIAL"></span>**Dial** (3)
</dt> <dt>

<span id="HID"></span><span id="hid"></span>**HID** (4)
</dt> <dt>

<span id="NWA"></span><span id="nwa"></span>**NWA** (5)
</dt> <dt>

<span id="HWA"></span><span id="hwa"></span>**HWA** (6)
</dt> <dt>

<span id="X25"></span><span id="x25"></span>**X25** (7)
</dt> <dt>

<span id="ISDN"></span><span id="isdn"></span>**ISDN** (8)
</dt> <dt>

<span id="IPX"></span><span id="ipx"></span>**IPX** (9)
</dt> <dt>

<span id="DCC"></span><span id="dcc"></span>**DCC** (10)
</dt> <dt>

<span id="ICD"></span><span id="icd"></span>**ICD** (11)
</dt> <dt>

<span id="E.164"></span><span id="e.164"></span>**E.164** (12)
</dt> <dt>

<span id="SNA"></span><span id="sna"></span>**SNA** (13)
</dt> <dt>

<span id="OID_OSI"></span><span id="oid_osi"></span>**OID/OSI** (14)
</dt> <dt>

<span id="WWN"></span><span id="wwn"></span>**WWN** (15)
</dt> <dt>

<span id="NAA"></span><span id="naa"></span>**NAA** (16)
</dt> </dl>

</dd> <dt>

**NumberOfSlots**
</dt> <dd> <dl> <dt>

Data type: **UInt32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum number of physical disk slots in the subsystem or enclosure.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

An array of values that denote the current operational status of the subsystem.



| Value                                                                                                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span><dl> <dt>**Unknown**</dt> <dt>0</dt> </dl>                                                                              | The operational status is unknown.<br/>                                                                                                                                                           |
| <span id="Other"></span><span id="other"></span><span id="OTHER"></span><dl> <dt>**Other**</dt> <dt>1</dt> </dl>                                                                                      | A vendor-specific **OperationalStatus** has been specified by setting the **OtherOperationalStatusDescription** property.<br/>                                                                    |
| <span id="OK"></span><span id="ok"></span><dl> <dt>**OK**</dt> <dt>2</dt> </dl>                                                                                                                       | The storage subsystem is responding to commands and is in a normal operating state.<br/>                                                                                                          |
| <span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span><dl> <dt>**Degraded**</dt> <dt>3</dt> </dl>                                                                          | The storage subsystem is responding to commands, but is not running in an optimal operating state.<br/>                                                                                           |
| <span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span><dl> <dt>**Stressed**</dt> <dt>4</dt> </dl>                                                                          | The storage subsystem is functioning, but needs attention. For example, the storage subsystem might be overloaded or overheated.<br/>                                                             |
| <span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span><dl> <dt>**Predictive Failure**</dt> <dt>5</dt> </dl>                                  | The storage subsystem is functioning, but a failure is likely to occur in the near future.<br/>                                                                                                   |
| <span id="Error"></span><span id="error"></span><span id="ERROR"></span><dl> <dt>**Error**</dt> <dt>6</dt> </dl>                                                                                      | An error has occurred.<br/>                                                                                                                                                                       |
| <span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span><dl> <dt>**Non-Recoverable Error**</dt> <dt>7</dt> </dl>                      | A nonrecoverable error has occurred.<br/>                                                                                                                                                         |
| <span id="Starting"></span><span id="starting"></span><span id="STARTING"></span><dl> <dt>**Starting**</dt> <dt>8</dt> </dl>                                                                          | The storage subsystem is in the process of starting.<br/>                                                                                                                                         |
| <span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span><dl> <dt>**Stopping**</dt> <dt>9</dt> </dl>                                                                          | The storage subsystem is in the process of stopping.<br/>                                                                                                                                         |
| <span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span><dl> <dt>**Stopped**</dt> <dt>10</dt> </dl>                                                                             | The storage subsystem was stopped or shut down in a clean and orderly fashion.<br/>                                                                                                               |
| <span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span><dl> <dt>**In Service**</dt> <dt>11</dt> </dl>                                                                 | The storage subsystem is being configured, maintained, cleaned, or otherwise administered.<br/>                                                                                                   |
| <span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span><dl> <dt>**No Contact**</dt> <dt>12</dt> </dl>                                                                 | The storage provider has knowledge of the storage subsystem, but has never been able to establish communication with it.<br/>                                                                     |
| <span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span><dl> <dt>**Lost Communication**</dt> <dt>13</dt> </dl>                                 | The storage provider has knowledge of the storage subsystem and has contacted it successfully in the past, but the storage subsystem is currently unreachable.<br/>                               |
| <span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span><dl> <dt>**Aborted**</dt> <dt>14</dt> </dl>                                                                             | Similar to **Stopped**, except that the storage subsystem stopped abruptly and may require configuration or maintenance.<br/>                                                                     |
| <span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span><dl> <dt>**Dormant**</dt> <dt>15</dt> </dl>                                                                             | The storage subsystem is reachable, but it is inactive.<br/>                                                                                                                                      |
| <span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span><dl> <dt>**Supporting Entity in Error**</dt> <dt>16</dt> </dl> | This status value does not necessarily indicate trouble with the storage subsystem, but it does indicate that another device or connection that the subsystem depends on may need attention.<br/> |
| <span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span><dl> <dt>**Completed**</dt> <dt>17</dt> </dl>                                                                     | The storage subsystem has completed an operation. This status value should be combined with **OK**, **Error**, or **Degraded**, depending on the outcome of the operation<br/>                    |
| <span id="Power_Mode_"></span><span id="power_mode_"></span><span id="POWER_MODE_"></span><dl> <dt>**Power Mode** </dt> <dt>18 </dt> </dl>                                                            | This value is reserved for system use.<br/>                                                                                                                                                       |



 

</dd> <dt>

**OtherHostTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ( "Indexed" ), [**ModelCorrespondence {"CIM\_StorageClientSettingData.ClientTypes"}**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If the corresponding entry in the **SupportedHostType** array is **Other**, the entry in this property contains a string describing the manufacturer and operating system or environment.

If the corresponding entry in the **SupportedHostType** array is not **Other**, the entry in this property allows variations or qualifications of **ClientTypes** for example, different versions of Solaris.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of strings, each containing a custom identifier for the subsystem. If this property is set, the **NameFormat** property must be set to **Other** and the **OtherIdentifyingInfoDescription** property must also be set.

</dd> <dt>

**OtherIdentifyingInfoDescription**
</dt> <dd> <dl> <dt>

Data type: **String** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array containing string descriptions of the formats used in each of the custom identifiers in the **OtherIdentifyingInfo** array. There must be a 1:1 mapping between the elements in this array and the elements **OtherIdentifyingInfo** array.

</dd> <dt>

**OtherOperationalStatusDescription**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A string representation of the vendor-defined operational status. This property should only be set if the value of the **OperationalStatus** property is **Other**.

</dd> <dt>

**PhysicalDisksPerStoragePoolMin**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The minimum number of physical disks needed for a storage pool on this subsystem.

</dd> <dt>

**ReplicasPerSourceCloneMax**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**ReplicasPerSourceMirrorMax**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reserved for future use.

</dd> <dt>

**ReplicasPerSourceSnapshotMax**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

Reserved for system use.

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The serial number of the storage subsystem array.

</dd> <dt>

**SupportedHostType**
</dt> <dd> <dl> <dt>

Data type: **UInt16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

An array of values that specify the supported host types.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)
</dt> <dt>

<span id="Standard"></span><span id="standard"></span><span id="STANDARD"></span>**Standard** (2)
</dt> <dt>

<span id="Solaris"></span><span id="solaris"></span><span id="SOLARIS"></span>**Solaris** (3)
</dt> <dt>

<span id="HPUX"></span><span id="hpux"></span>**HPUX** (4)
</dt> <dt>

<span id="OpenVMS"></span><span id="openvms"></span><span id="OPENVMS"></span>**OpenVMS** (5)
</dt> <dt>

<span id="Tru64"></span><span id="tru64"></span><span id="TRU64"></span>**Tru64** (6)
</dt> <dt>

<span id="Netware"></span><span id="netware"></span><span id="NETWARE"></span>**Netware** (7)
</dt> <dt>

<span id="Sequent"></span><span id="sequent"></span><span id="SEQUENT"></span>**Sequent** (8)
</dt> <dt>

<span id="AIX"></span><span id="aix"></span>**AIX** (9)
</dt> <dt>

<span id="DGUX"></span><span id="dgux"></span>**DGUX** (10)
</dt> <dt>

<span id="Dynix"></span><span id="dynix"></span><span id="DYNIX"></span>**Dynix** (11)
</dt> <dt>

<span id="Irix"></span><span id="irix"></span><span id="IRIX"></span>**Irix** (12)
</dt> <dt>

<span id="Cisco_iSCSI_Storage_Router"></span><span id="cisco_iscsi_storage_router"></span><span id="CISCO_ISCSI_STORAGE_ROUTER"></span>**Cisco iSCSI Storage Router** (13)
</dt> <dt>

<span id="Linux"></span><span id="linux"></span><span id="LINUX"></span>**Linux** (14)
</dt> <dt>

<span id="Microsoft_Windows"></span><span id="microsoft_windows"></span><span id="MICROSOFT_WINDOWS"></span>**Microsoft Windows** (15)
</dt> <dt>

<span id="OS400"></span><span id="os400"></span>**OS400** (16)
</dt> <dt>

<span id="TRESPASS"></span><span id="trespass"></span>**TRESPASS** (17)
</dt> <dt>

<span id="HI-UX"></span><span id="hi-ux"></span>**HI-UX** (18)
</dt> <dt>

<span id="VMware_ESXi"></span><span id="vmware_esxi"></span><span id="VMWARE_ESXI"></span>**VMware ESXi** (19)
</dt> <dt>

<span id="Microsoft_Windows_Server_2008"></span><span id="microsoft_windows_server_2008"></span><span id="MICROSOFT_WINDOWS_SERVER_2008"></span>**Microsoft Windows Server 2008** (20)
</dt> <dt>

<span id="Microsoft_Windows_Server_2003"></span><span id="microsoft_windows_server_2003"></span><span id="MICROSOFT_WINDOWS_SERVER_2003"></span>**Microsoft Windows Server 2003** (21)
</dt> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>**DMTF Reserved** (22..32767)
</dt> <dt>

<span id="Vendor_Specific"></span><span id="vendor_specific"></span><span id="VENDOR_SPECIFIC"></span>**Vendor Specific** (32768..65535)
</dt> </dl>

</dd> <dt>

**SupportsAutomaticStoragePoolSelection**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if automatic storage pool selection is supported.

</dd> <dt>

**SupportsCloneLocal**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Clone Local**.

</dd> <dt>

**SupportsCloneRemote**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Clone Remote**.

</dd> <dt>

**SupportsMaskingVirtualDiskToHosts**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**TRUE** if the storage subsystem supports showing and hiding (masking) a virtual disk to a host initiator through the [**MSFT\_VirtualDisk.Show**](msft-virtualdisk-show.md)[**MSFT\_VirtualDisk.Hide**](msft-virtualdisk-hide.md) methods and by the use of masking sets.

</dd> <dt>

**SupportsMirrorLocal**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Mirror Local**.

</dd> <dt>

**SupportsMirrorRemote**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Mirror Remote**.

</dd> <dt>

**SupportsMultipleResiliencySettingsPerStoragePool**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, all resiliency settings will be copied from the primordial pool and added to a concrete pool upon its creation. If **FALSE**, the storage pool should copy the resiliency setting name specified in the *ResiliencySettingNameDefault* parameter of the [**MSFT\_StorageSubSystem.CreateStoragePool**](createstoragepool-msft-storagesubsystem.md) method. If no resiliency setting name was specified, the resiliency setting specified in the primordial pool's **ResiliencySettingNameDefault** property should be used.

</dd> <dt>

**SupportsSnapshotLocal**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Snapshot Local**.

</dd> <dt>

**SupportsSnapshotRemote**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this storage subsystem supports replication type **Snapshot Remote**.

</dd> <dt>

**SupportsStoragePoolAddPhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if the storage pools in this storage subsystem support adding physical disks to expand capacity.

</dd> <dt>

**SupportsStoragePoolCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if the storage subsystem supports the ability to create new concrete storage pools from one or more physical disks. If **FALSE**, either the subsystem uses pre-created storage pools, or it does not support storage pools at all.

</dd> <dt>

**SupportsStoragePoolDeletion**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if the storage subsystem supports the deletion of its storage pools.

</dd> <dt>

**SupportsStoragePoolFriendlyNameModification**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if the storage subsystem supports storage pool friendly name modification.

</dd> <dt>

**SupportsStoragePoolRemovePhysicalDisk**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if the storage pools in this subsystem support the replacement or removal of physical disks by use of the [**MSFT\_StoragePool.RemovePhysicalDisk**](removephysicaldisk-msft-storagepool.md) method.

</dd> <dt>

**SupportsStorageTierCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this subsystem supports the ability to create new storage tiers. If **FALSE**, either the subsystem uses pre-created storage tiers, or it does not support storage tiers.

</dd> <dt>

**SupportsStorageTierDeletion**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this subsystem supports the deletion of storage tiers.

</dd> <dt>

**SupportsStorageTieredVirtualDiskCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this subsystem supports the creation of tiered virtual disks.

</dd> <dt>

**SupportsStorageTierFriendlyNameModification**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this subsystem supports the modification of the storage tier friendly name.

</dd> <dt>

**SupportsStorageTierResize**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

If **TRUE**, this subsystem supports the resizing of storage tiers..

</dd> <dt>

**SupportsVirtualDiskCapacityExpansion**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can increase the size of a virtual disk by using the [**MSFT\_VirtualDisk.Resize**](msft-virtualdisk-resize.md) method.

</dd> <dt>

**SupportsVirtualDiskCapacityReduction**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can reduce the size of a virtual disk by using the [**MSFT\_VirtualDisk.Resize**](msft-virtualdisk-resize.md) method.

</dd> <dt>

**SupportsVirtualDiskCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can create a virtual disk by using the [**MSFT\_StorageSubSystem.CreateVirtualDisk**](msft-storagesubsystem-createvirtualdisk.md) method or the [**MSFT\_StoragePool.CreateVirtualDisk**](createvirtualdisk-msft-storagepool.md) method.

</dd> <dt>

**SupportsVirtualDiskDeletion**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can delete a virtual disk by using the [**MSFT\_VirtualDisk.DeleteObject**](msft-virtualdisk-deleteobject.md) method.

</dd> <dt>

**SupportsVirtualDiskModification**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can modify attributes or other properties on a virtual disk by using methods such as [**MSFT\_VirtuDisk.SetFriendlyName**](msft-virtualdisk-setfriendlyname.md) and [**MSFT\_VirtuDisk.SetAttributes**](msft-virtualdisk-setattributes.md).

</dd> <dt>

**SupportsVirtualDiskRepair**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if a user can repair a virtual disk by using the [**MSFT\_VirtualDisk.Repair**](msft-virtualdisk-repair.md) method.

</dd> <dt>

**SupportsVolumeCreation**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Required**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

**TRUE** if this subsystem supports direct creation of volumes on a storage pool.

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

An identifier for the subsystem that is independent from any location-based information. For example, this property might contain the subsystem's serial number or asset tag number.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





