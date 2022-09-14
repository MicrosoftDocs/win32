---
description: The Win32\_ProcessStartup abstract WMI class represents the startup configuration of a Windows-based process.
ms.assetid: 78508404-cab2-42fb-a0ed-0e6e7d21408c
ms.tgt_platform: multiple
title: Win32_ProcessStartup class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_ProcessStartup
- Win32_ProcessStartup.CreateFlags
- Win32_ProcessStartup.EnvironmentVariables
- Win32_ProcessStartup.ErrorMode
- Win32_ProcessStartup.FillAttribute
- Win32_ProcessStartup.PriorityClass
- Win32_ProcessStartup.ShowWindow
- Win32_ProcessStartup.Title
- Win32_ProcessStartup.WinstationDesktop
- Win32_ProcessStartup.X
- Win32_ProcessStartup.XCountChars
- Win32_ProcessStartup.XSize
- Win32_ProcessStartup.Y
- Win32_ProcessStartup.YCountChars
- Win32_ProcessStartup.YSize
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_ProcessStartup class

The **Win32\_ProcessStartup** abstract [WMI class](../wmisdk/retrieving-a-class.md) represents the startup configuration of a Windows-based process. The class is defined as a method type definition, which means that it is only used for passing information to the [**Create**](create-method-in-class-win32-process.md) method of the [**Win32\_Process**](win32-process.md) class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties.

## Syntax

``` syntax
[Abstract, UUID("{8502C4DB-5FBB-11D2-AAC1-006008C78BC7}"), AMENDMENT]
class Win32_ProcessStartup : Win32_MethodParameterClass
{
  uint32 CreateFlags;
  string EnvironmentVariables[];
  uint16 ErrorMode = 1;
  uint32 FillAttribute;
  uint32 PriorityClass;
  uint16 ShowWindow;
  string Title;
  string WinstationDesktop;
  uint32 X;
  uint32 XCountChars;
  uint32 XSize;
  uint32 Y;
  uint32 YCountChars;
  uint32 YSize;
};
```

## Members

The **Win32\_ProcessStartup** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_ProcessStartup** class has these properties.

<dl> <dt>

**CreateFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Functions\|[**CreateProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa)\|dwCreationFlags")
</dt> </dl>

Additional values that control the priority class and the creation of the process. The following creation values can be specified in any combination, except as noted.

<dt>

<span id="Debug_Process"></span><span id="debug_process"></span><span id="DEBUG_PROCESS"></span>

<span id="Debug_Process"></span><span id="debug_process"></span><span id="DEBUG_PROCESS"></span>**Debug\_Process** (1)


</dt> <dd>

If this flag is set, the calling process is treated as a debugger, and the new process is being debugged. The system notifies the debugger of all debug events that occur in the process being debugged.

</dd> <dt>

<span id="Debug_Only_This_Process"></span><span id="debug_only_this_process"></span><span id="DEBUG_ONLY_THIS_PROCESS"></span>

<span id="Debug_Only_This_Process"></span><span id="debug_only_this_process"></span><span id="DEBUG_ONLY_THIS_PROCESS"></span>**Debug\_Only\_This\_Process** (2)


</dt> <dd>

If this flag is not set and the calling process is being debugged, the new process becomes another process being debugged. If the calling process is not a process of being debugged, no debugging-related actions occur.

</dd> <dt>

<span id="Create_Suspended"></span><span id="create_suspended"></span><span id="CREATE_SUSPENDED"></span>

<span id="Create_Suspended"></span><span id="create_suspended"></span><span id="CREATE_SUSPENDED"></span>**Create\_Suspended** (4)


</dt> <dd>

The primary thread of the new process is created in a suspended state and does not run until the [**ResumeThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-resumethread) method is called.

</dd> <dt>

<span id="Detached_Process"></span><span id="detached_process"></span><span id="DETACHED_PROCESS"></span>

<span id="Detached_Process"></span><span id="detached_process"></span><span id="DETACHED_PROCESS"></span>**Detached\_Process** (8)


</dt> <dd>

For console processes, the new process does not have access to the console of the parent process. This flag cannot be used if the **Create\_New\_Console** flag is set.

</dd> <dt>

<span id="Create_New_Console"></span><span id="create_new_console"></span><span id="CREATE_NEW_CONSOLE"></span>

<span id="Create_New_Console"></span><span id="create_new_console"></span><span id="CREATE_NEW_CONSOLE"></span>**Create\_New\_Console** (16)


</dt> <dd>

This new process has a new console, instead of inheriting the parent console. This flag cannot be used with the **Detached\_Process** flag.

</dd> <dt>

<span id="Create_New_Process_Group"></span><span id="create_new_process_group"></span><span id="CREATE_NEW_PROCESS_GROUP"></span>

<span id="Create_New_Process_Group"></span><span id="create_new_process_group"></span><span id="CREATE_NEW_PROCESS_GROUP"></span>**Create\_New\_Process\_Group** (512)


</dt> <dd>

This new process is the root process of a new process group. The process group includes all of the processes that are descendants of this root process. The process identifier of the new process group is the same as the process identifier that is returned in the **ProcessID** property of the [**Win32\_Process**](win32-process.md) class. Process groups are used by the [**GenerateConsoleCtrlEvent**](/windows/console/generateconsolectrlevent) method to enable the sending of either a CTRL+C signal or a CTRL+BREAK signal to a group of console processes.

</dd> <dt>

<span id="Create_Unicode_Environment"></span><span id="create_unicode_environment"></span><span id="CREATE_UNICODE_ENVIRONMENT"></span>

<span id="Create_Unicode_Environment"></span><span id="create_unicode_environment"></span><span id="CREATE_UNICODE_ENVIRONMENT"></span>**Create\_Unicode\_Environment** (1024)


</dt> <dd>

The environment settings listed in the **EnvironmentVariables** property use Unicode characters. If this flag is not set, the environment block uses ANSI characters.

</dd> <dt>

<span id="Create_Default_Error_Mode"></span><span id="create_default_error_mode"></span><span id="CREATE_DEFAULT_ERROR_MODE"></span>

<span id="Create_Default_Error_Mode"></span><span id="create_default_error_mode"></span><span id="CREATE_DEFAULT_ERROR_MODE"></span>**Create\_Default\_Error\_Mode** (67108864)


</dt> <dd>

Newly created processes are given the system default error mode of the calling process instead of inheriting the error mode of the parent process. This flag is useful for multithreaded shell applications that run with hard errors disabled.

</dd> <dt>

<span id="CREATE_BREAKAWAY_FROM_JOB"></span><span id="create_breakaway_from_job"></span>

<span id="CREATE_BREAKAWAY_FROM_JOB"></span><span id="create_breakaway_from_job"></span>**CREATE\_BREAKAWAY\_FROM\_JOB** (16777216)


</dt> <dd>

Used for the created process not to be limited by the job object.

</dd> </dl>

</dd> <dt>

**EnvironmentVariables**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32Registry\|HKEY\_CURRENT\_USER\\\\Environment")
</dt> </dl>

List of settings for the configuration of a computer. Environment variables specify search paths for files, directories for temporary files, application-specific options, and other similar information. The system maintains a block of environment settings for each user and one for the computer. The system environment block represents environment variables for all of the users of a specific computer. A user's environment block represents the environment variables that the system maintains for a specific user, and includes the set of system environment variables. By default, each process receives a copy of the environment block for its parent process. Typically, this is the environment block for the user who is logged on. A process can specify different environment blocks for its child processes.

</dd> <dt>

**ErrorMode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Error Functions\|SetErrorMode")
</dt> </dl>

On some non-x86 processors, misaligned memory references cause an alignment fault exception. The **No\_Alignment\_Fault\_Except** flag lets you control whether or not an operating system automatically fixes such alignment faults, or makes them visible to an application. On a millions of instructions per second (MIPS) platform, an application must explicitly call [**SetErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode) with the **No\_Alignment\_Fault\_Except** flag to have the operating system automatically fix alignment faults.

How an operating system processes several types of serious errors. You can specify that the operating system process errors, or an application can receive and process errors.

The default setting is for the operating system to make alignment faults visible to an application. Because the x86 platform does not make alignment faults visible to an application, the **No\_Alignment\_Fault\_Except** flag does not make the operating system raise an alignment fault error—even if the flag is not set. The default state for [**SetErrorMode**](/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode) is to set all of the flags to 0 (zero).

<dt>



 (1)


</dt> <dd>

Default

</dd> <dt>

<span id="Fail_Critical_Errors"></span><span id="fail_critical_errors"></span><span id="FAIL_CRITICAL_ERRORS"></span>

<span id="Fail_Critical_Errors"></span><span id="fail_critical_errors"></span><span id="FAIL_CRITICAL_ERRORS"></span>**Fail\_Critical\_Errors** (2)


</dt> <dd>

If this flag is set, the operating system does not display the critical error handler message box when such an error occurs. Instead, the operating system sends the error to the calling process.

</dd> <dt>

<span id="No_Alignment_Fault_Except"></span><span id="no_alignment_fault_except"></span><span id="NO_ALIGNMENT_FAULT_EXCEPT"></span>

<span id="No_Alignment_Fault_Except"></span><span id="no_alignment_fault_except"></span><span id="NO_ALIGNMENT_FAULT_EXCEPT"></span>**No\_Alignment\_Fault\_Except** (4)


</dt> <dd>

If this flag is set, the operating system automatically fixes memory alignment faults and makes them invisible to the application. It does this for the calling and descendant processes. This flag applies to reduced instruction set computing (RISC) only, and has no effect on x86 processors.

</dd> <dt>

<span id="No_GP_Fault_Error_Box"></span><span id="no_gp_fault_error_box"></span><span id="NO_GP_FAULT_ERROR_BOX"></span>

<span id="No_GP_Fault_Error_Box"></span><span id="no_gp_fault_error_box"></span><span id="NO_GP_FAULT_ERROR_BOX"></span>**No\_GP\_Fault\_Error\_Box** (8)


</dt> <dd>

If this flag is set, the operating system does not display the general protection (GP) fault message box when a GP error occurs. This flag should only be set by debugging applications that handle GP errors.

</dd> <dt>

<span id="No_Open_File_Error_Box"></span><span id="no_open_file_error_box"></span><span id="NO_OPEN_FILE_ERROR_BOX"></span>

<span id="No_Open_File_Error_Box"></span><span id="no_open_file_error_box"></span><span id="NO_OPEN_FILE_ERROR_BOX"></span>**No\_Open\_File\_Error\_Box** (16)


</dt> <dd>

If this flag is set, the operating system does not display a message box when it fails to find a file. Instead, the error is returned to the calling process. This flag is currently ignored.

</dd> </dl>

</dd> <dt>

**FillAttribute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|dwFillAttribute")
</dt> </dl>

The text and background colors if a new console window is created in a console application. These values are ignored in graphical user interface (GUI) applications. To specify both foreground and background colors, add the values together. For example, to have red type (4) on a blue background (16), set the FillAttribute to 20.

<dt>

1
</dt> <dd>

Foreground\_Blue

</dd> <dt>

2
</dt> <dd>

Foreground\_Green

</dd> <dt>

4
</dt> <dd>

Foreground\_Red

</dd> <dt>

8
</dt> <dd>

Foreground\_Intensity

</dd> <dt>

16
</dt> <dd>

Background\_Blue

</dd> <dt>

32
</dt> <dd>

Background\_Green

</dd> <dt>

64
</dt> <dd>

Background\_Red

</dd> <dt>

128
</dt> <dd>

Background\_Intensity

</dd> </dl>

</dd> <dt>

**PriorityClass**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**JOBOBJECT\_BASIC\_LIMIT\_INFORMATION**](/windows/win32/api/winnt/ns-winnt-jobobject_basic_limit_information)\|PriorityClass")
</dt> </dl>

Priority class of the new process. Use this property to determine the schedule priorities of the threads in the process. If the property is left null, the priority class defaults to Normal—unless the priority class of the creating process is Idle or Below\_Normal. In these cases, the child process receives the default priority class of the calling process.

<dt>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>

<span id="Normal"></span><span id="normal"></span><span id="NORMAL"></span>**Normal** (32)


</dt> <dd>

Indicates a normal process with no special schedule needs.

</dd> <dt>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>

<span id="Idle"></span><span id="idle"></span><span id="IDLE"></span>**Idle** (64)


</dt> <dd>

Indicates a process with threads that run only when the system is idle and are preempted by the threads of any process running in a higher priority class. An example is a screen saver. The idle priority class is inherited by child processes.

</dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>**High** (128)


</dt> <dd>

Indicates a process that performs time-critical tasks that must be executed immediately to run correctly. The threads of a high-priority class process preempt the threads of normal-priority or idle-priority class processes. An example is Windows Task List, which must respond quickly when called by the user, regardless of the load on the operating system. Use extreme care when using the high-priority class, because a high-priority class CPU-bound application can use nearly all of the available cycles. Only a real-time priority preempts threads set to this level.

</dd> <dt>

<span id="Realtime"></span><span id="realtime"></span><span id="REALTIME"></span>

<span id="Realtime"></span><span id="realtime"></span><span id="REALTIME"></span>**Realtime** (256)


</dt> <dd>

Indicates a process that has the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes—including high-priority threads and operating system processes performing important tasks. For example, a real-time process that executes for more than a very brief interval can cause disk caches not to flush, or cause a mouse to be unresponsive.

</dd> <dt>

<span id="Below_Normal"></span><span id="below_normal"></span><span id="BELOW_NORMAL"></span>

<span id="Below_Normal"></span><span id="below_normal"></span><span id="BELOW_NORMAL"></span>**Below\_Normal** (16384)


</dt> <dd>

Indicates a process that has a priority higher than Idle but lower than Normal.

</dd> <dt>

<span id="Above_Normal"></span><span id="above_normal"></span><span id="ABOVE_NORMAL"></span>

<span id="Above_Normal"></span><span id="above_normal"></span><span id="ABOVE_NORMAL"></span>**Above\_Normal** (32768)


</dt> <dd>

Indicates a process that has a priority higher than Normal but lower than High.

</dd> </dl>

</dd> <dt>

**ShowWindow**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|wShowWindow")
</dt> </dl>

How the window is displayed to the user. It can be any of the values that can be specified in the *nCmdShow* parameter for the [ShowWindow](/windows/desktop/api/winuser/nf-winuser-showwindow) function.

</dd> <dt>

**Title**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|lpTitle")
</dt> </dl>

Text displayed in the title bar when a new console window is created; used for console processes. If **NULL**, the name of the executable file is used as the window title. This property must be **NULL** for GUI or console processes that do not create a new console window.

</dd> <dt>

**WinstationDesktop**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|lpDesktop")
</dt> </dl>

The name of the desktop or the name of both the desktop and window station for the process. A backslash in the string indicates that the string includes both desktop and window station names. If **WinstationDesktop** is **NULL**, the new process inherits the desktop and window station of its parent process. If **WinstationDesktop** is an empty string, the process does not inherit the desktop and window station of its parent process. The system determines if a new desktop and window station must be created. A window station is a secure object that contains a clipboard, a set of global atoms, and a group of desktop objects. The interactive window station that is assigned to the logon session of the interactive user also contains the keyboard, mouse, and display device. A desktop is a secure object contained within a window station. A desktop has a logical display surface and contains windows, menus, and hooks. A window station can have multiple desktops. Only the desktops of the interactive window station can be visible and receive user input.

</dd> <dt>

**X**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|dwX")
</dt> </dl>

The X offset of the upper left corner of a window if a new window is created—in pixels. The offsets are from the upper left corner of the screen. For GUI processes, the specified position is used the first time the new process calls [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) to create an overlapped window if the *X* parameter of **CreateWindow** is **CW\_USEDEFAULT**.

> \[!Note  X\]  
> and **Y** cannot be specified independently.

 

</dd> <dt>

**XCountChars**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|XCountChars")
</dt> </dl>

Screen buffer width in character columns. This property is used for processes that create a console window, and is ignored in GUI processes.

> [!Note]  
> **XCountChars** and **YCountChars** cannot be specified independently.

 

</dd> <dt>

**XSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|dwXSize")
</dt> </dl>

Pixel width of a window if a new window is created. For GUI processes, this is only used the first time the new process calls [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) to create an overlapped window if the nWidth parameter of **CreateWindow** is **CW\_USEDEFAULT**.

> [!Note]  
> **XSize** and **YSize** cannot be specified independently.

 

</dd> <dt>

**Y**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|dwY")
</dt> </dl>

Pixel offset of the upper-left corner of a window if a new window is created. The offsets are from the upper-left corner of the screen. For GUI processes, the specified position is used the first time the new process calls [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) to create an overlapped window if the *y* parameter of **CreateWindow** is **CW\_USEDEFAULT**.

> \[!Note  X\]  
> and **Y** cannot be specified independently.

 

</dd> <dt>

**YCountChars**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|YCountChars")
</dt> </dl>

Screen buffer height in character rows. This property is used for processes that create a console window, but is ignored in GUI processes.

> [!Note]  
> **XCountChars** and **YCountChars** cannot be specified independently.

 

</dd> <dt>

**YSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](../wmisdk/standard-qualifiers.md) ("Win32API\|Process and Thread Structures\|[**STARTUPINFO**](/windows/win32/api/processthreadsapi/ns-processthreadsapi-startupinfoa)\|dwYSize")
</dt> </dl>

Pixel height of a window if a new window is created. For GUI processes, this is used only the first time the new process calls [**CreateWindow**](/windows/win32/api/winuser/nf-winuser-createwindowa) to create an overlapped window if the *nWidth* parameter of **CreateWindow** is **CW\_USEDEFAULT**.

> [!Note]  
> **XSize** and **YSize** cannot be specified independently.

 

</dd> </dl>

## Remarks

This class is derived from [**Win32\_MethodParameterClass**](win32-methodparameterclass.md).

Overview

The [**Win32\_Process**](win32-process.md) [**Create**](create-method-in-class-win32-process.md) method enables you to configure startup options for any new process running on a computer. For example, you can configure a process so that it starts in a "hidden" window, which prevents a user from seeing, and possibly interrupting, it. If the process runs in a command window, you can configure the size, title, and foreground and background colors of the window.

Startup options are configured using the **Win32\_ProcessStartup** class. **Win32\_ProcessStartup** is a Method Type class; the Method Type class exists solely to pass information to a method. In this case, all the properties of an instance of **Win32\_ProcessStartup** are passed to an instance of [**Win32\_Process**](win32-process.md).

**Using Win32\_ProcessStartup**

1.  Create an instance of **Win32\_ProcessStartup**.
2.  Configure the properties of the new instance.
3.  Include the instance as part of the [**Win32\_Process**](win32-process.md) Create method.

For example, if you have created a **Win32\_ProcessStartup** instance named objConfig, you would pass the object name in the Create method as follows:

`errReturn = objProcess.Create("Database.exe", null, objConfig, intProcessID)`

## Examples

You can use the **Win32\_ProcessStartup** class to configure various startup options for a process. These options include, but are not limited to, such things as creating a process in a hidden window and creating a higher-priority process. The following VBScript creates a process in a hidden window.


```VB
Const HIDDEN_WINDOW = 12
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set objStartup = objWMIService.Get("Win32_ProcessStartup")
Set objConfig = objStartup.SpawnInstance_
objConfig.ShowWindow = HIDDEN_WINDOW
Set objProcess = GetObject("winmgmts:root\cimv2:Win32_Process")
errReturn = objProcess.Create("Notepad.exe", null, objConfig, intProcessID)
```



The following VBScript creates a higher-priority process.


```VB
Const ABOVE_NORMAL = 32768
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set objStartup = objWMIService.Get("Win32_ProcessStartup")
Set objConfig = objStartup.SpawnInstance_
objConfig.PriorityClass = ABOVE_NORMAL
Set objProcess = GetObject("winmgmts:root\cimv2:Win32_Process")
objProcess.Create "Database.exe", Null, objConfig, intProcessID
```



The following VBScript code example creates a Notepad process on the local computer. **Win32\_ProcessStartup** is used to configure the process settings.


```VB
Const SW_NORMAL = 1
strComputer = "."
strCommand = "Notepad.exe" 
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")

' Configure the Notepad process to show a window
Set objStartup = objWMIService.Get("Win32_ProcessStartup")
Set objConfig = objStartup.SpawnInstance_
objConfig.ShowWindow = SW_NORMAL

' Create Notepad process
Set objProcess = objWMIService.Get("Win32_Process")
intReturn = objProcess.Create _
    (strCommand, Null, objConfig, intProcessID)
If intReturn <> 0 Then
    Wscript.Echo "Process could not be created." & vbNewLine & _
                 "Command line: " & strCommand & vbNewLine & _
                 "Return value: " & intReturn
Else
    Wscript.Echo "Process created." & vbNewLine & _
                 "Command line: " & strCommand & vbNewLine & _
                 "Process ID: " & intProcessID
End If
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

[**Win32\_MethodParameterClass**](win32-methodparameterclass.md)
</dt> <dt>

[Operating System Classes](./operating-system-classes.md)
</dt> <dt>

[**Win32\_Process**](win32-process.md)
</dt> <dt>

[**\_\_ProviderHostQuotaConfiguration**](../wmisdk/--providerhostquotaconfiguration.md)
</dt> <dt>

[WMI Tasks: Processes](../wmisdk/wmi-tasks--processes.md)
</dt> </dl>

 

 
