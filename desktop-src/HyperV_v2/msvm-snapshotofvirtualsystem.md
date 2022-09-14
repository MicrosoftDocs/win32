---
description: Associates a virtual system with a snapshot that was captured from the virtual system.
ms.assetid: CF1C1C04-02BC-4AC3-8327-FEE54ECE8541
title: Msvm_SnapshotOfVirtualSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_SnapshotOfVirtualSystem
- Msvm_SnapshotOfVirtualSystem.Antecedent
- Msvm_SnapshotOfVirtualSystem.Dependent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_SnapshotOfVirtualSystem class

Associates a virtual system with a snapshot that was captured from the virtual system.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_SnapshotOfVirtualSystem : CIM_SnapshotOfVirtualSystem
{
  Msvm_ComputerSystem           REF Antecedent;
  Msvm_VirtualSystemSettingData REF Dependent;
};
```

## Members

The **Msvm\_SnapshotOfVirtualSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_SnapshotOfVirtualSystem** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_ComputerSystem**](msvm-computersystem.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**Msvm\_ComputerSystem**](msvm-computersystem.md) class that represents the virtual system. This property is derived from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **[**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A reference to an instance of the [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) class that represents the snapshot. This property is derived from [**CIM\_Dependency**](/windows/desktop/CIMWin32Prov/cim-dependency).

</dd> </dl>

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

[**CIM\_SnapshotOfVirtualSystem**](cim-snapshotofvirtualsystem.md)
</dt> <dt>

[**CreateSnapshot**](createsnapshot-msvm-virtualsystemsnapshotservice.md)
</dt> </dl>

 

