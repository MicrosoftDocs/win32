---
Description: 'The Win32\_LoggedOnUser association WMI class relates a session and a user account.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b1233f90-4898-4ced-84d2-0858027e935a'
ms.prod: 'windows-server-dev'
ms.technology:
- cimwin32
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'Win32\_LoggedOnUser class'
---

# Win32\_LoggedOnUser class

The **Win32\_LoggedOnUser** association [WMI class](https://msdn.microsoft.com/library/aa393244) relates a session and a user account.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8BB5B3EC-E1F7-4b39-942A-605D5F55789A}"), AMENDMENT]
class Win32_LoggedOnUser : CIM_Dependency
{
  Win32_LogonSession REF Dependent;
  Win32_Account      REF Antecedent;
};
```

## Members

The **Win32\_LoggedOnUser** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_LoggedOnUser** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Account**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Antecedent), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**Win32\_Account**](win32-account.md) that describes the account used in the initiation of this session. The account could be either a user account or a system account.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogonSession**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) (Dependent), [**key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

A [**Win32\_LogonSession**](win32-logonsessionmappeddisk.md) that describes the session that the account is currently using.

</dd> </dl>

## Remarks

The **Win32\_LoggedOnUser** class is derived from [**CIM\_Dependency**](cim-dependency.md).

## Examples

The [get-loggedonuser function](https://Gallery.TechNet.Microsoft.Com/scriptcenter/0e43993a-895a-4afe-a2b2-045a5146048a) PowerShell sample gets the logged on users on a local or remote computer, with session information.

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

 

 




