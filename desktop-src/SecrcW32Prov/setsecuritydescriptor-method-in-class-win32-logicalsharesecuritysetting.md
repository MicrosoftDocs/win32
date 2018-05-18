---
Description: 'The SetSecurityDescriptor&\#8194;WMI class method sets a security descriptor to a specified structure.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'e067f6e3-f748-457c-b579-6d7b05a4a8a0'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetSecurityDescriptor method of the Win32\_LogicalShareSecuritySetting class'
---

# SetSecurityDescriptor method of the Win32\_LogicalShareSecuritySetting class

The **SetSecurityDescriptor** [WMI class](https://msdn.microsoft.com/library/aa393244) method sets a security descriptor to a specified structure.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetSecurityDescriptor(
  [in] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

An expression that resolves to an instance of a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md).

</dd> </dl>

## Return value

The **SetSecurityDescriptor** method can return the error codes listed in the following list. For more information, see [WMI Return Codes](https://msdn.microsoft.com/library/aa394574).

<dl> <dt>

**Success**
</dt> <dd>

0

Successful completion.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user does not have access to the requested information.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Unknown failure.

</dd> <dt>

**Privilege missing**
</dt> <dd>

9

The user does not have adequate privileges.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

The specified parameter is not valid.

</dd> <dt>

**Other**
</dt> <dd>

22–4294967295

</dd> </dl>

## Remarks

For a VBScript code example of how to get the security descriptor, change it, and write it back, see [**SetSecurityDescriptor Method in Class Win32\_LogicalFileSecuritySetting**](setsecuritydescriptor-method-in-class-win32-logicalfilesecuritysetting.md).

The **SeSecurityPrivilege** privilege is required to execute this method. For more information, see [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

When a new [*security access control list (SACL)*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) is not specified in a call to a **SetSecurityDescriptor** method, then the security descriptor SACL on the target securable object is set to **NULL** so that the previous SACL setting does not persist.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_LogicalShareSecuritySetting**](win32-logicalsharesecuritysetting.md)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[**Win32\_SecurityDescriptor**](win32-securitydescriptor.md)
</dt> <dt>

[Maintaining WMI Security](https://msdn.microsoft.com/library/aa392291)
</dt> </dl>

 

 




