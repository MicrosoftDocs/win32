---
Description: The TRACE\_LOGFILE\_HEADER structure contains information about an event tracing session and its events.
ms.assetid: 13fdabe6-c904-4546-b876-c145f6a6c345
title: TRACE_LOGFILE_HEADER structure
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TRACE_LOGFILE_HEADER
api_type: 
- HeaderDef
api_location: 
- Evntrace.h
---

# TRACE\_LOGFILE\_HEADER structure

The TRACE\_LOGFILE\_HEADER structure contains information about an event tracing session and its events.

## Syntax


```C++
typedef struct _TRACE_LOGFILE_HEADER {
  ULONG                 BufferSize;
  union {
    ULONG  Version;
    struct {
      UCHAR MajorVersion;
      UCHAR MinorVersion;
      UCHAR SubVersion;
      UCHAR SubMinorVersion;
    } VersionDetail;
  };
  ULONG                 ProviderVersion;
  ULONG                 NumberOfProcessors;
  LARGE_INTEGER         EndTime;
  ULONG                 TimerResolution;
  ULONG                 MaximumFileSize;
  ULONG                 LogFileMode;
  ULONG                 BuffersWritten;
  union {
    GUID   LogInstanceGuid;
    struct {
      ULONG StartBuffers;
      ULONG PointerSize;
      ULONG EventsLost;
      ULONG CpuSpeedInMHz;
    };
  };
  LPWSTR                LoggerName;
  LPWSTR                LogFileName;
  TIME_ZONE_INFORMATION TimeZone;
  LARGE_INTEGER         BootTime;
  LARGE_INTEGER         PerfFreq;
  LARGE_INTEGER         StartTime;
  ULONG                 ReservedFlags;
  ULONG                 BuffersLost;
} TRACE_LOGFILE_HEADER, *PTRACE_LOGFILE_HEADER;
```



## Members

<dl> <dt>

**BufferSize**
</dt> <dd>

Size of the event tracing session's buffers, in bytes.

</dd> <dt>

**Version**
</dt> <dd>

Version number of the operating system. This is a roll-up of the members of **VersionDetail**. Starting with the low-order bytes, the first two bytes contain **MajorVersion**, the next two bytes contain **MinorVersion**, the next two bytes contain **SubVersion**, and the last two bytes contain **SubMinorVersion**.

</dd> <dt>

**VersionDetail**
</dt> <dd> <dl> <dt>

**MajorVersion**
</dt> <dd>

Major version number of the operating system.

</dd> <dt>

**MinorVersion**
</dt> <dd>

Minor version number of the operating system.

</dd> <dt>

**SubVersion**
</dt> <dd>

Reserved.

</dd> <dt>

**SubMinorVersion**
</dt> <dd>

Reserved.

</dd> </dl> </dd> <dt>

**ProviderVersion**
</dt> <dd>

Build number of the operating system.

</dd> <dt>

**NumberOfProcessors**
</dt> <dd>

Number of processors on the system.

</dd> <dt>

**EndTime**
</dt> <dd>

Time at which the event tracing session stopped, in 100-nanosecond intervals since midnight, January 1, 1601. This value may be 0 if you are consuming events in real time or from a log file to which the provide is still logging events.

</dd> <dt>

**TimerResolution**
</dt> <dd>

Resolution of the hardware timer, in units of 100 nanoseconds. For usage, see the Remarks for [**EVENT\_TRACE\_HEADER**](event-trace-header.md).

</dd> <dt>

**MaximumFileSize**
</dt> <dd>

Maximum size of the log file, in megabytes.

</dd> <dt>

**LogFileMode**
</dt> <dd>

Current logging mode for the event tracing session. For a list of values, see [Logging Mode Constants](logging-mode-constants.md).

</dd> <dt>

**BuffersWritten**
</dt> <dd>

Total number of buffers written by the event tracing session.

</dd> <dt>

**LogInstanceGuid**
</dt> <dd>

Reserved.

</dd> <dt>

**StartBuffers**
</dt> <dd>

Reserved.

</dd> <dt>

**PointerSize**
</dt> <dd>

Size of a pointer data type, in bytes.

</dd> <dt>

**EventsLost**
</dt> <dd>

Number of events lost during the event tracing session. Events may be lost due to insufficient memory or a very high rate of incoming events.

</dd> <dt>

**CpuSpeedInMHz**
</dt> <dd>

CPU speed, in megahertz.

**Windows 2000:** This member is not supported.

</dd> <dt>

**LoggerName**
</dt> <dd>

Do not use.

The name of the event tracing session is the first null-terminated string following this structure in memory.

</dd> <dt>

**LogFileName**
</dt> <dd>

Do Not use.

The name of the event tracing log file is the second null-terminated string following this structure in memory. The first string is the name of the session.

</dd> <dt>

**TimeZone**
</dt> <dd>

A [**TIME\_ZONE\_INFORMATION**](https://msdn.microsoft.com/en-us/library/ms725481(v=VS.85).aspx) structure that contains the time zone for the **BootTime**, **EndTime** and **StartTime** members.

</dd> <dt>

**BootTime**
</dt> <dd>

Time at which the system was started, in 100-nanosecond intervals since midnight, January 1, 1601. **BootTime** is supported only for traces written to the Global Logger session.

</dd> <dt>

**PerfFreq**
</dt> <dd>

Frequency of the high-resolution performance counter, if one exists.

</dd> <dt>

**StartTime**
</dt> <dd>

Time at which the event tracing session started, in 100-nanosecond intervals since midnight, January 1, 1601.

</dd> <dt>

**ReservedFlags**
</dt> <dd>

Specifies the clock type. For details, see the **ClientContext** member of [**WNODE\_HEADER**](wnode-header.md).

</dd> <dt>

**BuffersLost**
</dt> <dd>

Total number of buffers lost during the event tracing session.

</dd> </dl>

## Remarks

Be sure to initialize the memory for this structure to zero before setting any members.

The first event from any log file contains the data defined in this structure. You can use this structure to access the event data or you can use the [**EventTrace\_Header**](eventtrace-header.md) MOF class to decode the event data. Using this structure to read the event data may return unexpected results if the consumer is on a different computer from the one that generated the log file or the log file was written in a WOW (32-bit) session on a 64-bit computer. This is because the **LoggerName** and **LogFileName** members are pointers and can vary in size depending on the **PointerSize** member.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                            |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Evntrace.h</dt> </dl> |



## See also

<dl> <dt>

[**EVENT\_TRACE\_LOGFILE**](event-trace-logfile.md)
</dt> <dt>

[**LARGE\_INTEGER**](https://msdn.microsoft.com/en-us/library/Aa383713(v=VS.85).aspx)
</dt> <dt>

[**TIME\_ZONE\_INFORMATION**](https://msdn.microsoft.com/en-us/library/ms725481(v=VS.85).aspx)
</dt> </dl>

 

 




