---
description: The Win32\_PrinterController association WMI class relates a printer and the local device to which the printer is connected. Note that this class only returns instances for local printers.
ms.assetid: fb483b28-11f1-4153-893e-492f71763712
ms.tgt_platform: multiple
title: Win32_PrinterController class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Win32_PrinterController
- Win32_PrinterController.AccessState
- Win32_PrinterController.Antecedent
- Win32_PrinterController.Dependent
- Win32_PrinterController.NegotiatedDataWidth
- Win32_PrinterController.NegotiatedSpeed
- Win32_PrinterController.NumberOfHardResets
- Win32_PrinterController.NumberOfSoftResets
api_type:
- DllExport
api_location:
- CIMWin32.dll
---

# Win32\_PrinterController class

The **Win32\_PrinterController** association [WMI class](../wmisdk/retrieving-a-class.md) relates a printer and the local device to which the printer is connected. Note that this class only returns instances for local printers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_PrinterController : CIM_ControlledBy
{
  uint16             AccessState;
  CIM_Controller REF Antecedent;
  Win32_Printer  REF Dependent;
  uint32             NegotiatedDataWidth;
  uint64             NegotiatedSpeed;
  uint32             NumberOfHardResets;
  uint32             NumberOfSoftResets;
};
```

## Members

The **Win32\_PrinterController** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PrinterController** class has these properties.

<dl> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of the controller access to the device. This information is necessary when a logical device can be commanded by, or accessed through, multiple controllers.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Unknown

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Active

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Inactive

</dd> </dl>

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Controller**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/standard-qualifiers.md)
</dt> </dl>

Reference to the [**CIM\_Controller**](cim-controller.md) instance representing the local device associated with this printer.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Printer**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](../wmisdk/standard-qualifiers.md)
</dt> </dl>

Reference to the [**Win32\_Printer**](win32-printer.md) instance representing the printer associated with the local device.

This property is inherited from [**CIM\_Dependency**](cim-dependency.md).

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Data width in use between devices (when several bus or connection data widths are possible). Data width is specified in bits. If data width is not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero).

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

</dd> <dt>

**NegotiatedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Speed in use between devices (when several bus or connection speeds are possible). Speed is specified in bits per second. If connection or bus speeds are not negotiated, or if this information is not available or important to device management, the property should be set to 0 (zero).

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

For more information about using **uint64** values in scripts, see [Scripting in WMI](../wmisdk/creating-a-wmi-script.md).

</dd> <dt>

**NumberOfHardResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of hard resets issued by the controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**NumberOfSoftResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of soft resets issued by the controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> </dl>

## Remarks

The **Win32\_PrinterController** class is derived from [**CIM\_ControlledBy**](cim-controlledby.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                        |
| MOF<br/>                      | <dl> <dt>Win32\_Printer.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl>       |



## See also

<dl> <dt>

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dt>

[Computer System Hardware Classes](computer-system-hardware-classes.md)
</dt> </dl>

 

 
