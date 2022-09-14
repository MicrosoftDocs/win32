---
description: An association used to represent virtual system migration network settings of the virtual system migration service.
ms.assetid: 5704dce7-1db3-4049-8c61-58bfa9596766
title: Msvm_VirtualSystemMigrationServiceSettingDataComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemMigrationServiceSettingDataComponent
- Msvm_VirtualSystemMigrationServiceSettingDataComponent.GroupComponent
- Msvm_VirtualSystemMigrationServiceSettingDataComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemMigrationServiceSettingDataComponent class

An association used to represent virtual system migration network settings of the virtual system migration service.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemMigrationServiceSettingDataComponent : CIM_Component
{
  Msvm_VirtualSystemMigrationServiceSettingData REF GroupComponent;
  Msvm_VirtualSystemMigrationNetworkSettingData REF PartComponent;
};
```

## Members

The **Msvm\_VirtualSystemMigrationServiceSettingDataComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemMigrationServiceSettingDataComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemMigrationServiceSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("GroupComponent"), [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers)
</dt> </dl>

A reference to an instance of the [**Msvm\_VirtualSystemMigrationServiceSettingData**](msvm-virtualsystemmigrationservicesettingdata.md) class that represents the migration service settings.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemMigrationNetworkSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("PartComponent")
</dt> </dl>

A reference to an instance of the [**Msvm\_VirtualSystemMigrationNetworkSettingData**](msvm-virtualsystemmigrationnetworksettingdata.md) class that represents the migration network settings.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                    |
| Namespace<br/>                | Root\\Virtualization\\V2<br/>                                                                     |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.V2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Vmms.exe</dt> </dl>                     |



 

