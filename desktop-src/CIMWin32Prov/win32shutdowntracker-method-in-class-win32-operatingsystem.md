---
description: The Win32ShutdownTracker method provides the same set of shutdown options supported by the Win32Shutdown method in Win32\_OperatingSystem, but it also allows you to specify comments, a reason for shutdown, or a timeout.
ms.assetid: 2c5502c9-9ec0-4f9e-b661-1f8015556008
ms.tgt_platform: multiple
title: Win32ShutdownTracker method of the Win32_OperatingSystem class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_OperatingSystem.Win32ShutdownTracker
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Win32ShutdownTracker method of the Win32\_OperatingSystem class

The **Win32ShutdownTracker** method provides the same set of shutdown options supported by the [**Win32Shutdown**](win32shutdown-method-in-class-win32-operatingsystem.md) method in [**Win32\_OperatingSystem**](win32-operatingsystem.md), but it also allows you to specify comments, a reason for shutdown, or a timeout.

## Syntax


```mof
uint32 Win32ShutdownTracker(
  [in] uint32 Timeout,
  [in] string Comment,
  [in] uint32 ReasonCode,
  [in] sint32 Flags
);
```



## Parameters

<dl> <dt>

*Timeout* \[in\]
</dt> <dd>

Time, in seconds, before shutdown takes place. The default value is 0 (zero).

</dd> <dt>

*Comment* \[in\]
</dt> <dd>

Message to display in the shutdown dialog box that is also stored as a comment in the event log entry.

</dd> <dt>

*ReasonCode* \[in\]
</dt> <dd>

Reason for initiating the shutdown.

</dd> <dt>

*Flags* \[in\]
</dt> <dd>

Bitmapped set of flags to shut the computer down. To force a command, add the Force flag (4) to the command value. Using Force in conjunction with Shutdown or Reboot on a remote computer immediately shuts down everything (including WMI, COM, and so on), or reboots the remote computer. This results in an indeterminate return value.

<dt>

0 (0x0)
</dt> <dd>

Log Off

</dd> <dt>

4 (0x4)
</dt> <dd>

Forced Log Off (0 + 4)

</dd> <dt>

1 (0x1)
</dt> <dd>

Shutdown

</dd> <dt>

5 (0x5)
</dt> <dd>

Forced Shutdown (1 + 4)

</dd> <dt>

2 (0x2)
</dt> <dd>

Reboot

</dd> <dt>

6 (0x6)
</dt> <dd>

Forced Reboot (2 + 4)

</dd> <dt>

8 (0x8)
</dt> <dd>

Power Off

</dd> <dt>

12 (0xC)
</dt> <dd>

Forced Power Off (8 + 4)

</dd> </dl> </dd> </dl>

## Return value

Returns zero (0) to indicate success. Any other number indicates an error. For error codes, see [**WMI Error Constants**](../wmisdk/wmi-error-constants.md) or [**WbemErrorEnum**](/windows/win32/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](../debug/system-error-codes.md).

<dl> <dt>

**Success** (0)
</dt> <dt>

**Other** (1–4294967295)
</dt> </dl>

## Remarks

The calling process must have the **SE\_SHUTDOWN\_NAME** privilege.

## Examples

The following VBScript code sample describes how to call **Win32ShutdownTracker**.


```VB
Set objArgs = Wscript.Arguments 

intTimeOut = objArgs(0) 'Countdown time (in seconds) before action
strComment = objArgs(1) 'Message to display
intFlags = objArgs(2) 'Set of flags to shutdown the computer:
'0 = Logoff, 4 = Forced Logoff (0+4), 1 = Shutdown, 2 = Reboot, 6 = Forced Reboot (2+4), 8 = Power Off, 12 = Forced Power Off (8+4) - 2 (Reboot) 

strComputer = "." 

Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate,(Shutdown)}!\\" & strComputer & "\root\cimv2")

Set colOperatingSystems = objWMIService.ExecQuery ("Select * from Win32_OperatingSystem") 

For Each objOperatingSystem in colOperatingSystems 
objOperatingSystem.Win32ShutdownTracker intTimeOut,strComment,0,intFlags 
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

[**Win32Shutdown**](win32shutdown-method-in-class-win32-operatingsystem.md)
</dt> </dl>

 

 
