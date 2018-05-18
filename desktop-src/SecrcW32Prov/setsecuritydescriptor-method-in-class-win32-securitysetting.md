---
Description: 'The SetSecurityDescriptor&\#8194;WMI class method sets a security descriptor to the specified structure.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'b1a4afd0-4431-4dd1-8224-3fd92478ed6a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'SetSecurityDescriptor method of the Win32\_SecuritySetting class'
---

# SetSecurityDescriptor method of the Win32\_SecuritySetting class

The **SetSecurityDescriptor** [WMI class](https://msdn.microsoft.com/library/aa393244) method sets a security descriptor to the specified structure.

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

Expression that resolves to an instance of [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md).

</dd> </dl>

## Return value

Returns a value of 0 (zero) on success, and any other number to indicate an error.

<dl> <dt>

**0**
</dt> <dd>

The request was accepted.

</dd> <dt>

**1**
</dt> <dd>

The request is not supported.

</dd> <dt>

**2**
</dt> <dd>

The user did not have the necessary access.

</dd> <dt>

**8**
</dt> <dd>

Interactive process.

</dd> <dt>

**9**
</dt> <dd>

The name specified was not valid.

</dd> <dt>

**21**
</dt> <dd>

Parameters passed to the service are not valid.

</dd> </dl>

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

[**Win32\_SecuritySetting**](win32-securitysetting.md)
</dt> </dl>

 

 




