---
description: Associates a network adapter with its hardware data.
ms.assetid: 8a20c1d6-358a-41c4-b318-fbd7d43d7dc6
title: MSFT\_NetAdapterHardwareInfoElementSetting class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapterHardwareInfoElementSetting
- MSFT_NetAdapterHardwareInfoElementSetting.IsDefault
- MSFT_NetAdapterHardwareInfoElementSetting.IsCurrent
- MSFT_NetAdapterHardwareInfoElementSetting.IsNext
- MSFT_NetAdapterHardwareInfoElementSetting.IsMinimum
- MSFT_NetAdapterHardwareInfoElementSetting.IsMaximum
- MSFT_NetAdapterHardwareInfoElementSetting.ManagedElement
- MSFT_NetAdapterHardwareInfoElementSetting.SettingData
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapterHardwareInfoElementSetting class

Associates a network adapter with its hardware data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapterHardwareInfoElementSetting : MSFT_NetAdapterElementSettingData
{
  uint16                                 REF IsDefault;
  uint16                                 REF IsCurrent;
  uint16                                 REF IsNext;
  uint16                                 REF IsMinimum = 0;
  uint16                                 REF IsMaximum = 0;
  MSFT_NetAdapter                        REF ManagedElement;
  MSFT_NetAdapterHardwareInfoSettingData REF SettingData;
};
```

## Members

The **MSFT\_NetAdapterHardwareInfoElementSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapterHardwareInfoElementSetting** class has these properties.

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

**IsMaximum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated SettingData instance. All other properties of the associated SettingData instance are not affected by this property. Note: It is assumed that the semantics of each property of this set are designed to be compared mathematically. When IsMaximum = "Is Maximum", this property indicates that the affected property values specified in the associated SettingData instance shall define maximum setting values. When IsMaximum = "Is Not Maximum", this property indicates that the affected property values specified in the associated SettingData instance shall not define maximum setting values. When IsMaximum = "Unknown", this property indicates that the affected property values specified in the associated SettingData instance may correspond to maximum setting values. When IsMaximum = "Not Applicable", this property indicates that the affected property values specified in the associated SettingData instance shall not be interpreted with respect to whether each defines a maximum.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)
</dt> <dt>

<span id="Is_Maximum"></span><span id="is_maximum"></span><span id="IS_MAXIMUM"></span>**Is Maximum** (2)
</dt> <dt>

<span id="Is_Not_Maximum"></span><span id="is_not_maximum"></span><span id="IS_NOT_MAXIMUM"></span>**Is Not Maximum** (3)
</dt> </dl>

</dd> <dt>

**IsMinimum**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property affects the interpretation of all non-null, non-enumerated, non-binary, numeric, non-key properties of the associated SettingData instance. All other properties of the associated SettingData instance are not affected by this property. Be aware that it is assumed that the semantics of each property of this set are designed to be compared mathematically. When IsMinimum = "Is Minimum", this property indicates that the affected property values specified in the associated SettingData instance shall define minimum setting values. When IsMinimum = "Is Not Minimum", this property indicates that the affected property values specified in the associated SettingData instance shall not define minimum setting values. When IsMinimum = "Unknown", this property indicates that the affected property values specified in the associated SettingData instance may correspond to minimum setting values. When IsMinimum = "Not Applicable", this property indicates that the affected property values specified in the associated SettingData instance shall not be interpreted with respect to whether each defines a minimum.

This property inherits from [**CIM\_ElementSettingData**](/previous-versions/windows/desktop/virtual/cim-elementsettingdata).

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Not_Applicable"></span><span id="not_applicable"></span><span id="NOT_APPLICABLE"></span>**Not Applicable** (1)
</dt> <dt>

<span id="Is_Minimum"></span><span id="is_minimum"></span><span id="IS_MINIMUM"></span>**Is Minimum** (2)
</dt> <dt>

<span id="Is_Not_Minimum"></span><span id="is_not_minimum"></span><span id="IS_NOT_MINIMUM"></span>**Is Not Minimum** (3)
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

A reference to the managed element. This property inherits from [**MSFT\_NetAdapterElementSettingData**](msft-netadapterelementsettingdata.md).

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_NetAdapterHardwareInfoSettingData**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

A reference to the hardware information setting data for the network adapter.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

