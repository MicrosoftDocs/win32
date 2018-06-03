---
title: Win32\_SettingCheck class
description: The Win32\_SettingCheck abstract, association WMI class relates an Installer check with any setting information it requires.
ms.assetid: f783b38b-0246-406e-94f5-5a60835c632c
keywords:
- Win32_SettingCheck class
- Win32_SettingCheck class, described
topic_type:
- apiref
api_name:
- Win32_SettingCheck
- Win32_SettingCheck.Check
- Win32_SettingCheck.Setting
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

# Win32\_SettingCheck class

The **Win32\_SettingCheck** abstract, association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer check with any setting information it requires.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
class Win32_SettingCheck
{
  CIM_Check   REF Check;
  CIM_Setting REF Setting;
};
```

## Members

The **Win32\_SettingCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SettingCheck** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) instance.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Setting**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reference to a [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) instance.

</dd> </dl>

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

 

 





