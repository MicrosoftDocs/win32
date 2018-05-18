---
title: Win32\_ODBCDriverAttribute class
description: The Win32\_ODBCDriverAttribute association WMI class relates an Installer check with any setting information it requires.
ms.assetid: '6d89f523-5aeb-449f-8637-45ff41f8fa5f'
keywords: ["Win32_ODBCDriverAttribute class", "Win32_ODBCDriverAttribute class, described"]
topic_type:
- apiref
api_name:
- Win32_ODBCDriverAttribute
- Win32_ODBCDriverAttribute.Check
- Win32_ODBCDriverAttribute.Setting
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ODBCDriverAttribute class

The **Win32\_ODBCDriverAttribute** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer check with any setting information it requires.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ODBCDriverAttribute : Win32_SettingCheck
{
  Win32_ODBCDriverSpecification REF Check;
  Win32_ODBCAttribute           REF Setting;
};
```

## Members

The **Win32\_ODBCDriverAttribute** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ODBCDriverAttribute** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ODBCDriverSpecification**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ODBCDriverSpecification**](win32-odbcdriverspecification.md) instance.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ODBCAttribute**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ODBCAttribute**](win32-odbcattribute.md) instance.

</dd> </dl>

## Remarks

The **Win32\_ODBCDriverAttribute** class is derived from [**Win32\_SettingCheck**](win32-settingcheck.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





