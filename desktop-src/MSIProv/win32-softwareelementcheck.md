---
title: Win32\_SoftwareElementCheck class
description: This Win32\_SoftwareElementCheck association WMI class relates an Installer element with any condition or locational information that a feature may require.
ms.assetid: f1f0ad6f-f907-40f4-89e7-0921001d14e2
keywords:
- Win32_SoftwareElementCheck class
- Win32_SoftwareElementCheck class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareElementCheck
- Win32_SoftwareElementCheck.Check
- Win32_SoftwareElementCheck.Element
- Win32_SoftwareElementCheck.Phase
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

# Win32\_SoftwareElementCheck class

This **Win32\_SoftwareElementCheck** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer element with any condition or locational information that a feature may require.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareElementCheck : CIM_SoftwareElementChecks
{
  CIM_Check             REF Check;
  Win32_SoftwareElement REF Element;
  uint16                    Phase;
};
```

## Members

The **Win32\_SoftwareElementCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SoftwareElementCheck** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to a [**CIM\_Check**](https://msdn.microsoft.com/library/aa387206) instance.

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

</dd> <dt>

**Phase**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Referenced check is an in-state check or a next-state check.



| Value                                                                                                | Meaning               |
|------------------------------------------------------------------------------------------------------|-----------------------|
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | In-State<br/>   |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Next-State<br/> |



 

</dd> </dl>

## Remarks

The **Win32\_SoftwareElementCheck** class is derived from [**CIM\_SoftwareElementChecks**](https://msdn.microsoft.com/library/aa388470).

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

 

 





