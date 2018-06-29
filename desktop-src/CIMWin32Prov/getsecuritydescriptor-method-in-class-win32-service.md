---
Description: Returns the security descriptor that controls access to the service.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99c8346e-e8d6-4f3c-bbdc-437dcf852b2a
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: GetSecurityDescriptor method of the Win32\_Service class
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Service.GetSecurityDescriptor
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# GetSecurityDescriptor method of the Win32\_Service class

The **GetSecurityDescriptor** method returns the security descriptor that controls access to the service. The descriptor is returned as an instance of [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402).

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

The security descriptor associated with the service.

</dd> </dl>

## Return value

Returns one of the values listed in the following list, or a different value to indicate an error. For additional error codes, see [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559) or [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978). For general **HRESULT** values, see [System Error Codes](https://msdn.microsoft.com/library/windows/desktop/ms681381).

<dl> <dt>

**Success**
</dt> <dd>

0

The request was accepted.

</dd> <dt>


</dt> <dd>

1

The request is not supported.

</dd> <dt>

**Access denied**
</dt> <dd>

2

The user did not have the necessary access.

</dd> <dt>


</dt> <dd>

3

The service cannot be stopped because other services that are running are dependent on it.

</dd> <dt>


</dt> <dd>

4

The requested control code is not valid, or it is unacceptable to the service.

</dd> <dt>


</dt> <dd>

5

The requested control code cannot be sent to the service because the state of the service ([**Win32\_BaseService**](win32-baseservice.md).**State** property) is equal to 0, 1, or 2.

</dd> <dt>


</dt> <dd>

6

The service has not been started.

</dd> <dt>


</dt> <dd>

7

The service did not respond to the start request in a timely fashion.

</dd> <dt>

**Unknown failure**
</dt> <dd>

8

Unknown failure when starting the service.

</dd> <dt>

**Privilege missing**
</dt> <dd>

9

The directory path to the service executable file was not found.

</dd> <dt>


</dt> <dd>

10

The service is already running.

</dd> <dt>


</dt> <dd>

11

The database to add a new service is locked.

</dd> <dt>


</dt> <dd>

12

A dependency this service relies on has been removed from the system.

</dd> <dt>


</dt> <dd>

13

The service failed to find the service needed from a dependent service.

</dd> <dt>


</dt> <dd>

14

The service has been disabled from the system.

</dd> <dt>


</dt> <dd>

15

The service does not have the correct authentication to run on the system.

</dd> <dt>


</dt> <dd>

16

This service is being removed from the system.

</dd> <dt>


</dt> <dd>

17

The service has no execution thread.

</dd> <dt>


</dt> <dd>

18

The service has circular dependencies when it starts.

</dd> <dt>


</dt> <dd>

19

A service is running under the same name.

</dd> <dt>


</dt> <dd>

20

The service name has invalid characters.

</dd> <dt>

**Invalid parameter**
</dt> <dd>

21

Invalid parameters have been passed to the service.

</dd> <dt>


</dt> <dd>

22

The account under which this service runs is either invalid or lacks the permissions to run the service.

</dd> <dt>


</dt> <dd>

23

The service exists in the database of services available from the system.

</dd> <dt>


</dt> <dd>

24

The service is currently paused in the system.

</dd> <dt>

**Other**
</dt> <dd>

22 4294967295

</dd> </dl>

## Remarks

The [**Win32\_SecurityDescriptor**](https://msdn.microsoft.com/library/aa394402) instance represents a [**SECURITY\_DESCRIPTOR\_CONTROL**](https://msdn.microsoft.com/library/windows/desktop/aa379566) data type and contains a [*discretionary access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721573#-security-discretionary-access-control-list-gly) (DACL) and a [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information, see [Access Control Lists](https://msdn.microsoft.com/library/windows/desktop/aa374872).

If the **SeSecurityPrivilege** is not granted or enabled when getting a security descriptor, then only the DACL is returned in the returned security descriptor. For more information, see [**Privilege Constants**](https://msdn.microsoft.com/library/aa392758) and [Executing Privileged Operations](https://msdn.microsoft.com/library/aa390428).

## Examples

When retrieving a security descriptor in VBScript, be sure to "Security" and run as as Admin, as shown in the following code snippet. Otherwise, your code may throw a permissions error.


```VB
Set objWMIService = GetObject("winmgmts:" _
  & "{impersonationLevel=impersonate, (Security)}!\\" & strComputer & "\root\cimv2")
```



Similarly, in VB.NET, be sure to set "EnablePrivileges = True" and run the Application as Admin.


```VB
Scope = New ManagementScope([String].Format("\\{0}\root\CIMV2", ComputerName), Nothing)
Scope.Options.EnablePrivileges = True
```



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

[**Win32\_Service**](win32-service.md)
</dt> <dt>

[**Privilege Constants**](https://msdn.microsoft.com/library/aa392758)
</dt> <dt>

[WMI Security Descriptor Objects](https://msdn.microsoft.com/library/aa394577)
</dt> <dt>

[Changing Access Security on Securable Objects](https://msdn.microsoft.com/library/aa384905)
</dt> <dt>

[User Account Control and WMI](https://msdn.microsoft.com/library/aa826699)
</dt> </dl>

 

 




