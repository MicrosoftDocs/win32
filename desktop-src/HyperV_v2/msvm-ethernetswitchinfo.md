---
description: Defines the association between an Ethernet switch and a switch resource.
ms.assetid: fb29f4cb-50c4-4865-b267-21ff99bb4a8b
title: Msvm_EthernetSwitchInfo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_EthernetSwitchInfo
- Msvm_EthernetSwitchInfo.Antecedent
- Msvm_EthernetSwitchInfo.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_EthernetSwitchInfo class

Defines the association between an Ethernet switch and a switch resource.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_EthernetSwitchInfo : CIM_Dependency
{
  Msvm_VirtualEthernetSwitch REF Antecedent;
  Msvm_EthernetSwitchData    REF Dependent;
};
```

## Members

The **Msvm\_EthernetSwitchInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_EthernetSwitchInfo** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualEthernetSwitch**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent")
</dt> </dl>

A reference to the [**Msvm\_VirtualEthernetSwitch**](msvm-virtualethernetswitch.md) class that represents the hosting system. This property is derived from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_EthernetSwitchData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A reference to the [**Msvm\_EthernetSwitchData**](msvm-ethernetswitchdata.md) class that represents the switch resource. This property is derived from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

