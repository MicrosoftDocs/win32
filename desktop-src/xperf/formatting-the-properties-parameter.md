---
title: Formatting the Properties Parameter
description: Formatting the Properties Parameter
ms.assetid: 49f8413e-bbc7-4a90-9964-88b049011bff
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Formatting the Properties Parameter

The *Properties* parameter of the [**StartKernelTrace**](startkerneltrace.md) function points to an **EVENT\_TRACE\_PROPERTIES** structure. This structure specifies the configuration of certain aspects of session behavior.

You must follow these guidelines when formatting the contents of this structure:

1.  You must format the first member of the **EVENT\_TRACE\_PROPERTIES** structure as a [WNODE\_HEADER](http://go.microsoft.com/fwlink/p/?linkid=141502) structure. In the following discussion, this member is referred as *Wnode*.

2.  You must set the following **EVENT\_TRACE\_PROPERTIES.Wnode** members in order to configure kernel trace control:

    <dl> <dt>

<span id="Wnode.BufferSize"></span><span id="wnode.buffersize"></span><span id="WNODE.BUFFERSIZE"></span>**Wnode.BufferSize**
</dt> <dd>

    This member contains the total size of memory allocated, in bytes, of the event tracing session properties. The size of memory must include enough space to store:

    -   The EVENT\_TRACE\_PROPERTIES structure.
    -   The session name string.
    -   The log file name string.

    </dd> <dt>

<span id="Wnode.Guid"></span><span id="wnode.guid"></span><span id="WNODE.GUID"></span>**Wnode.Guid**
</dt> <dd>

    Each tracing session must have a GUID defined to reference the session.

    For an NT Kernel Logger session, this member must be set to **SystemTraceControlGuid**. For more information about **SystemTraceControlGuid**, see[NT Kernel Logger Constants](http://go.microsoft.com/fwlink/p/?linkid=141503).

    </dd> <dt>

<span id="Wnode.ClientContext"></span><span id="wnode.clientcontext"></span><span id="WNODE.CLIENTCONTEXT"></span>**Wnode.ClientContext**
</dt> <dd>

    This member sets the clock resolution that is used when the logging time stamp for each event is calculated. The default value for this member is Query performance counter (1).

    You can specify one of the following values:

    

    | Value        | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
    |--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | 1<br/> | Query performance counter (QPC). <br/> The QPC provides a high-resolution (100 nanoseconds) time stamp which is comparatively more expensive to retrieve. <br/> You should use this resolution if you have high event rates, or if the consumer merges events from different buffers.<br/> Note that on older computers, the time stamp may not be accurate because the counter sometimes skips forward due to hardware errors.<br/>                                                                                                                                                               |
    | 2<br/> | System time. <br/> The system time provides a low-resolution (10 milliseconds) time stamp which is comparatively less expensive to retrieve.<br/> Note that if the volume of events is high, the resolution for system time may not be fine enough to determine the sequence of events. In this case, a set of events will have the same time stamp, but the order in which Event Tracing for Windows (ETW) delivers the events may not be correct.<br/>                                                                                                                                                 |
    | 3<br/> | CPU cycle counter. <br/> The CPU counter provides the highest resolution time stamp and is the least expensive to retrieve. However, the CPU counter is unreliable and should not be used in production. For example, on some computers, the timers will change frequency due to thermal and power changes, in addition to stopping in some states. <br/> If your hardware does not support this clock type, ETW uses system time.<br/> In Windows Server 2003, Windows XP SP1, and Windows XP, this value is not supported. It was introduced in Windows Server 2003 SP1 and Windows XP SP2.<br/> |

    

     

    </dd> <dt>

<span id="Wnode.Flags"></span><span id="wnode.flags"></span><span id="WNODE.FLAGS"></span>**Wnode.Flags**
</dt> <dd>

    This member must contain **WNODE\_FLAG\_TRACED\_GUID** to indicate that the structure contains event tracing information and the information is sent to a logger. **WNODE\_FLAG\_TRACED\_GUID** is defined in Evntrace.h.

    </dd> </dl>

3.  Other EVENT\_TRACE\_PROPERTIES members that you should set include the following:

    <dl> <dt>

<span id="LogFileMode"></span><span id="logfilemode"></span><span id="LOGFILEMODE"></span>**LogFileMode**
</dt> <dd>

    Indicates which logging modes are to be used in the kernel event tracing session. You can use this member to specify that events are to be written to a log file, a real-time consumer, or both.

    This member can also be used to specify that the session is a private logger session. One or more modes can be specified. For a list of possible modes, see [LoggingModeConstants](http://go.microsoft.com/fwlink/p/?linkid=14505).

    > [!Note]  
    > Do not specify real-time logging unless there are real-time consumers ready to consume the events. If there are no real-time consumers the events are written to a playback file. The size of the playback file is limited. If the limit is reached, no new events are logged to the log file or the playback file. The logging functions fail with **STATUS\_LOG\_FILE\_FULL**.

     

    </dd> <dt>

<span id="EnableFlags"></span><span id="enableflags"></span><span id="ENABLEFLAGS"></span>**EnableFlags**
</dt> <dd>

    The EnableFlags member is used only for NT Kernel Logger sessions. EnableFlags identifies to the kernel logger which events to trace. By using logical OR, this member can contain one or more values. In addition to the events specified, the kernel logger also logs hardware configuration events.

    With the introduction of the Kernel Tracing Control API, the following trace control flags are added:

    -   **EVENT\_TRACE\_FLAG\_DISPATCHER**

    -   **EVENT\_TRACE\_FLAG\_VIRTUAL\_ALLOC**

    Starting with the Microsoft Windows SDK for Windows Server 2008 and .NET Framework 3.5, these new flags are available in the Evntrace.h file included in the SDK.

    For more information on these new flags, see New Trace Control Flags. Event trace flags that exist are explained at [EVENT\_TRACE\_PROPERTIES](http://go.microsoft.com/fwlink/p/?linkid=141500).

    </dd> <dt>

<span id="LogFileNameOffset"></span><span id="logfilenameoffset"></span><span id="LOGFILENAMEOFFSET"></span>**LogFileNameOffset**
</dt> <dd>

    This number represents the offset from the start of the structure's allocated memory to beginning of the null-terminated string that contains the log file name.

    Consider the following list when you name and allocate the log file:

    -   It is recommended that the file name should use an .etl extension.

    -   All folders in the path must exist.

    -   The path can be relative, absolute, local, or remote.

    -   The path must not contain environment variables as they are not expanded.

    -   The user who initiates the trace must have write permission for the folder.

    -   The log file name is limited to 1,024 characters.

    -   If you set **LogFileMode** to **EVENT\_TRACE\_PRIVATE\_LOGGER\_MODE** or **EVENT\_TRACE\_FILE\_MODE\_NEWFILE**, be sure to allocate enough memory to include the process identifier that is appended to the file name for private logger's sessions, and the sequential number that is added to log files created using the new file log mode.

    Also, consider the following when you work with log file configurations:

    -   If you do not want to log events to a log file (for example, you specify **EVENT\_TRACE\_REAL\_TIME\_MODE** only), set *LogFileNameOffset* to zero. If you specify only real-time logging and also provide an offset with a valid log file name, WPT/ETW uses the log file name to create a sequential log file and log events to the log file. WPT/ETW also creates the sequential log file if **LogFileMode** is zero and you provide an offset with a valid log file name.

    -   If you want to log events to a log file, you must allocate enough memory for this structure to include the log file name and session name following the structure. The log file name must follow the session name in memory.

    -   Trace files are created using the default security descriptor, meaning that the log file will have the same ACL as the parent directory. If you want access to the files restricted, create a parent directory with the appropriate ACLs.

    </dd> <dt>

<span id="LoggerNameOffset"></span><span id="loggernameoffset"></span><span id="LOGGERNAMEOFFSET"></span>**LoggerNameOffset**
</dt> <dd>

    This member represents the offset from the start of the structure's allocated memory to beginning of the null-terminated string that contains the session name.

    Consider the following list when naming logger sessions:

    -   The session name is limited to 1,024 characters.

    -   The session name is case-insensitive and must be unique.

    -   When allocating memory for this structure, sufficient memory must be reserved to include the session name and log file name following the structure.

    -   The session name must come before the log file name in memory. The log file name must be copied into the offset area. The StartKernelTrace function writes the session name defined by KERNEL\_LOGGER\_NAME.

    As per the type of log file chosen, it may be necessary to set the MaximumFileSize member. For more details on how to set the fields of **EVENT\_TRACE\_PROPERTIES**, see [EVENT\_TRACE\_PROPERTIES Structure.](http://go.microsoft.com/fwlink/p/?linkid=141500).

    > [!Note]  
    > It is not necessary to set the logger name at the **LoggerNameOffset** as **StartKernelTrace** will always use the KERNEL\_LOGGER\_NAME value to call **StartKernelTrace**. The **StartKernelTrace** API checks if the **Wnode.Guid** corresponds to **SystemTraceControlGuid** and returns **ERROR\_INVALID\_PARAMETER** if it does not. If **Wnode.Guid** corresponds to **KernelRundownGuid**, the logger name should be specified. The **KernelRundownGuid** is the control GUID used to log events such as existing process information, thread information, images loaded per process, and hardware configuration like CPU, Video, Disk, Network cards, Services, Power, PNP, and Disk IDE Channels.

     

    </dd> </dl>

 

 





