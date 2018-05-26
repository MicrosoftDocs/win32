---
Description: Updates the launch security descriptor of the DCOM application with a new security descriptor that is defined by an instance of a Win32\_SecurityDescriptor class.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 72245d22-1a0a-4069-b5d6-9d59e4de4aab
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: SetLaunchSecurityDescriptor method of the Win32\_DCOMApplicationSetting class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetLaunchSecurityDescriptor method of the Win32\_DCOMApplicationSetting class

The **SetLaunchSecurityDescriptor** method updates the launch security descriptor of the DCOM application with a new security descriptor that is defined by an instance of a [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) class. This security descriptor controls who is allowed to launch the application. The account running the script or application that calls this method must have the **SeSecurityPrivilege** and **SeRestorePrivilege** privileges. For more information, see [Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905).

## Syntax


```mof
uint32 SetLaunchSecurityDescriptor(
  [in] Win32_SecurityDescriptor Descriptor
);
```



## Parameters

<dl> <dt>

*Descriptor* \[in\]
</dt> <dd>

The security descriptor to set that controls who can start the DCOM application.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For more information, see [WMI Return Codes](https://msdn.microsoft.com/library/aa394574) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

<dl> <dt>

**Success**
</dt> <dd>

0

Successful completion.

</dd> <dt>

**2**
</dt> <dd>

The user does not have access to the requested information.

</dd> <dt>

**8**
</dt> <dd>

Unknown failure.

</dd> <dt>

**9**
</dt> <dd>

The user does not have adequate privileges to execute the method.

</dd> <dt>

**21**
</dt> <dd>

A parameter specified in the method call is not valid.

</dd> <dt>

**Other**
</dt> <dd>

1 4294967295

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) data type and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) and a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information, see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758) and [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

You can update both the DACL and the SACL in the [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance when calling this method, but you also can update only the DACL or only the SACL.

The following values in [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) determine whether the DACL, the SACL, or both are updated.

-   **SE\_DACL\_PRESENT**

    Indicates that the DACL should be updated. If this is not set, then WMI preserves the original value of the DACL.

-   **SE\_SACL\_PRESENT**

    Indicates that the SACL should be updated. If this is not set, then WMI preserves the original value of the SACL. To update the SACL, the account must have the **SeSecurityPrivilege** privilege enabled. For scripting, the privilege name is **SeSecurityPrivilege**. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758).

If the Group trustee and the Owner trustee properties are not **NULL**, then they are updated. Otherwise, WMI preserves the original values. For more information, see [WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577).

When a new SACL is **NULL** in a call to this method, then the security descriptor SACL on the target securable object is left unchanged.

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

 

 




