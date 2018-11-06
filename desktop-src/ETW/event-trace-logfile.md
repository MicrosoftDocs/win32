---
Description: The EVENT\_TRACE\_LOGFILE structure specifies how the consumer wants to read events (from a log file or in real-time) and the callbacks that will receive the events.
ms.assetid: 179451e9-7e3c-4d3a-bcc6-3ad9d382229a
title: EVENT_TRACE_LOGFILE structure
ms.topic: structure
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- EVENT_TRACE_LOGFILE
- EVENT_TRACE_LOGFILEA
- EVENT_TRACE_LOGFILEW
api_type:
- HeaderDef
api_location:
- Evntrace.h
---

# EVENT\_TRACE\_LOGFILE structure

The **EVENT\_TRACE\_LOGFILE** structure specifies how the consumer wants to read events (from a log file or in real-time) and the callbacks that will receive the events.

When ETW flushes a buffer, this structure contains information about the event tracing session and the buffer that ETW flushed.

## Syntax


```C++
typedef struct _EVENT_TRACE_LOGFILE {
  LPTSTR                       LogFileName;
  LPTSTR                       LoggerName;
  LONGLONG                     CurrentTime;
  ULONG                        BuffersRead;
  union {
    ULONG LogFileMode;
    ULONG ProcessTraceMode;
  };
  EVENT_TRACE                  CurrentEvent;
  TRACE_LOGFILE_HEADER         LogfileHeader;
  PEVENT_TRACE_BUFFER_CALLBACK BufferCallback;
  ULONG                        BufferSize;
  ULONG                        Filled;
  ULONG                        EventsLost;
  union {
    PEVENT_CALLBACK        EventCallback;
    PEVENT_RECORD_CALLBACK EventRecordCallback;
  };
  ULONG                        IsKernelTrace;
  PVOID                        Context;
} EVENT_TRACE_LOGFILE, *PEVENT_TRACE_LOGFILE;
```



## Members

<dl> <dt>

**LogFileName**
</dt> <dd>

Name of the log file used by the event tracing session. Specify a value for this member if you are consuming from a log file. This member must be **NULL** if **LoggerName** is specified.

You must know the log file name the controller specified. If the controller logged events to a private session (the controller set the **LogFileMode** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) to **EVENT\_TRACE\_PRIVATE\_LOGGER\_MODE**), the file name must include the process identifier that ETW appended to the log file name. For example, if the controller named the log file xyz.etl and the process identifier is 123, ETW uses xyz.etl\_123 as the file name.

If the controller set the **LogFileMode** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) to **EVENT\_TRACE\_FILE\_MODE\_NEWFILE**, the log file name must include the sequential serial number used to create each new log file.

The user consuming the events must have permissions to read the file.

</dd> <dt>

**LoggerName**
</dt> <dd>

Name of the event tracing session. Specify a value for this member if you want to consume events in real time. This member must be **NULL** if **LogFileName** is specified.

You can only consume events in real time if the controller set the **LogFileMode** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md) to **EVENT\_TRACE\_REAL\_TIME\_MODE**.

Only users with administrative privileges, users in the Performance Log Users group, and applications running as LocalSystem, LocalService, NetworkService can consume events in real time. To grant a restricted user the ability to consume events in real time, add them to the Performance Log Users group or call [**EventAccessControl**](/windows/desktop/api/Evntcons/nf-evntcons-eventaccesscontrol).

**Windows XP and Windows 2000:** Anyone can consume real time events.

</dd> <dt>

**CurrentTime**
</dt> <dd>

On output, the current time, in 100-nanosecond intervals since midnight, January 1, 1601.

</dd> <dt>

**BuffersRead**
</dt> <dd>

On output, the number of buffers processed.

</dd> <dt>

**LogFileMode**
</dt> <dd>

Reserved. Do not use.

</dd> <dt>

**ProcessTraceMode**
</dt> <dd>

Modes for processing events. The modes are defined in the Evntcons.h header file. You can specify one or more of the following modes:



| Value                                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="PROCESS_TRACE_MODE_EVENT_RECORD"></span><span id="process_trace_mode_event_record"></span><dl> <dt>**PROCESS\_TRACE\_MODE\_EVENT\_RECORD**</dt> </dl>    | Specify this mode if you want to receive events in the new [**EVENT\_RECORD**](https://msdn.microsoft.com/en-us/library/Aa363769(v=VS.85).aspx) format. To receive events in the new format you must specify a callback in the **EventRecordCallback** member. If you do not specify this mode, you receive events in the old format through the callback specified in the **EventCallback** member.<br/> **Prior to Windows Vista:** Not supported.<br/>                                             |
| <span id="PROCESS_TRACE_MODE_RAW_TIMESTAMP"></span><span id="process_trace_mode_raw_timestamp"></span><dl> <dt>**PROCESS\_TRACE\_MODE\_RAW\_TIMESTAMP**</dt> </dl> | Specify this mode if you do not want the time stamp value in the **TimeStamp** member of [**EVENT\_HEADER**](https://msdn.microsoft.com/en-us/library/Aa363759(v=VS.85).aspx) and [**EVENT\_TRACE\_HEADER**](event-trace-header.md) converted to system time (leaves the time stamp value in the resolution that the controller specified in the **Wnode.ClientContext** member of [**EVENT\_TRACE\_PROPERTIES**](event-trace-properties.md)).<br/> **Prior to Windows Vista:** Not supported.<br/> |
| <span id="PROCESS_TRACE_MODE_REAL_TIME"></span><span id="process_trace_mode_real_time"></span><dl> <dt>**PROCESS\_TRACE\_MODE\_REAL\_TIME**</dt> </dl>             | Specify this mode to receive events in real time (you must specify this mode if **LoggerName** is not **NULL**).<br/>                                                                                                                                                                                                                                                                                                                                        |



 

</dd> <dt>

**CurrentEvent**
</dt> <dd>

On output, an [**EVENT\_TRACE**](event-trace.md) structure that contains the last event processed.

</dd> <dt>

**LogfileHeader**
</dt> <dd>

On output, a [**TRACE\_LOGFILE\_HEADER**](trace-logfile-header.md) structure that contains general information about the session and the computer on which the session ran.

</dd> <dt>

**BufferCallback**
</dt> <dd>

Pointer to the [**BufferCallback**](buffercallback.md) function that receives buffer-related statistics for each buffer ETW flushes. ETW calls this callback after it delivers all the events in the buffer. This callback is optional.

</dd> <dt>

**BufferSize**
</dt> <dd>

On output, contains the size of each buffer, in bytes.

</dd> <dt>

**Filled**
</dt> <dd>

On output, contains the number of bytes in the buffer that contain valid information.

</dd> <dt>

**EventsLost**
</dt> <dd>

Not used.

</dd> <dt>

**EventCallback**
</dt> <dd>

Pointer to the [**EventCallback**](eventcallback.md) function that ETW calls for each event in the buffer.

Specify this callback if you are consuming events from a provider that used one of the [**TraceEvent**](traceevent.md) functions to log events.

</dd> <dt>

**EventRecordCallback**
</dt> <dd>

Pointer to the [**EventRecordCallback**](eventrecordcallback.md) function that ETW calls for each event in the buffer.

Specify this callback if you are consuming events from a provider that used one of the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) functions to log events.

**Prior to Windows Vista:** Not supported.

</dd> <dt>

**IsKernelTrace**
</dt> <dd>

On output, if this member is **TRUE**, the event tracing session is the NT Kernel Logger. Otherwise, it is another event tracing session.

</dd> <dt>

**Context**
</dt> <dd>

Context data that a consumer can specify when calling [**OpenTrace**](opentrace.md). If the consumer uses [**EventRecordCallback**](eventrecordcallback.md) to consume events, ETW sets the **UserContext** member of the [**EVENT\_RECORD**](https://msdn.microsoft.com/en-us/library/Aa363769(v=VS.85).aspx) structure to this value.

**Prior to Windows Vista:** Not supported.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

Consumers pass this structure to the [**OpenTrace**](opentrace.md) function.

When ETW flushes a buffer, it passes the structure to the consumer's [**BufferCallback**](buffercallback.md) function.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |
| Unicode and ANSI names<br/>   | **EVENT\_TRACE\_LOGFILEW** (Unicode) and **EVENT\_TRACE\_LOGFILEA** (ANSI)<br/> |



## See also

<dl> <dt>

[**BufferCallback**](buffercallback.md)
</dt> <dt>

[**OpenTrace**](opentrace.md)
</dt> </dl>

 

 




