---
title: Win32\_PowerSettingDefinitionRangeData class
description: Represents the possible range data values for a power setting. Associations relate this class with the Win32\_PowerSetting instance it describes.
ms.assetid: fd350e07-360a-498e-8a33-69d0f38f5bd0
keywords:
- Win32_PowerSettingDefinitionRangeData class
- Win32_PowerSettingDefinitionRangeData class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingDefinitionRangeData
- Win32_PowerSettingDefinitionRangeData.Description
- Win32_PowerSettingDefinitionRangeData.InstanceID
- Win32_PowerSettingDefinitionRangeData.ElementName
- Win32_PowerSettingDefinitionRangeData.SettingValue
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_PowerSettingDefinitionRangeData class

Represents the possible range data values for a power setting. Associations relate this class with the [**Win32\_PowerSetting**](win32-powersetting.md) instance it describes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDefinitionRangeData : CIM_SettingData
{
  string Description;
  string InstanceID;
  string ElementName;
  uint32 SettingValue;
};
```

## Members

The **Win32\_PowerSettingDefinitionRangeData** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDefinitionRangeData** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the description of the range data type.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the range value defines the minimum (ValueMin), maximum (ValueMax), or increment value (ValueIncrement) of the range.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for the power setting definition range data instance.

The **InstanceID** string must be in the following format: "Microsoft:PowerSettingDefinitionRangeData\\{value\_type}\\{Definition\_GUID}". The {value\_type} portion of the string corresponds to a minimum, maximum, or increment value, and the {Definition\_GUID) portion corresponds to the unique GUID.

</dd> <dt>

**SettingValue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the range data expressed as an integer.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





