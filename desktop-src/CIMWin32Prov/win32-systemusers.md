---
Description: The Win32\_SystemUsers association WMI class relates a computer system and a user account on that system.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0f6cba69-86f7-4795-a47d-6fb8ed0a00b8
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Win32_SystemUsers class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SystemUsers
- Win32_SystemUsers.GroupComponent
- Win32_SystemUsers.PartComponent
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_SystemUsers class

The **Win32\_SystemUsers** association [WMI class](https://msdn.microsoft.com/en-us/library/Aa393244(v=VS.85).aspx) relates a computer system and a user account on that system.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{8502C4F2-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_SystemUsers : CIM_SystemComponent
{
  Win32_ComputerSystem REF GroupComponent;
  Win32_UserAccount    REF PartComponent;
};
```

## Members

The **Win32\_SystemUsers** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SystemUsers** class has these properties.

<dl> <dt>

**GroupComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_ComputerSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("GroupComponent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_ComputerSystem")
</dt> </dl>

Reference to the instance representing the computer system containing the user account.

</dd> <dt>

**PartComponent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_UserAccount**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](https://msdn.microsoft.com/en-us/library/Aa392157(v=VS.85).aspx), [**Override**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("PartComponent"), [**MappingStrings**](https://msdn.microsoft.com/en-us/library/Aa393650(v=VS.85).aspx) ("WMI\|Win32\_UserAccount")
</dt> </dl>

Reference to the instance representing the user account on the computer system.

</dd> </dl>

## Remarks

The **Win32\_SystemUsers** class is derived from [**CIM\_SystemComponent**](cim-systemcomponent.md).

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

[**CIM\_SystemComponent**](cim-systemcomponent.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/en-us/library/Dn792258(v=VS.85).aspx)
</dt> </dl>

 

 




