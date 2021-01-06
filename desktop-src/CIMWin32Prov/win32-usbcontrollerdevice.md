---
description: The Win32\_USBControllerDevice association WMI class relates a universal serial bus (USB) controller and the CIM\_LogicalDevice instance connected to it.
ms.assetid: a0c64984-9116-4cb8-86e0-38c897cb7119
ms.tgt_platform: multiple
title: Win32_USBControllerDevice class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_USBControllerDevice
- Win32_USBControllerDevice.NegotiatedDataWidth
- Win32_USBControllerDevice.NegotiatedSpeed
- Win32_USBControllerDevice.AccessState
- Win32_USBControllerDevice.NumberOfHardResets
- Win32_USBControllerDevice.NumberOfSoftResets
- Win32_USBControllerDevice.Antecedent
- Win32_USBControllerDevice.Dependent
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_USBControllerDevice class

The **Win32\_USBControllerDevice** association [WMI class](../wmisdk/retrieving-a-class.md) relates a universal serial bus (USB) controller and the [**CIM\_LogicalDevice**](cim-logicaldevice.md) instance connected to it.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{DE57D792-A032-11D2-90F0-0060081A46FD}"), AMENDMENT]
class Win32_USBControllerDevice : CIM_ControlledBy
{
  uint32                NegotiatedDataWidth;
  uint64                NegotiatedSpeed;
  uint16                AccessState;
  uint32                NumberOfHardResets;
  uint32                NumberOfSoftResets;
  CIM_USBController REF Antecedent;
  CIM_LogicalDevice REF Dependent;
};
```

## Members

The **Win32\_USBControllerDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_USBControllerDevice** class has these properties.

<dl> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the controller is actively commanding or accessing the device. This information is necessary when a logical device can be commanded by, or accessed through, multiple controllers.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Active"></span><span id="active"></span><span id="ACTIVE"></span>

**Active** (1)


</dt> <dd></dd> <dt>

<span id="Inactive"></span><span id="inactive"></span><span id="INACTIVE"></span>

**Inactive** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_USBController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("Antecedent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("CIM\|CIM\_USBController")
</dt> </dl>

A [**CIM\_USBController**](cim-usbcontroller.md) representing the Universal Serial Bus (USB) controller associated with this device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](../wmisdk/key-qualifier.md), [**Override**](../wmisdk/standard-qualifiers.md) ("Dependent"), [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) describing the logical device connected to the Universal Serial Bus (USB) controller.

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("bits")
</dt> </dl>

When several bus or connection-data widths are possible, this property defines the one in use between the devices. Data width is specified in bits. If data width is not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero).

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

</dd> <dt>

**NegotiatedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](../wmisdk/standard-qualifiers.md) ("bits per second")
</dt> </dl>

When several bus or connection speeds are possible, this property defines the one being used between the devices. Speed is specified in bits-per-second. If connection or bus speeds are not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero).

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

</dd> <dt>

**NumberOfHardResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of hard resets issued by the controller. A hard reset returns the device to its initialization or boot-up state. All internal device state information and data are lost.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**NumberOfSoftResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of soft resets issued by the controller. A soft reset does not completely clear current device state and data. Exact semantics are dependent on the device and on the protocols and mechanisms used to communicate to it.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> </dl>

## Remarks

The **Win32\_USBControllerDevice** class is derived from [**CIM\_ControlledBy**](cim-controlledby.md).

For a discussion on using, see the [Displaying USB Devices using WMI](https://devblogs.microsoft.com/powershell/displaying-usb-devices-using-wmi/) blog article. For a discussion of using association classes, see the [Get-USB – Using WMI Association Classes in PowerShell](https://devblogs.microsoft.com/powershell/get-usb-using-wmi-association-classes-in-powershell/) article.

## Examples

The following PowerShell example retrieves the dependent logical device and displays the relevant information.


```PowerShell
gwmi Win32_USBControllerDevice |%{[wmi]($_.Dependent)} | Sort Manufacturer,Description,DeviceID | Ft -GroupBy Manufacturer Description,Service,DeviceID
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

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
