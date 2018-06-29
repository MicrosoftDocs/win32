---
Description: Gets the security descriptor that controls who can access a DCOM application.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5ddd563b-f731-47ac-8a13-20940adfa86d
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: GetAccessSecurityDescriptor method of the Win32\_DCOMApplicationSetting class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_DCOMApplicationSetting.GetAccessSecurityDescriptor
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetAccessSecurityDescriptor method of the Win32\_DCOMApplicationSetting class

The **GetAccessSecurityDescriptor** WMI method gets the security descriptor that controls who can access a DCOM application. The security descriptor is an instance of the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) class. The account running the script or application that calls this method must have the **SeSecurityPrivilege** and **SeRestorePrivilege** privilege. For more information, see [Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905).

## Syntax


```mof
uint32 GetAccessSecurityDescriptor(
  [out] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[out\]
</dt> <dd>

The security descriptor to set for the DCOM application.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For more information, see [WMI Return Codes](https://msdn.microsoft.com/library/aa394574) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

<dl> <dt>

**Success**
</dt> <dd>

0

Successful completion

</dd> <dt>

**2**
</dt> <dd>

The user does not have access to the requested information

</dd> <dt>

**8**
</dt> <dd>

Unknown failure

</dd> <dt>

**9**
</dt> <dd>

The user does not have adequate privileges to execute the method

</dd> <dt>

**21**
</dt> <dd>

A parameter specified in the method call is invalid

</dd> <dt>

**Other**
</dt> <dd>

1 4294967295

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) data type and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) and a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information, see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758) and [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_DCOMApplicationSetting**](win32-dcomapplicationsetting.md)
</dt> <dt>

[**Privilege Constants**](https://msdn.microsoft.com/library/aa392758)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> </dl>

 

 




