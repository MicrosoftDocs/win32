---
Description: Associates a service with its hosting computer system.
ms.assetid: 888ABA71-6D67-4933-89E6-40F731AA7153
title: Msvm\_HostedService class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

Data type: **[**CIM\_ManagedElement**](https://msdn.microsoft.com/library/mt432218)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the hosting computer system. This property is inherited from [**CIM\_HostedService**](https://msdn.microsoft.com/library/aa387865).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Service**](https://msdn.microsoft.com/library/aa388442)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to the service being hosted. This property is inherited from [**CIM\_HostedService**](https://msdn.microsoft.com/library/aa387865).

</dd> </dl>

## Remarks

Access to the **Msvm\_HostedService** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

See [Querying Networking Objects](querying-networking-objects.md).

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

[**CIM\_HostedService**](cim-hostedservice.md)
</dt> <dt>

[**CIM\_HostedService**](https://msdn.microsoft.com/library/aa387865)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

 




