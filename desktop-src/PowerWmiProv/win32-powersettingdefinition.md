---
title: Win32\_PowerSettingDefinition class
description: Represents a power setting definition.
ms.assetid: '5cb52048-72b4-455c-a1a2-864394d68047'
keywords: ["Win32_PowerSettingDefinition class", "Win32_PowerSettingDefinition class, described"]
topic_type:
- apiref
api_name:
- Win32_PowerSettingDefinition
- Win32_PowerSettingDefinition.InstanceID
api_location:
- PowerWmiProvider.dll
api_type:
- DllExport
---

# Win32\_PowerSettingDefinition class

Represents a power setting definition. It extends the [**CIM\_Capabilities**](https://msdn.microsoft.com/library/cc136806) class and is used to define a power setting. An association links this object with the [**Win32\_PowerSetting**](win32-powersetting.md) that it defines. Associations are also created that link the **Win32\_PowerSettingDefinition** object with objects that define the power setting. These will be either [**Win32\_PowerSettingDefinitionPossibleValue**](win32-powersettingdefinitionpossiblevalue.md) objects for discrete settings or [**Win32\_PowerSettingDefinitionRangeData**](win32-powersettingdefinitionrangedata.md) objects for settings that are ranges.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Provider("PowerWmiProvider"), Dynamic]
class Win32_PowerSettingDefinition : CIM_Capabilities
{
  string InstanceID;
};
```

## Members

The **Win32\_PowerSettingDefinition** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PowerSettingDefinition** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the unique identifier for the power setting definition.

The **InstanceID** string must be in the following format: "Microsoft:SettingDefinition\\{Definition\_GUID}".

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
| Namespace<br/>                | Root\\CIMV2\\power<br/>                                                                   |
| MOF<br/>                      | <dl> <dt>PowerWmiProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>PowerWmiProvider.dll</dt> </dl> |



 

 





