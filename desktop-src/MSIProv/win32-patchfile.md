---
title: Win32\_PatchFile class
description: The Win32\_PatchFile association WMI class relates an Installer check with any setting information it requires.
ms.assetid: 01ea9d36-2631-425a-8ffe-109e48ffc5dd
keywords:
- Win32_PatchFile class
- Win32_PatchFile class, described
topic_type:
- apiref
api_name:
- Win32_PatchFile
- Win32_PatchFile.Check
- Win32_PatchFile.Setting
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

# Win32\_PatchFile class

The **Win32\_PatchFile** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer check with any setting information it requires.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_PatchFile : Win32_SettingCheck
{
  Win32_FileSpecification REF Check;
  Win32_Patch             REF Setting;
};
```

## Members

The **Win32\_PatchFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_PatchFile** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **Win32\_FileSpecification**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of a file specification available to the update.

</dd> <dt>

**Setting**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Patch**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the properties of the update applied to the associated file.

</dd> </dl>

## Remarks

The **Win32\_PatchFile** class is derived from [**Win32\_SettingCheck**](win32-settingcheck.md).

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

 

 





