---
title: Msvm\_ControlledBy class
description: Associates a storage device with the storage controller that owns the device.
ms.assetid: 8f870f9d-1ad4-42a4-a9cb-dd71829f18bb
keywords:
- Msvm_ControlledBy class Hyper-V
- Msvm_ControlledBy class Hyper-V , described
topic_type:
- apiref
api_name:
- Msvm_ControlledBy
- Msvm_ControlledBy.NegotiatedSpeed
- Msvm_ControlledBy.NegotiatedDataWidth
- Msvm_ControlledBy.Antecedent
- Msvm_ControlledBy.Dependent
- Msvm_ControlledBy.AccessState
- Msvm_ControlledBy.TimeOfDeviceReset
- Msvm_ControlledBy.NumberOfHardResets
- Msvm_ControlledBy.NumberOfSoftResets
- Msvm_ControlledBy.DeviceNumber
- Msvm_ControlledBy.AccessMode
- Msvm_ControlledBy.AccessPriority
api_location:
- Root\Virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Msvm\_ControlledBy class

Associates a storage device with the storage controller that owns the device. This association is used with both IDE and floppy controllers.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ControlledBy : CIM_ControlledBy
{
  uint64                NegotiatedSpeed;
  uint32                NegotiatedDataWidth;
  CIM_Controller    REF Antecedent;
  CIM_LogicalDevice REF Dependent;
  uint16                AccessState;
  datetime              TimeOfDeviceReset;
  uint32                NumberOfHardResets;
  uint32                NumberOfSoftResets;
  string                DeviceNumber;
  uint16                AccessMode;
  uint16                AccessPriority;
};
```

## Members

The **Msvm\_ControlledBy** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ControlledBy** class has these properties.

<dl> <dt>

**AccessMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property that describes the accessibility of the device through the controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

<dt>

<span id="ReadWrite"></span><span id="readwrite"></span><span id="READWRITE"></span>

**ReadWrite** (2)


</dt> <dd></dd> <dt>

<span id="ReadOnly"></span><span id="readonly"></span><span id="READONLY"></span>

**ReadOnly** (3)


</dt> <dd></dd> <dt>

<span id="NoAccess"></span><span id="noaccess"></span><span id="NOACCESS"></span>

**NoAccess** (4)


</dt> <dd></dd> </dl>

</dd> <dt>

**AccessPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The priority for access of the device through the controller. A lower value indicates a higher priority.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the controller is actively managing the device.

This property is always set to 1.

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

Data type: **CIM\_Controller**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical devices.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the associated device in the context of the controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port Association\|001.3")
</dt> </dl>

When several bus and connection data widths are possible, the NegotiatedDataWidth property defines the one that is in use between the Devices. Data width is specified in bits. If data width is not negotiated, or if this information is not available or not important to Device management, the property should be set to 0.

This property is always set to 0.

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

</dd> <dt>

**NegotiatedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Units**](https://msdn.microsoft.com/library/aa393650) ("Bits per Second"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("MIF.DMTF\|Bus Port Association\|001.2")
</dt> </dl>

When several bus and connection speeds are possible, this property defines the speed that is in use between the devices, in bits per second. If connection or bus speeds are not negotiated, or if this information is not available, or not important to device management, the property should be set to "0".

This property is always set to 0.

This property is inherited from [**CIM\_DeviceConnection**](cim-deviceconnection.md).

</dd> <dt>

**NumberOfHardResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Counter**
</dt> </dl>

The number of hard resets issued by the controller. A hard reset returns a device to its initialization or boot-up state, after which all internal device state information and data are lost.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**NumberOfSoftResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Counter**
</dt> </dl>

The number of soft resets issued by the controller. A soft reset does not clear the device state or data.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> <dt>

**TimeOfDeviceReset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the downstream device was last reset by the controller.

This property is inherited from [**CIM\_ControlledBy**](cim-controlledby.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_ControlledBy** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dt>

[**CIM\_ControlledBy**](https://msdn.microsoft.com/library/aa387230)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

 





