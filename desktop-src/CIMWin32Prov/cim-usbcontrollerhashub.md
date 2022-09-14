---
description: The CIM\_USBControllerHasHub class defines the hubs that are downstream of the USB controller.
ms.assetid: 38bc0342-3ff0-42c8-9c1e-ea5a5822e1d3
ms.tgt_platform: multiple
title: CIM_USBControllerHasHub class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_USBControllerHasHub
- CIM_USBControllerHasHub.NegotiatedDataWidth
- CIM_USBControllerHasHub.NegotiatedSpeed
- CIM_USBControllerHasHub.AccessState
- CIM_USBControllerHasHub.NumberOfHardResets
- CIM_USBControllerHasHub.NumberOfSoftResets
- CIM_USBControllerHasHub.Dependent
- CIM_USBControllerHasHub.Antecedent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# CIM\_USBControllerHasHub class

The **CIM\_USBControllerHasHub** class defines the hubs that are downstream of the USB controller.

> [!IMPORTANT]
> The DMTF (Distributed Management Task Force) CIM (Common Information Model) classes are the parent classes upon which WMI classes are built. WMI currently supports only the [CIM 2.x version schemas](https://dmtf.org/standards/cim/schemas).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of its inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[AMENDMENT]
class CIM_USBControllerHasHub : CIM_ControlledBy
{
  uint32                NegotiatedDataWidth;
  uint64                NegotiatedSpeed;
  uint16                AccessState;
  uint32                NumberOfHardResets;
  uint32                NumberOfSoftResets;
  CIM_USBHub        REF Dependent;
  CIM_USBController REF Antecedent;
};
```

## Members

The **CIM\_USBControllerHasHub** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_USBControllerHasHub** class has these properties.

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

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_USBController**](cim-usbcontroller.md) describing the USBController.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_USBHub**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A [**CIM\_USBHub**](cim-usbhub.md) describing the USBHub that is associated with the Controller.

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

The **CIM\_USBControllerHasHub** class is derived from [**CIM\_ControlledBy**](cim-controlledby.md).

WMI does not implement this class. For WMI classes derived from **CIM\_USBControllerHasHub**, see [Win32 Classes](win32-provider.md).

This documentation is derived from the CIM class descriptions published by the DMTF. Microsoft may have made changes to correct minor errors, conform to Microsoft SDK documentation standards, or provide more information.

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
</dt> </dl>

 

