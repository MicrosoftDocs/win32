---
description: Associates a managed element with its configuration data.
ms.assetid: 4DB78E43-E387-478E-999C-770B35925721
title: Msvm_ElementSettingData class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Msvm_ElementSettingData
- Msvm_ElementSettingData.ManagedElement
- Msvm_ElementSettingData.SettingData
- Msvm_ElementSettingData.IsDefault
- Msvm_ElementSettingData.IsCurrent
- Msvm_ElementSettingData.IsNext
api_type: 
- DllExport
api_location: 
- vmms.exe
---

# Msvm\_ElementSettingData class

Associates a managed element with its configuration data. Some of the more notable applications of this association are its use in linking a virtual machine and the logical devices that have been assigned to that system with their snapshot configuration information. Current configuration information is associated with the virtual machine and its devices through the [**Msvm\_SettingsDefineState**](msvm-settingsdefinestate.md) association.

The following syntax is simplified Managed Object Format (MOF) code, and it includes all of the inherited properties.

## Syntax

``` syntax
[Association, Aggregation, Dynamic, Provider("VmmsWmiInstanceAndMethodProvider"), AMENDMENT]
class Msvm_ElementSettingData : CIM_ElementSettingData
{
  CIM_ManagedElement REF ManagedElement;
  CIM_SettingData    REF SettingData;
  uint16                 IsDefault = 0;
  uint16                 IsCurrent = 0;
  uint16                 IsNext = 0;
};
```

## Members

The **Msvm\_ElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Msvm\_ElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is currently being used in the operation of the element or that this information is unknown. This property is inherited from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata). The default value is 0 (Unknown).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>**Is Current** (1)
</dt> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>**Is Not Current** (2)
</dt> </dl>

</dd> <dt>

**IsDefault**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is a default setting for the element or that this information is unknown. This property is inherited from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata). The default value is 0 (Unknown).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Default"></span><span id="is_default"></span><span id="IS_DEFAULT"></span>**Is Default** (1)
</dt> <dt>

<span id="Is_Not_Default"></span><span id="is_not_default"></span><span id="IS_NOT_DEFAULT"></span>**Is Not Default** (2)
</dt> </dl>

</dd> <dt>

**IsNext**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the referenced setting is the next setting to be applied. This property is inherited from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata). The default value is 0 (Unknown).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Next"></span><span id="is_next"></span><span id="IS_NEXT"></span>**Is Next** (1)
</dt> <dt>

<span id="Is_Not_Next"></span><span id="is_not_next"></span><span id="IS_NOT_NEXT"></span>**Is Not Next** (2)
</dt> <dt>

<span id="Is_Next_For_Single_Use"></span><span id="is_next_for_single_use"></span><span id="IS_NEXT_FOR_SINGLE_USE"></span>**Is Next For Single Use** (3)
</dt> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](/previous-versions/windows/desktop/iscsitarg/cim-managedelement)**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the virtual machine or virtual device. This property is inherited from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_SettingData**](/previous-versions//cc136911(v=vs.85))**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to the snapshotted settings for the virtual machine or virtual device. This property is inherited from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata).

</dd> </dl>

## Remarks

Access to the **Msvm\_ElementSettingData** class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](/windows/desktop/WmiSdk/user-account-control-and-wmi).

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

[**CIM\_ElementSettingData**](cim-elementsettingdata.md)
</dt> <dt>

[**CIM\_ElementSettingData**](/previous-versions/windows/desktop/iscsitarg/cim-elementsettingdata)
</dt> <dt>

[Virtual System Management Classes](virtual-system-management-classes.md)
</dt> </dl>

 

