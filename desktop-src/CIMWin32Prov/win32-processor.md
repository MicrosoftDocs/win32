---
description: Represents a device that can interpret a sequence of instructions on a computer running on a Windows operating system.
ms.assetid: 26f3c7bf-c56a-4cf3-98d4-92ab05b8d244
ms.tgt_platform: multiple
title: Win32_Processor class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Processor
- Win32_Processor.Reset
- Win32_Processor.SetPowerState
- Win32_Processor.AddressWidth
- Win32_Processor.Architecture
- Win32_Processor.AssetTag
- Win32_Processor.Availability
- Win32_Processor.Caption
- Win32_Processor.Characteristics
- Win32_Processor.ConfigManagerErrorCode
- Win32_Processor.ConfigManagerUserConfig
- Win32_Processor.CpuStatus
- Win32_Processor.CreationClassName
- Win32_Processor.CurrentClockSpeed
- Win32_Processor.CurrentVoltage
- Win32_Processor.DataWidth
- Win32_Processor.Description
- Win32_Processor.DeviceID
- Win32_Processor.ErrorCleared
- Win32_Processor.ErrorDescription
- Win32_Processor.ExtClock
- Win32_Processor.Family
- Win32_Processor.InstallDate
- Win32_Processor.L2CacheSize
- Win32_Processor.L2CacheSpeed
- Win32_Processor.L3CacheSize
- Win32_Processor.L3CacheSpeed
- Win32_Processor.LastErrorCode
- Win32_Processor.Level
- Win32_Processor.LoadPercentage
- Win32_Processor.Manufacturer
- Win32_Processor.MaxClockSpeed
- Win32_Processor.Name
- Win32_Processor.NumberOfCores
- Win32_Processor.NumberOfEnabledCore
- Win32_Processor.NumberOfLogicalProcessors
- Win32_Processor.OtherFamilyDescription
- Win32_Processor.PartNumber
- Win32_Processor.PNPDeviceID
- Win32_Processor.PowerManagementCapabilities
- Win32_Processor.PowerManagementSupported
- Win32_Processor.ProcessorId
- Win32_Processor.ProcessorType
- Win32_Processor.Revision
- Win32_Processor.Role
- Win32_Processor.SecondLevelAddressTranslationExtensions
- Win32_Processor.SerialNumber
- Win32_Processor.SocketDesignation
- Win32_Processor.Status
- Win32_Processor.StatusInfo
- Win32_Processor.Stepping
- Win32_Processor.SystemCreationClassName
- Win32_Processor.SystemName
- Win32_Processor.ThreadCount
- Win32_Processor.UniqueId
- Win32_Processor.UpgradeMethod
- Win32_Processor.Version
- Win32_Processor.VirtualizationFirmwareEnabled
- Win32_Processor.VMMonitorModeExtensions
- Win32_Processor.VoltageCaps
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32_Processor class

The **Win32_Processor** [WMI class][0] represents a device that can interpret a sequence of instructions on a computer running on a Windows operating system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4BB-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_Processor : CIM_Processor
{
  uint16   AddressWidth;
  uint16   Architecture;
  string   AssetTag;
  uint16   Availability;
  string   Caption;
  uint32   Characteristics;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  uint16   CpuStatus;
  string   CreationClassName;
  uint32   CurrentClockSpeed;
  uint16   CurrentVoltage;
  uint16   DataWidth;
  string   Description;
  string   DeviceID;
  boolean  ErrorCleared;
  string   ErrorDescription;
  uint32   ExtClock;
  uint16   Family;
  datetime InstallDate;
  uint32   L2CacheSize;
  uint32   L2CacheSpeed;
  uint32   L3CacheSize;
  uint32   L3CacheSpeed;
  uint32   LastErrorCode;
  uint16   Level;
  uint16   LoadPercentage;
  string   Manufacturer;
  uint32   MaxClockSpeed;
  string   Name;
  uint32   NumberOfCores;
  uint32   NumberOfEnabledCore;
  uint32   NumberOfLogicalProcessors;
  string   OtherFamilyDescription;
  string   PartNumber;
  string   PNPDeviceID;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  string   ProcessorId;
  uint16   ProcessorType;
  uint16   Revision;
  string   Role;
  boolean  SecondLevelAddressTranslationExtensions;
  string   SerialNumber;
  string   SocketDesignation;
  string   Status;
  uint16   StatusInfo;
  string   Stepping;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   ThreadCount;
  string   UniqueId;
  uint16   UpgradeMethod;
  string   Version;
  boolean  VirtualizationFirmwareEnabled;
  boolean  VMMonitorModeExtensions;
  uint32   VoltageCaps;
};
```

## Members

The **Win32_Processor** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32_Processor** class has these methods.

| Method            | Description                                                                                                                                                                                             |
|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reset**         | Not implemented. For more information about how to implement this method, see the [**Reset**](reset-method-in-class-cim-controller.md) method in [**CIM_Processor**](cim-processor.md).                 |
| **SetPowerState** | Not implemented. For more information about how to implement this method, see the [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method in [**CIM_Processor**](cim-processor.md). |


### Properties

The <b>Win32_Processor</b> class has these properties.
<dl>
  <dt><b>AddressWidth</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Units</b>][1] ("bits")</dt>
    </dl>
On a 32-bit operating system, the value is 32 and on a 64-bit operating system it is 64.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).
  </dd>
  <dt><b>Architecture</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
    <dl>Processor architecture used by the platform.
      <dt><b>x86</b> (0)</dt>
      <dt><b>MIPS</b> (1)</dt>
      <dt><b>Alpha</b> (2)</dt>
      <dt><b>PowerPC</b> (3)</dt>
      <dt><b>ARM</b> (5)</dt>
      <dt><b>ia64</b> (6)</dt>
      <dd>Itanium-based systems</dd>
      <dt><b>x64</b> (9)</dt>
    </dl>
  </dd>
  <dt><b>AssetTag</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Asset Tag")</dt>
    </dl>
Represents the asset tag of this processor.

This value comes from the <b>Asset Tag</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

<b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.
  </dd>
  <dt><b>Availability</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Operational State\|003.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus")</dt>
    </dl>
    <dl>Availability and status of the device.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).
      <dt><b>Other</b> (1)</dt>
      <dt><b>Unknown</b> (2)</dt>
      <dt><b>Running/Full Power</b> (3)</dt>
      <dd>Running or Full Power</dd>
      <dt><b>Warning</b> (4)</dt>
      <dt><b>In Test</b> (5)</dt>
      <dt><b>Not Applicable</b> (6)</dt>
      <dt><b>Power Off</b> (7)</dt>
      <dt><b>Off Line</b> (8)</dt>
      <dt><b>Off Duty</b> (9)</dt>
      <dt><b>Degraded</b> (10)</dt>
      <dt><b>Not Installed</b> (11)</dt>
      <dt><b>Install Error</b> (12)</dt>
      <dt><b>Power Save - Unknown</b> (13)</dt>
      <dd>The device is known to be in a power save state, but its exact status is unknown.</dd>
      <dt><b>Power Save - Low Power Mode</b> (14)</dt>
      <dd>The device is in a power save state, but is still functioning, and may exhibit decreased performance.</dd>
      <dt><b>Power Save - Standby</b> (15)</dt>
      <dd>The device is not functioning, but can be brought to full power quickly.</dd>
      <dt><b>Power Cycle</b> (16)</dt>
      <dt><b>Power Save - Warning</b> (17)</dt>
      <dd>The device is in a warning state, though also in a power save state.</dd>
      <dt><b>Paused</b> (18)</dt>
      <dd>The device is paused.</dd>
      <dt><b>Not Ready</b> (19)</dt>
      <dd>The device is not ready.</dd>
      <dt><b>Not Configured</b> (20)</dt>
      <dd>The device is not configured.</dd>
      <dt><b>Quiesced</b> (21)</dt>
      <dd>The device is quiet.</dd>
    </dl>
  </dd>
  <dt><b>Caption</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MaxLen</b>][1] (64), [<b>DisplayName</b>][1] ("Caption")</dt>
    </dl>
Short description of an object (a one-line string).

This property is inherited from [<b>CIM_ManagedSystemElement</b>](cim-managedsystemelement.md).
  </dd>
  <dt><b>Characteristics</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Characteristics")</dt>
    </dl>
Defines which functions the processor supports.

This value comes from the <b>Processor Characteristics</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

<b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.
  </dd>
  <dt><b>ConfigManagerErrorCode</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Schema</b>][1] ("Win32")</dt>
    </dl>
    <dl>Windows API Configuration Manager error code.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).
      <dt><b>This device is working properly.</b> (0)</dt>
      <dd>
Device is working properly.</dd>
      <dt><b>This device is not configured correctly.</b> (1)</dt>
      <dd>Device is not configured correctly.</dd>
      <dt><b>Windows cannot load the driver for this device.</b> (2)</dt>
      <dt><b>The driver for this device might be corrupted, or your system may be running low on memory or other resources.</b> (3)</dt>
      <dd>Driver for this device might be corrupted or the system may be low on memory or other resources.</dd>
      <dt><b>This device is not working properly. One of its drivers or your registry might be corrupted.</b> (4)</dt>
      <dd>Device is not working properly. One of its drivers or the registry might be corrupted.</dd>
      <dt><b>The driver for this device needs a resource that Windows cannot manage.</b> (5)</dt>
      <dd>Driver for the device requires a resource that Windows cannot manage.</dd>
      <dt><b>The boot configuration for this device conflicts with other devices.</b> (6)</dt>
      <dd>Boot configuration for the device conflicts with other devices.</dd>
      <dt><b>Cannot filter.</b> (7)</dt>
      <dt><b>The driver loader for the device is missing.</b> (8)</dt>
      <dd>Driver loader for the device is missing.</dd>
      <dt><b>This device is not working properly because the controlling firmware is reporting the resources for the device incorrectly.</b> (9)</dt>
      <dd>Device is not working properly. The controlling firmware is incorrectly reporting the resources for the device.</dd>
      <dt><b>This device cannot start.</b> (10)</dt>
      <dd>Device cannot start.</dd>
      <dt><b>This device failed.</b> (11)</dt>
      <dd>Device failed.</dd>
      <dt><b>This device cannot find enough free resources that it can use.</b> (12)</dt>
      <dd>Device cannot find enough free resources to use.</dd>
      <dt><b>Windows cannot verify this device's resources.</b> (13)</dt>
      <dd>Windows cannot verify the device's resources.</dd>
      <dt><b>This device cannot work properly until you restart your computer.</b> (14)</dt>
      <dd>Device cannot work properly until the computer is restarted.</dd>
      <dt><b>This device is not working properly because there is probably a re-enumeration problem.</b> (15)</dt>
      <dd>Device is not working properly due to a possible re-enumeration problem.</dd>
      <dt><b>Windows cannot identify all the resources this device uses.</b> (16)</dt>
      <dd>Windows cannot identify all of the resources that the device uses.</dd>
      <dt><b>This device is asking for an unknown resource type.</b> (17)</dt>
      <dd>Device is requesting an unknown resource type.</dd>
      <dt><b>Reinstall the drivers for this device.</b> (18)</dt>
      <dd>Device drivers must be reinstalled.</dd>
      <dt><b>Failure using the VxD loader.</b> (19)</dt>
      <dt><b>Your registry might be corrupted.</b> (20)</dt>
      <dd>Registry might be corrupted.</dd>
      <dt><b>System failure: Try changing the driver for this device. If that does not work, see your hardware documentation. Windows is removing this device.</b> (21)</dt>
      <dd>System failure. If changing the device driver is ineffective, see the hardware documentation. Windows is removing the device.</dd>
      <dt><b>This device is disabled.</b> (22)</dt>
      <dd>Device is disabled.</dd>
      <dt><b>System failure: Try changing the driver for this device. If that doesn't work, see your hardware documentation.</b> (23)</dt>
      <dd>System failure. If changing the device driver is ineffective, see the hardware documentation.</dd>
      <dt><b>This device is not present, is not working properly, or does not have all its drivers installed.</b> (24)</dt>
      <dd>Device is not present, not working properly, or does not have all of its drivers installed.</dd>
      <dt><b>Windows is still setting up this device.</b> (25)</dt>
      <dd>Windows is still setting up the device.</dd>
      <dt><b>Windows is still setting up this device.</b> (26)</dt>
      <dd>Windows is still setting up the device.</dd>
      <dt><b>This device does not have valid log configuration.</b> (27)</dt>
      <dd>Device does not have valid log configuration.</dd>
      <dt><b>The drivers for this device are not installed.</b> (28)</dt>
      <dd>Device drivers are not installed.</dd>
      <dt><b>This device is disabled because the firmware of the device did not give it the required resources.</b> (29)</dt>
      <dd>Device is disabled. The device firmware did not provide the required resources.</dd>
      <dt><b>This device is using an Interrupt Request (IRQ) resource that another device is using.</b> (30)</dt>
      <dd>Device is using an IRQ resource that another device is using.</dd>
      <dt><b>This device is not working properly because Windows cannot load the drivers required for this device.</b> (31)</dt>
      <dd>Device is not working properly. Windows cannot load the required device drivers.</dd>
    </dl>
  </dd>
  <dt><b>ConfigManagerUserConfig</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Schema</b>][1] ("Win32")</dt>
    </dl>
If <b>TRUE</b>, the device is using a configuration that the user defines.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>CpuStatus</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Status")</dt>
    </dl>
    <dl>Current status of the processor. Status changes indicate processor usage, but not the physical condition of the processor.

This value comes from the <b>Status</b> member of the <b>Processor Information</b> structure in the SMBIOS information.
      <dt><b>Unknown</b> (0)</dt>
      <dt><b>CPU Enabled</b> (1)</dt>
      <dt><b>CPU Disabled by User via BIOS Setup</b> (2)</dt>
      <dt><b>CPU Disabled By BIOS (POST Error)</b> (3)</dt>
      <dt><b>CPU is Idle</b> (4)</dt>
      <dt><b>Reserved</b> (5)</dt>
      <dt><b>Reserved</b> (6)</dt>
      <dt><b>Other</b> (7)</dt>
    </dl></dd>
  <dt><b>CreationClassName</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>CIM_Key</b>][2]</dt>
    </dl>
Name of the first concrete class that appears in the inheritance chain used to create an instance. When used with the other key properties of the class, the property allows all instances of this class and its subclasses to be identified uniquely.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>CurrentClockSpeed</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Processor\|006.6"), [<b>Units</b>][1] ("megahertz")</dt>
    </dl>
Current speed of the processor, in MHz.
This value comes from the <b>Current Speed</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>CurrentVoltage</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Voltage"), [<b>Units</b>][1] ("tenth-volts")</dt>
    </dl>
Voltage of the processor. If the eighth bit is set, bits 0-6 contain the voltage multiplied by 10. If the eighth bit is not set, then the bit setting in <b>VoltageCaps</b> represents the voltage value. <b>CurrentVoltage</b> is only set when SMBIOS designates a voltage value.

Example: Value for a processor voltage of 1.8 volts is 0x12 (1.8 x 10).

This value comes from the <b>Voltage</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>DataWidth</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Units</b>][1] ("bits")</dt>
    </dl>
On a 32-bit processor, the value is 32 and on a 64-bit processor it is 64.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>Description</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>DisplayName</b>][1] ("Description")</dt>
    </dl>
Description of the object.

This property is inherited from [<b>CIM_ManagedSystemElement</b>](cim-managedsystemelement.md).</dd>
  <dt><b>DeviceID</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Key</b>][3], [<b>Override</b>][1] ("DeviceId"), [<b>MappingStrings</b>][1] ("Win32API\|System Information Structures\|[<b>SYSTEM_INFO</b>][4]\|dwNumberOfProcessors")</dt>
    </dl>
Unique identifier of a processor on the system.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>ErrorCleared</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
If <b>TRUE</b>, the error reported in <b>LastErrorCode</b> is clear.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>ErrorDescription</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
More information about the error recorded in <b>LastErrorCode</b>, and information about corrective actions that can be taken.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>ExtClock</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|External Clock"), [<b>Units</b>][1] ("megahertz")</dt>
    </dl>
External clock frequency, in MHz. If the frequency is unknown, this property is set to <b>NULL</b>.

This value comes from the <b>External Clock</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>Family</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Processor\|014.3"), [<b>ModelCorrespondence</b>][1] ("[<b>CIM_Processor</b>](cim-processor.md).<b>OtherFamilyDescription</b>")</dt>
    </dl>
    <dl>Processor family type.

This value comes from the <b>Processor Information</b> structure in the SMBIOS version information. For SMBIOS versions 2.0 thru 2.5 the value comes from the <b>Processor Family</b> member. For SMBIOS version 2.6+ the value comes from the <b>Processor Family 2</b> member.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).
      <dt><b>Other</b> (1)</dt>
      <dt><b>Unknown</b> (2)</dt>
      <dt><b>8086</b> (3)</dt>
      <dt><b>80286</b> (4)</dt>
      <dt><b>80386</b> (5)</dt>
      <dt><b>80486</b> (6)</dt>
      <dt><b>8087</b> (7)</dt>
      <dt><b>80287</b> (8)</dt>
      <dt><b>80387</b> (9)</dt>
      <dt><b>80487</b> (10)</dt>
      <dt><b>Pentium(R) brand</b> (11)</dt>
      <dt><b>Pentium(R) Pro</b> (12)</dt>
      <dt><b>Pentium(R) II</b> (13)</dt>
      <dt><b>Pentium(R) processor with MMX(TM) technology</b> (14)</dt>
      <dt><b>Celeron(TM)</b> (15)</dt>
      <dt><b>Pentium(R) II Xeon(TM)</b> (16)</dt>
      <dt><b>Pentium(R) III</b> (17)</dt>
      <dt><b>M1 Family</b> (18)</dt>
      <dt><b>M2 Family</b> (19)</dt>
      <dt><b>Intel(R) Celeron(R) M processor</b> (20)</dt>
      <dt><b>Intel(R) Pentium(R) 4 HT processor</b> (21)</dt>
      <dt><b>K5 Family</b> (24)</dt>
      <dt><b>K6 Family</b> (25)</dt>
      <dt><b>K6-2</b> (26)</dt>
      <dt><b>K6-3</b> (27)</dt>
      <dt><b>AMD Athlon(TM) Processor Family</b> (28)</dt>
      <dt><b>AMD(R) Duron(TM) Processor</b> (29)</dt>
      <dt><b>AMD29000 Family</b> (30)</dt>
      <dt><b>K6-2+</b> (31)</dt>
      <dt><b>Power PC Family</b> (32)</dt>
      <dt><b>Power PC 601</b> (33)</dt>
      <dt><b>Power PC 603</b> (34)</dt>
      <dt><b>Power PC 603+</b> (35)</dt>
      <dt><b>Power PC 604</b> (36)</dt>
      <dt><b>Power PC 620</b> (37)</dt>
      <dt><b>Power PC X704</b> (38)</dt>
      <dt><b>Power PC 750</b> (39)</dt>
      <dt><b>Intel(R) Core(TM) Duo processor</b> (40)</dt>
      <dt><b>Intel(R) Core(TM) Duo mobile processor</b> (41)</dt>
      <dt><b>Intel(R) Core(TM) Solo mobile processor</b> (42)</dt>
      <dt><b>Intel(R) Atom(TM) processor</b> (43)</dt>
      <dt><b>Alpha Family</b> (48)</dt>
      <dt><b>Alpha 21064</b> (49)</dt>
      <dt><b>Alpha 21066</b> (50)</dt>
      <dt><b>Alpha 21164</b> (51)</dt>
      <dt><b>Alpha 21164PC</b> (52)</dt>
      <dt><b>Alpha 21164a</b> (53)</dt>
      <dt><b>Alpha 21264</b> (54)</dt>
      <dt><b>Alpha 21364</b> (55)</dt>
      <dt><b>AMD Turion(TM) II Ultra Dual-Core Mobile M Processor Family</b> (56)</dt>
      <dt><b>AMD Turion(TM) II Dual-Core Mobile M Processor Family</b> (57)</dt>
      <dt><b>AMD Athlon(TM) II Dual-Core Mobile M Processor Family</b> (58)</dt>
      <dt><b>AMD Opteron(TM) 6100 Series Processor</b> (59)</dt>
      <dt><b>AMD Opteron(TM) 4100 Series Processor</b> (60)</dt>
      <dt><b>MIPS Family</b> (64)</dt>
      <dt><b>MIPS R4000</b> (65)</dt>
      <dt><b>MIPS R4200</b> (66)</dt>
      <dt><b>MIPS R4400</b> (67)</dt>
      <dt><b>MIPS R4600</b> (68)</dt>
      <dt><b>MIPS R10000</b> (69)</dt>
      <dt><b>SPARC Family</b> (80)</dt>
      <dt><b>SuperSPARC</b> (81)</dt>
      <dt><b>microSPARC II</b> (82)</dt>
      <dt><b>microSPARC IIep</b> (83)</dt>
      <dt><b>UltraSPARC</b> (84)</dt>
      <dt><b>UltraSPARC II</b> (85)</dt>
      <dt><b>UltraSPARC IIi</b> (86)</dt>
      <dt><b>UltraSPARC III</b> (87)</dt>
      <dt><b>UltraSPARC IIIi</b> (88)</dt>
      <dt><b>68040</b> (96)</dt>
      <dt><b>68xxx Family</b> (97)</dt>
      <dt><b>68000</b> (98)</dt>
      <dt><b>68010</b> (99)</dt>
      <dt><b>68020</b> (100)</dt>
      <dt><b>68030</b> (101)</dt>
      <dt><b>Hobbit Family</b> (112)</dt>
      <dt><b>Crusoe(TM) TM5000 Family</b> (120)</dt>
      <dt><b>Crusoe(TM) TM3000 Family</b> (121)</dt>
      <dt><b>Efficeon(TM) TM8000 Family</b> (122)</dt>
      <dt><b>Weitek</b> (128)</dt>
      <dt><b>Itanium(TM) Processor</b> (130)</dt>
      <dt><b>AMD Athlon(TM) 64 Processor Family</b> (131)</dt>
      <dt><b>AMD Opteron(TM) Processor Family</b> (132)</dt>
      <dt><b>AMD Sempron(TM) Processor Family</b> (133)</dt>
      <dt><b>AMD Turion(TM) 64 Mobile Technology</b> (134)</dt>
      <dt><b>Dual-Core AMD Opteron(TM) Processor Family</b> (135)</dt>
      <dt><b>AMD Athlon(TM) 64 X2 Dual-Core Processor Family</b> (136)</dt>
      <dt><b>AMD Turion(TM) 64 X2 Mobile Technology</b> (137)</dt>
      <dt><b>Quad-Core AMD Opteron(TM) Processor Family</b> (138)</dt>
      <dt><b>Third-Generation AMD Opteron(TM) Processor Family</b> (139)</dt>
      <dt><b>AMD Phenom(TM) FX Quad-Core Processor Family</b> (140)</dt>
      <dt><b>AMD Phenom(TM) X4 Quad-Core Processor Family</b> (141)</dt>
      <dt><b>AMD Phenom(TM) X2 Dual-Core Processor Family</b> (142)</dt>
      <dt><b>AMD Athlon(TM) X2 Dual-Core Processor Family</b> (143)</dt>
      <dt><b>PA-RISC Family</b> (144)</dt>
      <dt><b>PA-RISC 8500</b> (145)</dt>
      <dt><b>PA-RISC 8000</b> (146)</dt>
      <dt><b>PA-RISC 7300LC</b> (147)</dt>
      <dt><b>PA-RISC 7200</b> (148)</dt>
      <dt><b>PA-RISC 7100LC</b> (149)</dt>
      <dt><b>PA-RISC 7100</b> (150)</dt>
      <dt><b>V30 Family</b> (160)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 3200 Series</b> (161)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 3000 Series</b> (162)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 5300 Series</b> (163)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 5100 Series</b> (164)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 5000 Series</b> (165)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor LV</b> (166)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor ULV</b> (167)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 7100 Series</b> (168)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 5400 Series</b> (169)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor</b> (170)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 5200 Series</b> (171)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 7200 Series</b> (172)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 7300 Series</b> (173)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 7400 Series</b> (174)</dt>
      <dt><b>Multi-Core Intel(R) Xeon(R) processor 7400 Series</b> (175)</dt>
      <dt><b>Pentium(R) III Xeon(TM)</b> (176)</dt>
      <dt><b>Pentium(R) III Processor with Intel(R) SpeedStep(TM) Technology</b> (177)</dt>
      <dt><b>Pentium(R) 4</b> (178)</dt>
      <dt><b>Intel(R) Xeon(TM)</b> (179)</dt>
      <dt><b>AS400 Family</b> (180)</dt>
      <dt><b>Intel(R) Xeon(TM) processor MP</b> (181)</dt>
      <dt><b>AMD Athlon(TM) XP Family</b> (182)</dt>
      <dt><b>AMD Athlon(TM) MP Family</b> (183)</dt>
      <dt><b>Intel(R) Itanium(R) 2</b> (184)</dt>
      <dt><b>Intel(R) Pentium(R) M processor</b> (185)</dt>
      <dt><b>Intel(R) Celeron(R) D processor</b> (186)</dt>
      <dt><b>Intel(R) Pentium(R) D processor</b> (187)</dt>
      <dt><b>Intel(R) Pentium(R) Processor Extreme Edition</b> (188)</dt>
      <dt><b>Intel(R) Core(TM) Solo Processor</b> (189)</dt>
      <dt><b>K7</b> (190)</dt>
      <dt><b>Intel(R) Core(TM)2 Duo Processor</b> (191)</dt>
      <dt><b>Intel(R) Core(TM)2 Solo processor</b> (192)</dt>
      <dt><b>Intel(R) Core(TM)2 Extreme processor</b> (193)</dt>
      <dt><b>Intel(R) Core(TM)2 Quad processor</b> (194)</dt>
      <dt><b>Intel(R) Core(TM)2 Extreme mobile processor</b> (195)</dt>
      <dt><b>Intel(R) Core(TM)2 Duo mobile processor</b> (196)</dt>
      <dt><b>Intel(R) Core(TM)2 Solo mobile processor</b> (197)</dt>
      <dt><b>Intel(R) Core(TM) i7 processor</b> (198)</dt>
      <dt><b>Dual-Core Intel(R) Celeron(R) Processor</b> (199)</dt>
      <dt><b>S/390 and zSeries Family</b> (200)</dt>
      <dt><b>ESA/390 G4</b> (201)</dt>
      <dt><b>ESA/390 G5</b> (202)</dt>
      <dt><b>ESA/390 G6</b> (203)</dt>
      <dt><b>z/Architectur base</b> (204)</dt>
      <dt><b>Intel(R) Core(TM) i5 processor</b> (205)</dt>
      <dt><b>Intel(R) Core(TM) i3 processor</b> (206)</dt>
      <dt><b>Intel(R) Core(TM) i9 processor</b> (207)</dt>
      <dt><b>VIA C7(TM)-M Processor Family</b> (210)</dt>
      <dt><b>VIA C7(TM)-D Processor Family</b> (211)</dt>
      <dt><b>VIA C7(TM) Processor Family</b> (212)</dt>
      <dt><b>VIA Eden(TM) Processor Family</b> (213)</dt>
      <dt><b>Multi-Core Intel(R) Xeon(R) processor</b> (214)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 3xxx Series</b> (215)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 3xxx Series</b> (216)</dt>
      <dt><b>VIA Nano(TM) Processor Family</b> (217)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 5xxx Series</b> (218)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 5xxx Series</b> (219)</dt>
      <dt><b>Dual-Core Intel(R) Xeon(R) processor 7xxx Series</b> (221)</dt>
      <dt><b>Quad-Core Intel(R) Xeon(R) processor 7xxx Series</b> (222)</dt>
      <dt><b>Multi-Core Intel(R) Xeon(R) processor 7xxx Series</b> (223)</dt>
      <dt><b>Multi-Core Intel(R) Xeon(R) processor 3400 Series</b> (224)</dt>
      <dt><b>Embedded AMD Opteron(TM) Quad-Core Processor Family</b> (230)</dt>
      <dt><b>AMD Phenom(TM) Triple-Core Processor Family</b> (231)</dt>
      <dt><b>AMD Turion(TM) Ultra Dual-Core Mobile Processor Family</b> (232)</dt>
      <dt><b>AMD Turion(TM) Dual-Core Mobile Processor Family</b> (233)</dt>
      <dt><b>AMD Athlon(TM) Dual-Core Processor Family</b> (234)</dt>
      <dt><b>AMD Sempron(TM) SI Processor Family</b> (235)</dt>
      <dt><b>AMD Phenom(TM) II Processor Family</b> (236)</dt>
      <dt><b>AMD Athlon(TM) II Processor Family</b> (237)</dt>
      <dt><b>Six-Core AMD Opteron(TM) Processor Family</b> (238)</dt>
      <dt><b>AMD Sempron(TM) M Processor Family</b> (239)</dt>
      <dt><b>i860</b> (250)</dt>
      <dt><b>i960</b> (251)</dt>
      <dt><b>Reserved (SMBIOS Extension)</b> (254)</dt>
      <dt><b>Reserved (Un-initialized Flash Content - Lo)</b> (255)</dt>
      <dt><b>SH-3</b> (260)</dt>
      <dt><b>SH-4</b> (261)</dt>
      <dt><b>ARM</b> (280)</dt>
      <dt><b>StrongARM</b> (281)</dt>
      <dt><b>6x86</b> (300)</dt>
      <dt><b>MediaGX</b> (301)</dt>
      <dt><b>MII</b> (302)</dt>
      <dt><b>WinChip</b> (320)</dt>
      <dt><b>DSP</b> (350)</dt>
      <dt><b>Video Processor</b> (500)</dt>
      <dt><b>Reserved (For Future Special Purpose Assignment)</b> (65534)</dt>
      <dt><b>Reserved (Un-initialized Flash Content - Hi)</b> (65535)</dt>
    </dl></dd>
  <dt><b>InstallDate</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>datetime</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|ComponentID\|001.5"), [<b>DisplayName</b>][1] ("Install Date")</dt>
    </dl>
Date and time the object is installed. This property does not require a value to indicate that the object is installed. This property is inherited from [<b>CIM_ManagedSystemElement</b>](cim-managedsystemelement.md).</dd>
  <dt><b>L2CacheSize</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI"), [<b>Units</b>][1] ("kilobytes")</dt>
    </dl>
Size of the Level 2 processor cache. A Level 2 cache is an external memory area that has a faster access time than the main RAM memory.
This value comes from the <b>L2 Cache Handle</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>L2CacheSpeed</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI"), [<b>Units</b>][1] ("megahertz")</dt>
    </dl>
Clock speed of the Level 2 processor cache. A Level 2 cache is an external memory area that has a faster access time than the main RAM memory.

This value comes from the <b>L2 Cache Handle</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>L3CacheSize</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI"), [<b>Units</b>][1] ("kilobytes")</dt>
    </dl>
Size of the Level 3 processor cache. A Level 3 cache is an external memory area that has a faster access time than the main RAM memory.

This value comes from the <b>L3 Cache Handle</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>L3CacheSpeed</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI"), [<b>Units</b>][1] ("megahertz")</dt>
    </dl>
Clockspeed of the Level 3 property cache. A Level 3 cache is an external memory area that has a faster access time than the main RAM memory.

This value comes from the <b>L3 Cache Handle</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>LastErrorCode</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
Last error code reported by the logical device.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>Level</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
Definition of the processor type. The value depends on the architecture of the processor.</dd>
  <dt><b>LoadPercentage</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Override</b>][1] ("LoadPercentage"), [<b>MappingStrings</b>][1] ("Win32API\|Performance Data"), [<b>Units</b>][1] ("percent")</dt>
    </dl>
Load capacity of each processor, averaged to the last second. Processor loading refers to the total computing burden for each processor at one time.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>Manufacturer</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
Name of the processor manufacturer.
Example: A. Datum Corporation
This value comes from the <b>Processor Manufacturer</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>MaxClockSpeed</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Processor\|006.5"), [<b>Units</b>][1] ("megahertz")</dt>
    </dl>
Maximum speed of the processor, in MHz.
This value comes from the <b>Max Speed</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>Name</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>DisplayName</b>][1] ("Name")</dt>
    </dl>
Label by which the object is known. When this property is a subclass, it can be overridden to be a key property.

This value comes from the <b>Processor Version</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

This property is inherited from [<b>CIM_ManagedSystemElement</b>](cim-managedsystemelement.md).</dd>
  <dt><b>NumberOfCores</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
Number of cores for the current instance of the processor. A core is a physical processor on the integrated circuit. For example, in a dual-core processor this property has a value of 2. For more information, see Remarks.

This value comes from the <b>Processor Information</b> structure in the SMBIOS version information. For SMBIOS versions 2.5 thru 2.9 the value comes from the <b>Core Count</b> member. For SMBIOS version 3.0+ the value comes from the <b>Core Count 2</b> member.</dd>
  <dt><b>NumberOfEnabledCore</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Core Enabled")</dt>
    </dl>
The number of enabled cores per processor socket.

This value comes from the <b>Processor Information</b> structure in the SMBIOS version information. For SMBIOS versions 2.5 thru 2.9 the value comes from the <b>Core Enabled</b> member. For SMBIOS version 3.0+ the value comes from the <b>Core Enabled 2</b> member.
    <b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.</dd>
  <dt><b>NumberOfLogicalProcessors</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
Number of logical processors for the current instance of the processor. For processors capable of hyperthreading, this value includes only the processors which have hyperthreading enabled. For more information, see Remarks.</dd>
  <dt><b>OtherFamilyDescription</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MaxLen</b>][1] (64), [<b>ModelCorrespondence</b>][1] ("[<b>CIM_Processor</b>](cim-processor.md).<b>Family</b>")</dt>
    </dl>
Processor family type. Used when the <b>Family</b> property is set to 1, which means Other. This string should be set to <b>NULL</b> when the <b>Family</b> property is a value that is not 1.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>PartNumber</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Part Number")</dt>
    </dl>
The part number of this processor as set by the manufacturer.

This value comes from the <b>Part Number</b> member of the <b>Processor Information</b> structure in the SMBIOS information.
    <b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.</dd>
  <dt><b>PNPDeviceID</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Schema</b>][1] ("Win32")</dt>
    </dl>
Windows Plug and Play device identifier of the logical device.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).
Example: \*PNP030b</dd>
  <dt><b>PowerManagementCapabilities</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b> array</dt>
      <dt>Access type: Read-only</dt>
    </dl>
    <dl>Array of the specific power-related capabilities of a logical device.
    
This property is inherited from <b>CIM_LogicalDevice</b>.
      <dt><b>Unknown</b> (0)</dt>
      <dt><b>Not Supported</b> (1)</dt>
      <dt><b>Disabled</b> (2)</dt>
      <dt><b>Enabled</b> (3)</dt>
      <dd>
The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.</dd>
      <dt><b>Power Saving Modes Entered Automatically</b> (4)</dt>
      <dd>The device can change its power state based on usage or other criteria.</dd>
      <dt><b>Power State Settable</b> (5)</dt>
      <dd>The [<b>SetPowerState</b>](setpowerstate-method-in-class-cim-controller.md) method is supported. This method is found on the parent <b>CIM_LogicalDevice</b> class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes][5].</dd>
      <dt><b>Power Cycling Supported</b> (6)</dt>
      <dd>The [<b>SetPowerState</b>](setpowerstate-method-in-class-cim-controller.md) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle).</dd>
      <dt><b>Timed Power On Supported</b> (7)</dt>
      <dd>Timed Power-On Supported
The [<b>SetPowerState</b>](setpowerstate-method-in-class-cim-controller.md) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle) and *Time* set to a specific date and time, or interval, for power-on.</dd>
    </dl>
  </dd>
  <dt><b>PowerManagementSupported</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
If <b>TRUE</b>, the power of the device can be managed, which means that it can be put into suspend mode, and so on. The property does not indicate that power management features are enabled, but it does indicate that the logical device power can be managed.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>ProcessorId</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Processor ID")</dt>
    </dl>
Processor information that describes the processor features. For an x86 class CPU, the field format depends on the processor support of the CPUID instruction. If the instruction is supported, the property contains 2 (two) <b>DWORD</b> formatted values. The first is an offset of 08h-0Bh, which is the EAX value that a CPUID instruction returns with input EAX set to 1. The second is an offset of 0Ch-0Fh, which is the EDX value that the instruction returns. Only the first two bytes of the property are significant and contain the contents of the DX register at CPU reset—all others are set to 0 (zero), and the contents are in <b>DWORD</b> format.

This value comes from the <b>Processor ID</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>ProcessorType</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Processor Type")</dt>
    </dl>
    <dl>Primary function of the processor.

This value comes from the <b>Processor Type</b> member of the <b>Processor Information</b> structure in the SMBIOS information.
      <dt><b>Other</b> (1)</dt>
      <dt><b>Unknown</b> (2)</dt>
      <dt><b>Central Processor</b> (3)</dt>
      <dt><b>Math Processor</b> (4)</dt>
      <dt><b>DSP Processor</b> (5)</dt>
      <dt><b>Video Processor</b> (6)</dt>
    </dl></dd>
  <dt><b>Revision</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
System revision level that depends on the architecture. The system revision level contains the same values as the <b>Version</b> property, but in a numerical format.</dd>
  <dt><b>Role</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
Role of the processor.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).

Examples: Central Processor or Math Processor</dd>
  <dt><b>SecondLevelAddressTranslationExtensions</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
If <b>True</b>, the processor supports address translation extensions used for virtualization.
    <b>Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows 8 and Windows Server 2012.</dd>
  <dt><b>SerialNumber</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Serial Number")</dt>
    </dl>
The serial number of this processor This value is set by the manufacturer and normally not changeable.

This value comes from the <b>Serial Number</b> member of the <b>Processor Information</b> structure in the SMBIOS information.
    <b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.</dd>
  <dt><b>SocketDesignation</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Socket Designation")</dt>
    </dl>
Type of chip socket used on the circuit.
Example: J202

This value comes from the <b>Socket Designation</b> member of the <b>Processor Information</b> structure in the SMBIOS information.</dd>
  <dt><b>Status</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MaxLen</b>][1] (10), [<b>DisplayName</b>][1] ("Status")</dt>
    </dl>
    <dl>Current status of an object. This property is inherited from [<b>CIM_ManagedSystemElement</b>](cim-managedsystemelement.md).
Values include the following:
      <dt><b>OK</b> ("OK")</dt>
      <dt><b>Error</b> ("Error")</dt>
      <dt><b>Degraded</b> ("Degraded")</dt>
      <dt><b>Unknown</b> ("Unknown")</dt>
      <dt><b>Pred Fail</b> ("Pred Fail")</dt>
      <dt><b>Starting</b> ("Starting")</dt>
      <dt><b>Stopping</b> ("Stopping")</dt>
      <dt><b>Service</b> ("Service")</dt>
      <dt><b>Stressed</b> ("Stressed")</dt>
      <dt><b>NonRecover</b> ("NonRecover")</dt>
      <dt><b>No Contact</b> ("No Contact")</dt>
      <dt><b>Lost Comm</b> ("Lost Comm")</dt>
    </dl></dd>
  <dt><b>StatusInfo</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Operational State\|003.3")</dt>
    </dl>
    <dl>State of the logical device. If this property does not apply to the logical device, use the value 5, which means Not Applicable.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).
      <dt><b>Other</b> (1)</dt>
      <dt><b>Unknown</b> (2)</dt>
      <dt><b>Enabled</b> (3)</dt>
      <dt><b>Disabled</b> (4)</dt>
      <dt><b>Not Applicable</b> (5)</dt>
    </dl></dd>
  <dt><b>Stepping</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>ModelCorrespondence</b>][1] ("[<b>CIM_Processor</b>](cim-processor.md).<b>Family</b>")</dt>
    </dl>
Revision level of the processor in the processor family.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>SystemCreationClassName</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Propagated</b>][1] ("[<b>CIM_System</b>](cim-system.md).<b>CreationClassName</b>"), [<b>CIM_Key</b>][2]</dt>
    </dl>
Value of the <b>CreationClassName</b> property for the scoping computer.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>SystemName</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>Propagated</b>][1] ("[<b>CIM_System</b>](cim-system.md).<b>Name</b>"), [<b>CIM_Key</b>][2]</dt>
    </dl>
Name of the scoping system.

This property is inherited from [<b>CIM_LogicalDevice</b>](cim-logicaldevice.md).</dd>
  <dt><b>ThreadCount</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Thread Count")</dt>
    </dl>
The number of threads per processor socket.

This value comes from the <b>Processor Information</b> structure in the SMBIOS version information. For SMBIOS versions 2.5 thru 2.9 the value comes from the <b>Thread Count</b> member. For SMBIOS version 3.0+ the value comes from the <b>Thread Count 2</b> member.
    <b>Windows Server 2012 R2, Windows 8.1, Windows Server 2012, Windows 8, Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows Server 2016 and Windows 10.</dd>
  <dt><b>UniqueId</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
    </dl>
Globally unique identifier for the processor. This identifier may only be unique within a processor family.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).</dd>
  <dt><b>UpgradeMethod</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint16</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("MIF.DMTF\|Processor\|006.7")</dt>
    </dl>
    <dl>CPU socket information, including the method by which this processor can be upgraded, if upgrades are supported. This property is an integer enumeration.

This value comes from the <b>Processor Upgrade</b> member of the <b>Processor Information</b> structure in the SMBIOS information.

This property is inherited from [<b>CIM_Processor</b>](cim-processor.md).
      <dt><b>Other</b> (1)</dt>
      <dt><b>Unknown</b> (2)</dt>
      <dt><b>Daughter Board</b> (3)</dt>
      <dt><b>ZIF Socket</b> (4)</dt>
      <dt><b>Replacement/Piggy Back</b> (5)</dt>
      <dd>
Replacement or Piggy Back</dd>
      <dt><b>None</b> (6)</dt>
      <dt><b>LIF Socket</b> (7)</dt>
      <dt><b>Slot 1</b> (8)</dt>
      <dt><b>Slot 2</b> (9)</dt>
      <dt><b>370 Pin Socket</b> (10)</dt>
      <dt><b>Slot A</b> (11)</dt>
      <dt><b>Slot M</b> (12)</dt>
      <dt><b>Socket 423</b> (13)</dt>
      <dt><b>Socket A (Socket 462)</b> (14)</dt>
      <dt><b>Socket 478</b> (15)</dt>
      <dt><b>Socket 754</b> (16)</dt>
      <dt><b>Socket 940</b> (17)</dt>
      <dt><b>Socket 939</b> (18)</dt>
    </dl>
  </dd>
  <dt><b>Version</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>string</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
Processor revision number that depends on the architecture.
Example: Model 2, Stepping 12</dd>
  <dt><b>VirtualizationFirmwareEnabled</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
If <b>True</b>, the Firmware has enabled virtualization extensions.
    <b>Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows 8 and Windows Server 2012.
  </dd>
  <dt><b>VMMonitorModeExtensions</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>boolean</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("WMI")</dt>
    </dl>
If <b>True</b>, the processor supports Intel or AMD Virtual Machine Monitor extensions.
    <b>Windows Server 2008 R2, Windows 7, Windows Server 2008 and Windows Vista:</b> This property is not supported before Windows 8 and Windows Server 2012.
  </dd>
  <dt><b>VoltageCaps</b></dt>
  <dd>
    <dl>
      <dt>Data type: <b>uint32</b></dt>
      <dt>Access type: Read-only</dt>
      <dt>Qualifiers: [<b>MappingStrings</b>][1] ("SMBIOS\|Type 4\|Processor Information\|Voltage"), [<b>Units</b>][1] ("volts")</dt>
    </dl>
    <dl>Voltage capabilities of the processor. Bits 0-3 of the field represent specific voltages that the processor socket can accept. All other bits should be set to 0 (zero). The socket is configurable if multiple bits are set. For more information about the actual voltage at which the processor is running, see <b>CurrentVoltage</b>. If the property is <b>NULL</b>, then the voltage capabilities are unknown.
      <dt><b>5</b> (1)</dt>
      <dd>5 volts</dd>
      <dt><b>3.3</b> (2)</dt>
      <dd>3.3 volts</dd>
      <dt><b>2.9</b> (4)</dt>
      <dd>2.9 volts</dd>
    </dl>
  </dd>
</dl>

## Remarks

On a multiprocessor computer, one instance of the **Win32_Processor** class exists for each processor.

To determine the total number of processor instances associated with a computer system object, use the [**Win32_ComputerSystemProcessor**](win32-computersystemprocessor.md) association class.

To determine if hyperthreading is enabled for the processor, compare **NumberOfLogicalProcessors** and **NumberOfCores**. If hyperthreading is enabled in the BIOS for the processor, then **NumberOfCores** is less than **NumberOfLogicalProcessors**. For example, a dual-processor system that contains two processors enabled for hyperthreading can run four threads or programs or simultaneously. In this case, **NumberOfCores** is 2 and **NumberOfLogicalProcessors** is 4.

The **Win32_Processor** class is derived from [**CIM_Processor**](cim-processor.md).

## Examples

The [WMI Information Retriever](https://Gallery.TechNet.Microsoft.Com/e493376c-1286-456b-bd4b-4ac3b0e9bb45) VBScript code example on the TechNet Gallery uses the [**Win32_ComputerSystemProcessor**](win32-computersystemprocessor.md) class to retrieve processor information from a number of remote computers.

The [Get-ComputerInfo - Query Computer Info From Local/Remote Computers - (WMI)](https://Gallery.TechNet.Microsoft.Com/Get-ComputerInfo-Query-23dd6042) PowerShell sample on TechNet Gallery uses a number of calls to hardware and software, including [**Win32_ComputerSystemProcessor**](win32-computersystemprocessor.md), to display information about a local or remote system.

The [Multithreaded System Asset Gathering with Powershell](https://Gallery.TechNet.Microsoft.Com/Multithreaded-System-Asset-856a8f7c) PowerShell example on TechNet gallery uses a number of classes, including [**Win32_ComputerSystemProcessor**](win32-computersystemprocessor.md), to retrieve data from a system.

The following VBScript code example retrieves data about the operating system version and the processor it is running on from **Win32_Processor**, [**Win32_ComputerSystem**](win32-computersystem.md), and [**Win32_OperatingSystem**](win32-operatingsystem.md). This example requires Windows Vista or later.


```VB

strComputer = "."
Set objWMIService = GetObject("winmgmts:" _
 & "{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")


Set colOSes = objWMIService.ExecQuery("Select * from Win32_OperatingSystem")
For Each objOS in colOSes
  Wscript.Echo "Computer Name: " & objOS.CSName

  Wscript.Echo "Operating System"
  Wscript.Echo "  Caption: " & objOS.Caption 'Name
  Wscript.Echo "  Version: " & objOS.Version 'Version & build
  Wscript.Echo "  BuildNumber: " & objOS.BuildNumber 'Build
  Wscript.Echo "  BuildType: " & objOS.BuildType
  Wscript.Echo "  OSProductSuite: " & objOS.OSProductsuite 'OS Product suite
  Wscript.Echo "  OSArchitecture: " & objOS.OSArchitecture
  Wscript.Echo "  OSType: " & objOS.OSType
  Wscript.Echo "  OtherTypeDescription: " & objOS.OtherTypeDescription
  WScript.Echo "  ServicePackMajorVersion: " & objOS.ServicePackMajorVersion & "." & _
   objOS.ServicePackMinorVersion

Next

Wscript.Echo "Processors"

Set colCompSys = objWMIService.ExecQuery("Select * from Win32_ComputerSystem")
For Each objCS in colCompSys
  WScript.Echo "  NumberOfProcessors: " & objCS.NumberOfProcessors
  WScript.Echo "  NumberOfLogicalProcessors: " & objCS.NumberOfLogicalProcessors
  WScript.Echo "  PCSystemType: " & objCS.PCSystemType
Next

Set colProcessors = objWMIService.ExecQuery("Select * from Win32_Processor")
For Each objProcessor in colProcessors
  WScript.Echo "  Manufacturer: " & objProcessor.Manufacturer
  WScript.Echo "  Name: " & objProcessor.Name
  WScript.Echo "  Description: " & objProcessor.Description
  WScript.Echo "  ProcessorID: " & objProcessor.ProcessorID
  WScript.Echo "  Architecture: " & objProcessor.Architecture
  WScript.Echo "  AddressWidth: " & objProcessor.AddressWidth
  WScript.Echo "  NumberOfCores: " & objProcessor.NumberOfCores
  WScript.Echo "  DataWidth: " & objProcessor.DataWidth
  WScript.Echo "  Family: " & objProcessor.Family
  WScript.Echo "  MaximumClockSpeed: " & objProcessor.MaxClockSpeed
Next
```

The following VBScript code example shows how to use **Win32_Processor** to determine the computer architecture.

```VB
Set objProc = GetObject("winmgmts:root\cimv2:Win32_Processor='cpu0'")

If objProc.Architecture = 0 Then
    WScript.Echo "x86"
ElseIf objProc.Architecture = 6 Then
    WScript.Echo "Itanium"
Else
    WScript.Echo "Unknown"
End If
```


## Requirements

| Requirement | Value |
|--------------------------|----------------------------------|
| Minimum supported client | Windows Vista                    |
| Minimum supported server | Windows Server 2008              |
| Namespace                | Root\\CIMV2                      |
| MOF                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL                      | <dl> <dt>CIMWin32.dll</dt> </dl> |

## See also

<dl>
    <dt>[<b>CIM_Processor</b>](cim-processor.md)</dt>
    <dt>[Computer System Hardware Classes](computer-system-hardware-classes.md)</dt>
    <dt>[WMI Tasks: Computer Hardware](../wmisdk/wmi-tasks--computer-hardware.md)</dt>
</dl>

  [0]: /windows/win32/wmisdk/retrieving-a-class
  [1]: /windows/win32/wmisdk/standard-qualifiers
  [2]: /windows/win32/wmisdk/standard-wmi-qualifiers
  [3]: /windows/win32/wmisdk/key-qualifier
  [4]: /windows/win32/api/sysinfoapi/ns-sysinfoapi-system_info
  [5]: /windows/win32/wmisdk/designing-managed-object-format--mof--classes
