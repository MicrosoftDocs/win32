---
title: Msvm\_HostedDependency class
description: Associates a virtual computer system instance with the computer system object representing the physical, hosting system.
ms.assetid: '02f0818e-d234-48d1-b6b0-67e54857a215'
keywords: ["Msvm_HostedDependency class Hyper-V", "Msvm_HostedDependency class Hyper-V , described"]
topic_type:
- apiref
api_name:
- Msvm_HostedDependency
- Msvm_HostedDependency.Antecedent
- Msvm_HostedDependency.Dependent
api_location:
- Root\Virtualization
api_type:
- Schema
---

# Msvm\_HostedDependency class

Associates a virtual computer system instance with the computer system object representing the physical, hosting system.

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

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Max**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

A reference to the hosting computer system.

This property is inherited from [**CIM\_HostedDependency**](cim-hosteddependency.md).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the virtual computer system.

This property is inherited from [**CIM\_HostedDependency**](cim-hosteddependency.md).

</dd> </dl>

## Remarks

Access to the **Msvm\_HostedDependency** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

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

[**CIM\_HostedDependency**](cim-hosteddependency.md)
</dt> <dt>

[**CIM\_HostedDependency**](https://msdn.microsoft.com/library/mt446122)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 





