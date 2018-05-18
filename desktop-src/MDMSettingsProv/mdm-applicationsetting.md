---
title: MDM\_ApplicationSetting class
description: Sets Windows modern application settings.
ms.assetid: '3ebe024a-5150-4705-9e73-dbc78bb4a58b'
keywords: ["MDM_ApplicationSetting class MDM Settings", "MDM_ApplicationSetting class MDM Settings , described"]
topic_type:
- apiref
api_name:
- MDM_ApplicationSetting
- MDM_ApplicationSetting.PackageFamilyName
- MDM_ApplicationSetting.SettingName
- MDM_ApplicationSetting.SettingType
- MDM_ApplicationSetting.SettingValue
api_location:
- MDMSettingsProv.dll
api_type:
- DllExport
---

# MDM\_ApplicationSetting class

Sets Windows modern application settings.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("MDMSettingsProv"), AMENDMENT]
class MDM_ApplicationSetting
{
  string PackageFamilyName;
  string SettingName;
  Uint32 SettingType;
  string SettingValue;
};
```

## Members

The **MDM\_ApplicationSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **MDM\_ApplicationSetting** class has these properties.

<dl> <dt>

**PackageFamilyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The package family name.

</dd> <dt>

**SettingName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The setting name.

</dd> <dt>

**SettingType**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The setting type.

<dt>

<span id="string"></span><span id="STRING"></span>

**string** (0)


</dt> <dd></dd> <dt>

<span id="int"></span><span id="INT"></span>

**int** (1)


</dt> <dd></dd> <dt>

<span id="bool"></span><span id="BOOL"></span>

**bool** (2)


</dt> <dd></dd> <dt>

<span id="double"></span><span id="DOUBLE"></span>

**double** (3)


</dt> <dd></dd> </dl>

</dd> <dt>

**SettingValue**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The setting value.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                         |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\CIMv2\\MDM<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>MDMSettingsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMSettingsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[Mobile Device Management Settings Classes](https://msdn.microsoft.com/library/dn610402)
</dt> </dl>

 

 





