---
description: Associates the Msvm\_SnapshotCollection to the contained Msvm\_VirtualSystemSettingData objects.
ms.assetid: 21005e8a-0bc6-4ea7-8f6f-d79803b43bc0
title: Msvm_CollectedSnapshots class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_CollectedSnapshots
- Msvm_CollectedSnapshots.Collection
- Msvm_CollectedSnapshots.Member
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_CollectedSnapshots class

Associates the [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) to the contained [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_CollectedSnapshots : CIM_CollectedMSEs
{
  Msvm_SnapshotCollection       REF Collection;
  Msvm_VirtualSystemSettingData REF Member;
};
```

## Members

The **Msvm\_CollectedSnapshots** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_CollectedSnapshots** class has these properties.

<dl> <dt>

**Collection**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_SnapshotCollection**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Aggregate**](/windows/desktop/WmiSdk/standard-qualifiers), [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Collection")
</dt> </dl>

An [**Msvm\_SnapshotCollection**](msvm-snapshotcollection.md) grouping or 'bag' object that represents the collection.

</dd> <dt>

**Member**
</dt> <dd> <dl> <dt>

Data type: **Msvm\_VirtualSystemSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](/windows/desktop/WmiSdk/standard-qualifiers) ("Member")
</dt> </dl>

An [**Msvm\_VirtualSystemSettingData**](msvm-virtualsystemsettingdata.md) containing the members of the collection.

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

[**CIM\_CollectedMSEs**](cim-collectedmses.md)
</dt> </dl>

 

