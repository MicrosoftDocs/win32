---
title: Win32\_PowerSettingDefinitionPossibleValue class
description: Represents possible values for a power setting. Associations relate this class with the Win32\_PowerSetting instance that it describes.
ms.assetid: 3ba764e2-6282-43b2-ab71-e0dc5017bab0
keywords:
- Win32_PowerSettingDefinitionPossibleValue class
- Win32_PowerSettingDefinitionPossibleValue class, described
topic_type:
- apiref
api_name:
- Win32_PowerSettingDefinitionPossibleValue
- Win32_PowerSettingDefinitionPossibleValue.InstanceID
- Win32_PowerSettingDefinitionPossibleValue.ElementName
- Win32_PowerSettingDefinitionPossibleValue.SettingIndex
- Win32_PowerSettingDefinitionPossibleValue.UInt32Value
- Win32_PowerSettingDefinitionPossibleValue.UInt64Value
- Win32_PowerSettingDefinitionPossibleValue.StringValue
- Win32_PowerSettingDefinitionPossibleValue.BinaryValue
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

# Win32\_PowerSettingDefinitionPossibleValue class

Represents possible values for a power setting. Associations relate this class with the [**Win32\_PowerSetting**](win32-powersetting.md) instance that it describes.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDefinitionPossibleValue : CIM_SettingData
{
  string InstanceID;
  string ElementName;
  uint32 SettingIndex;
  uint32 UInt32Value;
  uint32 UInt64Value;
  string StringValue;
  uint8  BinaryValue[];
};
```

## Members

The **Win32\_PowerSettingDefinitionPossibleValue** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDefinitionPossibleValue** class has these properties.

<dl> <dt>

**BinaryValue**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the possible value that is expressed as a binary array. This value is **NULL** if the type of this value is not a binary value.

</dd> <dt>

**ElementName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the friendly name of the possible value setting.

</dd> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for power setting definition possible value instance.

The **InstanceID** string must be in the following format: "PowerSettingDefinitionPossibleValue\\{Definition\_GUID}".

</dd> <dt>

**SettingIndex**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the possible value that is expressed as an integer index. This property is used when the possible value represents a discrete value.

</dd> <dt>

**StringValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the possible value that is expressed as a string. This value is **NULL** if the type of this value is not a string.

</dd> <dt>

**UInt32Value**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the possible value that is expressed as an unsigned 32-bit integer.

</dd> <dt>

**UInt64Value**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies the value of the possible value that is expressed as an unsigned 64-bit integer.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





