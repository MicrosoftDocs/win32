---
description: The Win32Shutdown &\#8194; WMI class method provides the full set of shutdown options supported by Win32 operating systems. These include logoff, shutdown, reboot, and forcing a logoff, shutdown, or reboot.
ms.assetid: 7108570a-81ba-46d5-8b05-de6194f93f18
ms.tgt_platform: multiple
title: Win32Shutdown method of the Win32_OperatingSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OperatingSystem.Win32Shutdown
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Win32Shutdown method of the Win32\_OperatingSystem class

The **Win32Shutdown**   [WMI class](../wmisdk/retrieving-a-class.md) method provides the full set of shutdown options supported by Win32 operating systems. These include logoff, shutdown, reboot, and forcing a logoff, shutdown, or reboot.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](../wmisdk/calling-a-method.md).

## Syntax


```mof
uint32 Win32Shutdown(
  [in] sint32 Flags,
  [in] sint32 Reserved = 
);
```



## Parameters

<dl> <dt>

*Flags* \[in\]
</dt> <dd>

Bitmapped set of flags to shut the computer down. To force a command, add the Force flag (4) to the command value. Using Force in conjunction with Shutdown or Reboot on a remote computer immediately shuts down everything (including WMI, COM, and so on), or reboots the remote computer. This results in an indeterminate return value.

<dt>

0 (0x0)
</dt> <dd>

**Log Off** - Logs the user off the computer. Logging off stops all processes associated with the security context of the process that called the exit function, logs the current user off the system, and displays the logon dialog box.

</dd> <dt>

4 (0x4)
</dt> <dd>

**Forced Log Off (0 + 4)** - Logs the user off the computer immediately and does not notify applications that the logon session is ending. This can result in a loss of data.

</dd> <dt>

1 (0x1)
</dt> <dd>

**Shutdown** - Shuts down the computer to a point where it is safe to turn off the power. (All file buffers are flushed to disk, and all running processes are stopped.) Users see the message, `It is now safe to turn off your computer.`

During shutdown the system sends a message to each running application. The applications perform any cleanup while processing the message and return True to indicate that they can be terminated.

</dd> <dt>

5 (0x5)
</dt> <dd>

**Forced Shutdown (1 + 4)** - Shuts down the computer to a point where it is safe to turn off the power. (All file buffers are flushed to disk, and all running processes are stopped.) Users see the message,` It is now safe to turn off your computer.`

When the forced shutdown approach is used, all services, including WMI, are shut down immediately. Because of this, you will not be able to receive a return value if you are running the script against a remote computer.

</dd> <dt>

2 (0x2)
</dt> <dd>

**Reboot** - Shuts down and then restarts the computer.

</dd> <dt>

6 (0x6)
</dt> <dd>

**Forced Reboot (2 + 4)** - Shuts down and then restarts the computer.

When the forced reboot approach is used, all services, including WMI, are shut down immediately. Because of this, you will not be able to receive a return value if you are running the script against a remote computer.

</dd> <dt>

8 (0x8)
</dt> <dd>

**Power Off** - Shuts down the computer and turns off the power (if supported by the computer in question).

</dd> <dt>

12 (0xC)
</dt> <dd>

**Forced Power Off (8 + 4)** - Shuts down the computer and turns off the power (if supported by the computer in question).

When the forced power off approach is used, all services, including WMI, are shut down immediately. Because of this, you will not be able to receive a return value if you are running the script against a remote computer.

</dd> </dl> </dd> <dt>

*Reserved* \[in\]
</dt> <dd>

A means to extend **Win32Shutdown**. Currently, the *Reserved* parameter is ignored.

</dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](../wmisdk/wmi-error-constants.md) or [**WbemErrorEnum**](/windows/win32/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](../debug/system-error-codes.md).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1–4294967295)
</dt> </dl>

## Remarks

For more efficient management of computers in an organization, administrators need the ability to remotely shut down or restart a computer, or to remotely log off a user. The ability to carry out these tasks allows administrators to install software, reconfigure computer settings, remove computers from the network, and perform other tasks without having to manually shut down or restart each computer.

For example, to perform a network upgrade, you might need to shut down all the computers running on a particular network segment. To force a Group Policy upgrade, you need to log users off their computers. If a computer virus is present anywhere in your organization, you might want to shut down as many computers as possible, before the virus has an opportunity to spread. The ability to shut down and restart computers and to log off users programmatically instead of manually can be an enormous time-saver.

The calling process must have the **SE\_SHUTDOWN\_NAME** privilege.

The [**Win32ShutdownTracker**](win32shutdowntracker-method-in-class-win32-operatingsystem.md) method provides the same set of shutdown options supported by the **Win32Shutdown** method in [**Win32\_OperatingSystem**](win32-operatingsystem.md) but it also allows you to specify comments, a reason for shutdown, or a timeout.

The Win32Shutdown method does not have a parameter for locking a workstation, leaving the user logged on. However, workstations can be locked from the command line by using the following command:

`% windir %\System32\rundll32.exe user32.dll,LockWorkStation`

## Examples

The [Log Out, Reboot, or Shut Down Multiple Computers](https://Gallery.TechNet.Microsoft.Com/2e88d504-a4e5-499b-b09a-f90617a6d87d) VBScript sample on TechNet Gallery uses Win32Shutdown to log off, shut down, reboot, or power off (depending on the selection) the computers listed in the Server array.

The [ComputerManagement.ps1](https://Gallery.TechNet.Microsoft.Com/ef8de213-45b6-4751-8c77-01d1b6623e16) PowerShell sample on TechNet Gallery includes a method that calls Win32Shutdown on a remote computer.

The following PowerShell example uses the Win32Shutdown method to shut down the specified computer.


```PowerShell
$computername= "."
$win32OS = get-wmiobject win32_operatingsystem -computername $computername
$win32OS.psbase.Scope.Options.EnablePrivileges = $true
$win32OS.win32shutdown(8)
```



The following PowerShell code sample uses the EnableAllPrivileges from get-wmiobject cmdlet to achieve the proper priviliges.


```PowerShell
$win32OS = get-wmiobject win32_operatingsystem -computername $computername -EnableAllPrivileges
$win32OS.win32shutdown(8)
```



The following VB.NET sample code uses the Shutdown method to reboot or log off a system.


```VB
Dim

testResult AsSingle

Dim WMIServiceObject, ComputerObject AsObject 

'Now get some privileges 

WMIServiceObject = GetObject(
"Winmgmts:{impersonationLevel=impersonate,(Debug,Shutdown)}")
ForEach ComputerObject In WMIServiceObject.InstancesOf("Win32_OperatingSystem") 
    testResult = ComputerObject.Win32Shutdown(2 + 4, 0) 
    'reboot
    'testResult = ComputerObject.Win32Shutdown(0, 0) 'logoff 
    ' testResult = ComputerObject.Win32Shutdown(8 + 4, 0) 'shutdown 

If testResult <> 0 Then 

MsgBox("Sorry, an error has occurred while trying to perform selected operation") 

Else 

'Operation selected in statement above if condition would be carried out 

EndIf 

Next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> <dt>

[**Win32\_OperatingSystem**](win32-operatingsystem.md)
</dt> <dt>

[**Win32ShutdownTracker**](win32shutdowntracker-method-in-class-win32-operatingsystem.md)
</dt> <dt>

[WMI Tasks: Desktop Management](../wmisdk/wmi-tasks--desktop-management.md)
</dt> <dt>

[Executing Privileged Operations Using VBScript](../wmisdk/executing-privileged-operations-using-vbscript.md)
</dt> </dl>

 

 
