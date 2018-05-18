---
title: Win32\_ActionCheck class
description: The Win32\_ActionCheck association WMI class relates an Installer action with any locational information it requires.
ms.assetid: '5ab516e4-0c58-4403-9eb8-3f0388a3d3d8'
keywords: ["Win32_ActionCheck class", "Win32_ActionCheck class, described"]
topic_type:
- apiref
api_name:
- Win32_ActionCheck
- Win32_ActionCheck.Action
- Win32_ActionCheck.Check
api_location:
- Msiprov.dll
api_type:
- DllExport
---

# Win32\_ActionCheck class

The **Win32\_ActionCheck** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates an Installer action with any locational information it requires. This location is in the form of a file or directory specification.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_ActionCheck
{
  CIM_Action Action;
  CIM_Check  Check;
};
```

## Members

The **Win32\_ActionCheck** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ActionCheck** class has these properties.

<dl> <dt>

**Action**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Action**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the installer action.

</dd> <dt>

**Check**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Check**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650), [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Reference to the instance that represents the installer check.

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

 

 





