---
title: Win32\_PowerSettingElementSettingDataIndex class
description: Represents the association between the power setting and the corresponding setting data.
ms.assetid: '1c3e5fff-4fc1-489e-8d36-2686d3ede008'
keywords: ["Win32_PowerSettingElementSettingDataIndex class", "Win32_PowerSettingElementSettingDataIndex class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerSettingElementSettingDataIndex
- Win32_PowerSettingElementSettingDataIndex.ManagedElement
- Win32_PowerSettingElementSettingDataIndex.SettingData
- Win32_PowerSettingElementSettingDataIndex.IsACSetting
- Win32_PowerSettingElementSettingDataIndex.IsCurrent
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerSettingElementSettingDataIndex class

Represents the association between the power setting and the corresponding setting data. An instance of **Win32\_PowerSettingElementSettingDataIndex** is created for each power setting value. The **IsACSetting** property determines whether the setting is the AC or DC value.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingElementSettingDataIndex : CIM_ElementSettingData
{
  Win32_PowerSetting          REF ManagedElement;
  Win32_PowerSettingDataIndex REF SettingData;
  uint16                          IsACSetting;
  uint16                          IsCurrent;
};
```

## Members

The **Win32\_PowerSettingElementSettingDataIndex** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingElementSettingDataIndex** class has these properties.

<dl> <dt>

**IsACSetting**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether the referenced setting is used when the system is running on AC power. For a given **ManagedElement** and all instances of a **SettingData** subclass, there must be at most one instance of **ElementSettingData** that references the **ManagedElement** and an instance of the **SettingData** subclass where there is a specified non-null, non-key property of the **SettingData** subclass, and the value is set to 1.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_AC_Setting"></span><span id="is_ac_setting"></span><span id="IS_AC_SETTING"></span>**Is AC Setting** (1)
</dt> <dt>

<span id="Is_Not_AC_Setting_"></span><span id="is_not_ac_setting_"></span><span id="IS_NOT_AC_SETTING_"></span>**Is Not AC Setting** (2 )
</dt> </dl>

</dd> <dt>

**IsCurrent**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates that the referenced setting is currently being used in the operation of the element or that this information is unknown.

<dl> <dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>**Unknown** (0)
</dt> <dt>

<span id="Is_Current"></span><span id="is_current"></span><span id="IS_CURRENT"></span>**Is Current** (1)
</dt> <dt>

<span id="Is_Not_Current"></span><span id="is_not_current"></span><span id="IS_NOT_CURRENT"></span>**Is Not Current** (2)
</dt> </dl>

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSetting**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the **InstanceID** of the power setting to which the setting data applies.

</dd> <dt>

**SettingData**
</dt> <dd> <dl> <dt>

Data type: **Win32\_PowerSettingDataIndex**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the **InstanceID** of the setting data that corresponds to the value of the setting.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





