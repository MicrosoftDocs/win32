---
Description: Associates a virtual machine instance with the computer system object that represents the physical, hosting system.
ms.assetid: 755624D7-04D0-47EA-8623-DEDE6B1D5CBC
title: Msvm_HostedDependency class
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_HostedDependency
- Msvm_HostedDependency.Antecedent
- Msvm_HostedDependency.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_HostedDependency class

Associates a virtual machine instance with the computer system object that represents the physical, hosting system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_HostedDependency : CIM_HostedDependency
{
  CIM_ManagedElement REF Antecedent;
  CIM_ManagedElement REF Dependent;
};
```

## Members

The **Msvm\_HostedDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_HostedDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the hosting computer system. This property is inherited from [**CIM\_HostedDependency**](https://msdn.microsoft.com/library/cc136861).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the virtual machine. This property is inherited from [**CIM\_HostedDependency**](https://msdn.microsoft.com/library/cc136861).

</dd> </dl>

## Remarks

Access to the **Msvm\_HostedDependency** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[**CIM\_HostedDependency**](https://msdn.microsoft.com/library/cc136861)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 




