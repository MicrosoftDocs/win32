---
description: The Win32\_CacheMemory&\#32;WMI class represents internal and external cache memory on a computer system.
ms.assetid: 9cfb992d-fbac-4e56-b4f3-61c0c93f5852
ms.tgt_platform: multiple
title: Win32_CacheMemory class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_CacheMemory
- Win32_CacheMemory.Reset
- Win32_CacheMemory.SetPowerState
- Win32_CacheMemory.Access
- Win32_CacheMemory.AdditionalErrorData
- Win32_CacheMemory.Associativity
- Win32_CacheMemory.Availability
- Win32_CacheMemory.BlockSize
- Win32_CacheMemory.CacheSpeed
- Win32_CacheMemory.CacheType
- Win32_CacheMemory.Caption
- Win32_CacheMemory.ConfigManagerErrorCode
- Win32_CacheMemory.ConfigManagerUserConfig
- Win32_CacheMemory.CorrectableError
- Win32_CacheMemory.CreationClassName
- Win32_CacheMemory.CurrentSRAM
- Win32_CacheMemory.Description
- Win32_CacheMemory.DeviceID
- Win32_CacheMemory.EndingAddress
- Win32_CacheMemory.ErrorAccess
- Win32_CacheMemory.ErrorAddress
- Win32_CacheMemory.ErrorCleared
- Win32_CacheMemory.ErrorCorrectType
- Win32_CacheMemory.ErrorData
- Win32_CacheMemory.ErrorDataOrder
- Win32_CacheMemory.ErrorDescription
- Win32_CacheMemory.ErrorInfo
- Win32_CacheMemory.ErrorMethodology
- Win32_CacheMemory.ErrorResolution
- Win32_CacheMemory.ErrorTime
- Win32_CacheMemory.ErrorTransferSize
- Win32_CacheMemory.FlushTimer
- Win32_CacheMemory.InstallDate
- Win32_CacheMemory.InstalledSize
- Win32_CacheMemory.LastErrorCode
- Win32_CacheMemory.Level
- Win32_CacheMemory.LineSize
- Win32_CacheMemory.Location
- Win32_CacheMemory.MaxCacheSize
- Win32_CacheMemory.Name
- Win32_CacheMemory.NumberOfBlocks
- Win32_CacheMemory.OtherErrorDescription
- Win32_CacheMemory.PNPDeviceID
- Win32_CacheMemory.PowerManagementCapabilities
- Win32_CacheMemory.PowerManagementSupported
- Win32_CacheMemory.Purpose
- Win32_CacheMemory.ReadPolicy
- Win32_CacheMemory.ReplacementPolicy
- Win32_CacheMemory.StartingAddress
- Win32_CacheMemory.Status
- Win32_CacheMemory.StatusInfo
- Win32_CacheMemory.SupportedSRAM
- Win32_CacheMemory.SystemCreationClassName
- Win32_CacheMemory.SystemLevelAddress
- Win32_CacheMemory.SystemName
- Win32_CacheMemory.WritePolicy
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_CacheMemory class

The **Win32\_CacheMemory** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents internal and external cache memory on a computer system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{FAF76B97-798C-11D2-AAD1-006008C78BC7}"), AMENDMENT]
class Win32_CacheMemory : CIM_CacheMemory
{
  uint16   Access;
  uint8    AdditionalErrorData[];
  uint16   Associativity;
  uint16   Availability;
  uint64   BlockSize;
  uint32   CacheSpeed;
  uint16   CacheType;
  string   Caption;
  uint32   ConfigManagerErrorCode;
  boolean  ConfigManagerUserConfig;
  boolean  CorrectableError;
  string   CreationClassName;
  uint16   CurrentSRAM[];
  string   Description;
  string   DeviceID;
  uint64   EndingAddress;
  uint16   ErrorAccess;
  uint64   ErrorAddress;
  boolean  ErrorCleared;
  uint16   ErrorCorrectType;
  uint8    ErrorData[];
  uint16   ErrorDataOrder;
  string   ErrorDescription;
  uint16   ErrorInfo;
  string   ErrorMethodology;
  uint64   ErrorResolution;
  datetime ErrorTime;
  uint32   ErrorTransferSize;
  uint32   FlushTimer;
  datetime InstallDate;
  uint32   InstalledSize;
  uint32   LastErrorCode;
  uint16   Level;
  uint32   LineSize;
  uint16   Location;
  uint32   MaxCacheSize;
  string   Name;
  uint64   NumberOfBlocks;
  string   OtherErrorDescription;
  string   PNPDeviceID;
  uint16   PowerManagementCapabilities[];
  boolean  PowerManagementSupported;
  string   Purpose;
  uint16   ReadPolicy;
  uint16   ReplacementPolicy;
  uint64   StartingAddress;
  string   Status;
  uint16   StatusInfo;
  uint16   SupportedSRAM[];
  string   SystemCreationClassName;
  boolean  SystemLevelAddress;
  string   SystemName;
  uint16   WritePolicy;
};
```

## Members

The **Win32\_CacheMemory** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_CacheMemory** class has these methods.



| Method            | Description                                                                                                                                                                                                  |
|:------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Reset**         | Not implemented. To implement this method, see the [**Reset**](reset-method-in-class-cim-controller.md) method in [**CIM\_CacheMemory**](cim-cachememory.md) for documentation.<br/>                 |
| **SetPowerState** | Not implemented. To implement this method, see the [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method in [**CIM\_CacheMemory**](cim-cachememory.md) for documentation.<br/> |



 

### Properties

The **Win32\_CacheMemory** class has these properties.

<dl> <dt>

**Access**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Type of access.

This property is inherited from [**CIM\_StorageExtent**](cim-storageextent.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>

<span id="Readable"></span><span id="readable"></span><span id="READABLE"></span>**Readable** (1)


</dt> <dd></dd> <dt>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>

<span id="Writeable"></span><span id="writeable"></span><span id="WRITEABLE"></span>**Writeable** (2)


</dt> <dd>

Writable

</dd> <dt>

<span id="Read_Write_Supported"></span><span id="read_write_supported"></span><span id="READ_WRITE_SUPPORTED"></span>

<span id="Read_Write_Supported"></span><span id="read_write_supported"></span><span id="READ_WRITE_SUPPORTED"></span>**Read/Write Supported** (3)


</dt> <dd></dd> <dt>

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>

<span id="Write_Once"></span><span id="write_once"></span><span id="WRITE_ONCE"></span>**Write Once** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**AdditionalErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.18", "MIF.DMTF\|Physical Memory Array\|001.13"), [**MAX**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Array of octets that hold additional error information. An example is ECC Syndrome or the return of the check bits if a CRC-based error methodology is used. In the latter case, if a single-bit error is recognized and the CRC algorithm is known, it is possible to determine the exact bit that failed. This type of data (ECC Syndrome, Check Bit, Parity Bit data, or other vendor supplied information) is included in this field. If the **ErrorInfo** property is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**Associativity**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.15")
</dt> </dl>

An integer enumeration that defines the system cache associativity.

This value comes from the **Associativity** member of the **Cache Information** structure in the SMBIOS information.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Direct_Mapped"></span><span id="direct_mapped"></span><span id="DIRECT_MAPPED"></span>

**Direct Mapped** (3)


</dt> <dd></dd> <dt>

<span id="2-way_Set-Associative"></span><span id="2-way_set-associative"></span><span id="2-WAY_SET-ASSOCIATIVE"></span>

**2-way Set-Associative** (4)


</dt> <dd></dd> <dt>

<span id="4-way_Set-Associative"></span><span id="4-way_set-associative"></span><span id="4-WAY_SET-ASSOCIATIVE"></span>

**4-way Set-Associative** (5)


</dt> <dd></dd> <dt>

<span id="Fully_Associative"></span><span id="fully_associative"></span><span id="FULLY_ASSOCIATIVE"></span>

**Fully Associative** (6)


</dt> <dd></dd> <dt>

<span id="8-way_Set-Associative"></span><span id="8-way_set-associative"></span><span id="8-WAY_SET-ASSOCIATIVE"></span>

**8-way Set-Associative** (7)


</dt> <dd></dd> <dt>

<span id="16-way_Set-Associative"></span><span id="16-way_set-associative"></span><span id="16-WAY_SET-ASSOCIATIVE"></span>

**16-way Set-Associative** (8)


</dt> <dd></dd> </dl>

</dd> <dt>

**Availability**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Operational State\|003.5", "MIB.IETF\|HOST-RESOURCES-MIB.hrDeviceStatus")
</dt> </dl>

Availability and status of the device.

This value comes from the **Cache Configuration** member of the **Cache Information** structure in the SMBIOS information.

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


</dt> <dd></dd> <dt>

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

**BlockSize**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|HOST-RESOURCES-MIB.hrStorageAllocationUnits"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Size in bytes of the blocks that form this storage extent. If unknown or if a block concept is not valid (for example, for aggregate extents, memory, or logical disks), enter a 1.

This property is inherited from [**CIM\_StorageExtent**](cim-storageextent.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**CacheSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Cache Speed"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("nanoseconds")
</dt> </dl>

Speed of the cache.

This value comes from the **Cache Speed** member of the **Cache Information** structure in the SMBIOS information.

</dd> <dt>

**CacheType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.9")
</dt> </dl>

Type of cache.

This value comes from the **System Cache Type** member of the **Cache Information** structure in the SMBIOS information.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Instruction"></span><span id="instruction"></span><span id="INSTRUCTION"></span>

**Instruction** (3)


</dt> <dd></dd> <dt>

<span id="Data"></span><span id="data"></span><span id="DATA"></span>

**Data** (4)


</dt> <dd></dd> <dt>

<span id="Unified"></span><span id="unified"></span><span id="UNIFIED"></span>

**Unified** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Caption")
</dt> </dl>

Short description of the object a one-line string.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**ConfigManagerErrorCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32")
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

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32")
</dt> </dl>

If **True**, the device is using a user-defined configuration.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**CorrectableError**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.12", "MIF.DMTF\|Physical Memory Array\|001.8")
</dt> </dl>

If **True**, the most recent error was correctable. If the **ErrorInfo** property is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**CreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Name of the first concrete class to appear in the inheritance chain used in the creation of an instance. When used with the other key properties of the class, the property allows all instances of this class and its subclasses to be uniquely identified.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**CurrentSRAM**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Current SRAM Type")
</dt> </dl>

Array of types of Static Random Access Memory (SRAM) being used for the cache memory.

This value comes from the **Current SRAM Type** member of the **Cache Information** structure in the SMBIOS information.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (0)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (1)


</dt> <dd></dd> <dt>

<span id="Non-Burst"></span><span id="non-burst"></span><span id="NON-BURST"></span>

**Non-Burst** (2)


</dt> <dd></dd> <dt>

<span id="Burst"></span><span id="burst"></span><span id="BURST"></span>

**Burst** (3)


</dt> <dd></dd> <dt>

<span id="Pipeline_Burst"></span><span id="pipeline_burst"></span><span id="PIPELINE_BURST"></span>

**Pipeline Burst** (4)


</dt> <dd></dd> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (5)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Description")
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

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("DeviceId"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("WMI")
</dt> </dl>

Unique identifier of the cache represented by an instance of **Win32\_CacheMemory**.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

Example: "Cache Memory 1"

</dd> <dt>

**EndingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.4", "MIF.DMTF\|Memory Device Mapped Addresses\|001.5"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("kilobytes")
</dt> </dl>

Ending address, referenced by an application or operating system and mapped by a memory controller, for this memory object. The ending address is specified in kilobytes.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**ErrorAccess**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.15", "MIF.DMTF\|Physical Memory Array\|001.10")
</dt> </dl>

Memory access operation that caused the last error. The type of error is described by the **ErrorInfo** property. If **ErrorInfo** is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (3)


</dt> <dd></dd> <dt>

<span id="Write"></span><span id="write"></span><span id="WRITE"></span>

**Write** (4)


</dt> <dd></dd> <dt>

<span id="Partial_Write"></span><span id="partial_write"></span><span id="PARTIAL_WRITE"></span>

**Partial Write** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.19", "MIF.DMTF\|Memory Device\|002.20", "MIF.DMTF\|Physical Memory Array\|001.14")
</dt> </dl>

Address of the last memory error. The type of error is described by the **ErrorInfo** property. If **ErrorInfo** is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**ErrorCleared**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the error reported in **LastErrorCode** is now cleared.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ErrorCorrectType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Error Correction Type")
</dt> </dl>

Error correction method used by the cache memory.

This value comes from the **Error Correction Type** member of the **Cache Information** structure in the SMBIOS information.

<dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (3)


</dt> <dd></dd> <dt>

<span id="Parity"></span><span id="parity"></span><span id="PARITY"></span>

**Parity** (4)


</dt> <dd></dd> <dt>

<span id="Single-bit_ECC"></span><span id="single-bit_ecc"></span><span id="SINGLE-BIT_ECC"></span>

**Single-bit ECC** (5)


</dt> <dd></dd> <dt>

<span id="Multi-bit_ECC"></span><span id="multi-bit_ecc"></span><span id="MULTI-BIT_ECC"></span>

**Multi-bit ECC** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ArrayType**](/windows/desktop/WmiSdk/standard-qualifiers) ("Indexed"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.17", "MIF.DMTF\|Physical Memory Array\|001.12"), [**MAX**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Array of data captured during the last erroneous memory access. The data occupies the first *n* octets of the array necessary to hold the number of bits specified by the **ErrorTransferSize** property. If **ErrorTransferSize** is 0 (zero), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**ErrorDataOrder**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Ordering for data stored in the **ErrorData** property. If **ErrorTransferSize** is 0 (zero), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Least_Significant_Byte_First"></span><span id="least_significant_byte_first"></span><span id="LEAST_SIGNIFICANT_BYTE_FIRST"></span>

**Least Significant Byte First** (1)


</dt> <dd></dd> <dt>

<span id="Most_Significant_Byte_First"></span><span id="most_significant_byte_first"></span><span id="MOST_SIGNIFICANT_BYTE_FIRST"></span>

**Most Significant Byte First** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

More information about the error recorded in **LastErrorCode**, and information on any corrective actions that may be taken.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**ErrorInfo**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.12", "MIF.DMTF\|Physical Memory Array\|001.8"), [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Memory**](cim-memory.md).**OtherErrorDescription**")
</dt> </dl>

Type of error that occurred most recently. The values 12-14 are undefined in the CIM schema because in DMI they mix the semantics of the type of error and whether it was correctable or not. The latter is indicated in the property **CorrectableError**.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="OK"></span><span id="ok"></span>

**OK** (3)


</dt> <dd></dd> <dt>

<span id="Bad_Read"></span><span id="bad_read"></span><span id="BAD_READ"></span>

**Bad Read** (4)


</dt> <dd></dd> <dt>

<span id="Parity_Error"></span><span id="parity_error"></span><span id="PARITY_ERROR"></span>

**Parity Error** (5)


</dt> <dd></dd> <dt>

<span id="Single-Bit_Error"></span><span id="single-bit_error"></span><span id="SINGLE-BIT_ERROR"></span>

**Single-Bit Error** (6)


</dt> <dd></dd> <dt>

<span id="Double-Bit_Error"></span><span id="double-bit_error"></span><span id="DOUBLE-BIT_ERROR"></span>

**Double-Bit Error** (7)


</dt> <dd></dd> <dt>

<span id="Multi-Bit_Error"></span><span id="multi-bit_error"></span><span id="MULTI-BIT_ERROR"></span>

**Multi-Bit Error** (8)


</dt> <dd></dd> <dt>

<span id="Nibble_Error"></span><span id="nibble_error"></span><span id="NIBBLE_ERROR"></span>

**Nibble Error** (9)


</dt> <dd></dd> <dt>

<span id="Checksum_Error"></span><span id="checksum_error"></span><span id="CHECKSUM_ERROR"></span>

**Checksum Error** (10)


</dt> <dd></dd> <dt>

<span id="CRC_Error"></span><span id="crc_error"></span><span id="CRC_ERROR"></span>

**CRC Error** (11)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (12)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (13)


</dt> <dd></dd> <dt>

<span id="Undefined"></span><span id="undefined"></span><span id="UNDEFINED"></span>

**Undefined** (14)


</dt> <dd></dd> </dl>

</dd> <dt>

**ErrorMethodology**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Physical Memory Array\|001.7")
</dt> </dl>

Details on the parity or CRC algorithms, ECC, or other mechanisms used.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**ErrorResolution**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.21", "MIF.DMTF\|Physical Memory Array\|001.15"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Range, in bytes, to which the last error can be resolved. For example, if error addresses are resolved to bit 11 (that is, on a typical page basis), then errors can be resolved to 4 KB boundaries and this property is set to 4000. If the **ErrorInfo** property is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**ErrorTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Time that the last memory error occurred. The type of error is described by the **ErrorInfo** property. If the **ErrorInfo** property is equal to 3 (OK), then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**ErrorTransferSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Device\|002.16", "MIF.DMTF\|Physical Memory Array\|001.11"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits")
</dt> </dl>

Size of the data transfer in bits that caused the last error. 0 (zero) indicates no error. If the **ErrorInfo** property is equal to 3 (OK), then this property should be set to 0 (zero).

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**FlushTimer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.14"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("seconds")
</dt> </dl>

Maximum amount of time, in seconds, dirty lines or buckets may remain in the cache before they are flushed. A value of 0 (zero) indicates that a cache flush is not controlled by a flushing timer.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5"), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Install Date")
</dt> </dl>

Date and time the object was installed. This property does not need a value to indicate that the object is installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**InstalledSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Installed Size"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("kilobytes")
</dt> </dl>

Current size of the installed cache memory.

This value comes from the **Installed Size** member of the **Cache Information** structure in the SMBIOS information.

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

**Level**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.2")
</dt> </dl>

Level of the cache.

This value comes from the **Cache Configuration** member of the **Cache Information** structure in the SMBIOS information.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Primary"></span><span id="primary"></span><span id="PRIMARY"></span>

<span id="Primary"></span><span id="primary"></span><span id="PRIMARY"></span>**Primary** (3)


</dt> <dd></dd> <dt>

<span id="Secondary"></span><span id="secondary"></span><span id="SECONDARY"></span>

<span id="Secondary"></span><span id="secondary"></span><span id="SECONDARY"></span>**Secondary** (4)


</dt> <dd></dd> <dt>

<span id="Tertiary"></span><span id="tertiary"></span><span id="TERTIARY"></span>

<span id="Tertiary"></span><span id="tertiary"></span><span id="TERTIARY"></span>**Tertiary** (5)


</dt> <dd></dd> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**LineSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.10"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bytes")
</dt> </dl>

Size, in bytes, of a single cache bucket or line.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Location")
</dt> </dl>

Physical location of the cache memory.

This value comes from the **Cache Configuration** member of the **Cache Information** structure in the SMBIOS information.

<dt>

<span id="Internal"></span><span id="internal"></span><span id="INTERNAL"></span>

**Internal** (0)


</dt> <dd></dd> <dt>

<span id="External"></span><span id="external"></span><span id="EXTERNAL"></span>

**External** (1)


</dt> <dd></dd> <dt>

<span id="Reserved"></span><span id="reserved"></span><span id="RESERVED"></span>

**Reserved** (2)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**MaxCacheSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Maximum Cache Size"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("kilobytes")
</dt> </dl>

Maximum cache size installable to this particular cache memory.

This value comes from the **Maximum Cache Size** member of the **Cache Information** structure in the SMBIOS information.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Name")
</dt> </dl>

Label by which the object is known. When subclassed, the property can be overridden to be a key property.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**NumberOfBlocks**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIB.IETF\|HOST-RESOURCES-MIB.hrStorageSize")
</dt> </dl>

Total number of consecutive blocks, each block the size of the value contained in the **BlockSize** property, which form this storage extent. Total size of the storage extent can be calculated by multiplying the value of the **BlockSize** property by the value of this property. If the value of **BlockSize** is 1, this property is the total size of the storage extent.

This property is inherited from [**CIM\_StorageExtent**](cim-storageextent.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**OtherErrorDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**ModelCorrespondence**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_Memory**](cim-memory.md).**ErrorInfo**")
</dt> </dl>

Free-form string providing more information if the **ErrorType** property is set to 1, Other. Otherwise, this string has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**PNPDeviceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Schema**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32")
</dt> </dl>

Windows Plug and Play device identifier of the logical device.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

Example: "\*PNP030b"

</dd> <dt>

**PowerManagementCapabilities**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Array of the specific power-related capabilities of a logical device.

This property is inherited from **CIM\_LogicalDevice**.

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

The [**SetPowerState**](setpowerstate-method-in-class-cim-controller.md) method is supported. This method is found on the parent **CIM\_LogicalDevice** class and can be implemented. For more information, see [Designing Managed Object Format (MOF) Classes](/windows/desktop/WmiSdk/designing-managed-object-format--mof--classes).

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

If **True**, the device can be power-managed (can be put into suspend mode, and so on). The property does not indicate that power management features are currently enabled, only that the logical device is capable of power management.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**Purpose**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Free-form string describing the media and its use.

This value comes from the **Socket Designation** member of the **Cache Information** structure in the SMBIOS information.

This property is inherited from [**CIM\_StorageExtent**](cim-storageextent.md).

</dd> <dt>

**ReadPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.13")
</dt> </dl>

Policy that shall be employed by the cache for handling read requests.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Read"></span><span id="read"></span><span id="READ"></span>

**Read** (3)


</dt> <dd></dd> <dt>

<span id="Read-Ahead"></span><span id="read-ahead"></span><span id="READ-AHEAD"></span>

**Read-Ahead** (4)


</dt> <dd></dd> <dt>

<span id="Read_and_Read-Ahead"></span><span id="read_and_read-ahead"></span><span id="READ_AND_READ-AHEAD"></span>

**Read and Read-Ahead** (5)


</dt> <dd></dd> <dt>

<span id="Determination_Per_I_O"></span><span id="determination_per_i_o"></span><span id="DETERMINATION_PER_I_O"></span>

**Determination Per I/O** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**ReplacementPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.12")
</dt> </dl>

Algorithm to determine which cache lines or buckets should be reused.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Least_Recently_Used__LRU_"></span><span id="least_recently_used__lru_"></span><span id="LEAST_RECENTLY_USED__LRU_"></span>

**Least Recently Used (LRU)** (3)


</dt> <dd></dd> <dt>

<span id="First_In_First_Out__FIFO_"></span><span id="first_in_first_out__fifo_"></span><span id="FIRST_IN_FIRST_OUT__FIFO_"></span>

**First In First Out (FIFO)** (4)


</dt> <dd></dd> <dt>

<span id="Last_In_First_Out__LIFO_"></span><span id="last_in_first_out__lifo_"></span><span id="LAST_IN_FIRST_OUT__LIFO_"></span>

**Last In First Out (LIFO)** (5)


</dt> <dd></dd> <dt>

<span id="Least_Frequently_Used__LFU_"></span><span id="least_frequently_used__lfu_"></span><span id="LEAST_FREQUENTLY_USED__LFU_"></span>

**Least Frequently Used (LFU)** (6)


</dt> <dd></dd> <dt>

<span id="Most_Frequently_Used__MFU_"></span><span id="most_frequently_used__mfu_"></span><span id="MOST_FREQUENTLY_USED__MFU_"></span>

**Most Frequently Used (MFU)** (7)


</dt> <dd></dd> <dt>

<span id="Data_Dependent_Multiple_Algorithms"></span><span id="data_dependent_multiple_algorithms"></span><span id="DATA_DEPENDENT_MULTIPLE_ALGORITHMS"></span>

**Data Dependent Multiple Algorithms** (8)


</dt> <dd></dd> </dl>

</dd> <dt>

**StartingAddress**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Memory Array Mapped Addresses\|001.3", "MIF.DMTF\|Memory Device Mapped Addresses\|001.4"), [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("kilobytes")
</dt> </dl>

Beginning address, referenced by an application or operating system and mapped by a memory controller, for this memory object. The starting address is specified in kilobytes.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10), [**DisplayName**](/windows/desktop/WmiSdk/standard-qualifiers) ("Status")
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

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|Operational State\|003.3")
</dt> </dl>

State of the logical device. If this property does not apply to the logical device, the value 5 (Not Applicable) should be used.

This value comes from the **Cache Configuration** member of the **Cache Information** structure in the SMBIOS information.

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

**SupportedSRAM**
</dt> <dd> <dl> <dt>

Data type: **uint16** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("SMBIOS\|Type 7\|Supported SRAM Type")
</dt> </dl>

Array of supported types of Static Random Access Memory (SRAM) that can be used for the cache memory.

This value comes from the **Supported SRAM Type** member of the **Cache Information** structure in the SMBIOS information.

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (0)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (1)


</dt> <dd></dd> <dt>

<span id="Non-Burst"></span><span id="non-burst"></span><span id="NON-BURST"></span>

**Non-Burst** (2)


</dt> <dd></dd> <dt>

<span id="Burst"></span><span id="burst"></span><span id="BURST"></span>

**Burst** (3)


</dt> <dd></dd> <dt>

<span id="Pipeline_Burst"></span><span id="pipeline_burst"></span><span id="PIPELINE_BURST"></span>

**Pipeline Burst** (4)


</dt> <dd></dd> <dt>

<span id="Synchronous"></span><span id="synchronous"></span><span id="SYNCHRONOUS"></span>

**Synchronous** (5)


</dt> <dd></dd> <dt>

<span id="Asynchronous"></span><span id="asynchronous"></span><span id="ASYNCHRONOUS"></span>

**Asynchronous** (6)


</dt> <dd></dd> </dl>

</dd> <dt>

**SystemCreationClassName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](cim-system.md).**CreationClassName**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Value of the scoping computer's **CreationClassName** property.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**SystemLevelAddress**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the address information in the property **ErrorAddress** is a system-level address. If **False**, it is a physical address. If the **ErrorInfo** property is equal to 3, then this property has no meaning.

This property is inherited from [**CIM\_Memory**](cim-memory.md).

</dd> <dt>

**SystemName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Propagated**](/windows/desktop/WmiSdk/standard-qualifiers) ("[**CIM\_System**](cim-system.md).**Name**"), [**CIM\_Key**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Name of the scoping system.

This property is inherited from [**CIM\_LogicalDevice**](cim-logicaldevice.md).

</dd> <dt>

**WritePolicy**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|System Cache\|003.5")
</dt> </dl>

Write policy definition.

This value comes from the **Cache Configuration** member of the **Cache Information** structure in the SMBIOS information.

This property is inherited from [**CIM\_CacheMemory**](cim-cachememory.md).

<dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (2)


</dt> <dd></dd> <dt>

<span id="Write_Back"></span><span id="write_back"></span><span id="WRITE_BACK"></span>

**Write Back** (3)


</dt> <dd></dd> <dt>

<span id="Write_Through"></span><span id="write_through"></span><span id="WRITE_THROUGH"></span>

**Write Through** (4)


</dt> <dd></dd> <dt>

<span id="Varies_with_Address"></span><span id="varies_with_address"></span><span id="VARIES_WITH_ADDRESS"></span>

**Varies with Address** (5)


</dt> <dd></dd> <dt>

<span id="Determination_Per_I_O"></span><span id="determination_per_i_o"></span><span id="DETERMINATION_PER_I_O"></span>

**Determination Per I/O** (6)


</dt> <dd></dd> </dl>

</dd> </dl>

## Remarks

The **Win32\_CacheMemory** class is derived from [**CIM\_CacheMemory**](cim-cachememory.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_CacheMemory**](cim-cachememory.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

