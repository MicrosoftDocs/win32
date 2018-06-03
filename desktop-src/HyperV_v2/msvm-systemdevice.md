---
Description: Associates a logical device with the parent system.
ms.assetid: 2BEAAEC8-F8F2-4CC7-A209-EE3EE3C6FA90
title: Msvm\_SystemDevice class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Msvm\_SystemDevice class

Logical devices can be aggregated by a system. This relationship is made explicit by the system device association.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SystemDevice : CIM_SystemDevice
{
  CIM_System        REF GroupComponent;
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

Data type: **[**CIM\_System**](https://msdn.microsoft.com/library/aa388503)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650), [**Min**](https://msdn.microsoft.com/library/aa393650) ( 1 ), [**Max**](https://msdn.microsoft.com/library/aa393650) ( 1 )
</dt> </dl>

The parent system in the association. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_LogicalDevice**](https://msdn.microsoft.com/library/aa387884)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The logical device that is an element of a system. This property is inherited from [**CIM\_Component**](https://msdn.microsoft.com/library/aa387218).

</dd> </dl>

## Remarks

Access to the **Msvm\_SystemDevice** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Requirements



|                                     |                                                                                                         |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_SystemDevice**](cim-systemdevice.md)
</dt> <dt>

[**CIM\_SystemDevice**](https://msdn.microsoft.com/library/aa388509)
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

 




