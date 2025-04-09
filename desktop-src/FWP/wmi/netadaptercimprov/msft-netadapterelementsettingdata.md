---
description: Associates a network port with its configuration data.
ms.assetid: 626ffadb-5bb3-47e5-9ede-a6dd0c614428
title: MSFT\_NetAdapterElementSettingData class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterElementSettingData
- MSFT_NetAdapterElementSettingData.IsDefault
- MSFT_NetAdapterElementSettingData.IsCurrent
- MSFT_NetAdapterElementSettingData.IsNext
- MSFT_NetAdapterElementSettingData.ManagedElement
- MSFT_NetAdapterElementSettingData.SettingData
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterElementSettingData class

Associates a network port with its configuration data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetAdapterElementSettingData : CIM_ElementSettingData
{
  uint16                     REF IsDefault;
  uint16                     REF IsCurrent;
  uint16                     REF IsNext;
  MSFT_NetAdapter            REF ManagedElement;
  MSFT_NetAdapterSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetAdapterElementSettingData** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterElementSettingData** class has these properties.

<dl> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is currently used in the operation of the element or that this information is unknown. For a given managed element and all instances of a setting data subclass, there shall be at most one instance of ElementSettingData which references the managed element and an instance of the SettingData subclass where there is a specified non-null, non-key property of the SettingData subclass, and the IsMaximum property on the referencing ElementSettingData instance has a value of "Is Maximum" or the IsMinimum property on the referencing ElementSettingData instance has a value of "Is Minimum" and the IsCurrent property on the referencing ElementSettingData instance has a value of "Is Current".

There shall be at most one instance of ElementSettingData which references a managed element and an instance of a SettingData subclass where the IsCurrent property has a value of "Is Current" and the IsMinimum property does not have a value of "Is Minimum" and the IsMaximum property does not have a value of "Is Maximum".

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

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

Indicates that the referenced setting is a default setting for the element or that this information is unknown. This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

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

Indicates whether or not the referenced setting is the next setting to be applied. For example, the application could occur on a reinitialization, reset, or reconfiguration request. This could be a permanent setting, or a setting used only one time, as indicated by the flag. If it is a permanent setting then the setting is applied every time the managed element reinitializes, until this flag is manually reset. However, if it is single use, then the flag is automatically cleared after the settings are applied.

If this flag is specified (that is, set to a value other than "Unknown"), then this takes precedence over any SettingData that may have been specified as Default. For example: If the managed element is a computer system, and the value of this flag is "Is Next", then the setting will be effective next time the system resets. Unless this flag is changed, it will persist for subsequent system resets. However, if this flag is set to "Is Next For Single Use", then this setting will only be used once and the flag would be reset after that to "Is Not Next". In the preceding example, if the system restarts in a quick succession, the setting will not be used at the second restart.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

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

Data type: **MSFT\_NetAdapter**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The managed element. This property overrides the property from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapterSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The SettingData object associated with the element. This property overrides the property from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

