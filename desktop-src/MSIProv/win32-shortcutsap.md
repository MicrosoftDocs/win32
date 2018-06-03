---
title: Win32\_ShortcutSAP class
description: The Win32\_ShortcutSAP association WMI class relates the connection between an application access point and the corresponding shortcut.
ms.assetid: ca7d75a6-8072-4a12-829d-52a59ec180f5
keywords:
- Win32_ShortcutSAP class
- Win32_ShortcutSAP class, described
topic_type:
- apiref
api_name:
- Win32_ShortcutSAP
- Win32_ShortcutSAP.Action
- Win32_ShortcutSAP.Element
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

# Win32\_ShortcutSAP class

The **Win32\_ShortcutSAP** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the connection between an application access point and the corresponding shortcut.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ShortcutSAP
{
  Win32_ShortcutAction    REF Action;
  Win32_CommandLineAccess REF Element;
};
```

## Members

The **Win32\_ShortcutSAP** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ShortcutSAP** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ShortcutAction**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_ShortcutAction**](win32-shortcutaction.md) instance.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_CommandLineAccess**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_CommandLineAccess**](win32-commandlineaccess.md) instance.

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

 

 





