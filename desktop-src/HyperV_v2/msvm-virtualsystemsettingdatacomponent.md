---
description: A generic association used to establish part of relationships between one instance of CIM\_VirtualSystemSettingData and one or more instances of CIM\_ResourceAllocationSettingData.
ms.assetid: 936B41E7-1B3B-4A7B-86F0-E2F4497CE610
title: Msvm_VirtualSystemSettingDataComponent class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_VirtualSystemSettingDataComponent
- Msvm_VirtualSystemSettingDataComponent.GroupComponent
- Msvm_VirtualSystemSettingDataComponent.PartComponent
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_VirtualSystemSettingDataComponent class

A generic association used to establish 'part of' relationships between one instance of [**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85)) and one or more instances of [**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata).

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_VirtualSystemSettingDataComponent : CIM_VirtualSystemSettingDataComponent
{
  CIM_VirtualSystemSettingData      REF GroupComponent;
  CIM_ResourceAllocationSettingData REF PartComponent;
};
```

## Members

The **Msvm\_VirtualSystemSettingDataComponent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_VirtualSystemSettingDataComponent** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_VirtualSystemSettingData**](/previous-versions//cc136954(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Override**, **Min** (1), **Max** (1)
</dt> </dl>

The parent element in the association. This property is inherited from [**CIM\_VirtualSystemSettingDataComponent**](/previous-versions//cc150674(v=vs.85)).

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ResourceAllocationSettingData**](/previous-versions/windows/desktop/clushyperv/cim-resourceallocationsettingdata)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The child element in the association. This property is inherited from [**CIM\_VirtualSystemSettingDataComponent**](/previous-versions//cc150674(v=vs.85)).

</dd> </dl>

## Remarks

Access to the **Msvm\_VirtualSystemSettingDataComponent** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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

[**CIM\_VirtualSystemSettingDataComponent**](cim-virtualsystemsettingdatacomponent.md)
</dt> <dt>

[**CIM\_VirtualSystemSettingDataComponent**](/previous-versions//cc150674(v=vs.85))
</dt> <dt>

[Virtual System Classes](virtual-system-classes.md)
</dt> </dl>

 

