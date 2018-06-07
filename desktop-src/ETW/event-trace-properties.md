---
Description: The EVENT\_TRACE\_PROPERTIES structure contains information about an event tracing session. You use this structure when you define a session, change the properties of a session, or query for the properties of a session.
ms.assetid: 0c967971-8df1-4679-a8a9-a783f5b35860
title: EVENT\_TRACE\_PROPERTIES structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# EVENT\_TRACE\_PROPERTIES structure

The **EVENT\_TRACE\_PROPERTIES** structure contains information about an event tracing session. You use this structure when you define a session, change the properties of a session, or query for the properties of a session.

## Syntax


```C++
typedef struct _EVENT_TRACE_PROPERTIES {
  WNODE_HEADER Wnode;
  ULONG        BufferSize;
  ULONG        MinimumBuffers;
  ULONG        MaximumBuffers;
  ULONG        MaximumFileSize;
  ULONG        LogFileMode;
  ULONG        FlushTimer;
  ULONG        EnableFlags;
  LONG         AgeLimit;
  ULONG        NumberOfBuffers;
  ULONG        FreeBuffers;
  ULONG        EventsLost;
  ULONG        BuffersWritten;
  ULONG        LogBuffersLost;
  ULONG        RealTimeBuffersLost;
  HANDLE       LoggerThreadId;
  ULONG        LogFileNameOffset;
  ULONG        LoggerNameOffset;
} EVENT_TRACE_PROPERTIES, *PEVENT_TRACE_PROPERTIES;
```



## Members

<dl> <dt>

**Wnode**
</dt> <dd>

A [**WNODE\_HEADER**](wnode-header.md) structure. You must specify the **BufferSize**, **Flags**, and **Guid** members, and optionally the **ClientContext** member.

</dd> <dt>

**BufferSize**
</dt> <dd>

Amount of memory allocated for each event tracing session buffer, in kilobytes. The maximum buffer size is 1 MB. ETW uses the size of physical memory to calculate this value. For more information, see Remarks.

If an application expects a relatively low event rate, the buffer size should be set to the memory page size. If the event rate is expected to be relatively high, the application should specify a larger buffer size, and should increase the maximum number of buffers.

The buffer size affects the rate at which buffers fill and must be flushed. Although a small buffer size requires less memory, it increases the rate at which buffers must be flushed.

</dd> <dt>

**MinimumBuffers**
</dt> <dd>

Minimum number of buffers allocated for the event tracing session's buffer pool. The minimum number of buffers that you can specify is two buffers per processor. For example, on a single processor computer, the minimum number of buffers is two. Note that if you use the EVENT\_TRACE\_NO\_PER\_PROCESSOR\_BUFFERING logging mode, the number of processors is assumed to be 1.

</dd> <dt>

**MaximumBuffers**
</dt> <dd>

Maximum number of buffers allocated for the event tracing session's buffer pool. Typically, this value is the minimum number of buffers plus twenty. ETW uses the buffer size and the size of physical memory to calculate this value. This value must be greater than or equal to the value for **MinimumBuffers**. Note that you do not need to set this value if **LogFileMode** contains **EVENT\_TRACE\_BUFFERING\_MODE**; instead, the total memory buffer size is instead the product of **MinimumBuffers** and **BufferSize**.

</dd> <dt>

**MaximumFileSize**
</dt> <dd>

Maximum size of the file used to log events, in megabytes. Typically, you use this member to limit the size of a circular log file when you set **LogFileMode** to **EVENT\_TRACE\_FILE\_MODE\_CIRCULAR**. This member must be specified if **LogFileMode** contains **EVENT\_TRACE\_FILE\_MODE\_PREALLOCATE**, **EVENT\_TRACE\_FILE\_MODE\_CIRCULAR** or **EVENT\_TRACE\_FILE\_MODE\_NEWFILE**

If you are using the system drive (the drive that contains the operating system) for logging, ETW checks for an additional 200MB of disk space, regardless of whether you are using the maximum file size parameter. Therefore, if you specify 100MB as the maximum file size for the trace file in the system drive, you need to have 300MB of free space on the drive.

</dd> <dt>

**LogFileMode**
</dt> <dd>

Logging modes for the event tracing session. You use this member to specify that you want events written to a log file, a real-time consumer, or both. You can also use this member to specify that the session is a private logger session. You can specify one or more modes. For a list of possible modes, see [Logging Mode Constants](logging-mode-constants.md).

Do not specify real-time logging unless there are real-time consumers ready to consume the events. If there are no real-time consumers, ETW writes the events to a playback file. However, the size of the playback file is limited. If the limit is reached, no new events are logged (to the log file or playback file) and the logging functions fail with STATUS\_LOG\_FILE\_FULL.

**Prior to Windows Vista:** If there was no real-time consumer, the events were discarded and logging continues.

If a consumer begins processing real-time events, the events in the playback file are consumed first. After all events in the playback file are consumed, the session will begin logging new events.

</dd> <dt>

**FlushTimer**
</dt> <dd>

How often, in seconds, the trace buffers are forcibly flushed. The minimum flush time is 1 second. This forced flush is in addition to the automatic flush that occurs whenever a buffer is full and when the trace session stops.

If zero, ETW flushes buffers as soon as they become full. If nonzero, ETW flushes all buffers that contain events based on the timer value. Typically, you want to flush buffers only when they become full. Forcing the buffers to flush (either by setting this member to a nonzero value or by calling [**FlushTrace**](flushtrace.md)) can increase the file size of the log file with unfilled buffer space.

If the consumer is consuming events in real time, you may want to set this member to a nonzero value if the event rate is low to force events to be delivered before the buffer is full.

For the case of a realtime logger, a value of zero (the default value) means that the flush time will be set to 1 second. A realtime logger is when **LogFileMode** is set to **EVENT\_TRACE\_REAL\_TIME\_MODE**.

</dd> <dt>

**EnableFlags**
</dt> <dd>

A system logger must set **EnableFlags** to indicate which SystemTraceProvider events should be included in the trace. This is also used for NT Kernel Logger sessions. This member can contain one or more of the following values. In addition to the events you specify, the kernel logger also logs hardware configuration events on Windows XP or system configuration events on Windows Server 2003.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Flag</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_ALPC"></span><span id="event_trace_flag_alpc"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_ALPC</strong></strong></dt> <dt>0x00100000</dt> </dl></td>
<td>Enables the [<strong>ALPC</strong>](alpc.md) event types.<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_CSWITCH"></span><span id="event_trace_flag_cswitch"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_CSWITCH</strong></strong></dt> <dt>0x00000010</dt> </dl></td>
<td>Enables the following [<strong>Thread</strong>](thread.md) event type:
<ul>
<li>[<strong>CSwitch</strong>](cswitch.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_DBGPRINT"></span><span id="event_trace_flag_dbgprint"></span><dl> <dt><strong>EVENT_TRACE_FLAG_DBGPRINT</strong></dt> <dt>0x00040000</dt> </dl></td>
<td>Enables the <strong>DbgPrint</strong> and <strong>DbgPrintEx</strong> calls to be converted to ETW events.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_DISK_FILE_IO"></span><span id="event_trace_flag_disk_file_io"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DISK_FILE_IO</strong></strong></dt> <dt>0x00000200</dt> </dl></td>
<td>Enables the following [<strong>FileIo</strong>](fileio.md) event type (you must also enable EVENT_TRACE_FLAG_DISK_IO):<br/>
<ul>
<li>[<strong>FileIo_Name</strong>](fileio-name.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_DISK_IO"></span><span id="event_trace_flag_disk_io"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DISK_IO</strong></strong></dt> <dt>0x00000100</dt> </dl></td>
<td>Enables the following [<strong>DiskIo</strong>](diskio.md) event types:<br/>
<ul>
<li>[<strong>DiskIo_TypeGroup1</strong>](diskio-typegroup1.md)</li>
<li>[<strong>DiskIo_TypeGroup3</strong>](diskio-typegroup3.md)</li>
</ul></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_DISK_IO_INIT"></span><span id="event_trace_flag_disk_io_init"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DISK_IO_INIT</strong></strong></dt> <dt>0x00000400</dt> </dl></td>
<td>Enables the following [<strong>DiskIo</strong>](diskio.md) event type:
<ul>
<li>[<strong>DiskIo_TypeGroup2</strong>](diskio-typegroup2.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_DISPATCHER"></span><span id="event_trace_flag_dispatcher"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DISPATCHER</strong></strong></dt> <dt>0x00000800</dt> </dl></td>
<td>Enables the following [<strong>Thread</strong>](thread.md) event type:
<ul>
<li>[<strong>ReadyThread</strong>](readythread.md)</li>
</ul>
<br/> This value is supported on Windows 7, Windows Server 2008 R2, and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_DPC"></span><span id="event_trace_flag_dpc"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DPC</strong></strong></dt> <dt>0x00000020</dt> </dl></td>
<td>Enables the following [<strong>PerfInfo</strong>](perfinfo.md) event type:
<ul>
<li>[<strong>DPC</strong>](dpc.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_DRIVER"></span><span id="event_trace_flag_driver"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_DRIVER</strong></strong></dt> <dt>0x00800000</dt> </dl></td>
<td>Enables the following [<strong>DiskIo</strong>](diskio.md) event types:
<ul>
<li>[<strong>DriverCompleteRequest</strong>](drivercompleterequest.md)</li>
<li>[<strong>DriverCompleteRequestReturn</strong>](drivercompleterequestreturn.md)</li>
<li>[<strong>DriverCompletionRoutine</strong>](drivercompletionroutine.md)</li>
<li>[<strong>DriverMajorFunctionCall</strong>](drivermajorfunctioncall.md)</li>
<li>[<strong>DriverMajorFunctionReturn</strong>](drivermajorfunctionreturn.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_FILE_IO"></span><span id="event_trace_flag_file_io"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_FILE_IO</strong></strong></dt> <dt>0x02000000</dt> </dl></td>
<td>Enables the following [<strong>FileIo</strong>](fileio.md) event types:
<ul>
<li>[<strong>FileIo_OpEnd</strong>](fileio-opend.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_FILE_IO_INIT"></span><span id="event_trace_flag_file_io_init"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_FILE_IO_INIT</strong></strong></dt> <dt>0x04000000</dt> </dl></td>
<td>Enables the following [<strong>FileIo</strong>](fileio.md) event type:
<ul>
<li>[<strong>FileIo_Create</strong>](fileio-create.md)</li>
<li>[<strong>FileIo_DirEnum</strong>](fileio-direnum.md)</li>
<li>[<strong>FileIo_Info</strong>](fileio-info.md)</li>
<li>[<strong>FileIo_ReadWrite</strong>](fileio-readwrite.md)</li>
<li>[<strong>FileIo_SimpleOp</strong>](fileio-simpleop.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_IMAGE_LOAD"></span><span id="event_trace_flag_image_load"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_IMAGE_LOAD</strong></strong></dt> <dt>0x00000004</dt> </dl></td>
<td>Enables the following [<strong>Image</strong>](image.md) event type:<br/>
<ul>
<li>[<strong>Image_Load</strong>](image-load.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_INTERRUPT"></span><span id="event_trace_flag_interrupt"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_INTERRUPT</strong></strong></dt> <dt>0x00000040</dt> </dl></td>
<td>Enables the following [<strong>PerfInfo</strong>](perfinfo.md) event type:
<ul>
<li>[<strong>ISR</strong>](isr.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_JOB"></span><span id="event_trace_flag_job"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_JOB</strong></strong></dt> <dt>0x00080000</dt> </dl></td>
<td>This value is supported on Windows 10<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS"></span><span id="event_trace_flag_memory_hard_faults"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_MEMORY_HARD_FAULTS</strong></strong></dt> <dt>0x00002000</dt> </dl></td>
<td>Enables the following [<strong>PageFault_V2</strong>](pagefault-v2.md) event type:<br/>
<ul>
<li>[<strong>PageFault_HardFault</strong>](pagefault-hardfault.md)</li>
</ul></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS"></span><span id="event_trace_flag_memory_page_faults"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_MEMORY_PAGE_FAULTS</strong></strong></dt> <dt>0x00001000</dt> </dl></td>
<td>Enables the following [<strong>PageFault_V2</strong>](pagefault-v2.md) event type:<br/>
<ul>
<li>[<strong>PageFault_TypeGroup1</strong>](pagefault-typegroup1.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_NETWORK_TCPIP"></span><span id="event_trace_flag_network_tcpip"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_NETWORK_TCPIP</strong></strong></dt> <dt>0x00010000</dt> </dl></td>
<td>Enables the [<strong>TcpIp</strong>](tcpip.md) and [<strong>UdpIp</strong>](udpip.md) event types.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_NO_SYSCONFIG"></span><span id="event_trace_flag_no_sysconfig"></span><dl> <dt><strong>EVENT_TRACE_FLAG_NO_SYSCONFIG</strong></dt> <dt>0x10000000</dt> </dl></td>
<td>Do not do a system configuration rundown.<br/> This value is supported on Windows 8, Windows Server 2012, and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_PROCESS"></span><span id="event_trace_flag_process"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_PROCESS</strong></strong></dt> <dt>0x00000001</dt> </dl></td>
<td>Enables the following [<strong>Process</strong>](process.md) event type:<br/>
<ul>
<li>[<strong>Process_TypeGroup1</strong>](process-typegroup1.md)</li>
</ul></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_PROCESS_COUNTERS"></span><span id="event_trace_flag_process_counters"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_PROCESS_COUNTERS</strong></strong></dt> <dt>0x00000008</dt> </dl></td>
<td>Enables the following [<strong>Process_V2</strong>](process-v2.md) event type:
<ul>
<li>[<strong>Process_V2_TypeGroup2</strong>](process-v2-typegroup2.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_PROFILE"></span><span id="event_trace_flag_profile"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_PROFILE</strong></strong></dt> <dt>0x01000000</dt> </dl></td>
<td>Enables the following [<strong>PerfInfo</strong>](perfinfo.md) event type:
<ul>
<li>[<strong>SampledProfile</strong>](sampledprofile.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_REGISTRY"></span><span id="event_trace_flag_registry"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_REGISTRY</strong></strong></dt> <dt>0x00020000</dt> </dl></td>
<td>Enables the [<strong>Registry</strong>](registry.md) event types.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_SPLIT_IO"></span><span id="event_trace_flag_split_io"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_SPLIT_IO</strong></strong></dt> <dt>0x00200000</dt> </dl></td>
<td>Enables the [<strong>SplitIo</strong>](splitio.md) event types.<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_SYSTEMCALL"></span><span id="event_trace_flag_systemcall"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_SYSTEMCALL</strong></strong></dt> <dt>0x00000080</dt> </dl></td>
<td>Enables the following [<strong>PerfInfo</strong>](perfinfo.md) event type:
<ul>
<li>[<strong>SysCallEnter</strong>](syscallenter.md)</li>
<li>[<strong>SysCallExit</strong>](syscallexit.md)</li>
</ul>
<br/> This value is supported on Windows Vista and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_THREAD"></span><span id="event_trace_flag_thread"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_THREAD</strong></strong></dt> <dt>0x00000002</dt> </dl></td>
<td>Enables the following [<strong>Thread</strong>](thread.md) event type:<br/>
<ul>
<li>[<strong>Thread_TypeGroup1</strong>](thread-typegroup1.md)</li>
</ul></td>
</tr>
<tr class="even">
<td><span id="EVENT_TRACE_FLAG_VAMAP"></span><span id="event_trace_flag_vamap"></span><dl> <dt><strong>EVENT_TRACE_FLAG_VAMAP</strong></dt> <dt>0x00008000</dt> </dl></td>
<td>Enables the map and unmap (excluding image files) event type.<br/> This value is supported on Windows 8, Windows Server 2012, and later.<br/></td>
</tr>
<tr class="odd">
<td><span id="EVENT_TRACE_FLAG_VIRTUAL_ALLOC"></span><span id="event_trace_flag_virtual_alloc"></span><dl> <dt><strong><strong>EVENT_TRACE_FLAG_VIRTUAL_ALLOC</strong></strong></dt> <dt>0x00004000</dt> </dl></td>
<td>Enables the following [<strong>PageFault_V2</strong>](pagefault-v2.md) event type:
<ul>
<li>[<strong>PageFault_VirtualAlloc</strong>](pagefault-virtualalloc.md)</li>
</ul>
<br/> This value is supported on Windows 7, Windows Server 2008 R2, and later.<br/></td>
</tr>
</tbody>
</table>



 

</dd> <dt>

**AgeLimit**
</dt> <dd>

Not used.

**Windows 2000:** Time delay before unused buffers are freed, in minutes. The default is 15 minutes.

</dd> <dt>

**NumberOfBuffers**
</dt> <dd>

On output, the number of buffers allocated for the event tracing session's buffer pool.

</dd> <dt>

**FreeBuffers**
</dt> <dd>

On output, the number of buffers that are allocated but unused in the event tracing session's buffer pool.

</dd> <dt>

**EventsLost**
</dt> <dd>

On output, the number of events that were not recorded.

</dd> <dt>

**BuffersWritten**
</dt> <dd>

On output, the number of buffers written.

</dd> <dt>

**LogBuffersLost**
</dt> <dd>

On output, the number of buffers that could not be written to the log file.

</dd> <dt>

**RealTimeBuffersLost**
</dt> <dd>

On output, the number of buffers that could not be delivered in real-time to the consumer.

</dd> <dt>

**LoggerThreadId**
</dt> <dd>

On output, the thread identifier for the event tracing session.

</dd> <dt>

**LogFileNameOffset**
</dt> <dd>

Offset from the start of the structure's allocated memory to beginning of the null-terminated string that contains the log file name.

The file name should use the .etl extension. All folders in the path must exist. The path can be relative, absolute, local, or remote. The path cannot contain environment variables (they are not expanded). The user must have permission to write to the folder.

The log file name is limited to 1,024 characters. If you set **LogFileMode** to **EVENT\_TRACE\_PRIVATE\_LOGGER\_MODE** or **EVENT\_TRACE\_FILE\_MODE\_NEWFILE**, be sure to allocate enough memory to include the process identifier that is appended to the file name for private loggers sessions, and the sequential number that is added to log files created using the new file log mode.

If you do not want to log events to a log file (for example, you specify **EVENT\_TRACE\_REAL\_TIME\_MODE** only), set *LogFileNameOffset* to 0. If you specify only real-time logging and also provide an offset with a valid log file name, ETW will use the log file name to create a sequential log file and log events to the log file. ETW also creates the sequential log file if **LogFileMode** is 0 and you provide an offset with a valid log file name.

If you want to log events to a log file, you must allocate enough memory for this structure to include the log file name and session name following the structure. The log file name must follow the session name in memory.

Trace files are created using the default security descriptor, meaning that the log file will have the same ACL as the parent directory. If you want access to the files restricted, create a parent directory with the appropriate ACLs.

</dd> <dt>

**LoggerNameOffset**
</dt> <dd>

Offset from the start of the structure's allocated memory to beginning of the null-terminated string that contains the session name.

The session name is limited to 1,024 characters. The session name is case-insensitive and must be unique.

**Windows 2000:** Session names are case-sensitive. As a result, duplicate session names are allowed. However, to reduce confusion, you should make sure your session names are unique.

When you allocate the memory for this structure, you must allocate enough memory to include the session name and log file name following the structure. The session name must come before the log file name in memory. You must copy the log file name to the offset but you do not copy the session name to the offset—the [**StartTrace**](starttrace.md) function copies the name for you.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

Events from providers are written to a session's buffers. When a buffer is full, the session flushes the buffer either by writing the events to a log file, delivering them to a real-time consumer, or both. If the session's buffers are filled faster than they can be flushed, new buffers are allocated and added to the session's buffer pool, up to the maximum number specified. Beyond this limit, the session discards incoming events until a buffer becomes available. Each session keeps a record of the number of events discarded (see the **EventsLost** member).

ETW does not free unused buffers.

**Windows 2000:** ETW frees unused buffers based on the **AgeLimit** member value.

You use the **BufferSize**, **MinimumBuffers**, and **MaximumBuffers** members to configure the buffers for an event tracing session when you define the session or anytime during the tracing session. ETW uses the physical memory and number of processors available on the computer to determine if the values are reasonable. If ETW determines the values are not reasonable, ETW will determine the correct size and overwrite the values.

Typically, you should not set these values and instead let ETW determine the size and number of buffers.

To view session statistics, such as **EventsLost** while the session is running, call the [**ControlTrace**](controltrace.md) function and set the *ControlCode* parameter to EVENT\_TRACE\_CONTROL\_QUERY.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**ControlTrace**](controltrace.md)
</dt> <dt>

[**QueryAllTraces**](queryalltraces.md)
</dt> <dt>

[**WNODE\_HEADER**](wnode-header.md)
</dt> </dl>

 

 




