---
title: Win32\_CheckCheck class
description: This Win32\_CheckCheck association WMI class relates an Installer action with any locational information it requires.
ms.assetid: '758cbc7c-33f4-42bb-9185-7832c0437464'
keywords: ["Win32_CheckCheck class", "Win32_CheckCheck class, described"]
topic_type:
- apiref
api_name:
- Win32_CheckCheck
- Win32_CheckCheck.Check
- Win32_CheckCheck.Location
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_CheckCheck class

This **Win32\_CheckCheck** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer action with any locational information it requires. This location is in the form of a file or directory specification.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_CheckCheck
{
  CIM_Action REF Check;
  CIM_Check  REF Location;
};
```

## Members

The **Win32\_CheckCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_CheckCheck** class has these properties.

<dl> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing the installer action.

</dd> <dt>

**Location**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance representing the location, in the form of a file or directory specification.

</dd> </dl>

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

 

 





