---
description: Associates a virtual system a snapshot of the virtual system.
ms.assetid: f85f6914-dbb8-42c9-a732-11d48613c15c
title: CIM_SnapshotOfVirtualSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CIM_SnapshotOfVirtualSystem
- CIM_SnapshotOfVirtualSystem.Antecedent
- CIM_SnapshotOfVirtualSystem.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# CIM\_SnapshotOfVirtualSystem class

Associates a virtual system a snapshot of the virtual system.

## Syntax

``` syntax
[Association, Abstract, Version("2.22.0"), AMENDMENT]
class CIM_SnapshotOfVirtualSystem : CIM_Dependency
{
  CIM_ComputerSystem           REF Antecedent;
  CIM_VirtualSystemSettingData REF Dependent;
};
```

## Members

The **CIM\_SnapshotOfVirtualSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_SnapshotOfVirtualSystem** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Antecedent"), [**Min**](/windows/desktop/WmiSdk/standard-qualifiers) (0), [**Max**](/windows/desktop/WmiSdk/standard-qualifiers) (1)
</dt> </dl>

A reference to the computer system that represents the virtual system.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Dependent")
</dt> </dl>

A reference to the settings data object that represents the snapshot of the virtual system.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                          |
| Namespace<br/>                | Root\\virtualization\\v2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

