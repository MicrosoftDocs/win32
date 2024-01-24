---
description: The event type class for the log file header event. This class contains information about the event tracing session.
ms.assetid: 3d0c4044-da06-4850-95c4-99b4ea28fcd9
title: EventTrace_Header class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EventTrace_Header
- EventTrace_Header.BufferSize
- EventTrace_Header.Version
- EventTrace_Header.ProviderVersion
- EventTrace_Header.NumberOfProcessors
- EventTrace_Header.EndTime
- EventTrace_Header.TimerResolution
- EventTrace_Header.MaxFileSize
- EventTrace_Header.LogFileMode
- EventTrace_Header.BuffersWritten
- EventTrace_Header.StartBuffers
- EventTrace_Header.PointerSize
- EventTrace_Header.EventsLost
- EventTrace_Header.CPUSpeed
- EventTrace_Header.LoggerName
- EventTrace_Header.LogFileName
- EventTrace_Header.TimeZoneInformation
- EventTrace_Header.BootTime
- EventTrace_Header.PerfFreq
- EventTrace_Header.StartTime
- EventTrace_Header.ReservedFlags
- EventTrace_Header.BuffersLost
api_type: 
- NA
api_location: 
---

# EventTrace\_Header class

The event type class for the log file header event. This class contains information about the event tracing session.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType(0)]
class EventTrace_Header : EventTraceEvent
{
  uint32 BufferSize;
  uint32 Version;
  uint32 ProviderVersion;
  uint32 NumberOfProcessors;
  uint64 EndTime;
  uint32 TimerResolution;
  uint32 MaxFileSize;
  uint32 LogFileMode;
  uint32 BuffersWritten;
  uint32 StartBuffers;
  uint32 PointerSize;
  uint32 EventsLost;
  uint32 CPUSpeed;
  uint32 LoggerName;
  uint32 LogFileName;
  uint8  TimeZoneInformation[];
  uint64 BootTime;
  uint64 PerfFreq;
  uint64 StartTime;
  uint32 ReservedFlags;
  uint32 BuffersLost;
};
```

## Members

The **EventTrace\_Header** class has these types of members:

-   [Properties](#properties)

### Properties

The **EventTrace\_Header** class has these properties.

<dl> <dt>

**BootTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (17)
</dt> </dl>

Time at which the system was started, in 100-nanosecond intervals since midnight, January 1, 1601.

</dd> <dt>

**BufferSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (1)
</dt> </dl>

Size of the event tracing session's buffers, in kilobytes.

</dd> <dt>

**BuffersLost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (21)
</dt> </dl>

Total number of buffers lost.

</dd> <dt>

**BuffersWritten**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (9)
</dt> </dl>

Total number of buffers written by the event tracing session.

</dd> <dt>

**CPUSpeed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (13)
</dt> </dl>

CPU speed, in megahertz.

**Windows 2000:** Not supported.

</dd> <dt>

**EndTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (5)
</dt> </dl>

Time at which the event tracing session stopped, in 100-nanosecond intervals since midnight, January 1, 1601. This value may be 0 if you are consuming events in real time or from a log file to which the provide is still logging events.

</dd> <dt>

**EventsLost**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (12)
</dt> </dl>

Number of events lost during the event tracing session.

</dd> <dt>

**LogFileMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (8), **Format("x")**
</dt> </dl>

Current logging mode for the event tracing session. For a list of values, see Logging Mode Constants.

</dd> <dt>

**LogFileName**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (15), **Pointer**
</dt> </dl>

Name of the event tracing log file that contains the events.

</dd> <dt>

**LoggerName**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (14), **Pointer**
</dt> </dl>

Name of the event tracing session.

</dd> <dt>

**MaxFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (7)
</dt> </dl>

Maximum size of the log file, in megabytes.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (4)
</dt> </dl>

Number of processors on the system.

</dd> <dt>

**PerfFreq**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (18)
</dt> </dl>

Frequency of the high-resolution performance counter, if one exists.

</dd> <dt>

**PointerSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (11)
</dt> </dl>

Size of a pointer data type, in bytes.

</dd> <dt>

**ProviderVersion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (3)
</dt> </dl>

Build number of the operating system.

</dd> <dt>

**ReservedFlags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (20)
</dt> </dl>

Reserved.

</dd> <dt>

**StartBuffers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (10)
</dt> </dl>

Reserved.

</dd> <dt>

**StartTime**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (19)
</dt> </dl>

Time at which the event tracing session started, in 100-nanosecond intervals since midnight, January 1, 1601.

</dd> <dt>

**TimerResolution**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (6)
</dt> </dl>

Resolution of the hardware timer, in units of 100 nanoseconds.

</dd> <dt>

**TimeZoneInformation**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (16), **Extension("NoPrint")**, **Max** (176)
</dt> </dl>

A [**TIME\_ZONE\_INFORMATION**](/windows/win32/api/timezoneapi/ns-timezoneapi-time_zone_information) structure that contains the time zone for the **BootTime**, **EndTime** and **StartTime** members.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **WmiDataId** (2)
</dt> </dl>

Version number of the operating system. Starting with the low-order bytes, the first two bytes contain major version, the next two bytes contain minor version, the next two bytes contain service pack major version, and the last two bytes contain service pack minor version.

</dd> </dl>

## Remarks

Typically, you want to save the values for the following properties for use later when processing events from the log file.

-   **TimerResolution**—use with the **KernelTime** and **UserTime** members of the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure to determine the CPU cost for a set of instructions. For details, see the Remarks section of [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header).
-   **PointerSize**—for properties that contain the **Pointer** qualifier, use this value to determine the size of the pointer. Note that this value may not be accurate. For example, on a 64-bit computer, a 32-bit application will log 4-byte pointers; however, the session will set **PointerSize** to 8.
-   **LogFileMode**—use to determine if this session is a private logger session. There are some properties that do not contain data for private logger sessions. For example, the **KernelTime** and **UserTime** members of the [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[**EventTraceEvent**](eventtraceevent.md)
</dt> <dt>

[**TRACE\_LOGFILE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-trace_logfile_header)
</dt> </dl>

 

 
