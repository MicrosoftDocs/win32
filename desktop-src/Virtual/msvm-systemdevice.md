---
title: Msvm\_SystemDevice class
description: Associates a logical device with the parent system.
ms.assetid: '0be1695d-42a9-441a-b731-ca00868c085c'
keywords: ["Msvm_SystemDevice class Hyper-V", "Msvm_SystemDevice class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_SystemDevice
- Msvm_SystemDevice.GroupComponent
- Msvm_SystemDevice.PartComponent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_SystemDevice class

Logical devices can be aggregated by a system. This relationship is made explicit by the system device association.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemDevice : CIM_SystemDevice
{
  CIM_System        REF GroupComponent;
  CIM_LogicalDevice REF PartComponent;
};
```

## Members

The **Msvm\_SystemDevice** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SystemDevice** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_System**](cim-system.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](https://msdn.microsoft.com/library/aa393650), [**Min**](https://msdn.microsoft.com/library/aa393650) (1), [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The parent system in the association. This property is inherited from [**CIM\_SystemDevice**](https://msdn.microsoft.com/library/aa388509).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](cim-logicaldevice.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Weak**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

The logical device that is an element of a system. This property is inherited from [**CIM\_SystemDevice**](https://msdn.microsoft.com/library/aa388509).

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemDevice** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_SystemDevice**](cim-systemdevice.md)
</dt> <dt>

[**CIM\_SystemDevice**](https://msdn.microsoft.com/library/aa388509)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 





