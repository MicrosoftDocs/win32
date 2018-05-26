---
Description: This class defines a view class for a physical computer system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 44cbf854-70d0-4277-888c-cadd03e2630a
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: CIM\_PhysicalComputerSystemView class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CIM\_PhysicalComputerSystemView class

This class defines a view class for a physical computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[UMLPackagePath("CIM::Core::CoreElements"), Experimental, Version("2.35.0"), AMENDMENT]
class CIM_PhysicalComputerSystemView : CIM_View
{
  string  Caption;
  string  Description;
  string  ElementName;
  string  InstanceID;
  uint16  EnabledState;
  uint16  RequestedState;
  uint16  OperationalStatus[];
  uint16  HealthState;
  boolean FRUInfoSupported;
  string  Tag;
  string  Manufacturer;
  string  Model;
  string  SKU;
  string  SerialNumber;
  string  Version;
  string  PartNumber;
  uint16  PowerUtilizationModesSupported[];
  uint16  PowerUtilizationMode;
  uint64  PowerAllocationLimit;
  string  NumericSensorElementName[];
  uint16  NumericSensorEnabledState[];
  uint16  NumericSensorHealthState[];
  string  NumericSensorCurrentState[];
  uint16  NumericSensorPrimaryStatus[];
  uint16  NumericSensorBaseUnits[];
  sint32  NumericSensorUnitModifier[];
  uint16  NumericSensorRateUnits[];
  sint32  NumericSensorCurrentReading[];
  uint16  NumericSensorSensorType[];
  string  NumericSensorOtherSensorTypeDescription[];
  sint32  NumericSensorUpperThresholdNonCritical[];
  sint32  NumericSensorUpperThresholdCritical[];
  sint32  NumericSensorUpperThresholdFatal[];
  string  LogInstanceID[];
  uint64  LogMaxNumberOfRecords[];
  uint64  LogCurrentNumberOfRecords[];
  uint16  LogOverwritePolicy[];
  uint16  LogState[];
  string  StructuredBootString[];
  uint8   PersistentBootConfigOrder[];
  uint8   OneTimeBootSource;
  uint16  NumberOfProcessors;
  uint16  NumberOfProcessorCores;
  uint16  NumberOfProcessorThreads;
  uint16  ProcessorFamily;
  uint32  ProcessorMaxClockSpeed;
  uint64  MemoryBlockSize;
  uint64  MemoryNumberOfBlocks;
  uint64  MemoryConsumableBlocks;
  uint16  CurrentBIOSMajorVersion;
  uint16  CurrentBIOSMinorVersion;
  uint16  CurrentBIOSRevisionNumber;
  uint16  CurrentBIOSBuildNumber;
  uint16  CurrentManagementFirmwareMajorVersion;
  uint16  CurrentManagementFirmwareMinorVersion;
  uint16  CurrentManagementFirmwareRevisionNumber;
  uint16  CurrentManagementFirmwareBuildNumber;
  string  CurrentManagementFirmwareElementName;
  string  CurrentManagementFirmwareVersionString;
  uint16  OSType;
  string  OSVersion;
  uint16  OSEnabledState;
  string  CurrentBIOSVersionString;
  uint16  Dedicated[];
  string  IdentifyingDescriptions[];
  string  OtherDedicatedDescriptions[];
  string  OtherIdentifyingInfo[];
  uint32  ProcessorCurrentClockSpeed;
  string  NumericSensorContext[];
  sint32  NumericSensorLowerThresholdNonCritical[];
  sint32  NumericSensorLowerThresholdCritical[];
  sint32  NumericSensorLowerThresholdFatal[];
};
```

## Members

The **CIM\_PhysicalComputerSystemView** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **CIM\_PhysicalComputerSystemView** class has these methods.



| Method                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ClearLog**](clearlog-cim-physicalcomputersystemview.md)                                               | An extrinsic method for clearing a log on this physical computer system.Requests that the Log be cleared of all entries.The return value shall be 0 if the request was successfully executed, 1 if the request is not supported, and 2 if an error occurred. A return code of 4096 shall indicate the request to clear log was successfully initiated, a ConcreteJob has been created, and its reference returned in the output parameter Job.<br/>                                                                                                                                                                                                                                                                                                                                                  |
| [**InstallSoftwareFromURI**](installsoftwarefromuri-cim-physicalcomputersystemview.md)                   | An extrinsic method for installing software on this physical computer system. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. The return value shall be 1 if the request is not supported, and 2 if an error occurred. If 4096 is returned, a ConcreteJob will be started to to perform the install. The Job's reference will be returned in the output parameter Job.<br/>                                                                                                                                                                                                                                                                                                                                                                          |
| [**ModifyPersistentBootConfigOrder**](modifypersistentbootconfigorder-cim-physicalcomputersystemview.md) | This method is used to change the order of boot sources for the persistent boot configuration specified by the property CIM\_PhysicalComputerSystemView.PersistentBootConfigOrder.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**RequestStateChange**](requeststatechange-cim-physicalcomputersystemview.md)                           | An extrinsic method for changing the state of this physical computer system. Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost.A return code of 0 shall indicate the state change was successfully initiated.A return code of 1 shall indicate that the method is not supported. A return code of 2 shall indicate that the method failed.A return code of 4096 shall indicate the state change was successfully initiated, a ConcreteJob has been created, and its reference returned in the output parameter Job.<br/> |
| [**SetOneTimeBootSource**](setonetimebootsource-cim-physicalcomputersystemview.md)                       | This method is used to set the one time boot source for the next boot on this computer system.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |



 

### Properties

The **CIM\_PhysicalComputerSystemView** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **MaxLen** (64)
</dt> </dl>

The Caption property is a short textual description (one- line string) of the object.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**CurrentBIOSBuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.BuildNumber")
</dt> </dl>

The build number component of the current BIOS version information.

</dd> <dt>

**CurrentBIOSMajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.MajorVersion")
</dt> </dl>

The major number component of the current BIOS version information.

</dd> <dt>

**CurrentBIOSMinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.MinorVersion")
</dt> </dl>

The minor number component of the current BIOS version information.

</dd> <dt>

**CurrentBIOSRevisionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.RevisionNumber")
</dt> </dl>

The revision number component of the current BIOS version information.

</dd> <dt>

**CurrentBIOSVersionString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.VersionString")
</dt> </dl>

The BIOS version information in string format.

</dd> <dt>

**CurrentManagementFirmwareBuildNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.BuildNumber")
</dt> </dl>

The build number component of the version information for the current management firmware on this physical computer system.

</dd> <dt>

**CurrentManagementFirmwareElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.ElementName")
</dt> </dl>

The user-friendly name for the current management firmware on this physical computer system.

</dd> <dt>

**CurrentManagementFirmwareMajorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.MajorVersion")
</dt> </dl>

The major number component of the version information for the current management firmware on this physical computer system.

</dd> <dt>

**CurrentManagementFirmwareMinorVersion**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.MinorVersion")
</dt> </dl>

The minor number component of the version information for the current management firmware on this physical computer system.

</dd> <dt>

**CurrentManagementFirmwareRevisionNumber**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.RevisionNumber")
</dt> </dl>

The revision number component of the version information for the current management firmware on this physical computer system.

</dd> <dt>

**CurrentManagementFirmwareVersionString**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_SoftwareIdentity.VersionString")
</dt> </dl>

The version string for the current management firmware on this physical computer system.

</dd> <dt>

**Dedicated**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.Dedicated", "CIM\_PhysicalComputerSystemView.OtherDedicatedDescriptions")
</dt> </dl>

See CIM\_ComputerSystem.Dedicated for details.

The possible values are.

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


</dt> <dd></dd> <dt>

<span id="Management"></span><span id="management"></span><span id="MANAGEMENT"></span>

**Management** (14)


</dt> <dd></dd> <dt>

<span id="Block_Server"></span><span id="block_server"></span><span id="BLOCK_SERVER"></span>

**Block Server** (15)


</dt> <dd></dd> <dt>

<span id="File_Server"></span><span id="file_server"></span><span id="FILE_SERVER"></span>

**File Server** (16)


</dt> <dd></dd> <dt>

<span id="Mobile_User_Device"></span><span id="mobile_user_device"></span><span id="MOBILE_USER_DEVICE"></span>

**Mobile User Device** (17)


</dt> <dd></dd> <dt>

<span id="Repeater"></span><span id="repeater"></span><span id="REPEATER"></span>

**Repeater** (18)


</dt> <dd></dd> <dt>

<span id="Bridge_Extender"></span><span id="bridge_extender"></span><span id="BRIDGE_EXTENDER"></span>

**Bridge/Extender** (19)


</dt> <dd></dd> <dt>

<span id="Gateway"></span><span id="gateway"></span><span id="GATEWAY"></span>

**Gateway** (20)


</dt> <dd></dd> <dt>

<span id="Storage_Virtualizer"></span><span id="storage_virtualizer"></span><span id="STORAGE_VIRTUALIZER"></span>

**Storage Virtualizer** (21)


</dt> <dd></dd> <dt>

<span id="Media_Library"></span><span id="media_library"></span><span id="MEDIA_LIBRARY"></span>

**Media Library** (22)


</dt> <dd></dd> <dt>

<span id="ExtenderNode"></span><span id="extendernode"></span><span id="EXTENDERNODE"></span>

**ExtenderNode** (23)


</dt> <dd></dd> <dt>

<span id="NAS_Head"></span><span id="nas_head"></span><span id="NAS_HEAD"></span>

**NAS Head** (24)


</dt> <dd></dd> <dt>

<span id="Self-contained_NAS"></span><span id="self-contained_nas"></span><span id="SELF-CONTAINED_NAS"></span>

**Self-contained NAS** (25)


</dt> <dd></dd> <dt>

<span id="UPS"></span><span id="ups"></span>

**UPS** (26)


</dt> <dd></dd> <dt>

<span id="IP_Phone"></span><span id="ip_phone"></span><span id="IP_PHONE"></span>

**IP Phone** (27)


</dt> <dd></dd> <dt>

<span id="Management_Controller"></span><span id="management_controller"></span><span id="MANAGEMENT_CONTROLLER"></span>

**Management Controller** (28)


</dt> <dd></dd> <dt>

<span id="Chassis_Manager"></span><span id="chassis_manager"></span><span id="CHASSIS_MANAGER"></span>

**Chassis Manager** (29)


</dt> <dd></dd> <dt>

<span id="Host-based_RAID_controller"></span><span id="host-based_raid_controller"></span><span id="HOST-BASED_RAID_CONTROLLER"></span>

**Host-based RAID controller** (30)


</dt> <dd></dd> <dt>

<span id="Storage_Device_Enclosure"></span><span id="storage_device_enclosure"></span><span id="STORAGE_DEVICE_ENCLOSURE"></span>

**Storage Device Enclosure** (31)


</dt> <dd></dd> <dt>

<span id="Desktop"></span><span id="desktop"></span><span id="DESKTOP"></span>

**Desktop** (32)


</dt> <dd></dd> <dt>

<span id="Laptop"></span><span id="laptop"></span><span id="LAPTOP"></span>

**Laptop** (33)


</dt> <dd></dd> <dt>

<span id="Virtual_Tape_Library"></span><span id="virtual_tape_library"></span><span id="VIRTUAL_TAPE_LIBRARY"></span>

**Virtual Tape Library** (34)


</dt> <dd></dd> <dt>

<span id="Virtual_Library_System"></span><span id="virtual_library_system"></span><span id="VIRTUAL_LIBRARY_SYSTEM"></span>

**Virtual Library System** (35)


</dt> <dd></dd> <dt>

<span id="Network_PC_Thin_Client"></span><span id="network_pc_thin_client"></span><span id="NETWORK_PC_THIN_CLIENT"></span>

**Network PC/Thin Client** (36)


</dt> <dd></dd> <dt>

<span id="FC_Switch"></span><span id="fc_switch"></span><span id="FC_SWITCH"></span>

**FC Switch** (37)


</dt> <dd></dd> <dt>

<span id="Ethernet_Switch"></span><span id="ethernet_switch"></span><span id="ETHERNET_SWITCH"></span>

**Ethernet Switch** (38)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>39 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Strings identifying the boot sources on this physical computer system. See CIM\_BootSourceSetting.StructuredBootfor details.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM\_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

This member is introduced in [**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218).

</dd> <dt>

**EnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.EnabledState")
</dt> </dl>

This property corresponds to the EnabledState property of the logical computer system represented by CIM\_ComputerSystem. See CIM\_EnabledLogicalElement.EnabledState for details on EnabledState.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**FRUInfoSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalAssetCapabilities.FRUInfoSupported")
</dt> </dl>

This property indicates the availability of the FRU Information on this physical computer system. See CIM\_PhysicalAssetCapabilities.FRUInfoSupported for details.

</dd> <dt>

**HealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.HealthState")
</dt> </dl>

This property corresponds to the HealthState property of the logical computer system represented by CIM\_ComputerSystem. See CIM\_ManagedSystemElement.HealthState for details.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (5)


</dt> <dd></dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

**Degraded/Warning** (10)


</dt> <dd></dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

**Minor failure** (15)


</dt> <dd></dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

**Major failure** (20)


</dt> <dd></dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

**Critical failure** (25)


</dt> <dd></dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-recoverable error** (30)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>31 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**IdentifyingDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.IdentifyingDescriptions", "CIM\_PhysicalComputerSystemView.OtherIdentifyingInfo")
</dt> </dl>

See CIM\_System.IdentifyingDescriptions for details.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("InstanceID")
</dt> </dl>

InstanceID is the property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace.

</dd> <dt>

**LogCurrentNumberOfRecords**
</dt> <dd> <dl> <dt>

Data type: **uint64** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RecordLog.CurrentNumberOfRecords", "CIM\_PhysicalComputerSystemView.LogInstanceID", "CIM\_PhysicalComputerSystemView.LogMaxNumberOfRecords")
</dt> </dl>

See CIM\_RecordLog.CurrentNumberOfRecords for details.

</dd> <dt>

**LogInstanceID**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RecordLog.InstanceID")
</dt> </dl>

This property represents the identifiers for the underlying logs on this physical computer system. See CIM\_RecordLog.InstanceID for details.

</dd> <dt>

**LogMaxNumberOfRecords**
</dt> <dd> <dl> <dt>

Data type: **uint64** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RecordLog.MaxNumberOfRecords", "CIM\_PhysicalComputerSystemView.LogInstanceID")
</dt> </dl>

See CIM\_RecordLog.MaxNumberOfRecords for details.

</dd> <dt>

**LogOverwritePolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RecordLog.OverwritePolicy", "CIM\_PhysicalComputerSystemView.LogInstanceID", "CIM\_PhysicalComputerSystemView.LogMaxNumberOfRecords", "CIM\_PhysicalComputerSystemView.LogCurrentNumberOfRecords")
</dt> </dl>

See CIM\_RecordLog.OverWritePolicy for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Wraps_When_Full"></span><span id="wraps_when_full"></span><span id="WRAPS_WHEN_FULL"></span>

**Wraps When Full** (2)


</dt> <dd></dd> <dt>

<span id="Never_Overwrites"></span><span id="never_overwrites"></span><span id="NEVER_OVERWRITES"></span>

**Never Overwrites** (7)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>8 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**LogState**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_RecordLog.LogState", "CIM\_PhysicalComputerSystemView.LogInstanceID", "CIM\_PhysicalComputerSystemView.LogMaxNumberOfRecords", "CIM\_PhysicalComputerSystemView.LogCurrentNumberOfRecords", "CIM\_PhysicalComputerSystemView.LogOverwritePolicy")
</dt> </dl>

See CIM\_RecordLog.LogState for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

**Normal** (2)


</dt> <dd></dd> <dt>

<span id="Erasing"></span><span id="erasing"></span><span id="ERASING"></span>

**Erasing** (3)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**Manufacturer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.Manufacturer")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.Manufacturer. See CIM\_PhysicalFrame.Manufacturer for details.

</dd> <dt>

**MemoryBlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Memory.BlockSize")
</dt> </dl>

See CIM\_Memory.BlockSize for details.

</dd> <dt>

**MemoryConsumableBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Memory.ConsumableBlocks")
</dt> </dl>

See CIM\_Memory.ConsumableBlocks for details.

</dd> <dt>

**MemoryNumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Memory.NumberOfBlocks")
</dt> </dl>

See CIM\_Memory.NumberOfBlocks for details.

</dd> <dt>

**Model**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.Model")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.Model. See CIM\_PhysicalFrame.Model for details.

</dd> <dt>

**NumberOfProcessorCores**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProcessorCapabilities.NumberOfProcessorCores")
</dt> </dl>

See CIM\_ProcessorCapabilities.NumberOfProcessorCores for details.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property identifies the number of processors on this physical computer system.

</dd> <dt>

**NumberOfProcessorThreads**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ProcessorCapabilities.NumberOfHardwareThreads")
</dt> </dl>

See CIM\_ProcessorCapabilities.NumberOfProcessorThreads for details.

</dd> <dt>

**NumericSensorBaseUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.BaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus")
</dt> </dl>

Base units of the values returned by the numeric sensors. See CIM\_NumericSensor.BaseUnits for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Degrees_C"></span><span id="degrees_c"></span><span id="DEGREES_C"></span>

**Degrees C** (2)


</dt> <dd></dd> <dt>

<span id="Degrees_F"></span><span id="degrees_f"></span><span id="DEGREES_F"></span>

**Degrees F** (3)


</dt> <dd></dd> <dt>

<span id="Degrees_K"></span><span id="degrees_k"></span><span id="DEGREES_K"></span>

**Degrees K** (4)


</dt> <dd></dd> <dt>

<span id="Volts"></span><span id="volts"></span><span id="VOLTS"></span>

**Volts** (5)


</dt> <dd></dd> <dt>

<span id="Amps"></span><span id="amps"></span><span id="AMPS"></span>

**Amps** (6)


</dt> <dd></dd> <dt>

<span id="Watts"></span><span id="watts"></span><span id="WATTS"></span>

**Watts** (7)


</dt> <dd></dd> <dt>

<span id="Joules"></span><span id="joules"></span><span id="JOULES"></span>

**Joules** (8)


</dt> <dd></dd> <dt>

<span id="Coulombs"></span><span id="coulombs"></span><span id="COULOMBS"></span>

**Coulombs** (9)


</dt> <dd></dd> <dt>

<span id="VA"></span><span id="va"></span>

**VA** (10)


</dt> <dd></dd> <dt>

<span id="Nits"></span><span id="nits"></span><span id="NITS"></span>

**Nits** (11)


</dt> <dd></dd> <dt>

<span id="Lumens"></span><span id="lumens"></span><span id="LUMENS"></span>

**Lumens** (12)


</dt> <dd></dd> <dt>

<span id="Lux"></span><span id="lux"></span><span id="LUX"></span>

**Lux** (13)


</dt> <dd></dd> <dt>

<span id="Candelas"></span><span id="candelas"></span><span id="CANDELAS"></span>

**Candelas** (14)


</dt> <dd></dd> <dt>

<span id="kPa"></span><span id="kpa"></span><span id="KPA"></span>

**kPa** (15)


</dt> <dd></dd> <dt>

<span id="PSI"></span><span id="psi"></span>

**PSI** (16)


</dt> <dd></dd> <dt>

<span id="Newtons"></span><span id="newtons"></span><span id="NEWTONS"></span>

**Newtons** (17)


</dt> <dd></dd> <dt>

<span id="CFM"></span><span id="cfm"></span>

**CFM** (18)


</dt> <dd></dd> <dt>

<span id="RPM"></span><span id="rpm"></span>

**RPM** (19)


</dt> <dd></dd> <dt>

<span id="Hertz"></span><span id="hertz"></span><span id="HERTZ"></span>

**Hertz** (20)


</dt> <dd></dd> <dt>

<span id="Seconds"></span><span id="seconds"></span><span id="SECONDS"></span>

**Seconds** (21)


</dt> <dd></dd> <dt>

<span id="Minutes"></span><span id="minutes"></span><span id="MINUTES"></span>

**Minutes** (22)


</dt> <dd></dd> <dt>

<span id="Hours"></span><span id="hours"></span><span id="HOURS"></span>

**Hours** (23)


</dt> <dd></dd> <dt>

<span id="Days"></span><span id="days"></span><span id="DAYS"></span>

**Days** (24)


</dt> <dd></dd> <dt>

<span id="Weeks"></span><span id="weeks"></span><span id="WEEKS"></span>

**Weeks** (25)


</dt> <dd></dd> <dt>

<span id="Mils"></span><span id="mils"></span><span id="MILS"></span>

**Mils** (26)


</dt> <dd></dd> <dt>

<span id="Inches"></span><span id="inches"></span><span id="INCHES"></span>

**Inches** (27)


</dt> <dd></dd> <dt>

<span id="Feet"></span><span id="feet"></span><span id="FEET"></span>

**Feet** (28)


</dt> <dd></dd> <dt>

<span id="Cubic_Inches"></span><span id="cubic_inches"></span><span id="CUBIC_INCHES"></span>

**Cubic Inches** (29)


</dt> <dd></dd> <dt>

<span id="Cubic_Feet"></span><span id="cubic_feet"></span><span id="CUBIC_FEET"></span>

**Cubic Feet** (30)


</dt> <dd></dd> <dt>

<span id="Meters"></span><span id="meters"></span><span id="METERS"></span>

**Meters** (31)


</dt> <dd></dd> <dt>

<span id="Cubic_Centimeters"></span><span id="cubic_centimeters"></span><span id="CUBIC_CENTIMETERS"></span>

**Cubic Centimeters** (32)


</dt> <dd></dd> <dt>

<span id="Cubic_Meters"></span><span id="cubic_meters"></span><span id="CUBIC_METERS"></span>

**Cubic Meters** (33)


</dt> <dd></dd> <dt>

<span id="Liters"></span><span id="liters"></span><span id="LITERS"></span>

**Liters** (34)


</dt> <dd></dd> <dt>

<span id="Fluid_Ounces"></span><span id="fluid_ounces"></span><span id="FLUID_OUNCES"></span>

**Fluid Ounces** (35)


</dt> <dd></dd> <dt>

<span id="Radians"></span><span id="radians"></span><span id="RADIANS"></span>

**Radians** (36)


</dt> <dd></dd> <dt>

<span id="Steradians"></span><span id="steradians"></span><span id="STERADIANS"></span>

**Steradians** (37)


</dt> <dd></dd> <dt>

<span id="Revolutions"></span><span id="revolutions"></span><span id="REVOLUTIONS"></span>

**Revolutions** (38)


</dt> <dd></dd> <dt>

<span id="Cycles"></span><span id="cycles"></span><span id="CYCLES"></span>

**Cycles** (39)


</dt> <dd></dd> <dt>

<span id="Gravities"></span><span id="gravities"></span><span id="GRAVITIES"></span>

**Gravities** (40)


</dt> <dd></dd> <dt>

<span id="Ounces"></span><span id="ounces"></span><span id="OUNCES"></span>

**Ounces** (41)


</dt> <dd></dd> <dt>

<span id="Pounds"></span><span id="pounds"></span><span id="POUNDS"></span>

**Pounds** (42)


</dt> <dd></dd> <dt>

<span id="Foot-Pounds"></span><span id="foot-pounds"></span><span id="FOOT-POUNDS"></span>

**Foot-Pounds** (43)


</dt> <dd></dd> <dt>

<span id="Ounce-Inches"></span><span id="ounce-inches"></span><span id="OUNCE-INCHES"></span>

**Ounce-Inches** (44)


</dt> <dd></dd> <dt>

<span id="Gauss"></span><span id="gauss"></span><span id="GAUSS"></span>

**Gauss** (45)


</dt> <dd></dd> <dt>

<span id="Gilberts"></span><span id="gilberts"></span><span id="GILBERTS"></span>

**Gilberts** (46)


</dt> <dd></dd> <dt>

<span id="Henries"></span><span id="henries"></span><span id="HENRIES"></span>

**Henries** (47)


</dt> <dd></dd> <dt>

<span id="Farads"></span><span id="farads"></span><span id="FARADS"></span>

**Farads** (48)


</dt> <dd></dd> <dt>

<span id="Ohms"></span><span id="ohms"></span><span id="OHMS"></span>

**Ohms** (49)


</dt> <dd></dd> <dt>

<span id="Siemens"></span><span id="siemens"></span><span id="SIEMENS"></span>

**Siemens** (50)


</dt> <dd></dd> <dt>

<span id="Moles"></span><span id="moles"></span><span id="MOLES"></span>

**Moles** (51)


</dt> <dd></dd> <dt>

<span id="Becquerels"></span><span id="becquerels"></span><span id="BECQUERELS"></span>

**Becquerels** (52)


</dt> <dd></dd> <dt>

<span id="PPM__parts_million_"></span><span id="ppm__parts_million_"></span><span id="PPM__PARTS_MILLION_"></span>

**PPM (parts/million)** (53)


</dt> <dd></dd> <dt>

<span id="Decibels"></span><span id="decibels"></span><span id="DECIBELS"></span>

**Decibels** (54)


</dt> <dd></dd> <dt>

<span id="DbA"></span><span id="dba"></span><span id="DBA"></span>

**DbA** (55)


</dt> <dd></dd> <dt>

<span id="DbC"></span><span id="dbc"></span><span id="DBC"></span>

**DbC** (56)


</dt> <dd></dd> <dt>

<span id="Grays"></span><span id="grays"></span><span id="GRAYS"></span>

**Grays** (57)


</dt> <dd></dd> <dt>

<span id="Sieverts"></span><span id="sieverts"></span><span id="SIEVERTS"></span>

**Sieverts** (58)


</dt> <dd></dd> <dt>

<span id="Color_Temperature_Degrees_K"></span><span id="color_temperature_degrees_k"></span><span id="COLOR_TEMPERATURE_DEGREES_K"></span>

**Color Temperature Degrees K** (59)


</dt> <dd></dd> <dt>

<span id="Bits"></span><span id="bits"></span><span id="BITS"></span>

**Bits** (60)


</dt> <dd></dd> <dt>

<span id="Bytes"></span><span id="bytes"></span><span id="BYTES"></span>

**Bytes** (61)


</dt> <dd></dd> <dt>

<span id="Words__data_"></span><span id="words__data_"></span><span id="WORDS__DATA_"></span>

**Words (data)** (62)


</dt> <dd></dd> <dt>

<span id="DoubleWords"></span><span id="doublewords"></span><span id="DOUBLEWORDS"></span>

**DoubleWords** (63)


</dt> <dd></dd> <dt>

<span id="QuadWords"></span><span id="quadwords"></span><span id="QUADWORDS"></span>

**QuadWords** (64)


</dt> <dd></dd> <dt>

<span id="Percentage"></span><span id="percentage"></span><span id="PERCENTAGE"></span>

**Percentage** (65)


</dt> <dd></dd> <dt>

<span id="Pascals"></span><span id="pascals"></span><span id="PASCALS"></span>

**Pascals** (66)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved**


</dt> <dd>67 65535</dd> </dl>

</dd> <dt>

**NumericSensorContext**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.SensorContext", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdFatal")
</dt> </dl>

See CIM\_Sensor.SensorContext for details.

</dd> <dt>

**NumericSensorCurrentReading**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.CurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits")
</dt> </dl>

See CIM\_NumericSensor.CurrentReading for details.

</dd> <dt>

**NumericSensorCurrentState**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.CurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState")
</dt> </dl>

Current states of numeric sensors. See CIM\_NumericSensor.CurrentState for details.

</dd> <dt>

**NumericSensorElementName**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.ElementName")
</dt> </dl>

User-friendly names of the numeric sensors on the computer system. See CIM\_NumericSensor.ElementName for details.

</dd> <dt>

**NumericSensorEnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.EnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorElementName")
</dt> </dl>

States of numeric sensors. See CIM\_NumericSensor.EnabledState for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**NumericSensorHealthState**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.HealthState", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState")
</dt> </dl>

Health states of numeric sensors. See CIM\_NumericSensor.HealthState for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (5)


</dt> <dd></dd> <dt>

<span id="Degraded_Warning"></span><span id="degraded_warning"></span><span id="DEGRADED_WARNING"></span>

**Degraded/Warning** (10)


</dt> <dd></dd> <dt>

<span id="Minor_failure"></span><span id="minor_failure"></span><span id="MINOR_FAILURE"></span>

**Minor failure** (15)


</dt> <dd></dd> <dt>

<span id="Major_failure"></span><span id="major_failure"></span><span id="MAJOR_FAILURE"></span>

**Major failure** (20)


</dt> <dd></dd> <dt>

<span id="Critical_failure"></span><span id="critical_failure"></span><span id="CRITICAL_FAILURE"></span>

**Critical failure** (25)


</dt> <dd></dd> <dt>

<span id="Non-recoverable_error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-recoverable error** (30)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>31 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**NumericSensorLowerThresholdCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.LowerThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdFatal")
</dt> </dl>

See CIM\_NumericSensor.LowerThresholdCritical description for details.

</dd> <dt>

**NumericSensorLowerThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.LowerThresholdFatal", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdFatal")
</dt> </dl>

See CIM\_NumericSensor.LowerThresholdFatal description for details.

</dd> <dt>

**NumericSensorLowerThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.LowerThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdFatal")
</dt> </dl>

See CIM\_NumericSensor.LowerThresholdNonCritical for details.

</dd> <dt>

**NumericSensorOtherSensorTypeDescription**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.OtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType")
</dt> </dl>

See CIM\_NumericSensor.OtherSensorTypeDescription for details.

</dd> <dt>

**NumericSensorPrimaryStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.PrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState")
</dt> </dl>

Primary statuses of numeric sensors. See CIM\_NumericSensor.PrimaryStatus for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (1)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (2)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (3)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>4 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**NumericSensorRateUnits**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.RateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier")
</dt> </dl>

See CIM\_NumericSensor.RateUnits for details.

The possible values are.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="Per_MicroSecond"></span><span id="per_microsecond"></span><span id="PER_MICROSECOND"></span>

**Per MicroSecond** (1)


</dt> <dd></dd> <dt>

<span id="Per_MilliSecond"></span><span id="per_millisecond"></span><span id="PER_MILLISECOND"></span>

**Per MilliSecond** (2)


</dt> <dd></dd> <dt>

<span id="Per_Second"></span><span id="per_second"></span><span id="PER_SECOND"></span>

**Per Second** (3)


</dt> <dd></dd> <dt>

<span id="Per_Minute"></span><span id="per_minute"></span><span id="PER_MINUTE"></span>

**Per Minute** (4)


</dt> <dd></dd> <dt>

<span id="Per_Hour"></span><span id="per_hour"></span><span id="PER_HOUR"></span>

**Per Hour** (5)


</dt> <dd></dd> <dt>

<span id="Per_Day"></span><span id="per_day"></span><span id="PER_DAY"></span>

**Per Day** (6)


</dt> <dd></dd> <dt>

<span id="Per_Week"></span><span id="per_week"></span><span id="PER_WEEK"></span>

**Per Week** (7)


</dt> <dd></dd> <dt>

<span id="Per_Month"></span><span id="per_month"></span><span id="PER_MONTH"></span>

**Per Month** (8)


</dt> <dd></dd> <dt>

<span id="Per_Year"></span><span id="per_year"></span><span id="PER_YEAR"></span>

**Per Year** (9)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved**


</dt> <dd>10 65535</dd> </dl>

</dd> <dt>

**NumericSensorSensorType**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.SensorType", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading")
</dt> </dl>

See CIM\_NumericSensor.SensorType for details.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Temperature"></span><span id="temperature"></span><span id="TEMPERATURE"></span>

**Temperature** (2)


</dt> <dd></dd> <dt>

<span id="Voltage"></span><span id="voltage"></span><span id="VOLTAGE"></span>

**Voltage** (3)


</dt> <dd></dd> <dt>

<span id="Current"></span><span id="current"></span><span id="CURRENT"></span>

**Current** (4)


</dt> <dd></dd> <dt>

<span id="Tachometer"></span><span id="tachometer"></span><span id="TACHOMETER"></span>

**Tachometer** (5)


</dt> <dd></dd> <dt>

<span id="Counter"></span><span id="counter"></span><span id="COUNTER"></span>

**Counter** (6)


</dt> <dd></dd> <dt>

<span id="Switch"></span><span id="switch"></span><span id="SWITCH"></span>

**Switch** (7)


</dt> <dd></dd> <dt>

<span id="Lock"></span><span id="lock"></span><span id="LOCK"></span>

**Lock** (8)


</dt> <dd></dd> <dt>

<span id="Humidity"></span><span id="humidity"></span><span id="HUMIDITY"></span>

**Humidity** (9)


</dt> <dd></dd> <dt>

<span id="Smoke_Detection"></span><span id="smoke_detection"></span><span id="SMOKE_DETECTION"></span>

**Smoke Detection** (10)


</dt> <dd></dd> <dt>

<span id="Presence"></span><span id="presence"></span><span id="PRESENCE"></span>

**Presence** (11)


</dt> <dd></dd> <dt>

<span id="Air_Flow"></span><span id="air_flow"></span><span id="AIR_FLOW"></span>

**Air Flow** (12)


</dt> <dd></dd> <dt>

<span id="Power_Consumption"></span><span id="power_consumption"></span><span id="POWER_CONSUMPTION"></span>

**Power Consumption** (13)


</dt> <dd></dd> <dt>

<span id="Power_Production"></span><span id="power_production"></span><span id="POWER_PRODUCTION"></span>

**Power Production** (14)


</dt> <dd></dd> <dt>

<span id="Pressure"></span><span id="pressure"></span><span id="PRESSURE"></span>

**Pressure** (15)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>16 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**NumericSensorUnitModifier**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits")
</dt> </dl>

Unit modifiers for the values returned by the numeric sensors. See CIM\_NumericSensor.UnitModifier description for details.

</dd> <dt>

**NumericSensorUpperThresholdCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UpperThresholdCritical", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical")
</dt> </dl>

See CIM\_NumericSensor.UpperThresholdCritical description for details.

</dd> <dt>

**NumericSensorUpperThresholdFatal**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UpperThresholdFatal", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorUpperThresholdCritical")
</dt> </dl>

See CIM\_NumericSensor.UpperThresholdFatal for details.

</dd> <dt>

**NumericSensorUpperThresholdNonCritical**
</dt> <dd> <dl> <dt>

Data type: **sint32** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_NumericSensor.UpperThresholdNonCritical", "CIM\_PhysicalComputerSystemView.NumericSensorElementName", "CIM\_PhysicalComputerSystemView.NumericSensorEnabledState", "CIM\_PhysicalComputerSystemView.NumericSensorHealthState", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentState", "CIM\_PhysicalComputerSystemView.NumericSensorPrimaryStatus", "CIM\_PhysicalComputerSystemView.NumericSensorBaseUnits", "CIM\_PhysicalComputerSystemView.NumericSensorUnitModifier", "CIM\_PhysicalComputerSystemView.NumericSensorRateUnits", "CIM\_PhysicalComputerSystemView.NumericSensorCurrentReading", "CIM\_PhysicalComputerSystemView.NumericSensorSensorType", "CIM\_PhysicalComputerSystemView.NumericSensorOtherSensorTypeDescription")
</dt> </dl>

See CIM\_NumericSensor.UpperThresholdNonCritical for details.

</dd> <dt>

**OneTimeBootSource**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property identifies the boot source that is used for the next one-time boot. The value of this property is an index referencing an element in the array of StructuredBootString.

</dd> <dt>

**OperationalStatus**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.OperationalStatus")
</dt> </dl>

This property corresponds to the OperationalStatus property of the logical computer system represented by CIM\_ComputerSystem. See CIM\_ManagedSystemElement.OperationalStatus Description for details.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (2)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** (3)


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** (4)


</dt> <dd></dd> <dt>

<span id="Predictive_Failure"></span><span id="predictive_failure"></span><span id="PREDICTIVE_FAILURE"></span>

**Predictive Failure** (5)


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (6)


</dt> <dd></dd> <dt>

<span id="Non-Recoverable_Error"></span><span id="non-recoverable_error"></span><span id="NON-RECOVERABLE_ERROR"></span>

**Non-Recoverable Error** (7)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (8)


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** (9)


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** (10)


</dt> <dd></dd> <dt>

<span id="In_Service"></span><span id="in_service"></span><span id="IN_SERVICE"></span>

**In Service** (11)


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** (12)


</dt> <dd></dd> <dt>

<span id="Lost_Communication"></span><span id="lost_communication"></span><span id="LOST_COMMUNICATION"></span>

**Lost Communication** (13)


</dt> <dd></dd> <dt>

<span id="Aborted"></span><span id="aborted"></span><span id="ABORTED"></span>

**Aborted** (14)


</dt> <dd></dd> <dt>

<span id="Dormant"></span><span id="dormant"></span><span id="DORMANT"></span>

**Dormant** (15)


</dt> <dd></dd> <dt>

<span id="Supporting_Entity_in_Error"></span><span id="supporting_entity_in_error"></span><span id="SUPPORTING_ENTITY_IN_ERROR"></span>

**Supporting Entity in Error** (16)


</dt> <dd></dd> <dt>

<span id="Completed"></span><span id="completed"></span><span id="COMPLETED"></span>

**Completed** (17)


</dt> <dd></dd> <dt>

<span id="Power_Mode"></span><span id="power_mode"></span><span id="POWER_MODE"></span>

**Power Mode** (18)


</dt> <dd></dd> <dt>

<span id="Relocating"></span><span id="relocating"></span><span id="RELOCATING"></span>

**Relocating** (19)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>20 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**OSEnabledState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_OperatingSystem.EnabledState")
</dt> </dl>

EnabledState of the current or last running operating system on this physcial computer system.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shutting_Down"></span><span id="shutting_down"></span><span id="SHUTTING_DOWN"></span>

**Shutting Down** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> <dt>

<span id="Enabled_but_Offline"></span><span id="enabled_but_offline"></span><span id="ENABLED_BUT_OFFLINE"></span>

**Enabled but Offline** (6)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

**In Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** (10)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>11 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**OSType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_OperatingSystem.OSType")
</dt> </dl>

Type information of the current or last running operating system on this physical computer system. See CIM\_OperatingSystem.OSType for details.

</dd> <dt>

**OSVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_OperatingSystem.Version")
</dt> </dl>

Version information of the current or last running operating system on this physical computer system. See CIM\_OperatingSystem.Version for details.

</dd> <dt>

**OtherDedicatedDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.OtherDedicatedDescriptions", "CIM\_PhysicalComputerSystemView.Dedicated")
</dt> </dl>

See CIM\_ComputerSystem.OtherDedicatedDescriptions for details.

</dd> <dt>

**OtherIdentifyingInfo**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Indexed"), [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256), [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.OtherIdentifyingInfo", "CIM\_PhysicalComputerSystemView.IdentifyingDescriptions")
</dt> </dl>

See CIM\_System.OtherIdentifyingInfo for details.

</dd> <dt>

**PartNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.PartNumber")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.PartNumber. See CIM\_PhysicalFrame.PartNumber for details.

</dd> <dt>

**PersistentBootConfigOrder**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](https://msdn.microsoft.com/library/aa393650) ("Ordered")
</dt> </dl>

An array of elements identifying the boot order of the persistent boot configuration that shall be used during the next boot of the computer system, unless the OneTimeBootSource for the next boot is specified. The value of each element in this array is an index referencing an element in the array of StructuredBootString.

</dd> <dt>

**PowerAllocationLimit**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PowerAllocationSettingData.Limit"), **PUnit** ("watt \* 10^-3")
</dt> </dl>

This property corresponds to CIM\_PowerAllocationSettingData.Limit. See CIM\_PowerAllocationSettingData.Limit for details.

</dd> <dt>

**PowerUtilizationMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PowerUtilizationManagementService.PowerUtilizationMode")
</dt> </dl>

This property corresponds to the PowerUtilizationMode of the CIM\_PowerUtilizationManagementService. See CIM\_PowerUtilizationManagementService.PowerUtilizationMode for details.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (2)


</dt> <dd></dd> <dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**PowerUtilizationModesSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PowerUtilizationManagementCapabilities.PowerUtilizationModesSupported")
</dt> </dl>

This property corresponds to PowerUtilizationModesSupported property of CIM\_PowerUtilizationManagementCapabilities. See CIM\_PowerUtilizationManagementCapabilities.PowerUtilizationModesSupported for details.

<dt>

<span id="Dynamic"></span><span id="dynamic"></span><span id="DYNAMIC"></span>

**Dynamic** (3)


</dt> <dd></dd> <dt>

<span id="Static"></span><span id="static"></span><span id="STATIC"></span>

**Static** (4)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>5 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**ProcessorCurrentClockSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Processor.CurrentClockSpeed"), **PUnit** ("hertz \* 10^6")
</dt> </dl>

See CIM\_Processor.CurrentClockSpeed for details.

</dd> <dt>

**ProcessorFamily**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Processor.Family")
</dt> </dl>

See CIM\_Processor.Family for details.

</dd> <dt>

**ProcessorMaxClockSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_Processor.MaxClockSpeed"), **PUnit** ("hertz \* 10^6")
</dt> </dl>

See CIM\_Processor.MaxClockSpeed for details.

</dd> <dt>

**RequestedState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_ComputerSystem.RequestedState")
</dt> </dl>

This property corresponds to the RequestedState property of the logical computer system represented by CIM\_ComputerSystem. See CIM\_EnabledLogicalElement.RequestedState for details on RequestedState.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (2)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (3)


</dt> <dd></dd> <dt>

<span id="Shut_Down"></span><span id="shut_down"></span><span id="SHUT_DOWN"></span>

**Shut Down** (4)


</dt> <dd></dd> <dt>

<span id="No_Change"></span><span id="no_change"></span><span id="NO_CHANGE"></span>

**No Change** (5)


</dt> <dd></dd> <dt>

<span id="Offline"></span><span id="offline"></span><span id="OFFLINE"></span>

**Offline** (6)


</dt> <dd></dd> <dt>

<span id="Test"></span><span id="test"></span><span id="TEST"></span>

**Test** (7)


</dt> <dd></dd> <dt>

<span id="Deferred"></span><span id="deferred"></span><span id="DEFERRED"></span>

**Deferred** (8)


</dt> <dd></dd> <dt>

<span id="Quiesce"></span><span id="quiesce"></span><span id="QUIESCE"></span>

**Quiesce** (9)


</dt> <dd></dd> <dt>

<span id="Reboot"></span><span id="reboot"></span><span id="REBOOT"></span>

**Reboot** (10)


</dt> <dd></dd> <dt>

<span id="Reset"></span><span id="reset"></span><span id="RESET"></span>

**Reset** (11)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (12)


</dt> <dd></dd> <dt>

<span id="DMTF_Reserved"></span><span id="dmtf_reserved"></span><span id="DMTF_RESERVED"></span>

**DMTF Reserved**


</dt> <dd>13 32767</dd> <dt>

<span id="Vendor_Reserved"></span><span id="vendor_reserved"></span><span id="VENDOR_RESERVED"></span>

**Vendor Reserved**


</dt> <dd>32768 65535</dd> </dl>

</dd> <dt>

**SerialNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.SerialNumber")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.SerialNumber. See CIM\_PhysicalFrame.SerialNumber for details.

</dd> <dt>

**SKU**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.SKU")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.SKU. See CIM\_PhysicalFrame.SKU for details.

</dd> <dt>

**StructuredBootString**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_BootSourceSetting.StructuredBootString")
</dt> </dl>

Strings identifying the boot sources on this physical computer system. See CIM\_BootSourceSetting.StructuredBootString description for details.

</dd> <dt>

**Tag**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.Tag")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.Tag. See CIM\_PhysicalFrame.Tag for details.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](https://msdn.microsoft.com/library/aa393650) ("CIM\_PhysicalFrame.Version")
</dt> </dl>

This property corresponds to CIM\_PhysicalFrame.Version. See CIM\_PhysicalFrame.Version for details.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                         |
| Namespace<br/>                | Root\\Microsoft\\Windows\\HardwareManagement<br/>                                   |
| MOF<br/>                      | <dl> <dt>Pcsvdevice.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PCSVdevice.dll</dt> </dl> |



 

 




