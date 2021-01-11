---
description: Associates a service with its hosting computer system.
ms.assetid: 888ABA71-6D67-4933-89E6-40F731AA7153
title: Msvm_HostedService class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_HostedService
- Msvm_HostedService.Antecedent
- Msvm_HostedService.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_HostedService class

Associates a service with its hosting computer system. Instances of [**Msvm\_VirtualizationManagementService**](msvm-virtualsystemmanagementservice.md) can be discovered through their association with a host.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_HostedService : CIM_HostedService
{
  CIM_ManagedElement REF Antecedent;
  CIM_Service        REF Dependent;
};
```

## Members

The **Msvm\_HostedService** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_HostedService** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the hosting computer system. This property is inherited from [**CIM\_HostedService**](/windows/desktop/CIMWin32Prov/cim-hostedservice).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Service**](/windows/desktop/CIMWin32Prov/cim-service)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the service being hosted. This property is inherited from [**CIM\_HostedService**](/windows/desktop/CIMWin32Prov/cim-hostedservice).

</dd> </dl>

## Remarks

Access to the **Msvm\_HostedService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dt>

[**CIM\_HostedService**](/windows/desktop/CIMWin32Prov/cim-hostedservice)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

