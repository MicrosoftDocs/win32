---
description: The Win32\_COMSetting abstract WMI class represents the settings associated with a Component Object Model (COM) component or COM application.
ms.assetid: e8cdbee8-41ab-4aff-b17b-707667138411
ms.tgt_platform: multiple
title: Win32_COMSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_COMSetting
- Win32_COMSetting.Caption
- Win32_COMSetting.Description
- Win32_COMSetting.SettingID
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_COMSetting class

The **Win32\_COMSetting** abstract [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents the settings associated with a Component Object Model (COM) component or COM application.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[abstract, UUID("{E5D8A560-F6C0-11d2-B35E-00105A1F8569}"), AMENDMENT]
class Win32_COMSetting : CIM_Setting
{
  string Caption;
  string Description;
  string SettingID;
};
```

## Members

The **Win32\_COMSetting** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_COMSetting** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> </dl>

## Remarks

The **Win32\_COMSetting** class is derived from [**CIM\_Setting**](cim-setting.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Setting**](cim-setting.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> </dl>

 

