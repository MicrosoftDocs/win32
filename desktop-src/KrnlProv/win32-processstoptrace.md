---
title: Win32\_ProcessStopTrace class
description: Indicates that a process is terminated.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b33efdfa-3e91-4983-abea-c262e8ce3ecb
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Win32_ProcessStopTrace class
- Win32_ProcessStopTrace class, described
topic_type:
- apiref
api_name:
- Win32_ProcessStopTrace
- Win32_ProcessStopTrace.SECURITY_DESCRIPTOR
- Win32_ProcessStopTrace.TIME_CREATED
- Win32_ProcessStopTrace.ProcessID
- Win32_ProcessStopTrace.ParentProcessID
- Win32_ProcessStopTrace.Sid
- Win32_ProcessStopTrace.ExitStatus
- Win32_ProcessStopTrace.ProcessName
- Win32_ProcessStopTrace.SessionID
api_location:
- Krnlprov.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Win32\_ProcessStopTrace class

The **Win32\_ProcessStopTrace** event [WMI class](https://msdn.microsoft.com/library/aa393244) indicates that a process is terminated.

The following syntax is simplified from Managed Object Format (MOF) code, and includes all of the inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class Win32_ProcessStopTrace : Win32_ProcessTrace
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
  uint32 ProcessID;
  uint32 ParentProcessID;
  uint8  Sid[];
  uint32 ExitStatus;
  string ProcessName;
  uint32 SessionID;
};
```

## Members

The **Win32\_ProcessStopTrace** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProcessStopTrace** class has these properties.

<dl> <dt>

**ExitStatus**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Exit status of the stopped process.

</dd> <dt>

**ParentProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Process that starts an event.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**ProcessID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The ProcessID property identifies the process involved in the event.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**ProcessName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the process that stops. You can use this name to get the instance of [**Win32\_Process**](https://msdn.microsoft.com/library/aa394372) for the same process.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634). For more information about constants used to set this security descriptor, see [WMI Security Constants](https://msdn.microsoft.com/library/aa394576).

</dd> <dt>

**SessionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Session under which the process exists.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**Sid**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The Sid property is the security identifier representing the user context under which the event happened.

This property is inherited from [**Win32\_ProcessTrace**](win32-processtrace.md).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](https://msdn.microsoft.com/library/aa394634).

For more information about using **uint64** values in scripts, see [Scripting in WMI](https://msdn.microsoft.com/library/aa389763).

</dd> </dl>

## Remarks

The **Win32\_ProcessStopTrace** class is derived from [**Win32\_ProcessTrace**](win32-processtrace.md).

## Examples

The following VBScript code example creates a Notepad process on the local computer that reports when the process stops. Run the script and close the Notepad window when the script shows the "Waiting for process to stop..." message.


```VB
Const SW_NORMAL = 1
strComputer = "."
strCommand = "Notepad.exe" 
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" _
                              & strComputer & "\root\cimv2")

Set objStartup = objWMIService.Get("Win32_ProcessStartup")
Set objConfig = objStartup.SpawnInstance_

objConfig.ShowWindow = SW_NORMAL
Set objProcess = objWMIService.Get("Win32_Process")
intReturn = objProcess.Create(strCommand, Null, objConfig, intProcessID)
If intReturn <> 0 Then
    Wscript.Echo "Process could not be created." & vbNewLine & _
                 "Command line: " & strCommand & vbNewLine & _
                 "Return value: " & intReturn
Else
    Wscript.Echo "Process created." & vbNewLine & _
                 "Command line: " & strCommand & vbNewLine & _
                 "Process ID: " & intProcessID    
    Set colProcessStopTrace = objWMIService.ExecNotificationQuery("SELECT * FROM Win32_ProcessStopTrace")
        WScript.Echo "Waiting for process to stop ..."
    Do
        Set objLatestEvent = colProcessStopTrace.NextEvent
        If objLatestEvent.ProcessId = intProcessID Then
            Wscript.Echo "StoppedProcess Name: " & objLatestEvent.ProcessName
            Wscript.Echo "Process ID: " & objLatestEvent.ProcessId
            WScript.Echo "Exit code: " & objLatestEvent.ExitStatus
    End If
  Loop
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Krnlprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Krnlprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_ProcessTrace**](win32-processtrace.md)
</dt> <dt>

[Operating System Classes](https://msdn.microsoft.com/library/dn792258)
</dt> <dt>

[**Win32\_Process**](https://msdn.microsoft.com/library/aa394372)
</dt> </dl>

 

 





