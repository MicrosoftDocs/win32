---
Description: The GetSecurityDescriptor&\#8194;WMI class method retrieves a representation of the security descriptor as a Win32\_SecurityDescriptor for the Win32\_SecuritySetting object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 84f517da-9e70-4ab2-8490-c16b7ca3310e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: GetSecurityDescriptor method of the Win32\_SecuritySetting class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSecurityDescriptor method of the Win32\_SecuritySetting class

The **GetSecurityDescriptor** [WMI class](https://msdn.microsoft.com/library/aa393244) method retrieves a representation of the security descriptor as a [**Win32\_SecurityDescriptor**](win32-securitydescriptor.md) for the [**Win32\_SecuritySetting**](win32-securitysetting.md) object.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetSecurityDescriptor(
  [out] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[out\]
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

The parameters passed to the service are not valid.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Secrcw32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/aa392727)
</dt> <dt>

[**Win32\_SecuritySetting**](win32-securitysetting.md)
</dt> </dl>

 

 




