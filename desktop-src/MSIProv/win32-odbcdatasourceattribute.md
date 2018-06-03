---
title: Win32\_ODBCDataSourceAttribute class
description: The Win32\_ODBCDataSourceAttribute association WMI class relates an Installer check with any setting information it requires.
ms.assetid: 3c4bd01e-ed3a-49e8-8148-c7e99748c5ed
keywords:
- Win32_ODBCDataSourceAttribute class
- Win32_ODBCDataSourceAttribute class, described
topic_type:
- apiref
api_name:
- Win32_ODBCDataSourceAttribute
- Win32_ODBCDataSourceAttribute.Check
- Win32_ODBCDataSourceAttribute.Setting
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_ODBCDataSourceAttribute class

The **Win32\_ODBCDataSourceAttribute** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer check with any setting information it requires.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ODBCDataSourceAttribute : Win32_SettingCheck
{
  Win32_ODBCDataSourceSpecification REF Check;
  Win32_ODBCSourceAttribute         REF Setting;
};
```

## Members

The **Win32\_ODBCDataSourceAttribute** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ODBCDataSourceAttribute** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ODBCDataSourceSpecification**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ODBCDataSourceSpecification**](win32-odbcdatasourcespecification.md) instance.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ODBCSourceAttribute**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ODBCSourceAttribute**](win32-odbcsourceattribute.md) instance.

</dd> </dl>

## Remarks

The **Win32\_ODBCDataSourceAttribute** class is derived from [**Win32\_SettingCheck**](win32-settingcheck.md).

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> </dl>

 

 





