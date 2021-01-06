---
description: The Shutdown&\#8194;WMI class method unloads programs and DLLs until it is safe to turn off the computer.
ms.assetid: 3f069699-810c-49bc-b77e-3fe43acc3dd5
ms.tgt_platform: multiple
title: Shutdown method of the Win32_OperatingSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OperatingSystem.Shutdown
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Shutdown method of the Win32\_OperatingSystem class

The **Shutdown** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method unloads programs and DLLs until it is safe to turn off the computer.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Shutdown();
```



## Parameters

This method has no parameters.

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1 4294967295)
</dt> </dl>

## Remarks

Computers occasionally need to be removed from the network, perhaps for scheduled maintenance, because the computer is not functioning correctly, or to complete a configuration process. For example, if a DHCP server is handing out erroneous IP addresses, you might want to shut the computer down until a service technician can be dispatched to fix the problem. If you suspect that a security breach has occurred, you might need to shut down certain servers to ensure that they cannot be accessed until the security issue has been resolved. Some configuration operations (such as changing a computer name) require you to restart the computer before the change takes effect.

This method immediately shuts the computer down, if possible. The system stops all running processes, flushes all file buffers to the disk, and then powers down the system. The calling process must have the **SE\_SHUTDOWN\_NAME** privilege, as described in the following example.


```VB
Set OpSysSet = GetObject("winmgmts:{(Shutdown)}//./root/cimv2").ExecQuery("select * from Win32_OperatingSystem where Primary=true")
```



For more information on setting a privilege, see [Executing Privileged Operations](/windows/desktop/WmiSdk/executing-privileged-operations) and [Executing Privileged Operations Using VBScript](/windows/desktop/WmiSdk/executing-privileged-operations-using-vbscript). For additional shutdown options, such as a logoff or a forced shutdown, see the [**Win32Shutdown**](win32shutdown-method-in-class-win32-operatingsystem.md) method.

## Examples

The following VBScript code shuts the local computer down.

> [!Note]  
> You must have the Shutdown privilege to successfully invoke the Shutdown method.

 


```VB
Set OpSysSet = GetObject("winmgmts:{(Shutdown)}//./root/cimv2").ExecQuery("select * from Win32_OperatingSystem where Primary=true")

for each OpSys in OpSysSet
 OpSys.Shutdown()
next
```



The following Perl code shuts the local computer down.

> [!Note]  
> You must have the Shutdown privilege to successfully invoke the Shutdown method.

 


```
use strict;
use Win32::OLE;

my $OpSysSet;

eval { $OpSysSet = Win32::OLE->GetObject("winmgmts:{(Shutdown)}//./root/cimv2")->
      ExecQuery("SELECT * FROM Win32_OperatingSystem WHERE Primary=true"); };

if(!$@ && defined $OpSysSet)
{
 close (STDERR);
 foreach my $OpSys (in $OpSysSet)
 {
  my $RetVal = $OpSys->Shutdown();
  if (!defined $RetVal || $RetVal != 0)
  { 
   print Win32::OLE->LastError, "\n";
  }
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
}
```



The following VBScript code shuts the specified remote computer down. Fill in *REMOTE\_SYSTEM\_NAME* with the name of the remote system to shutdown.

> [!Note]  
> You must have the RemoteShutdown privilege to successfully invoke the **Shutdown** method.

 


```VB
Set OpSysSet = GetObject("winmgmts:{(Debug,RemoteShutdown)}//REMOTE_SYSTEM_NAME/root/cimv2").ExecQuery("select * from Win32_OperatingSystem where Primary=true")

for each OpSys in OpSysSet
 OpSys.Shutdown()
next
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Win32\_OperatingSystem**](win32-operatingsystem.md)
</dt> <dt>

[WMI Tasks: Desktop Management](/windows/desktop/WmiSdk/wmi-tasks--desktop-management)
</dt> <dt>

[Executing Privileged Operations Using VBScript](/windows/desktop/WmiSdk/executing-privileged-operations-using-vbscript)
</dt> </dl>

 

