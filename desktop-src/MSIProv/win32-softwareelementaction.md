---
title: Win32\_SoftwareElementAction class
description: This Win32\_SoftwareElementAction association WMI class relates an Installer software element with an action that access the element.
ms.assetid: 0ff9726b-4edd-4219-a131-0fab88c91565
keywords:
- Win32_SoftwareElementAction class
- Win32_SoftwareElementAction class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareElementAction
- Win32_SoftwareElementAction.Action
- Win32_SoftwareElementAction.Element
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_SoftwareElementAction class

This **Win32\_SoftwareElementAction** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer software element with an action that access the element.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareElementAction : CIM_SoftwareElementActions
{
  CIM_Action            REF Action;
  Win32_SoftwareElement REF Element;
};
```

## Members

The **Win32\_SoftwareElementAction** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareElementAction** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_Action**](https://msdn.microsoft.com/library/aa386541) instance.

</dd> <dt>

**Element**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**Win32\_SoftwareElement**](win32-softwareelement.md) instance.

</dd> </dl>

## Remarks

The **Win32\_SoftwareElementAction** class is derived from [**CIM\_SoftwareElementActions**](https://msdn.microsoft.com/library/aa388468).

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

 

 





