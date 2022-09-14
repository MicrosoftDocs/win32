---
description: Represents the association between a team ExternalEthernetPort and a member ExternalEthernetPort.
ms.assetid: e21bea94-d6a8-4788-958e-78ce255837aa
title: Msvm_VirtualEthernetSwitchNicTeamingMember class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualEthernetSwitchNicTeamingMember
- Msvm_VirtualEthernetSwitchNicTeamingMember.Antecedent
- Msvm_VirtualEthernetSwitchNicTeamingMember.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualEthernetSwitchNicTeamingMember class

Represents the association between a team ExternalEthernetPort and a member ExternalEthernetPort.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualEthernetSwitchNicTeamingMember : CIM_Dependency
{
  Msvm_ExternalEthernetPort REF Antecedent;
  Msvm_ExternalEthernetPort REF Dependent;
};
```

## Members

The **Msvm\_VirtualEthernetSwitchNicTeamingMember** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualEthernetSwitchNicTeamingMember** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ExternalEthernetPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

An [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md) that references the team external ethernet port instance.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_ExternalEthernetPort**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

Reference to the member [**Msvm\_ExternalEthernetPort**](msvm-externalethernetport.md) instance.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

