---
description: Represents the capabilities and management capacity of the video controller on a computer system running Windows.
ms.assetid: 5c81994b-4a84-46ff-8689-09998dc66f91
ms.tgt_platform: multiple
title: Win32_VideoController class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_VideoController
- Win32_VideoController.Reset
- Win32_VideoController.SetPowerState
- Win32_VideoController.AcceleratorCapabilities
- Win32_VideoController.AdapterCompatibility
- Win32_VideoController.AdapterDACType
- Win32_VideoController.AdapterRAM
- Win32_VideoController.Availability
- Win32_VideoController.CapabilityDescriptions
- Win32_VideoController.Caption
- Win32_VideoController.ColorTableEntries
- Win32_VideoController.ConfigManagerErrorCode
- Win32_VideoController.ConfigManagerUserConfig
- Win32_VideoController.CreationClassName
- Win32_VideoController.CurrentBitsPerPixel
- Win32_VideoController.CurrentHorizontalResolution
- Win32_VideoController.CurrentNumberOfColors
- Win32_VideoController.CurrentNumberOfColumns
- Win32_VideoController.CurrentNumberOfRows
- Win32_VideoController.CurrentRefreshRate
- Win32_VideoController.CurrentScanMode
- Win32_VideoController.CurrentVerticalResolution
- Win32_VideoController.Description
- Win32_VideoController.DeviceID
- Win32_VideoController.DeviceSpecificPens
- Win32_VideoController.DitherType
- Win32_VideoController.DriverDate
- Win32_VideoController.DriverVersion
- Win32_VideoController.ErrorCleared
- Win32_VideoController.ErrorDescription
- Win32_VideoController.ICMIntent
- Win32_VideoController.ICMMethod
- Win32_VideoController.InfFilename
- Win32_VideoController.InfSection
- Win32_VideoController.InstallDate
- Win32_VideoController.InstalledDisplayDrivers
- Win32_VideoController.LastErrorCode
- Win32_VideoController.MaxMemorySupported
- Win32_VideoController.MaxNumberControlled
- Win32_VideoController.MaxRefreshRate
- Win32_VideoController.MinRefreshRate
- Win32_VideoController.Monochrome
- Win32_VideoController.Name
- Win32_VideoController.NumberOfColorPlanes
- Win32_VideoController.NumberOfVideoPages
- Win32_VideoController.PNPDeviceID
- Win32_VideoController.PowerManagementCapabilities
- Win32_VideoController.PowerManagementSupported
- Win32_VideoController.ProtocolSupported
- Win32_VideoController.ReservedSystemPaletteEntries
- Win32_VideoController.SpecificationVersion
- Win32_VideoController.Status
- Win32_VideoController.StatusInfo
- Win32_VideoController.SystemCreationClassName
- Win32_VideoController.SystemName
- Win32_VideoController.SystemPaletteEntries
- Win32_VideoController.TimeOfLastReset
- Win32_VideoController.VideoArchitecture
- Win32_VideoController.VideoMemoryType
- Win32_VideoController.VideoMode
- Win32_VideoController.VideoModeDescription
- Win32_VideoController.VideoProcessor
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_VideoController class

The **Win32\_VideoController** [WMI class](../wmisdk/retrieving-a-class.md) represents the capabilities and management capacity of the video controller on a computer system running Windows.

Hardware that is not compatible with Windows Display Driver Model (WDDM) returns inaccurate property values for instances of this class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{1008CCF1-7BFF-11D2-AAD2-006008C78BC7}"), AMENDMENT]
class Win32_VideoController : CIM_PCVideoController
{
  uint16   AcceleratorCapabilities[];
  string   AdapterCompatibility;
  string   AdapterDACType;
  uint32   AdapterRAM;
  uint16   Availability;
  string   CapabilityDescriptions[];
  string   Caption;
  uint32   ColorTableEntries;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  string   CreationClassName;
  uint32   CurrentBitsPerPixel;
  uint32   CurrentHorizontalResolution;
  uint64   CurrentNumberOfColors;
  uint32   CurrentNumberOfColumns;
  uint32   CurrentNumberOfRows;
  uint32   CurrentRefreshRate;
  uint16   CurrentScanMode;
  uint32   CurrentVerticalResolution;
  string   Description;
  string   DeviceID;
  uint32   DeviceSpecificPens;
  uint32   DitherType;
  datetime DriverDate;
  string   DriverVersion;
  boolean  ErrorCleared;
  string   ErrorDescription;
  uint32   ICMIntent;
  uint32   ICMMethod;
  string   InfFilename;
  string   InfSection;
  datetime InstallDate;
  string   InstalledDisplayDrivers;
  uint32   LastErrorCode;
  uint32   MaxMemorySupported;
  uint32   MaxNumberControlled;
  uint32   MaxRefreshRate;
  uint32   MinRefreshRate;
  boolean  Monochrome;
  string   Name;
  uint16   NumberOfColorPlanes;
  uint32   NumberOfVideoPages;
  string   PNPDeviceID;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  uint16   ProtocolSupported;
  uint32   ReservedSystemPaletteEntries;
  uint32   SpecificationVersion;
  string   Status;
  uint16   StatusInfo;
  string   SystemCreationClassName;
  string   SystemName;
  uint32   SystemPaletteEntries;
  datetime TimeOfLastReset;
  uint16   VideoArchitecture;
  uint16   VideoMemoryType;
  uint16   VideoMode;
  string   VideoModeDescription;
  string   VideoProcessor;
};
```

## Members

The **Win32\_VideoController** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_VideoController** class has these methods.



| Method            | Description                                                                                                                                                                                            |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reset**         | Not implemented. To implement this method, see the [**Reset**](reset-method-in-class-cim-controller.md) method in [**CIM\_PCVideoController**](cim-pcvideocontroller.md).<br/>                 |
| **SetPowerState** | Not implemented. To implement this method, see the [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method in [**CIM\_PCVideoController**](cim-pcvideocontroller.md).<br/> |



 

### Properties

The **Win32\_VideoController** class has these properties.

<dl> <dt>

**AcceleratorCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](../wmisdk/standard-qualifiers.md) ("[**CIM\_VideoController**](cim-videocontroller.md).**CapabilityDescriptions**")
</dt> </dl>

Array of graphics and 3-D capabilities of the video controller.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Graphics_Accelerator"></span><span id="graphics_accelerator"></span><span id="GRAPHICS_ACCELERATOR"></span>

<span id="Graphics_Accelerator"></span><span id="graphics_accelerator"></span><span id="GRAPHICS_ACCELERATOR"></span>**Graphics Accelerator** (2)


</dt> <dd></dd> <dt>

<span id="3D_Accelerator"></span><span id="3d_accelerator"></span><span id="3D_ACCELERATOR"></span>

<span id="3D_Accelerator"></span><span id="3d_accelerator"></span><span id="3D_ACCELERATOR"></span>**3D Accelerator** (3)


</dt> <dd>

3-D Accelerator

</dd> </dl>

</dd> <dt>

**AdapterCompatibility**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry")
</dt> </dl>

General chipset used for this controller to compare compatibilities with the system.

</dd> <dt>

**AdapterDACType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|HardwareInformation.DACType")
</dt> </dl>

Name or identifier of the digital-to-analog converter (DAC) chip. The character set of this property is alphanumeric.

</dd> <dt>

**AdapterRAM**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|HardwareInformation.MemorySize"), [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Memory size of the video adapter.

Example: 64000

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Operational State\|003.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus")
</dt> </dl>

Availability and status of the device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>

<span id="Running_Full_Power"></span><span id="running_full_power"></span><span id="RUNNING_FULL_POWER"></span>**Running/Full Power** (3)


</dt> <dd>

Running or Full Power

</dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>**Warning** (4)


</dt> <dd></dd> <dt>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>

<span id="In_Test"></span><span id="in_test"></span><span id="IN_TEST"></span>**In Test** (5)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (6)


</dt> <dd></dd> <dt>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>

<span id="Power_Off"></span><span id="power_off"></span><span id="POWER_OFF"></span>**Power Off** (7)


</dt> <dd></dd> <dt>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>

<span id="Off_Line"></span><span id="off_line"></span><span id="OFF_LINE"></span>**Off Line** (8)


</dt> <dd>

Offline

</dd> <dt>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>

<span id="Off_Duty"></span><span id="off_duty"></span><span id="OFF_DUTY"></span>**Off Duty** (9)


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>**Degraded** (10)


</dt> <dd></dd> <dt>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>

<span id="Not_Installed"></span><span id="not_installed"></span><span id="NOT_INSTALLED"></span>**Not Installed** (11)


</dt> <dd></dd> <dt>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>

<span id="Install_Error"></span><span id="install_error"></span><span id="INSTALL_ERROR"></span>**Install Error** (12)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>

<span id="Power_Save_-_Unknown"></span><span id="power_save_-_unknown"></span><span id="POWER_SAVE_-_UNKNOWN"></span>**Power Save - Unknown** (13)


</dt> <dd>

The device is known to be in a power save mode, but its exact status is unknown.

</dd> <dt>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>

<span id="Power_Save_-_Low_Power_Mode"></span><span id="power_save_-_low_power_mode"></span><span id="POWER_SAVE_-_LOW_POWER_MODE"></span>**Power Save - Low Power Mode** (14)


</dt> <dd>

The device is in a power save state but still functioning, and may exhibit degraded performance.

</dd> <dt>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>

<span id="Power_Save_-_Standby"></span><span id="power_save_-_standby"></span><span id="POWER_SAVE_-_STANDBY"></span>**Power Save - Standby** (15)


</dt> <dd>

The device is not functioning, but could be brought to full power quickly.

</dd> <dt>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>

<span id="Power_Cycle"></span><span id="power_cycle"></span><span id="POWER_CYCLE"></span>**Power Cycle** (16)


</dt> <dd></dd> <dt>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>

<span id="Power_Save_-_Warning"></span><span id="power_save_-_warning"></span><span id="POWER_SAVE_-_WARNING"></span>**Power Save - Warning** (17)


</dt> <dd>

The device is in a warning state, though also in a power save mode.

</dd> <dt>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>

<span id="Paused"></span><span id="paused"></span><span id="PAUSED"></span>**Paused** (18)


</dt> <dd>

The device is paused.

</dd> <dt>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>

<span id="Not_Ready"></span><span id="not_ready"></span><span id="NOT_READY"></span>**Not Ready** (19)


</dt> <dd>

The device is not ready.

</dd> <dt>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>

<span id="Not_Configured"></span><span id="not_configured"></span><span id="NOT_CONFIGURED"></span>**Not Configured** (20)


</dt> <dd>

The device is not configured.

</dd> <dt>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>

<span id="Quiesced"></span><span id="quiesced"></span><span id="QUIESCED"></span>**Quiesced** (21)


</dt> <dd>

The device is quiet.

</dd> </dl>

</dd> <dt>

**CapabilityDescriptions**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](../wmisdk/standard-qualifiers.md) ("Indexed"), [**ModelCorrespondence**](../wmisdk/standard-qualifiers.md) ("[**CIM\_VideoController**](cim-videocontroller.md).**AcceleratorCapabilities**")
</dt> </dl>

Free-form strings providing more detailed explanations for any of the video accelerator features indicated in the **AcceleratorCapabilities** array. Note, each entry of this array is related to the entry in the **AcceleratorCapabilities** array that is located at the same index.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (64), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Caption")
</dt> </dl>

Short description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ColorTableEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps)")
</dt> </dl>

Size of the system's color table. The device must have a color depth of no more than 8 bits per pixel; otherwise, this property is not set.

Example: 256

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](../wmisdk/standard-qualifiers.md) ("Win32")
</dt> </dl>

Win32 Configuration Manager error code.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

<dt>

<span id="This_device_is_working_properly."></span><span id="this_device_is_working_properly."></span><span id="THIS_DEVICE_IS_WORKING_PROPERLY."></span>

<span id="this_device_is_working_properly."></span><span id="THIS_DEVICE_IS_WORKING_PROPERLY."></span>**This device is working properly.** (0)


</dt> <dd>

Device is working properly.

</dd> <dt>

<span id="This_device_is_not_configured_correctly."></span><span id="this_device_is_not_configured_correctly."></span><span id="THIS_DEVICE_IS_NOT_CONFIGURED_CORRECTLY."></span>

<span id="this_device_is_not_configured_correctly."></span><span id="THIS_DEVICE_IS_NOT_CONFIGURED_CORRECTLY."></span>**This device is not configured correctly.** (1)


</dt> <dd>

Device is not configured correctly.

</dd> <dt>

<span id="Windows_cannot_load_the_driver_for_this_device."></span><span id="windows_cannot_load_the_driver_for_this_device."></span><span id="WINDOWS_CANNOT_LOAD_THE_DRIVER_FOR_THIS_DEVICE."></span>

<span id="windows_cannot_load_the_driver_for_this_device."></span><span id="WINDOWS_CANNOT_LOAD_THE_DRIVER_FOR_THIS_DEVICE."></span>**Windows cannot load the driver for this device.** (2)


</dt> <dd></dd> <dt>

<span id="The_driver_for_this_device_might_be_corrupted__or_your_system_may_be_running_low_on_memory_or_other_resources."></span><span id="the_driver_for_this_device_might_be_corrupted__or_your_system_may_be_running_low_on_memory_or_other_resources."></span><span id="THE_DRIVER_FOR_THIS_DEVICE_MIGHT_BE_CORRUPTED__OR_YOUR_SYSTEM_MAY_BE_RUNNING_LOW_ON_MEMORY_OR_OTHER_RESOURCES."></span>

<span id="the_driver_for_this_device_might_be_corrupted__or_your_system_may_be_running_low_on_memory_or_other_resources."></span><span id="THE_DRIVER_FOR_THIS_DEVICE_MIGHT_BE_CORRUPTED__OR_YOUR_SYSTEM_MAY_BE_RUNNING_LOW_ON_MEMORY_OR_OTHER_RESOURCES."></span>**The driver for this device might be corrupted, or your system may be running low on memory or other resources.** (3)


</dt> <dd>

Driver for this device might be corrupted, or the system may be low on memory or other resources.

</dd> <dt>

<span id="This_device_is_not_working_properly._One_of_its_drivers_or_your_registry_might_be_corrupted."></span><span id="this_device_is_not_working_properly._one_of_its_drivers_or_your_registry_might_be_corrupted."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY._ONE_OF_ITS_DRIVERS_OR_YOUR_REGISTRY_MIGHT_BE_CORRUPTED."></span>

<span id="This_device_is_not_working_properly._One_of_its_drivers_or_your_registry_might_be_corrupted."></span><span id="this_device_is_not_working_properly._one_of_its_drivers_or_your_registry_might_be_corrupted."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY._ONE_OF_ITS_DRIVERS_OR_YOUR_REGISTRY_MIGHT_BE_CORRUPTED."></span>**This device is not working properly. One of its drivers or your registry might be corrupted.** (4)


</dt> <dd>

Device is not working properly. One of its drivers or the registry might be corrupted.

</dd> <dt>

<span id="The_driver_for_this_device_needs_a_resource_that_Windows_cannot_manage."></span><span id="the_driver_for_this_device_needs_a_resource_that_windows_cannot_manage."></span><span id="THE_DRIVER_FOR_THIS_DEVICE_NEEDS_A_RESOURCE_THAT_WINDOWS_CANNOT_MANAGE."></span>

<span id="the_driver_for_this_device_needs_a_resource_that_windows_cannot_manage."></span><span id="THE_DRIVER_FOR_THIS_DEVICE_NEEDS_A_RESOURCE_THAT_WINDOWS_CANNOT_MANAGE."></span>**The driver for this device needs a resource that Windows cannot manage.** (5)


</dt> <dd>

Driver for the device requires a resource that Windows cannot manage.

</dd> <dt>

<span id="The_boot_configuration_for_this_device_conflicts_with_other_devices."></span><span id="the_boot_configuration_for_this_device_conflicts_with_other_devices."></span><span id="THE_BOOT_CONFIGURATION_FOR_THIS_DEVICE_CONFLICTS_WITH_OTHER_DEVICES."></span>

<span id="the_boot_configuration_for_this_device_conflicts_with_other_devices."></span><span id="THE_BOOT_CONFIGURATION_FOR_THIS_DEVICE_CONFLICTS_WITH_OTHER_DEVICES."></span>**The boot configuration for this device conflicts with other devices.** (6)


</dt> <dd>

Boot configuration for the device conflicts with other devices.

</dd> <dt>

<span id="Cannot_filter."></span><span id="cannot_filter."></span><span id="CANNOT_FILTER."></span>

<span id="cannot_filter."></span><span id="CANNOT_FILTER."></span>**Cannot filter.** (7)


</dt> <dd></dd> <dt>

<span id="The_driver_loader_for_the_device_is_missing."></span><span id="the_driver_loader_for_the_device_is_missing."></span><span id="THE_DRIVER_LOADER_FOR_THE_DEVICE_IS_MISSING."></span>

<span id="the_driver_loader_for_the_device_is_missing."></span><span id="THE_DRIVER_LOADER_FOR_THE_DEVICE_IS_MISSING."></span>**The driver loader for the device is missing.** (8)


</dt> <dd>

Driver loader for the device is missing.

</dd> <dt>

<span id="This_device_is_not_working_properly_because_the_controlling_firmware_is_reporting_the_resources_for_the_device_incorrectly."></span><span id="this_device_is_not_working_properly_because_the_controlling_firmware_is_reporting_the_resources_for_the_device_incorrectly."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_THE_CONTROLLING_FIRMWARE_IS_REPORTING_THE_RESOURCES_FOR_THE_DEVICE_INCORRECTLY."></span>

<span id="this_device_is_not_working_properly_because_the_controlling_firmware_is_reporting_the_resources_for_the_device_incorrectly."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_THE_CONTROLLING_FIRMWARE_IS_REPORTING_THE_RESOURCES_FOR_THE_DEVICE_INCORRECTLY."></span>**This device is not working properly because the controlling firmware is reporting the resources for the device incorrectly.** (9)


</dt> <dd>

Device is not working properly. The controlling firmware is incorrectly reporting the resources for the device.

</dd> <dt>

<span id="This_device_cannot_start."></span><span id="this_device_cannot_start."></span><span id="THIS_DEVICE_CANNOT_START."></span>

<span id="this_device_cannot_start."></span><span id="THIS_DEVICE_CANNOT_START."></span>**This device cannot start.** (10)


</dt> <dd>

Device cannot start.

</dd> <dt>

<span id="This_device_failed."></span><span id="this_device_failed."></span><span id="THIS_DEVICE_FAILED."></span>

<span id="this_device_failed."></span><span id="THIS_DEVICE_FAILED."></span>**This device failed.** (11)


</dt> <dd>

Device failed.

</dd> <dt>

<span id="This_device_cannot_find_enough_free_resources_that_it_can_use."></span><span id="this_device_cannot_find_enough_free_resources_that_it_can_use."></span><span id="THIS_DEVICE_CANNOT_FIND_ENOUGH_FREE_RESOURCES_THAT_IT_CAN_USE."></span>

<span id="this_device_cannot_find_enough_free_resources_that_it_can_use."></span><span id="THIS_DEVICE_CANNOT_FIND_ENOUGH_FREE_RESOURCES_THAT_IT_CAN_USE."></span>**This device cannot find enough free resources that it can use.** (12)


</dt> <dd>

Device cannot find enough free resources to use.

</dd> <dt>

<span id="Windows_cannot_verify_this_device_s_resources."></span><span id="windows_cannot_verify_this_device_s_resources."></span><span id="WINDOWS_CANNOT_VERIFY_THIS_DEVICE_S_RESOURCES."></span>

<span id="windows_cannot_verify_this_device_s_resources."></span><span id="WINDOWS_CANNOT_VERIFY_THIS_DEVICE_S_RESOURCES."></span>**Windows cannot verify this device's resources.** (13)


</dt> <dd>

Windows cannot verify the device's resources.

</dd> <dt>

<span id="This_device_cannot_work_properly_until_you_restart_your_computer."></span><span id="this_device_cannot_work_properly_until_you_restart_your_computer."></span><span id="THIS_DEVICE_CANNOT_WORK_PROPERLY_UNTIL_YOU_RESTART_YOUR_COMPUTER."></span>

<span id="this_device_cannot_work_properly_until_you_restart_your_computer."></span><span id="THIS_DEVICE_CANNOT_WORK_PROPERLY_UNTIL_YOU_RESTART_YOUR_COMPUTER."></span>**This device cannot work properly until you restart your computer.** (14)


</dt> <dd>

Device cannot work properly until the computer is restarted.

</dd> <dt>

<span id="This_device_is_not_working_properly_because_there_is_probably_a_re-enumeration_problem."></span><span id="this_device_is_not_working_properly_because_there_is_probably_a_re-enumeration_problem."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_THERE_IS_PROBABLY_A_RE-ENUMERATION_PROBLEM."></span>

<span id="This_device_is_not_working_properly_because_there_is_probably_a_re-enumeration_problem."></span><span id="this_device_is_not_working_properly_because_there_is_probably_a_re-enumeration_problem."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_THERE_IS_PROBABLY_A_RE-ENUMERATION_PROBLEM."></span>**This device is not working properly because there is probably a re-enumeration problem.** (15)


</dt> <dd>

Device is not working properly due to a possible re-enumeration problem.

</dd> <dt>

<span id="Windows_cannot_identify_all_the_resources_this_device_uses."></span><span id="windows_cannot_identify_all_the_resources_this_device_uses."></span><span id="WINDOWS_CANNOT_IDENTIFY_ALL_THE_RESOURCES_THIS_DEVICE_USES."></span>

<span id="windows_cannot_identify_all_the_resources_this_device_uses."></span><span id="WINDOWS_CANNOT_IDENTIFY_ALL_THE_RESOURCES_THIS_DEVICE_USES."></span>**Windows cannot identify all the resources this device uses.** (16)


</dt> <dd>

Windows cannot identify all of the resources that the device uses.

</dd> <dt>

<span id="This_device_is_asking_for_an_unknown_resource_type."></span><span id="this_device_is_asking_for_an_unknown_resource_type."></span><span id="THIS_DEVICE_IS_ASKING_FOR_AN_UNKNOWN_RESOURCE_TYPE."></span>

<span id="this_device_is_asking_for_an_unknown_resource_type."></span><span id="THIS_DEVICE_IS_ASKING_FOR_AN_UNKNOWN_RESOURCE_TYPE."></span>**This device is asking for an unknown resource type.** (17)


</dt> <dd>

Device is requesting an unknown resource type.

</dd> <dt>

<span id="Reinstall_the_drivers_for_this_device."></span><span id="reinstall_the_drivers_for_this_device."></span><span id="REINSTALL_THE_DRIVERS_FOR_THIS_DEVICE."></span>

<span id="reinstall_the_drivers_for_this_device."></span><span id="REINSTALL_THE_DRIVERS_FOR_THIS_DEVICE."></span>**Reinstall the drivers for this device.** (18)


</dt> <dd>

Device drivers must be reinstalled.

</dd> <dt>

<span id="Failure_using_the_VxD_loader."></span><span id="failure_using_the_vxd_loader."></span><span id="FAILURE_USING_THE_VXD_LOADER."></span>

<span id="failure_using_the_vxd_loader."></span><span id="FAILURE_USING_THE_VXD_LOADER."></span>**Failure using the VxD loader.** (19)


</dt> <dd></dd> <dt>

<span id="Your_registry_might_be_corrupted."></span><span id="your_registry_might_be_corrupted."></span><span id="YOUR_REGISTRY_MIGHT_BE_CORRUPTED."></span>

<span id="your_registry_might_be_corrupted."></span><span id="YOUR_REGISTRY_MIGHT_BE_CORRUPTED."></span>**Your registry might be corrupted.** (20)


</dt> <dd>

Registry might be corrupted.

</dd> <dt>

<span id="System_failure__Try_changing_the_driver_for_this_device._If_that_does_not_work__see_your_hardware_documentation._Windows_is_removing_this_device."></span><span id="system_failure__try_changing_the_driver_for_this_device._if_that_does_not_work__see_your_hardware_documentation._windows_is_removing_this_device."></span><span id="SYSTEM_FAILURE__TRY_CHANGING_THE_DRIVER_FOR_THIS_DEVICE._IF_THAT_DOES_NOT_WORK__SEE_YOUR_HARDWARE_DOCUMENTATION._WINDOWS_IS_REMOVING_THIS_DEVICE."></span>

<span id="System_failure__Try_changing_the_driver_for_this_device._If_that_does_not_work__see_your_hardware_documentation._Windows_is_removing_this_device."></span><span id="system_failure__try_changing_the_driver_for_this_device._if_that_does_not_work__see_your_hardware_documentation._windows_is_removing_this_device."></span><span id="SYSTEM_FAILURE__TRY_CHANGING_THE_DRIVER_FOR_THIS_DEVICE._IF_THAT_DOES_NOT_WORK__SEE_YOUR_HARDWARE_DOCUMENTATION._WINDOWS_IS_REMOVING_THIS_DEVICE."></span>**System failure: Try changing the driver for this device. If that does not work, see your hardware documentation. Windows is removing this device.** (21)


</dt> <dd>

System failure. If changing the device driver is ineffective, see the hardware documentation. Windows is removing the device.

</dd> <dt>

<span id="This_device_is_disabled."></span><span id="this_device_is_disabled."></span><span id="THIS_DEVICE_IS_DISABLED."></span>

<span id="this_device_is_disabled."></span><span id="THIS_DEVICE_IS_DISABLED."></span>**This device is disabled.** (22)


</dt> <dd>

Device is disabled.

</dd> <dt>

<span id="System_failure__Try_changing_the_driver_for_this_device._If_that_doesn_t_work__see_your_hardware_documentation."></span><span id="system_failure__try_changing_the_driver_for_this_device._if_that_doesn_t_work__see_your_hardware_documentation."></span><span id="SYSTEM_FAILURE__TRY_CHANGING_THE_DRIVER_FOR_THIS_DEVICE._IF_THAT_DOESN_T_WORK__SEE_YOUR_HARDWARE_DOCUMENTATION."></span>

<span id="System_failure__Try_changing_the_driver_for_this_device._If_that_doesn_t_work__see_your_hardware_documentation."></span><span id="system_failure__try_changing_the_driver_for_this_device._if_that_doesn_t_work__see_your_hardware_documentation."></span><span id="SYSTEM_FAILURE__TRY_CHANGING_THE_DRIVER_FOR_THIS_DEVICE._IF_THAT_DOESN_T_WORK__SEE_YOUR_HARDWARE_DOCUMENTATION."></span>**System failure: Try changing the driver for this device. If that doesn't work, see your hardware documentation.** (23)


</dt> <dd>

System failure. If changing the device driver is ineffective, see the hardware documentation.

</dd> <dt>

<span id="This_device_is_not_present__is_not_working_properly__or_does_not_have_all_its_drivers_installed."></span><span id="this_device_is_not_present__is_not_working_properly__or_does_not_have_all_its_drivers_installed."></span><span id="THIS_DEVICE_IS_NOT_PRESENT__IS_NOT_WORKING_PROPERLY__OR_DOES_NOT_HAVE_ALL_ITS_DRIVERS_INSTALLED."></span>

<span id="this_device_is_not_present__is_not_working_properly__or_does_not_have_all_its_drivers_installed."></span><span id="THIS_DEVICE_IS_NOT_PRESENT__IS_NOT_WORKING_PROPERLY__OR_DOES_NOT_HAVE_ALL_ITS_DRIVERS_INSTALLED."></span>**This device is not present, is not working properly, or does not have all its drivers installed.** (24)


</dt> <dd>

Device is not present, not working properly, or does not have all of its drivers installed.

</dd> <dt>

<span id="Windows_is_still_setting_up_this_device."></span><span id="windows_is_still_setting_up_this_device."></span><span id="WINDOWS_IS_STILL_SETTING_UP_THIS_DEVICE."></span>

<span id="windows_is_still_setting_up_this_device."></span><span id="WINDOWS_IS_STILL_SETTING_UP_THIS_DEVICE."></span>**Windows is still setting up this device.** (25)


</dt> <dd>

Windows is still setting up the device.

</dd> <dt>

<span id="Windows_is_still_setting_up_this_device."></span><span id="windows_is_still_setting_up_this_device."></span><span id="WINDOWS_IS_STILL_SETTING_UP_THIS_DEVICE."></span>

<span id="windows_is_still_setting_up_this_device."></span><span id="WINDOWS_IS_STILL_SETTING_UP_THIS_DEVICE."></span>**Windows is still setting up this device.** (26)


</dt> <dd>

Windows is still setting up the device.

</dd> <dt>

<span id="This_device_does_not_have_valid_log_configuration."></span><span id="this_device_does_not_have_valid_log_configuration."></span><span id="THIS_DEVICE_DOES_NOT_HAVE_VALID_LOG_CONFIGURATION."></span>

<span id="this_device_does_not_have_valid_log_configuration."></span><span id="THIS_DEVICE_DOES_NOT_HAVE_VALID_LOG_CONFIGURATION."></span>**This device does not have valid log configuration.** (27)


</dt> <dd>

Device does not have valid log configuration.

</dd> <dt>

<span id="The_drivers_for_this_device_are_not_installed."></span><span id="the_drivers_for_this_device_are_not_installed."></span><span id="THE_DRIVERS_FOR_THIS_DEVICE_ARE_NOT_INSTALLED."></span>

<span id="the_drivers_for_this_device_are_not_installed."></span><span id="THE_DRIVERS_FOR_THIS_DEVICE_ARE_NOT_INSTALLED."></span>**The drivers for this device are not installed.** (28)


</dt> <dd>

Device drivers are not installed.

</dd> <dt>

<span id="This_device_is_disabled_because_the_firmware_of_the_device_did_not_give_it_the_required_resources."></span><span id="this_device_is_disabled_because_the_firmware_of_the_device_did_not_give_it_the_required_resources."></span><span id="THIS_DEVICE_IS_DISABLED_BECAUSE_THE_FIRMWARE_OF_THE_DEVICE_DID_NOT_GIVE_IT_THE_REQUIRED_RESOURCES."></span>

<span id="this_device_is_disabled_because_the_firmware_of_the_device_did_not_give_it_the_required_resources."></span><span id="THIS_DEVICE_IS_DISABLED_BECAUSE_THE_FIRMWARE_OF_THE_DEVICE_DID_NOT_GIVE_IT_THE_REQUIRED_RESOURCES."></span>**This device is disabled because the firmware of the device did not give it the required resources.** (29)


</dt> <dd>

Device is disabled. The device firmware did not provide the required resources.

</dd> <dt>

<span id="This_device_is_using_an_Interrupt_Request__IRQ__resource_that_another_device_is_using."></span><span id="this_device_is_using_an_interrupt_request__irq__resource_that_another_device_is_using."></span><span id="THIS_DEVICE_IS_USING_AN_INTERRUPT_REQUEST__IRQ__RESOURCE_THAT_ANOTHER_DEVICE_IS_USING."></span>

<span id="this_device_is_using_an_interrupt_request__irq__resource_that_another_device_is_using."></span><span id="THIS_DEVICE_IS_USING_AN_INTERRUPT_REQUEST__IRQ__RESOURCE_THAT_ANOTHER_DEVICE_IS_USING."></span>**This device is using an Interrupt Request (IRQ) resource that another device is using.** (30)


</dt> <dd>

Device is using an IRQ resource that another device is using.

</dd> <dt>

<span id="This_device_is_not_working_properly_because_Windows_cannot_load_the_drivers_required_for_this_device."></span><span id="this_device_is_not_working_properly_because_windows_cannot_load_the_drivers_required_for_this_device."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_WINDOWS_CANNOT_LOAD_THE_DRIVERS_REQUIRED_FOR_THIS_DEVICE."></span>

<span id="this_device_is_not_working_properly_because_windows_cannot_load_the_drivers_required_for_this_device."></span><span id="THIS_DEVICE_IS_NOT_WORKING_PROPERLY_BECAUSE_WINDOWS_CANNOT_LOAD_THE_DRIVERS_REQUIRED_FOR_THIS_DEVICE."></span>**This device is not working properly because Windows cannot load the drivers required for this device.** (31)


</dt> <dd>

Device is not working properly. Windows cannot load the required device drivers.

</dd> </dl>

</dd> <dt>

**ConfigManagerUserConfig**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](../wmisdk/standard-qualifiers.md) ("Win32")
</dt> </dl>

If **TRUE**, the device is using a user-defined configuration.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, this property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**CurrentBitsPerPixel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.12"), [**Units**](../wmisdk/standard-qualifiers.md) ("bits")
</dt> </dl>

Number of bits used to display each pixel.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentHorizontalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.11"), [**Units**](../wmisdk/standard-qualifiers.md) ("pixels")
</dt> </dl>

Current number of horizontal pixels.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentNumberOfColors**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of colors supported at the current resolution.

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentNumberOfColumns**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.14")
</dt> </dl>

Number of columns for this video controller (if in character mode). Otherwise, enter 0 (zero).

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentNumberOfRows**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.13")
</dt> </dl>

Number of rows for this video controller (if in character mode). Otherwise, enter 0 (zero).

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentRefreshRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("CurrentRefreshRate"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|HardwareInformation."), [**Units**](../wmisdk/standard-qualifiers.md) ("hertz")
</dt> </dl>

Frequency at which the video controller refreshes the image for the monitor. A value of 0 (zero) indicates the default rate is being used, while 0xFFFFFFFF indicates the optimal rate is being used.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**CurrentScanMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.8")
</dt> </dl>

Current scan mode.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Interlaced"></span><span id="interlaced"></span><span id="INTERLACED"></span>

<span id="Interlaced"></span><span id="interlaced"></span><span id="INTERLACED"></span>**Interlaced** (3)


</dt> <dd></dd> <dt>

<span id="Non_Interlaced"></span><span id="non_interlaced"></span><span id="NON_INTERLACED"></span>

<span id="Non_Interlaced"></span><span id="non_interlaced"></span><span id="NON_INTERLACED"></span>**Non Interlaced** (4)


</dt> <dd>

Noninterlaced

</dd> </dl>

</dd> <dt>

**CurrentVerticalResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.10"), [**Units**](../wmisdk/standard-qualifiers.md) ("pixels")
</dt> </dl>

Current number of vertical pixels.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Description")
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("DeviceId"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

Identifier (unique to the computer system) for this video controller.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**DeviceSpecificPens**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps)")
</dt> </dl>

Current number of device-specific pens. A value of 0xffff means that the device does not support pens.

Example: 3

</dd> <dt>

**DitherType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|EnumDisplaySettings")
</dt> </dl>

Dither type of the video controller. The property can be one of the predefined values, or a driver-defined value greater than or equal to 256. If line art dithering is chosen, the controller uses a dithering method that produces well-defined borders between black, white, and gray scalings. Line art dithering is not suitable for images that include continuous graduations in intensity and hue such as scanned photographs.

<dt>

<span id="No_dithering"></span><span id="no_dithering"></span><span id="NO_DITHERING"></span>

**No dithering** (1)


</dt> <dd></dd> <dt>

<span id="Dithering_with_a_coarse_brush"></span><span id="dithering_with_a_coarse_brush"></span><span id="DITHERING_WITH_A_COARSE_BRUSH"></span>

**Dithering with a coarse brush** (2)


</dt> <dd></dd> <dt>

<span id="Dithering_with_a_fine_brush"></span><span id="dithering_with_a_fine_brush"></span><span id="DITHERING_WITH_A_FINE_BRUSH"></span>

**Dithering with a fine brush** (3)


</dt> <dd></dd> <dt>

<span id="Line_art_dithering"></span><span id="line_art_dithering"></span><span id="LINE_ART_DITHERING"></span>

**Line art dithering** (4)


</dt> <dd></dd> <dt>

<span id="Device_does_gray_scaling"></span><span id="device_does_gray_scaling"></span><span id="DEVICE_DOES_GRAY_SCALING"></span>

**Device does gray scaling** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**DriverDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\")
</dt> </dl>

Last modification date and time of the currently installed video driver.

</dd> <dt>

**DriverVersion**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|File Installation Library Functions\|GetFileVersionInfo")
</dt> </dl>

Version number of the video driver.

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the error reported in **LastErrorCode** property is now cleared.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string supplying more information about the error recorded in **LastErrorCode** property, and information on any corrective actions that may be taken.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ICMIntent**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Printing and Print Spooler Structures\|DevMode\|dmICMIntent")
</dt> </dl>

Specific value of one of the three possible color-matching methods or intents that should be used by default. This property is used primarily for non-ICM applications. ICM applications establish intents by using the ICM functions. This property can be a predefined value or a driver defined value greater than or equal to 256. Color matching based on saturation is the most appropriate choice for business graphs when dithering is not desired. Color matching based on contrast is the most appropriate choice for scanned or photographic images when dithering is desired. Color matching optimized to match the exact color requested is most appropriate for use with business logos or other images when an exact color match is desired.

<dt>

<span id="Saturation"></span><span id="saturation"></span><span id="SATURATION"></span>

**Saturation** (1)


</dt> <dd></dd> <dt>

<span id="Contrast"></span><span id="contrast"></span><span id="CONTRAST"></span>

**Contrast** (2)


</dt> <dd></dd> <dt>

<span id="Exact_Color"></span><span id="exact_color"></span><span id="EXACT_COLOR"></span>

**Exact Color** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**ICMMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Printing and Print Spooler Structures\|DevMode\|dmICMMethod")
</dt> </dl>

Method of handling ICM. For non-ICM applications, this property determines if ICM is enabled. For ICM applications, the system examines this property to determine how to handle ICM support. This property can be a predefined value or a driver-defined value greater than or equal to 256. The value determines which system handles image color matching.

<dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (1)


</dt> <dd></dd> <dt>

<span id="Windows"></span><span id="windows"></span><span id="WINDOWS"></span>

**Windows** (2)


</dt> <dd></dd> <dt>

<span id="Device_Driver"></span><span id="device_driver"></span><span id="DEVICE_DRIVER"></span>

**Device Driver** (3)


</dt> <dd></dd> <dt>

<span id="Destination_Device"></span><span id="destination_device"></span><span id="DESTINATION_DEVICE"></span>

**Destination Device** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**InfFilename**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\\\0000")
</dt> </dl>

Path to the video adapter's .inf file.

Example: "C:\\Windows\\SYSTEM32\\DRIVERS"

</dd> <dt>

**InfSection**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|SYSTEM\\\\CurrentControlSet\\\\Control\\\\Class\\\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\\\0000")
</dt> </dl>

Section of the .inf file where the Windows video information resides.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstalledDisplayDrivers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|System\\\\CurrentControlSet\\\\Services\\\\Class\\\\")
</dt> </dl>

Name of the installed display device driver.

</dd> <dt>

**LastErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Last error code reported by the logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**MaxMemorySupported**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("bytes")
</dt> </dl>

Maximum amount of memory supported in bytes.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**MaxNumberControlled**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Bus Port\|001.9")
</dt> </dl>

Maximum number of directly addressable entities supportable by this controller. A value of 0 (zero) should be used if the number is unknown.

This property is inherited from [**CIM\_Controller**](cim-controller.md).

</dd> <dt>

**MaxRefreshRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.5"), [**Units**](../wmisdk/standard-qualifiers.md) ("hertz")
</dt> </dl>

Maximum refresh rate of the video controller in hertz.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**MinRefreshRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.4"), [**Units**](../wmisdk/standard-qualifiers.md) ("hertz")
</dt> </dl>

Minimum refresh rate of the video controller in hertz.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**Monochrome**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("WMI")
</dt> </dl>

If **TRUE**, gray scale is used to display images.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**NumberOfColorPlanes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current number of color planes. If this value is not applicable for the current video configuration, enter 0 (zero).

This property is inherited from [**CIM\_PCVideoController**](cim-pcvideocontroller.md).

</dd> <dt>

**NumberOfVideoPages**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of video pages supported given the current resolutions and available memory.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](../wmisdk/standard-qualifiers.md) ("Win32")
</dt> </dl>

Windows Plug and Play device identifier of the logical device.

Example: "\*PNP030b"

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the specific power-related capabilities of a logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>

<span id="Not_Supported"></span><span id="not_supported"></span><span id="NOT_SUPPORTED"></span>**Not Supported** (1)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>**Disabled** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>**Enabled** (3)


</dt> <dd>

The power management features are currently enabled but the exact feature set is unknown or the information is unavailable.

</dd> <dt>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>

<span id="Power_Saving_Modes_Entered_Automatically"></span><span id="power_saving_modes_entered_automatically"></span><span id="POWER_SAVING_MODES_ENTERED_AUTOMATICALLY"></span>**Power Saving Modes Entered Automatically** (4)


</dt> <dd>

The device can change its power state based on usage or other criteria.

</dd> <dt>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>

<span id="Power_State_Settable"></span><span id="power_state_settable"></span><span id="POWER_STATE_SETTABLE"></span>**Power State Settable** (5)


</dt> <dd>

The [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method is supported. This method is found on the parent [**CIM\_LogicalDevice**](cim-logicaldevice.md) class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](../wmisdk/designing-managed-object-format--mof--classes.md).

</dd> <dt>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>

<span id="Power_Cycling_Supported"></span><span id="power_cycling_supported"></span><span id="POWER_CYCLING_SUPPORTED"></span>**Power Cycling Supported** (6)


</dt> <dd>

The [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle).

</dd> <dt>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>

<span id="Timed_Power_On_Supported"></span><span id="timed_power_on_supported"></span><span id="TIMED_POWER_ON_SUPPORTED"></span>**Timed Power On Supported** (7)


</dt> <dd>

Timed Power-On Supported

The [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method can be invoked with the *PowerState* parameter set to 5 (Power Cycle) and *Time* set to a specific date and time, or interval, for power-on.

</dd> </dl>

</dd> <dt>

**PowerManagementSupported**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **TRUE**, the device can be power-managed (can be put into suspend mode, and so on). The property does not indicate that power management features are currently enabled, only that the logical device is capable of power management.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ProtocolSupported**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Bus Port\|001.2", "MIF.DMTF\|Disks\|003.3")
</dt> </dl>

Protocol used by the controller to access "controlled" devices.

This property is inherited from [**CIM\_Controller**](cim-controller.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="EISA"></span><span id="eisa"></span>

<span id="EISA"></span><span id="eisa"></span>**EISA** (3)


</dt> <dd></dd> <dt>

<span id="ISA"></span><span id="isa"></span>

<span id="ISA"></span><span id="isa"></span>**ISA** (4)


</dt> <dd></dd> <dt>

<span id="PCI"></span><span id="pci"></span>

<span id="PCI"></span><span id="pci"></span>**PCI** (5)


</dt> <dd></dd> <dt>

<span id="ATA_ATAPI"></span><span id="ata_atapi"></span>

<span id="ATA_ATAPI"></span><span id="ata_atapi"></span>**ATA/ATAPI** (6)


</dt> <dd>

ATA or ATAPI

</dd> <dt>

<span id="Flexible_Diskette"></span><span id="flexible_diskette"></span><span id="FLEXIBLE_DISKETTE"></span>

<span id="Flexible_Diskette"></span><span id="flexible_diskette"></span><span id="FLEXIBLE_DISKETTE"></span>**Flexible Diskette** (7)


</dt> <dd></dd> <dt>

<span id="1496"></span>

<span id="1496"></span>**1496** (8)


</dt> <dd></dd> <dt>

<span id="SCSI_Parallel_Interface"></span><span id="scsi_parallel_interface"></span><span id="SCSI_PARALLEL_INTERFACE"></span>

<span id="SCSI_Parallel_Interface"></span><span id="scsi_parallel_interface"></span><span id="SCSI_PARALLEL_INTERFACE"></span>**SCSI Parallel Interface** (9)


</dt> <dd></dd> <dt>

<span id="SCSI_Fibre_Channel_Protocol"></span><span id="scsi_fibre_channel_protocol"></span><span id="SCSI_FIBRE_CHANNEL_PROTOCOL"></span>

<span id="SCSI_Fibre_Channel_Protocol"></span><span id="scsi_fibre_channel_protocol"></span><span id="SCSI_FIBRE_CHANNEL_PROTOCOL"></span>**SCSI Fibre Channel Protocol** (10)


</dt> <dd></dd> <dt>

<span id="SCSI_Serial_Bus_Protocol"></span><span id="scsi_serial_bus_protocol"></span><span id="SCSI_SERIAL_BUS_PROTOCOL"></span>

<span id="SCSI_Serial_Bus_Protocol"></span><span id="scsi_serial_bus_protocol"></span><span id="SCSI_SERIAL_BUS_PROTOCOL"></span>**SCSI Serial Bus Protocol** (11)


</dt> <dd></dd> <dt>

<span id="SCSI_Serial_Bus_Protocol-2__1394_"></span><span id="scsi_serial_bus_protocol-2__1394_"></span><span id="SCSI_SERIAL_BUS_PROTOCOL-2__1394_"></span>

<span id="SCSI_Serial_Bus_Protocol-2__1394_"></span><span id="scsi_serial_bus_protocol-2__1394_"></span><span id="SCSI_SERIAL_BUS_PROTOCOL-2__1394_"></span>**SCSI Serial Bus Protocol-2 (1394)** (12)


</dt> <dd></dd> <dt>

<span id="SCSI_Serial_Storage_Architecture"></span><span id="scsi_serial_storage_architecture"></span><span id="SCSI_SERIAL_STORAGE_ARCHITECTURE"></span>

<span id="SCSI_Serial_Storage_Architecture"></span><span id="scsi_serial_storage_architecture"></span><span id="SCSI_SERIAL_STORAGE_ARCHITECTURE"></span>**SCSI Serial Storage Architecture** (13)


</dt> <dd></dd> <dt>

<span id="VESA"></span><span id="vesa"></span>

<span id="VESA"></span><span id="vesa"></span>**VESA** (14)


</dt> <dd></dd> <dt>

<span id="PCMCIA"></span><span id="pcmcia"></span>

<span id="PCMCIA"></span><span id="pcmcia"></span>**PCMCIA** (15)


</dt> <dd></dd> <dt>

<span id="Universal_Serial_Bus"></span><span id="universal_serial_bus"></span><span id="UNIVERSAL_SERIAL_BUS"></span>

<span id="Universal_Serial_Bus"></span><span id="universal_serial_bus"></span><span id="UNIVERSAL_SERIAL_BUS"></span>**Universal Serial Bus** (16)


</dt> <dd></dd> <dt>

<span id="Parallel_Protocol"></span><span id="parallel_protocol"></span><span id="PARALLEL_PROTOCOL"></span>

<span id="Parallel_Protocol"></span><span id="parallel_protocol"></span><span id="PARALLEL_PROTOCOL"></span>**Parallel Protocol** (17)


</dt> <dd></dd> <dt>

<span id="ESCON"></span><span id="escon"></span>

<span id="ESCON"></span><span id="escon"></span>**ESCON** (18)


</dt> <dd></dd> <dt>

<span id="Diagnostic"></span><span id="diagnostic"></span><span id="DIAGNOSTIC"></span>

<span id="Diagnostic"></span><span id="diagnostic"></span><span id="DIAGNOSTIC"></span>**Diagnostic** (19)


</dt> <dd></dd> <dt>

<span id="I2C"></span><span id="i2c"></span>

<span id="I2C"></span><span id="i2c"></span>**I2C** (20)


</dt> <dd></dd> <dt>

<span id="Power"></span><span id="power"></span><span id="POWER"></span>

<span id="Power"></span><span id="power"></span><span id="POWER"></span>**Power** (21)


</dt> <dd></dd> <dt>

<span id="HIPPI"></span><span id="hippi"></span>

<span id="HIPPI"></span><span id="hippi"></span>**HIPPI** (22)


</dt> <dd></dd> <dt>

<span id="MultiBus"></span><span id="multibus"></span><span id="MULTIBUS"></span>

<span id="MultiBus"></span><span id="multibus"></span><span id="MULTIBUS"></span>**MultiBus** (23)


</dt> <dd></dd> <dt>

<span id="VME"></span><span id="vme"></span>

<span id="VME"></span><span id="vme"></span>**VME** (24)


</dt> <dd></dd> <dt>

<span id="IPI"></span><span id="ipi"></span>

<span id="IPI"></span><span id="ipi"></span>**IPI** (25)


</dt> <dd></dd> <dt>

<span id="IEEE-488"></span><span id="ieee-488"></span>

<span id="IEEE-488"></span><span id="ieee-488"></span>**IEEE-488** (26)


</dt> <dd></dd> <dt>

<span id="RS232"></span><span id="rs232"></span>

<span id="RS232"></span><span id="rs232"></span>**RS232** (27)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3_10BASE5"></span><span id="ieee_802.3_10base5"></span>

<span id="ieee_802.3_10base5"></span>**IEEE 802.3 10BASE5** (28)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3_10BASE2"></span><span id="ieee_802.3_10base2"></span>

<span id="ieee_802.3_10base2"></span>**IEEE 802.3 10BASE2** (29)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3_1BASE5"></span><span id="ieee_802.3_1base5"></span>

<span id="ieee_802.3_1base5"></span>**IEEE 802.3 1BASE5** (30)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3_10BROAD36"></span><span id="ieee_802.3_10broad36"></span>

<span id="ieee_802.3_10broad36"></span>**IEEE 802.3 10BROAD36** (31)


</dt> <dd></dd> <dt>

<span id="IEEE_802.3_100BASEVG"></span><span id="ieee_802.3_100basevg"></span>

<span id="ieee_802.3_100basevg"></span>**IEEE 802.3 100BASEVG** (32)


</dt> <dd></dd> <dt>

<span id="IEEE_802.5_Token-Ring"></span><span id="ieee_802.5_token-ring"></span><span id="IEEE_802.5_TOKEN-RING"></span>

<span id="IEEE_802.5_Token-Ring"></span><span id="ieee_802.5_token-ring"></span><span id="IEEE_802.5_TOKEN-RING"></span>**IEEE 802.5 Token-Ring** (33)


</dt> <dd></dd> <dt>

<span id="ANSI_X3T9.5_FDDI"></span><span id="ansi_x3t9.5_fddi"></span>

<span id="ansi_x3t9.5_fddi"></span>**ANSI X3T9.5 FDDI** (34)


</dt> <dd></dd> <dt>

<span id="MCA"></span><span id="mca"></span>

<span id="MCA"></span><span id="mca"></span>**MCA** (35)


</dt> <dd></dd> <dt>

<span id="ESDI"></span><span id="esdi"></span>

<span id="ESDI"></span><span id="esdi"></span>**ESDI** (36)


</dt> <dd></dd> <dt>

<span id="IDE"></span><span id="ide"></span>

<span id="IDE"></span><span id="ide"></span>**IDE** (37)


</dt> <dd></dd> <dt>

<span id="CMD"></span><span id="cmd"></span>

<span id="CMD"></span><span id="cmd"></span>**CMD** (38)


</dt> <dd></dd> <dt>

<span id="ST506"></span><span id="st506"></span>

<span id="ST506"></span><span id="st506"></span>**ST506** (39)


</dt> <dd></dd> <dt>

<span id="DSSI"></span><span id="dssi"></span>

<span id="DSSI"></span><span id="dssi"></span>**DSSI** (40)


</dt> <dd></dd> <dt>

<span id="QIC2"></span><span id="qic2"></span>

<span id="QIC2"></span><span id="qic2"></span>**QIC2** (41)


</dt> <dd></dd> <dt>

<span id="Enhanced_ATA_IDE"></span><span id="enhanced_ata_ide"></span><span id="ENHANCED_ATA_IDE"></span>

<span id="Enhanced_ATA_IDE"></span><span id="enhanced_ata_ide"></span><span id="ENHANCED_ATA_IDE"></span>**Enhanced ATA/IDE** (42)


</dt> <dd></dd> <dt>

<span id="AGP"></span><span id="agp"></span>

<span id="AGP"></span><span id="agp"></span>**AGP** (43)


</dt> <dd></dd> <dt>

<span id="TWIRP__two-way_infrared_"></span><span id="twirp__two-way_infrared_"></span><span id="TWIRP__TWO-WAY_INFRARED_"></span>

<span id="TWIRP__two-way_infrared_"></span><span id="twirp__two-way_infrared_"></span><span id="TWIRP__TWO-WAY_INFRARED_"></span>**TWIRP (two-way infrared)** (44)


</dt> <dd></dd> <dt>

<span id="FIR__fast_infrared_"></span><span id="fir__fast_infrared_"></span><span id="FIR__FAST_INFRARED_"></span>

<span id="FIR__fast_infrared_"></span><span id="fir__fast_infrared_"></span><span id="FIR__FAST_INFRARED_"></span>**FIR (fast infrared)** (45)


</dt> <dd></dd> <dt>

<span id="SIR__serial_infrared_"></span><span id="sir__serial_infrared_"></span><span id="SIR__SERIAL_INFRARED_"></span>

<span id="SIR__serial_infrared_"></span><span id="sir__serial_infrared_"></span><span id="SIR__SERIAL_INFRARED_"></span>**SIR (serial infrared)** (46)


</dt> <dd></dd> <dt>

<span id="IrBus"></span><span id="irbus"></span><span id="IRBUS"></span>

<span id="IrBus"></span><span id="irbus"></span><span id="IRBUS"></span>**IrBus** (47)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReservedSystemPaletteEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps)")
</dt> </dl>

Number of reserved entries in the system palette. The operating system may reserve entries to support standard colors for task bars and other desktop display items. This index is valid only if the device driver sets the **RC\_PALETTE** bit in the RASTERCAPS index, and is available only if the driver is compatible with 16-bit Windows. If the system is not using a palette, **ReservedSystemPaletteEntries** is not set.

Example: 20

</dd> <dt>

**SpecificationVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Printing and Print Spooler Structures\|DevMode\|dmSpecVersion")
</dt> </dl>

Version number of the initialization data specification (upon which the structure is based).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](../wmisdk/standard-qualifiers.md) (10), [**DisplayName**](../wmisdk/standard-qualifiers.md) ("Status")
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

Values include the following:

<dt>

<span id="OK"></span><span id="ok"></span>

**OK** ("OK")


</dt> <dd></dd> <dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** ("Error")


</dt> <dd></dd> <dt>

<span id="Degraded"></span><span id="degraded"></span><span id="DEGRADED"></span>

**Degraded** ("Degraded")


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** ("Unknown")


</dt> <dd></dd> <dt>

<span id="Pred_Fail"></span><span id="pred_fail"></span><span id="PRED_FAIL"></span>

**Pred Fail** ("Pred Fail")


</dt> <dd></dd> <dt>

<span id="Starting"></span><span id="starting"></span><span id="STARTING"></span>

**Starting** ("Starting")


</dt> <dd></dd> <dt>

<span id="Stopping"></span><span id="stopping"></span><span id="STOPPING"></span>

**Stopping** ("Stopping")


</dt> <dd></dd> <dt>

<span id="Service"></span><span id="service"></span><span id="SERVICE"></span>

**Service** ("Service")


</dt> <dd></dd> <dt>

<span id="Stressed"></span><span id="stressed"></span><span id="STRESSED"></span>

**Stressed** ("Stressed")


</dt> <dd></dd> <dt>

<span id="NonRecover"></span><span id="nonrecover"></span><span id="NONRECOVER"></span>

**NonRecover** ("NonRecover")


</dt> <dd></dd> <dt>

<span id="No_Contact"></span><span id="no_contact"></span><span id="NO_CONTACT"></span>

**No Contact** ("No Contact")


</dt> <dd></dd> <dt>

<span id="Lost_Comm"></span><span id="lost_comm"></span><span id="LOST_COMM"></span>

**Lost Comm** ("Lost Comm")


</dt> <dd></dd> </dl>

</dd> <dt>

**StatusInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Operational State\|003.3")
</dt> </dl>

State of the logical device. If this property does not apply to the logical device, the value 5 (Not Applicable) should be used.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** (3)


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** (4)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

**Not Applicable** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

Value of the scoping computer's **CreationClassName** property.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](../wmisdk/standard-qualifiers.md) ("[**CIM\_System**](cim-system.md).**Name**"), [**CIM\_Key**](../wmisdk/standard-wmi-qualifiers.md)
</dt> </dl>

Name of the scoping system.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**SystemPaletteEntries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps)")
</dt> </dl>

Current number of color index entries in the system palette. This index is valid only if the device driver sets the **RC\_PALETTE** bit in the RASTERCAPS index, and is available only if the driver is compatible with 16-bit Windows. If the system is not using a palette, **SystemPaletteEntries** is not set.

Example: 20

</dd> <dt>

**TimeOfLastReset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time this controller was last reset. This could mean the controller was powered down or reinitialized.

This property is inherited from [**CIM\_Controller**](cim-controller.md).

</dd> <dt>

**VideoArchitecture**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.2")
</dt> </dl>

Type of video architecture.

This property is inherited from [**CIM\_PCVideoController**](cim-pcvideocontroller.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="CGA"></span><span id="cga"></span>

**CGA** (3)


</dt> <dd></dd> <dt>

<span id="EGA"></span><span id="ega"></span>

**EGA** (4)


</dt> <dd></dd> <dt>

<span id="VGA"></span><span id="vga"></span>

**VGA** (5)


</dt> <dd></dd> <dt>

<span id="SVGA"></span><span id="svga"></span>

**SVGA** (6)


</dt> <dd></dd> <dt>

<span id="MDA"></span><span id="mda"></span>

**MDA** (7)


</dt> <dd></dd> <dt>

<span id="HGC"></span><span id="hgc"></span>

**HGC** (8)


</dt> <dd></dd> <dt>

<span id="MCGA"></span><span id="mcga"></span>

**MCGA** (9)


</dt> <dd></dd> <dt>

<span id="8514A"></span><span id="8514a"></span>

**8514A** (10)


</dt> <dd></dd> <dt>

<span id="XGA"></span><span id="xga"></span>

**XGA** (11)


</dt> <dd></dd> <dt>

<span id="Linear_Frame_Buffer"></span><span id="linear_frame_buffer"></span><span id="LINEAR_FRAME_BUFFER"></span>

**Linear Frame Buffer** (12)


</dt> <dd></dd> <dt>

<span id="PC-98"></span><span id="pc-98"></span>

**PC-98** (160)


</dt> <dd></dd> </dl>

</dd> <dt>

**VideoMemoryType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.6")
</dt> </dl>

Type of video memory.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="VRAM"></span><span id="vram"></span>

**VRAM** (3)


</dt> <dd></dd> <dt>

<span id="DRAM"></span><span id="dram"></span>

**DRAM** (4)


</dt> <dd></dd> <dt>

<span id="SRAM"></span><span id="sram"></span>

**SRAM** (5)


</dt> <dd></dd> <dt>

<span id="WRAM"></span><span id="wram"></span>

**WRAM** (6)


</dt> <dd></dd> <dt>

<span id="EDO_RAM"></span><span id="edo_ram"></span>

**EDO RAM** (7)


</dt> <dd></dd> <dt>

<span id="Burst_Synchronous_DRAM"></span><span id="burst_synchronous_dram"></span><span id="BURST_SYNCHRONOUS_DRAM"></span>

**Burst Synchronous DRAM** (8)


</dt> <dd></dd> <dt>

<span id="Pipelined_Burst_SRAM"></span><span id="pipelined_burst_sram"></span><span id="PIPELINED_BURST_SRAM"></span>

**Pipelined Burst SRAM** (9)


</dt> <dd></dd> <dt>

<span id="CDRAM"></span><span id="cdram"></span>

**CDRAM** (10)


</dt> <dd></dd> <dt>

<span id="3DRAM"></span><span id="3dram"></span>

**3DRAM** (11)


</dt> <dd></dd> <dt>

<span id="SDRAM"></span><span id="sdram"></span>

**SDRAM** (12)


</dt> <dd></dd> <dt>

<span id="SGRAM"></span><span id="sgram"></span>

**SGRAM** (13)


</dt> <dd></dd> </dl>

</dd> <dt>

**VideoMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("MIF.DMTF\|Video\|003.3")
</dt> </dl>

Current video mode.

This property is inherited from [**CIM\_PCVideoController**](cim-pcvideocontroller.md).

</dd> <dt>

**VideoModeDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Device Context Functions\|[**GetDeviceCaps**](/windows/win32/api/wingdi/nf-wingdi-getdevicecaps)")
</dt> </dl>

Current resolution, color, and scan mode settings of the video controller.

Example: "1024 x 768 x 256 colors"

</dd> <dt>

**VideoProcessor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string describing the video processor.

This property is inherited from [**CIM\_VideoController**](cim-videocontroller.md).

</dd> </dl>

## Remarks

The **Win32\_VideoController** class is derived from [**CIM\_PCVideoController**](cim-pcvideocontroller.md).

For more information about using this class, such as retrieving information from multiple monitors, see [Use PowerShell to Discover Multi-Monitor Information](https://devblogs.microsoft.com/scripting/use-powershell-to-discover-multi-monitor-information/).

## Examples

The [List Video Controller Properties](https://Gallery.TechNet.Microsoft.Com/6c1a585c-742f-4f51-bb57-23838e8f011f) VBScript sample lists the video controller properties.

The following PowerShell example lists the video controller properties.


```VB
$strComputer = "." 
 
$colItems = get-wmiobject -class "Win32_VideoController" -namespace "root\CIMV2" ` 
-computername $strComputer 
 
foreach ($objItem in $colItems) { 
      write-host "Accelerator Capabilities: " $objItem.AcceleratorCapabilities 
      write-host "Adapter Compatibility: " $objItem.AdapterCompatibility 
      write-host "Adapter DAC Type: " $objItem.AdapterDACType 
      write-host "Adapter RAM: " $objItem.AdapterRAM 
      write-host "Availability: " $objItem.Availability 
      write-host "Capability Descriptions: " $objItem.CapabilityDescriptions 
      write-host "Caption: " $objItem.Caption 
      write-host "Color Table Entries: " $objItem.ColorTableEntries 
      write-host "Configuration Manager Error Code: " $objItem.ConfigManagerErrorCode 
      write-host "Configuration Manager User Configuration: " $objItem.ConfigManagerUserConfig 
      write-host "Creation Class Name: " $objItem.CreationClassName 
      write-host "Current Bits Per Pixel: " $objItem.CurrentBitsPerPixel 
      write-host "Current Horizontal Resolution: " $objItem.CurrentHorizontalResolution 
      write-host "Current Number Of Colors: " $objItem.CurrentNumberOfColors 
      write-host "Current Number Of Columns: " $objItem.CurrentNumberOfColumns 
      write-host "Current Number Of Rows: " $objItem.CurrentNumberOfRows 
      write-host "Current Refresh Rate: " $objItem.CurrentRefreshRate 
      write-host "Current Scan Mode: " $objItem.CurrentScanMode 
      write-host "Current Vertical Resolution: " $objItem.CurrentVerticalResolution 
      write-host "Description: " $objItem.Description 
      write-host "Device ID: " $objItem.DeviceID 
      write-host "Device Specific Pens: " $objItem.DeviceSpecificPens 
      write-host "Dither Type: " $objItem.DitherType 
      write-host "Driver Date: " $objItem.DriverDate 
      write-host "Driver Version: " $objItem.DriverVersion 
      write-host "Error Cleared: " $objItem.ErrorCleared 
      write-host "Error Description: " $objItem.ErrorDescription 
      write-host "ICM Intent: " $objItem.ICMIntent 
      write-host "ICM Method: " $objItem.ICMMethod 
      write-host "Inf File Name: " $objItem.InfFilename 
      write-host "Inf Section: " $objItem.InfSection 
      write-host "Installation Date: " $objItem.InstallDate 
      write-host "Installed Display Drivers: " $objItem.InstalledDisplayDrivers 
      write-host "Last Error Code: " $objItem.LastErrorCode 
      write-host "Maximum Memory Supported: " $objItem.MaxMemorySupported 
      write-host "Maximum Number Controlled: " $objItem.MaxNumberControlled 
      write-host "Maximum Refresh Rate: " $objItem.MaxRefreshRate 
      write-host "Minimum Refresh Rate: " $objItem.MinRefreshRate 
      write-host "Monochrome: " $objItem.Monochrome 
      write-host "Name: " $objItem.Name 
      write-host "Number Of Color Planes: " $objItem.NumberOfColorPlanes 
      write-host "Number Of Video Pages: " $objItem.NumberOfVideoPages 
      write-host "PNP Device ID: " $objItem.PNPDeviceID 
      write-host "Power Management Capabilities: " $objItem.PowerManagementCapabilities 
      write-host "Power Management Supported: " $objItem.PowerManagementSupported 
      write-host "Protocol Supported: " $objItem.ProtocolSupported 
      write-host "Reserved System Palette Entries: " $objItem.ReservedSystemPaletteEntries 
      write-host "Specification Version: " $objItem.SpecificationVersion 
      write-host "Status: " $objItem.Status 
      write-host "Status Information: " $objItem.StatusInfo 
      write-host "System Creation Class Name: " $objItem.SystemCreationClassName 
      write-host "System Name: " $objItem.SystemName 
      write-host "System Palette Entries: " $objItem.SystemPaletteEntries 
      write-host "Time Of Last Reset: " $objItem.TimeOfLastReset 
      write-host "Video Architecture: " $objItem.VideoArchitecture 
      write-host "Video Memory Type: " $objItem.VideoMemoryType 
      write-host "Video Mode: " $objItem.VideoMode 
      write-host "Video Mode Description: " $objItem.VideoModeDescription 
      write-host "Video Processor: " $objItem.VideoProcessor 
      write-host 
} 
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_PCVideoController**](cim-pcvideocontroller.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
