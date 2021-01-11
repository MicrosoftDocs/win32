---
description: Defines the association between an installed Ethernet switch extension and an Ethernet switch extension.
ms.assetid: 306658ed-03a4-49fa-8704-f4b83a4bdd4f
title: Msvm_ConcreteDependency class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ConcreteDependency
- Msvm_ConcreteDependency.Antecedent
- Msvm_ConcreteDependency.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ConcreteDependency class

Defines the association between an installed Ethernet switch extension and an Ethernet switch extension.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ConcreteDependency : CIM_ConcreteDependency
{
  Msvm_InstalledEthernetSwitchExtension REF Antecedent;
  Msvm_EthernetSwitchExtension          REF Dependent;
};
```

## Members

The **Msvm\_ConcreteDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ConcreteDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_InstalledEthernetSwitchExtension**](msvm-installedethernetswitchextension.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A reference to an instance of the [**Msvm\_InstalledEthernetSwitchExtension**](msvm-installedethernetswitchextension.md) class that represents a virtual Ethernet switch extension component installed on the system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_EthernetSwitchExtension**](msvm-ethernetswitchextension.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A reference to an instance of the [**Msvm\_EthernetSwitchExtension**](msvm-ethernetswitchextension.md) class that represents the occurrence of the **Antecedent** bound to a specific virtual Ethernet switch.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

