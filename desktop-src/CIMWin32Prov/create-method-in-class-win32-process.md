---
description: The Create&\#8194;WMI class method creates a new process.
ms.assetid: be80abec-fab4-4403-bc29-d0d4a38e3c87
ms.tgt_platform: multiple
title: Create method of the Win32_Process class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_Process.Create
api_type: 
- COM
api_location: 
- CIMWin32.dll
---

# Create method of the Win32\_Process class

The **Create** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) method creates a new process.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](/windows/desktop/WmiSdk/calling-a-method).

## Syntax


```mof
uint32 Create(
  [in]  string               CommandLine,
  [in]  string               CurrentDirectory,
  [in]  Win32_ProcessStartup ProcessStartupInformation,
  [out] uint32               ProcessId
);
```



## Parameters

<dl> <dt>

*CommandLine* \[in\]
</dt> <dd>

Command line to execute. The system adds a null character to the command line, trimming the string if necessary, to indicate which file was actually used.

</dd> <dt>

*CurrentDirectory* \[in\]
</dt> <dd>

Current drive and directory for the child process. The string requires that the current directory resolves to a known path. A user can specify an absolute path or a path relative to the current working directory. If this parameter is **NULL**, the new process will have the same path as the calling process. This option is provided primarily for shells that must start an application and specify the application's initial drive and working directory.

</dd> <dt>

*ProcessStartupInformation* \[in\]
</dt> <dd>

The startup configuration of a Windows process. For more information, see [**Win32\_ProcessStartup**](win32-processstartup.md).

</dd> <dt>

*ProcessId* \[out\]
</dt> <dd>

Global process identifier that can be used to identify a process. The value is valid from the time the process is created until the time the process is terminated.

</dd> </dl>

## Return value

Returns a value of 0 (zero) if the process was successfully created, and any other number to indicate an error. For additional error codes, see [**WMI Error Constants**](/windows/desktop/WmiSdk/wmi-error-constants) or [**WbemErrorEnum**](/windows/desktop/api/wbemdisp/ne-wbemdisp-wbemerrorenum). For general **HRESULT** values, see [System Error Codes](/windows/desktop/Debug/system-error-codes).

<dl> <dt>

**Successful completion** (0)
</dt> <dt>

**Access denied** (2)
</dt> <dt>

**Insufficient privilege** (3)
</dt> <dt>

**Unknown failure** (8)
</dt> <dt>

**Path not found** (9)
</dt> <dt>

**Invalid parameter** (21)
</dt> <dt>

**Other** (22 4294967295)
</dt> </dl>

## Remarks

You can create an instance of the [**Win32\_ProcessStartup**](win32-processstartup.md) class to configure the process before calling this method.

A fully qualified path must be specified in cases where the program to be launched is not in the search path of Winmgmt.exe. If the newly created process attempts to interact with objects on the target system without the appropriate access privileges, it is terminated without notification to this method.

For security reasons the **Win32\_Process.Create** method cannot be used to start an interactive process remotely.

Processes created with the **Win32\_Process.Create** method are limited by the job object unless the **CREATE\_BREAKAWAY\_FROM\_JOB** flag is specified. For more information, see [**Win32\_ProcessStartup**](win32-processstartup.md) and [**\_\_ProviderHostQuotaConfiguration**](/windows/desktop/WmiSdk/--providerhostquotaconfiguration).

## Examples

The following VBScript example demonstrates how to invoke a CIM method as if it were an automation method of SWbemObject.


```VB
on error resume next

set process = GetObject("winmgmts:Win32_Process")

result = process.Create ("notepad.exe",null,null,processid)

WScript.Echo "Method returned result = " & result
WScript.Echo "Id of new process is " & processid

if err <>0 then
 WScript.Echo Err.Description, "0x" & Hex(Err.Number)
end if
```



The following Perl example demonstrates how to invoke a CIM method as if it were an automation method of SWbemObject.


```VB
use strict;
use Win32::OLE;

my ($process, $outParam, $processid, $inParam, $objMethod);

eval { $process = 
 Win32::OLE->GetObject("winmgmts:{impersonationLevel=impersonate}!\\\\.\\root\\cimv2:Win32_Process"); };

if (!$@ && defined $process)
{
 $objMethod = $process->Methods_("Create");

 #Spawn an instance of inParameters and assign the values.
 $inParam = $objMethod->inParameters->SpawnInstance_ if (defined $objMethod);
 $inParam->{CommandLine} = "notepad.exe";
 $inParam->{CurrentDirectory} = undef;
 $inParam->{ProcessStartupInformation} = undef;

 $outParam = $process->ExecMethod_("Create", $inParam) if (defined $inParam);
 if ($outParam->{ReturnValue})
 {
  print STDERR Win32::OLE->LastError, "\n";
 }
 else
 {
  print "Method returned result = $outParam->{ReturnValue}\n";
  print "Id of new process is $outParam->{ProcessId}\n"
 }
}
else
{
 print STDERR Win32::OLE->LastError, "\n";
}
```



The following VBScript code example creates a Notepad process on the local computer. [**Win32\_ProcessStartup**](win32-processstartup.md) is used to configure the process settings.


```VB
Const SW_NORMAL = 1
strComputer = "."
strCommand = "Notepad.exe" 
Set objWMIService = GetObject("winmgmts:" _
    & "{impersonationLevel=impersonate}!\\" _
    & strComputer & "\root\cimv2")

' Configure the Notepad process to show a window
Set objStartup = objWMIService.Get("Win32_ProcessStartup")
Set objConfig = objStartup.SpawnInstance_
objConfig.ShowWindow = SW_NORMAL

' Create Notepad process
Set objProcess = objWMIService.Get("Win32_Process")
intReturn = objProcess.Create _
    (strCommand, Null, objConfig, intProcessID)
If intReturn <> 0 Then
    Wscript.Echo "Process could not be created." & _
        vbNewLine & "Command line: " & strCommand & _
        vbNewLine & "Return value: " & intReturn
Else
    Wscript.Echo "Process created." & _
        vbNewLine & "Command line: " & strCommand & _
        vbNewLine & "Process ID: " & intProcessID
End If
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

[**Win32\_Process**](win32-process.md)
</dt> <dt>

[WMI Tasks: Processes](/windows/desktop/WmiSdk/wmi-tasks--processes)
</dt> </dl>

 

