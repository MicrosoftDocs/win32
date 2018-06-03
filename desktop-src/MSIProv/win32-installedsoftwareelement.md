---
title: Win32\_InstalledSoftwareElement class
description: The Win32\_InstalledSoftwareElement association WMI class allows you to identify the computer system on which a particular software element is installed.
ms.assetid: ee7e77d5-6767-463f-96e5-557d89543b61
keywords:
- Win32_InstalledSoftwareElement class
- Win32_InstalledSoftwareElement class, described
topic_type:
- apiref
api_name:
- Win32_InstalledSoftwareElement
- Win32_InstalledSoftwareElement.Software
- Win32_InstalledSoftwareElement.System
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

# Win32\_InstalledSoftwareElement class

The **Win32\_InstalledSoftwareElement** association [WMI class](https://msdn.microsoft.com/library/aa393244) allows you to identify the computer system on which a particular software element is installed.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_InstalledSoftwareElement : CIM_InstalledSoftwareElement
{
  Win32_SoftwareElement REF Software;
  CIM_ComputerSystem    REF System;
};
```

## Members

The **Win32\_InstalledSoftwareElement** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_InstalledSoftwareElement** class has these properties.

<dl> <dt>

**Software**
</dt> <dd> <dl> <dt>

Data type: **Win32\_SoftwareElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Dynamic**](https://msdn.microsoft.com/library/aa393651), [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing the installed software element.

</dd> <dt>

**System**
</dt> <dd> <dl> <dt>

Data type: **CIM\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651), [**Max**](https://msdn.microsoft.com/library/aa393650) (1), [**Dynamic**](https://msdn.microsoft.com/library/aa393651), [**Min**](https://msdn.microsoft.com/library/aa393650) (0), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing the computer system hosting a particular software element.

</dd> </dl>

## Remarks

The **Win32\_InstalledSoftwareElement** class is derived from [**CIM\_InstalledSoftwareElement**](https://msdn.microsoft.com/library/aa387870).

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

 

 





