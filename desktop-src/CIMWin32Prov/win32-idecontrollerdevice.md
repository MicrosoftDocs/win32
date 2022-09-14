---
description: The Win32\_IDEControllerDevice association WMI class relates an Integrated Drive Electronics (IDE) controller and the logical device connected to, for example, a disk drive.
ms.assetid: 1b0a551c-d836-4147-91ed-a0a7d97f4a5b
ms.tgt_platform: multiple
title: Win32_IDEControllerDevice class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_IDEControllerDevice
- Win32_IDEControllerDevice.NegotiatedDataWidth
- Win32_IDEControllerDevice.NegotiatedSpeed
- Win32_IDEControllerDevice.AccessState
- Win32_IDEControllerDevice.NumberOfHardResets
- Win32_IDEControllerDevice.NumberOfSoftResets
- Win32_IDEControllerDevice.Antecedent
- Win32_IDEControllerDevice.Dependent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_IDEControllerDevice class

The **Win32\_IDEControllerDevice** association [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) relates an Integrated Drive Electronics (IDE) controller and the logical device connected to, for example, a disk drive.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{5BC42B62-C7A1-11d2-911D-0060081A46FD}"), AMENDMENT]
class Win32_IDEControllerDevice : CIM_ControlledBy
{
  uint32                  NegotiatedDataWidth;
  uint64                  NegotiatedSpeed;
  uint16                  AccessState;
  uint32                  NumberOfHardResets;
  uint32                  NumberOfSoftResets;
  Win32_IDEController REF Antecedent;
  CIM_LogicalDevice   REF Dependent;
};
```

## Members

The **Win32\_IDEControllerDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_IDEControllerDevice** class has these properties.

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

Data type: **Win32\_IDEController**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\|Win32\_IDEController")
</dt> </dl>

A [**Win32\_IDEController**](win32-idecontroller.md) that represents the IDE controller associated with this device.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("CIM\|CIM\_LogicalDevice")
</dt> </dl>

A [**CIM\_LogicalDevice**](cim-logicaldevice.md) that represents the logical device connected to the IDE controller.

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits")
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

Qualifiers: [**Units**](/windows/desktop/WmiSdk/standard-qualifiers) ("bits per second")
</dt> </dl>

When several bus or connection speeds are possible, this property defines the one being used between the devices. Speed is specified in bits-per-second. If connection or bus speeds are not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script).

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

The **Win32\_IDEControllerDevice** class is derived from [**CIM\_ControlledBy**](cim-controlledby.md).

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

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

