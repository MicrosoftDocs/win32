---
Description: The Win32\_LogonSessionMappedDisk class represents an association between a logon session and the mapped logical disks defined within the session.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 013ae55e-6dd1-42fb-bcba-74d6afa1b905
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_LogonSessionMappedDisk class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_LogonSessionMappedDisk
- Win32_LogonSessionMappedDisk.Antecedent
- Win32_LogonSessionMappedDisk.Dependent
api_type: 
- DllExport
api_location: 
- cimwin32.dll
---

# Win32\_LogonSessionMappedDisk class

The Win32\_LogonSessionMappedDisk class represents an association between a logon session and the mapped logical disks defined within the session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32a"), AMENDMENT]
class Win32_LogonSessionMappedDisk : CIM_Dependency
{
  Win32_LogonSession      REF Antecedent;
  Win32_MappedLogicalDisk REF Dependent;
};
```

## Members

The **Win32\_LogonSessionMappedDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LogonSessionMappedDisk** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogonSession**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Antecedent property references a logon session.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_MappedLogicalDisk**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent"), [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The Dependent property references a mapped logical disk defined within the session referenced by the Antecedent property.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CimWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Cimwin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 




