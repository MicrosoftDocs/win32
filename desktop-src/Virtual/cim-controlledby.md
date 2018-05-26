---
title: CIM\_ControlledBy class
description: Represents a relationship between a controller and a logical device that is managed by the controller.
ms.assetid: 0f254114-3b20-4f4b-b7a7-d79048e8054b
keywords:
- CIM_ControlledBy class Hyper-V
- CIM_ControlledBy class Hyper-V , described
topic_type:
- apiref
api_name:
- CIM_ControlledBy
- CIM_ControlledBy.NegotiatedSpeed
- CIM_ControlledBy.NegotiatedDataWidth
- CIM_ControlledBy.Antecedent
- CIM_ControlledBy.Dependent
- CIM_ControlledBy.AccessState
- CIM_ControlledBy.TimeOfDeviceReset
- CIM_ControlledBy.NumberOfHardResets
- CIM_ControlledBy.NumberOfSoftResets
- CIM_ControlledBy.DeviceNumber
- CIM_ControlledBy.AccessMode
- CIM_ControlledBy.AccessPriority
api_location:
- Root\virtualization
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CIM\_ControlledBy class

Represents a relationship between a controller and a logical device that is managed by the controller.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.10.0"), AMENDMENT]
class CIM_ControlledBy : CIM_DeviceConnection
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

The **CIM\_ControlledBy** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ControlledBy** class has these properties.

<dl> <dt>

**AccessMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property that describes the accessibility of the device through the controller.

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

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the controller is actively managing the device.

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
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The controller.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_LogicalDevice**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The logical devices.

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the associated device in the context of the controller.

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

</dd> <dt>

**TimeOfDeviceReset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when the downstream device was last reset by the controller.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_DeviceConnection**](cim-deviceconnection.md)
</dt> </dl>

 

 





