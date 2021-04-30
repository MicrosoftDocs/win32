---
description: The CommandLineEventConsumer class starts an arbitrary process in the local system when an event is delivered to it.
ms.assetid: 0dcae783-1722-45a4-b5d4-3fcf455dacf8
ms.tgt_platform: multiple
title: CommandLineEventConsumer class
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- CommandLineEventConsumer
- CommandLineEventConsumer.CreatorSID
- CommandLineEventConsumer.MachineName
- CommandLineEventConsumer.MaximumQueueSize
- CommandLineEventConsumer.CommandLineTemplate
- CommandLineEventConsumer.CreateNewConsole
- CommandLineEventConsumer.CreateNewProcessGroup
- CommandLineEventConsumer.CreateSeparateWowVdm
- CommandLineEventConsumer.CreateSharedWowVdm
- CommandLineEventConsumer.DesktopName
- CommandLineEventConsumer.ExecutablePath
- CommandLineEventConsumer.FillAttributes
- CommandLineEventConsumer.ForceOffFeedback
- CommandLineEventConsumer.ForceOnFeedback
- CommandLineEventConsumer.KillTimeout
- CommandLineEventConsumer.Name
- CommandLineEventConsumer.Priority
- CommandLineEventConsumer.RunInteractively
- CommandLineEventConsumer.ShowWindowCommand
- CommandLineEventConsumer.UseDefaultErrorMode
- CommandLineEventConsumer.WindowTitle
- CommandLineEventConsumer.WorkingDirectory
- CommandLineEventConsumer.XCoordinate
- CommandLineEventConsumer.XNumCharacters
- CommandLineEventConsumer.XSize
- CommandLineEventConsumer.YCoordinate
- CommandLineEventConsumer.YNumCharacters
- CommandLineEventConsumer.YSize
- CommandLineEventConsumer.FillAttribute
api_type:
- DllExport
api_location:
- Wbemcons.dll
---

# CommandLineEventConsumer class

The **CommandLineEventConsumer** class starts an arbitrary process in the local system when an event is delivered to it. This class is one of the standard event consumers that WMI provides. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

> [!Note]  
> When using the **CommandLineEventConsumer** class, secure the executable that you want to start. If the executable is not in a secure location, or secured with a strong access control list (ACL), an unauthorized user can replace your executable with a malicious executable. For more information about ACLs, visit the Security section of the Microsoft Windows Software Development Kit (SDK), and see [Creating a Security Descriptor for a New Object](/windows/desktop/SecAuthZ/creating-a-security-descriptor-for-a-new-object-in-c--).

 

## Syntax

``` syntax
[AMENDMENT]
class CommandLineEventConsumer : __EventConsumer
{
  uint8   CreatorSID[];
  string  MachineName;
  uint32  MaximumQueueSize;
  string  CommandLineTemplate;
  boolean CreateNewConsole = False;
  boolean CreateNewProcessGroup = True;
  boolean CreateSeparateWowVdm = False;
  boolean CreateSharedWowVdm = False;
  string  DesktopName;
  string  ExecutablePath;
  uint32  FillAttributes;
  boolean ForceOffFeedback = False;
  boolean ForceOnFeedback = False;
  uint32  KillTimeout = 0;
  string  Name;
  sint32  Priority = 0x20;
  boolean RunInteractively = False;
  uint32  ShowWindowCommand;
  boolean UseDefaultErrorMode = False;
  string  WindowTitle;
  string  WorkingDirectory;
  uint32  XCoordinate;
  uint32  XNumCharacters;
  uint32  XSize;
  uint32  YCoordinate;
  uint32  YNumCharacters;
  uint32  YSize;
  uint32  FillAttribute;
};
```

## Members

The **CommandLineEventConsumer** class has these types of members:

-   [Properties](#properties)

### Properties

The **CommandLineEventConsumer** class has these properties.

<dl> <dt>

**CommandLineTemplate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Standard string template that specifies the process to be started. This property can be **NULL**, and the **ExecutablePath** property is used as the command line.

</dd> <dt>

**CreateNewConsole**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used. If a value is assigned to this property, a tracing message is generated. For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

</dd> <dt>

**CreateNewProcessGroup**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the new process is the root process of a new process group. The process group includes all processes that are descendants of this root process. The process identifier of the new process group is the same as this process identifier. Process groups are used by the [**GenerateConsoleCtrlEvent**](/windows/console/generateconsolectrlevent) method to enable sending a CTRL+C or CTRL+BREAK signal to a group of console processes.

</dd> <dt>

**CreateSeparateWowVdm**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the new process runs in a private Virtual DOS Machine (VDM). This is only valid when starting an application running on a 16-bit Windows operating system. If set to **False**, all applications running on a 16-bit Windows operating system run as threads in a single, shared VDM. For more information, see the Remarks section of this topic.

</dd> <dt>

**CreateSharedWowVdm**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) method runs the new process in the shared Virtual DOS Machine (VDM). This property can override the DefaultSeparateVDM switch in the Windows section of Win.ini if set to **True**. For more information, see the Remarks section of this topic.

</dd> <dt>

**CreatorSID**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Security identifier (SID) that uniquely identifies the user who creates a filter. WMI stores the SID of the user who creates an instance of [**\_\_EventConsumer**](--eventconsumer.md) or the Administrator SID, depending on the operating system. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md) and [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**DesktopName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Not used. If a value is assigned to this property a tracing message is generated. For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

</dd> <dt>

**ExecutablePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Module to execute. The string can specify the full path and file name of the module to execute, or it can specify a partial name. If a partial name is specified, the current drive and current directory are assumed.

The **ExecutablePath** property can be **NULL**. In that case, the module name must be the first white space-delimited token in the **CommandLineTemplate** property value. If using a long file name that contains a space, use quoted strings to indicate where the file name ends and the arguments begin to clarify the file name.

> [!Note]  
> Because the **CommandLineTemplate** property can be a template where the module to execute is supplied by a variable, a **NULL** **ExecutablePath** property permits the module that is specified in the parameter to execute, and then it is out of your control. Always set the **ExecutablePath** property in the **CommandLineEventConsumer** registration to include the required executable, which avoids overwriting by events parameters. If you must use a template and variable to specify the module to execute, be careful about who is granted full write privilege in the namespace.

 

</dd> <dt>

**FillAttribute**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the initial text and background colors if a new console window is created in a console application

</dd> <dt>

**FillAttributes**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Initial text and background colors, if a new console window is created in a console application. This property is ignored in a GUI application. The value can be any combination of the following values.

<dt>

1 (0x1)
</dt> <dd>

blue foreground

</dd> <dt>

2 (0x2)
</dt> <dd>

green foreground

</dd> <dt>

4 (0x4)
</dt> <dd>

red foreground

</dd> <dt>

8 (0x8)
</dt> <dd>

foreground intensity

</dd> <dt>

16 (0x10)
</dt> <dd>

blue background

</dd> <dt>

32 (0x20)
</dt> <dd>

green background

</dd> <dt>

64 (0x40)
</dt> <dd>

red background

</dd> <dt>

128 (0x80)
</dt> <dd>

background intensity

</dd> </dl>

For example, the following combinations produce red text on a white background:


```mof
0x4 | 0x40 | 0x20 | 0x10
```



  or  


```mof
0x74
```



</dd> <dt>

**ForceOffFeedback**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the feedback cursor is forced off while the process is starting. The normal cursor is displayed.

</dd> <dt>

**ForceOnFeedback**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the cursor is in feedback mode for two seconds after [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) is called. During those two seconds, if the process makes the first GUI call, the system gives five more seconds to the process. During those five seconds, if the process shows a window, the system gives another five seconds to the process to finish drawing the window.

</dd> <dt>

**KillTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number, in seconds, that the WMI service waits before killing a process 0 (zero) indicates a process is not to be killed. Killing a process prevents a process from running indefinitely.

</dd> <dt>

**MachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the computer to which Windows Management Instrumentation (WMI) sends events.

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**MaximumQueueSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Maximum queue for a specific consumer, in bytes.

This property is inherited from [**\_\_EventConsumer**](--eventconsumer.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](key-qualifier.md)
</dt> </dl>

Unique name of a consumer.

</dd> <dt>

**Priority**
</dt> <dd> <dl> <dt>

Data type: **sint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Scheduling priority level of the process threads. The following list lists the priority levels available.

<dt>

32 (0x20)
</dt> <dd>

Indicates a normal process without scheduling needs.

</dd> <dt>

64 (0x40)
</dt> <dd>

Indicates a process whose threads run only when the system is idle, and are preempted by the threads of any process running in a higher priority class. An example is a screen saver. The idle priority class is inherited by child processes.

</dd> <dt>

128 (0x80)
</dt> <dd>

Indicates a process that performs high-priority, time critical tasks. The threads of a high-priority class process preempts the threads of normal-priority or idle-priority class processes. An example is the Task List, which must respond quickly when called by the user regardless of the load on the system. Use extreme care when using the high-priority class, because a CPU-bound application with a high-priority class can use nearly all available cycles.

</dd> <dt>

256 (0x100)
</dt> <dd>

Indicates a process that has the highest possible priority. The threads of a real-time priority class process preempt the threads of all other processes, including operating system processes that perform important tasks. For example, a real-time process that executes for more than a brief interval can cause disk caches not to flush, or cause the mouse to be unresponsive.

</dd> </dl>

</dd> <dt>

**RunInteractively**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the process is launched in the interactive WinStation. If **False**, the process is launched in the default service WinStation. This property overrides the **DesktopName** property. This property is only used locally, and only if the interactive user is the same user who set up the consumer.

Starting with Windows Vista, the process running the **CommandLineEventConsumer** instance is started under the **LocalSystem** account and is in session 0. Services which run in session 0 cannot interact with user sessions.

</dd> <dt>

**ShowWindowCommand**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Window show state. It can be any of the values that can be specified in the *nCmdShow* parameter for the [ShowWindow](/windows/desktop/api/winuser/nf-winuser-showwindow) function.

</dd> <dt>

**UseDefaultErrorMode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

If **True**, the default error mode is used.

</dd> <dt>

**WindowTitle**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Title that appears on the title bar of the process. This property is ignored for GUI applications.

</dd> <dt>

**WorkingDirectory**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Working directory for this process.

</dd> <dt>

**XCoordinate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

X-offset, in pixels, from the left edge of the screen to the left edge of the window, if a new window is created.

</dd> <dt>

**XNumCharacters**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Screen buffer width, in character columns, if a new console window is created. This property is ignored in a GUI process.

</dd> <dt>

**XSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Width, in pixels, of a new window, if a new window is created.

</dd> <dt>

**YCoordinate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Y-offset, in pixels, from the top edge of the screen to the top edge of the window, if a new window is created.

</dd> <dt>

**YNumCharacters**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Screen buffer height, in character rows, if a new console window is created. This property is ignored in a GUI process.

</dd> <dt>

**YSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Height, in pixels, of the new window, if a new window is created.

</dd> </dl>

## Remarks

The **CommandLineEventConsumer** class is derived from the [**\_\_EventConsumer**](--eventconsumer.md) abstract class.

The **CreateSeparateWowVdm** property indicates whether or not the new process runs in a private Virtual DOS Machine (VDM). The advantage of running separately is that a crash only terminates the single VDM. Programs running in distinct VDMs continue to function normally, and the 16-bit Windows-based applications running in separate VDMs have separate input queues. This means that if one application stops responding momentarily, the applications in separate VDMs continue to receive input. The disadvantage of running separately is that it takes significantly more memory to do so. You should set this property to **True** only if the user requests that 16-bit Windows-based applications run in their own VDM.

> [!Note]  
> The **CommandLineEventConsumer** uses the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) method internally, and passes the **ExecutablePath** and **CommandLineTemplate** properties as the *lpApplicationName* and *lpCommandLine* parameters. The following Managed Object Format (MOF) code example does not use **CommandLineEventConsumer** correctly.

 


```mof
instance of CommandLineEventConsumer
{
  ExecutablePath = "C:\\windows\\system32\\cscript.exe";
  CommandLineTemplate = "C:\\scripts\\MyScript.js param1 param2";
};
```



The [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) method passes *lpCommandLine* as `argv[0]`, `argv[1]`, and so on. Because `argv[0]` for 16-bit applications used to be reserved for the executable file name, the previous MOF code results in the process being created as though the following command is entered at the command prompt: **c:\\windows\\system32\\cscript.exe param1 param2**.

The previous command does not succeed because Cscript.exe does not look at `argv[0]`, and so it does not recognize that it does not contain its own name, but something else ("c:\\\\scripts\\\\MyScript.js"). The following example identifies the recommended use of **CommandLineEventConsumer**.


```mof
instance of CommandLineEventConsumer
{
  ExecutablePath = "C:\\windows\\system32\\cscript.exe";
  CommandLineTemplate = "C:\\windows\\system32\\cscript.exe"
    "C:\\scripts\\MyScript.js param1 param2";
};
```



The previous use of **CommandLineEventConsumer** results in the process created as though the following command was entered at the command prompt: **c:\\windows\\system32\\cscript.exe c:\\scripts\\MyScript.js param1 param2**

Because "c:\\\\scripts\\\\MyScript.js" is now `argv[1]`, it is seen by Cscript.exe and the command succeeds.

For more information, see the [**CreateProcess**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-createprocessa) function.

## Examples

For an example of using **CommandLineEventConsumer** to create a consumer, see [Running a Program from the Command Line Based on an Event](running-a-program-from-the-command-line-based-on-an-event.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\subscription<br/>                                                           |
| MOF<br/>                      | <dl> <dt>Wbemcons.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemcons.dll</dt> </dl> |



## See also

<dl> <dt>

[Standard Consumer Classes](standard-consumer-classes.md)
</dt> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> <dt>

[Creating a Logical Consumer](creating-a-logical-consumer.md)
</dt> <dt>

[Receiving Events At All Times](receiving-events-at-all-times.md)
</dt> <dt>

[**\_\_EventConsumer**](--eventconsumer.md)
</dt> </dl>

 

