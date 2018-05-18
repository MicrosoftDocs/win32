---
Description: 'The Win32\_LogicalProgramGroupItemDataFile association WMI class relates the program group items of the Start menu and the files in which they are stored.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '9327c205-d0ad-4f2b-a65e-2a648e7c13e0'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_LogicalProgramGroupItemDataFile class'
---

# Win32\_LogicalProgramGroupItemDataFile class

The **Win32\_LogicalProgramGroupItemDataFile** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates the program group items of the **Start** menu and the files in which they are stored.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), Privileges("SeRestorePrivilege"), UUID("{08FFAD62-8050-11d2-90CE-0060081A46FD}"), AMENDMENT]
class Win32_LogicalProgramGroupItemDataFile : CIM_Dependency
{
  Win32_LogicalProgramGroupItem REF Antecedent;
  CIM_DataFile                  REF Dependent;
};
```

## Members

The **Win32\_LogicalProgramGroupItemDataFile** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogicalProgramGroupItemDataFile** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalProgramGroupItem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("WMI\|Win32\_LogicalProgramGroupItem")
</dt> </dl>

Reference to the instance representing the program groupings in the **Start** menu.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_DataFile**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**MappingStrings**](https://msdn.microsoft.com/library/aa393650) ("CIM\|CIM\_DataFile")
</dt> </dl>

Reference to the instance representing the class associated with the program group.

</dd> </dl>

## Remarks

The **Win32\_LogicalProgramGroupItemDataFile** class is derived from [**CIM\_Dependency**](cim-dependency.md).

The calling process that uses this class must have the **SE\_RESTORE\_NAME** privilege on the computer in which the registry resides. For example, if you enumerate this class on the local computer, the account under which your application runs must have this privilege. For more information, see [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> </dl>

 

 




