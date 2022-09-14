---
description: Associates a storage device with the storage controller that owns the device.
ms.assetid: 3DE05EDC-C54A-4C3C-9057-4418246037D5
title: Msvm_ControlledBy class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
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
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ControlledBy class

Associates a storage device with the storage controller that owns the device. This association is used with both IDE and floppy controllers.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ControlledBy : CIM_ControlledBy
{
  uint64                NegotiatedSpeed = 0;
  uint32                NegotiatedDataWidth = 0;
  CIM_Controller    REF Antecedent;
  CIM_LogicalDevice REF Dependent;
  uint16                AccessState = 1;
  datetime              TimeOfDeviceReset;
  uint32                NumberOfHardResets;
  uint32                NumberOfSoftResets;
  string                DeviceNumber;
  uint16                AccessMode = 2;
  uint16                AccessPriority = 0;
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

The accessibility of the device through the antecedent controller. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), and it is always set to 2 (read/write).

</dd> <dt>

**AccessPriority**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The priority given to accesses of the device through this controller. The highest priority path will have the lowest value. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), and it is always set to 0.

</dd> <dt>

**AccessState**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the controller is actively commanding or accessing the device. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), and it is always set to 1 (Active).

</dd> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Controller**](/windows/desktop/CIMWin32Prov/cim-controller)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the controller. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](/windows/desktop/CIMWin32Prov/cim-logicaldevice)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the controlled device. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby).

</dd> <dt>

**DeviceNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The address of the associated device in the context of the antecedent controller. This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby).

</dd> <dt>

**NegotiatedDataWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_DeviceConnection**](/windows/desktop/CIMWin32Prov/cim-deviceconnection), and it is always set to 0.

</dd> <dt>

**NegotiatedSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_DeviceConnection**](/windows/desktop/CIMWin32Prov/cim-deviceconnection), and it is always set to 0.

</dd> <dt>

**NumberOfHardResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), but it is not used.

</dd> <dt>

**NumberOfSoftResets**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), but it is not used.

</dd> <dt>

**TimeOfDeviceReset**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is inherited from [**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby), but it is not used.

</dd> </dl>

## Remarks

Access to the **Msvm\_ControlledBy** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_ControlledBy**](cim-controlledby.md)
</dt> <dt>

[**CIM\_ControlledBy**](/windows/desktop/CIMWin32Prov/cim-controlledby)
</dt> <dt>

[Storage Classes](storage-classes.md)
</dt> </dl>

 

