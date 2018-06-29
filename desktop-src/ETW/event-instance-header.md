---
Description: The EVENT\_INSTANCE\_HEADER structure contains standard event tracing information common to all events.
ms.assetid: 2a79d937-2a3b-4426-b31f-a1a3ce86a334
title: EVENT\_INSTANCE\_HEADER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EVENT_INSTANCE_HEADER
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# EVENT\_INSTANCE\_HEADER structure

The **EVENT\_INSTANCE\_HEADER** structure contains standard event tracing information common to all events. The structure also contains registration handles for the event trace class and related parent event, which you use to trace instances of a transaction or hierarchical relationships between related events.

## Syntax


```C++
typedef struct _EVENT_INSTANCE_HEADER {
  USHORT        Size;
  union {
    USHORT FieldTypeFlags;
    struct {
      UCHAR HeaderType;
      UCHAR MarkerFlags;
    };
  };
  union {
    ULONG  Version;
    struct {
      UCHAR  Type;
      UCHAR  Level;
      USHORT Version;
    } Class;
  };
  ULONG         ThreadId;
  ULONG         ProcessId;
  LARGE_INTEGER TimeStamp;
  ULONGLONG     RegHandle;
  ULONG         InstanceId;
  ULONG         ParentInstanceId;
  union {
    struct {
      ULONG ClientContext;
      ULONG Flags;
    };
    struct {
      ULONG KernelTime;
      ULONG UserTime;
    };
    ULONG64 ProcessorTime;
  };
  ULONGLONG     ParentRegHandle;
} EVENT_INSTANCE_HEADER;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Total number of bytes of the event. **Size** must include the size of the **EVENT\_INSTANCE\_HEADER** structure, plus the size of any event-specific data appended to this structure. The size must be less than the size of the event tracing session's buffer minus 72 (0x48).

</dd> <dt>

**FieldTypeFlags**
</dt> <dd>

Reserved.

</dd> <dt>

**HeaderType**
</dt> <dd>

Reserved.

</dd> <dt>

**MarkerFlags**
</dt> <dd>

Reserved.

</dd> <dt>

**Version**
</dt> <dd>

This is a roll-up of the members of **Class**. The low-order byte contains the Type, the next byte contains the Level, and the last two bytes contain the version.

</dd> <dt>

**Class**
</dt> <dd> <dl> <dt>

**Type**
</dt> <dd>

Type of event. A provider can define their own event types or use the predefined event types listed in the following table.



| Value                                                                                                                                                                                                     | Meaning                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="EVENT_TRACE_TYPE_CHECKPOINT"></span><span id="event_trace_type_checkpoint"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_CHECKPOINT**</dt> </dl> | Checkpoint event. Use for an event that is not at the start or end of an activity.<br/>                                                                                                                                                                                                                          |
| <span id="EVENT_TRACE_TYPE_DC_END"></span><span id="event_trace_type_dc_end"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_DC\_END**</dt> </dl>            | Data collection end event.<br/>                                                                                                                                                                                                                                                                                  |
| <span id="EVENT_TRACE_TYPE_DC_START"></span><span id="event_trace_type_dc_start"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_DC\_START**</dt> </dl>      | Data collection start event.<br/>                                                                                                                                                                                                                                                                                |
| <span id="EVENT_TRACE_TYPE_DEQUEUE"></span><span id="event_trace_type_dequeue"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_DEQUEUE**</dt> </dl>          | Dequeue event. Use when an activity is queued before it begins. Use EVENT\_TRACE\_TYPE\_START to mark the time when a work item is queued. Use the dequeue event type to mark the time when work on the item actually begins. Use EVENT\_TRACE\_TYPE\_END to mark the time when work on the item completes.<br/> |
| <span id="EVENT_TRACE_TYPE_END"></span><span id="event_trace_type_end"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_END**</dt> </dl>                      | End event. Use to trace the final state of a multi-step event.<br/>                                                                                                                                                                                                                                              |
| <span id="EVENT_TRACE_TYPE_EXTENSION"></span><span id="event_trace_type_extension"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_EXTENSION**</dt> </dl>    | Extension event. Use for an event that is a continuation of a previous event. For example, use the extension event type when an event trace records more data than can fit in a session buffer.<br/>                                                                                                             |
| <span id="EVENT_TRACE_TYPE_INFO"></span><span id="event_trace_type_info"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_INFO**</dt> </dl>                   | Informational event. This is the default event type.<br/>                                                                                                                                                                                                                                                        |
| <span id="EVENT_TRACE_TYPE_REPLY"></span><span id="event_trace_type_reply"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_REPLY**</dt> </dl>                | Reply event. Use when an application that requests resources can receive multiple responses. For example, if a client application requests a URL, and the web server replies by sending several files, each file received can be marked as a reply event.<br/>                                                   |
| <span id="EVENT_TRACE_TYPE_START"></span><span id="event_trace_type_start"></span><dl> <dt>**EVENT\_TRACE\_TYPE\_START**</dt> </dl>                | Start event. Use to trace the initial state of a multi-step event.<br/>                                                                                                                                                                                                                                          |



 

If your event trace class GUID supports multiple event types, consumers will use the event type to determine the event and how to interpret its contents.

</dd> <dt>

**Level**
</dt> <dd>

Provider-defined value that defines the severity level used to generate the event. The value ranges from 0 to 255. The controller specifies the severity level when it calls the [**EnableTrace**](enabletrace.md) function. The provider retrieves the severity level by calling the [**GetTraceEnableLevel**](gettraceenablelevel.md) function from its [*ControlCallback*](controlcallback.md) implementation. The provider uses the value to set this member.

ETW defines the following severity levels. Selecting a level higher than 1 will also include events for lower levels. For example, if the controller specifies TRACE\_LEVEL\_WARNING (3), the provider also generates TRACE\_LEVEL\_FATAL (1) and TRACE\_LEVEL\_ERROR (2) events.



| Value                                                                                                                                                                                                                                               | Meaning                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <span id="TRACE_LEVEL_FATAL"></span><span id="trace_level_fatal"></span><dl> <dt>**TRACE\_LEVEL\_FATAL**</dt> <dt>1</dt> </dl>                   | Abnormal exit or termination events.<br/>           |
| <span id="TRACE_LEVEL_ERROR"></span><span id="trace_level_error"></span><dl> <dt>**TRACE\_LEVEL\_ERROR**</dt> <dt>2</dt> </dl>                   | Severe error events.<br/>                           |
| <span id="TRACE_LEVEL_WARNING"></span><span id="trace_level_warning"></span><dl> <dt>**TRACE\_LEVEL\_WARNING**</dt> <dt>3</dt> </dl>             | Warning events such as allocation failures.<br/>    |
| <span id="TRACE_LEVEL_INFORMATION"></span><span id="trace_level_information"></span><dl> <dt>**TRACE\_LEVEL\_INFORMATION**</dt> <dt>4</dt> </dl> | Non-error events such as entry or exit events.<br/> |
| <span id="TRACE_LEVEL_VERBOSE"></span><span id="trace_level_verbose"></span><dl> <dt>**TRACE\_LEVEL\_VERBOSE**</dt> <dt>5</dt> </dl>             | Detailed trace events.<br/>                         |



 

</dd> <dt>

**Version**
</dt> <dd>

Indicates the version of the event trace class that you are using to log the event. Specify zero if there is only one version of your event trace class. The version tells the consumer which MOF class to use to decipher the event data.

</dd> </dl> </dd> <dt>

**ThreadId**
</dt> <dd>

On output, identifies the thread that generated the event.

Note that on Windows 2000, **ThreadId** was a **ULONGLONG** value.

</dd> <dt>

**ProcessId**
</dt> <dd>

On output, identifies the process that generated the event.

**Windows 2000:** This member is not supported.

</dd> <dt>

**TimeStamp**
</dt> <dd>

On output, contains the time the event occurred, in 100-nanosecond intervals since midnight, January 1, 1601.

</dd> <dt>

**RegHandle**
</dt> <dd>

Handle to a registered event trace class. Set this property before calling the [**TraceEventInstance**](traceeventinstance.md) function.

The [**RegisterTraceGuids**](registertraceguids.md) function creates this handle (see the *TraceGuidReg* parameter).

</dd> <dt>

**InstanceId**
</dt> <dd>

On output, contains the event trace instance identifier associated with **RegHandle**.

</dd> <dt>

**ParentInstanceId**
</dt> <dd>

On output, contains the event trace instance identifier associated with **ParentRegHandle**.

</dd> <dt>

**ClientContext**
</dt> <dd>

Reserved.

</dd> <dt>

**Flags**
</dt> <dd>

Must contain **WNODE\_FLAG\_TRACED\_GUID**, and may also contain any combination of the following.



| Value                                                                                                                                                                                          | Meaning                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WNODE_FLAG_USE_GUID_PTR"></span><span id="wnode_flag_use_guid_ptr"></span><dl> <dt>**WNODE\_FLAG\_USE\_GUID\_PTR**</dt> </dl> | Specify if the **GuidPtr** member contains the class GUID.<br/>                                                                                                                                    |
| <span id="WNODE_FLAG_USE_MOF_PTR"></span><span id="wnode_flag_use_mof_ptr"></span><dl> <dt>**WNODE\_FLAG\_USE\_MOF\_PTR**</dt> </dl>    | Specify if an array of [**MOF\_FIELD**](mof-field.md) structures contains the event data appended to this structure. The number of elements in the array is limited to **MAX\_MOF\_FIELDS**.<br/> |



 

</dd> <dt>

**KernelTime**
</dt> <dd>

Elapsed execution time for kernel-mode instructions, in CPU ticks. If you are using a private session, use the value in the **ProcessorTime** member instead.

</dd> <dt>

**UserTime**
</dt> <dd>

Elapsed execution time for user-mode instructions, in CPU ticks. If you are using a private session, use the value in the **ProcessorTime** member instead.

</dd> <dt>

**ProcessorTime**
</dt> <dd>

For private sessions, the elapsed execution time for user-mode instructions, in CPU ticks.

</dd> <dt>

**ParentRegHandle**
</dt> <dd>

Handle to a registered event trace class of a parent event. Set this property before calling the [**TraceEventInstance**](traceeventinstance.md) function if you want to trace a hierarchical relationship (parent element/child element) between related events.

The [**RegisterTraceGuids**](registertraceguids.md) function creates this handle (see the *TraceGuidReg* parameter).

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**TraceEventInstance**](traceeventinstance.md)
</dt> </dl>

 

 




