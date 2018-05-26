---
title: MDM\_ConfigSetting class
description: Represents configuration settings for the oma-dm agent.
ms.assetid: 58b6ca70-3784-4859-b597-f09ff56cf326
keywords:
- MDM_ConfigSetting class MDM Settings
- MDM_ConfigSetting class MDM Settings , described
topic_type:
- apiref
api_name:
- MDM_ConfigSetting
- MDM_ConfigSetting.SettingName
- MDM_ConfigSetting.SettingValue
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDM\_ConfigSetting class

Represents configuration settings for the oma-dm agent.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_ConfigSetting
{
  string SettingName;
  string SettingValue;
};
```

## Members

The **MDM\_ConfigSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_ConfigSetting** class has these properties.

<dl> <dt>

**SettingName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

Identifies a setting by name.

</dd> <dt>

**SettingValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The value that is associated with the **SettingName** property.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





