---
Description: The EVENT\_TRACE\_HEADER structure is used to pass a WMI event to the WMI event logger.
ms.assetid: faddcf82-1025-458f-ab33-c96cd5699ca5
title: EVENT\_TRACE\_HEADER structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# EVENT\_TRACE\_HEADER structure

The **EVENT\_TRACE\_HEADER** structure is used to pass a WMI event to the WMI event logger. It is overlaid on the [**WNODE\_HEADER**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-_wnode_header) portion of the [**WNODE\_EVENT\_ITEM**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-tagwnode_event_item) passed to [**IoWMIWriteEvent**](/windows-hardware/drivers/ddi/content/Wdm/nf-wdm-iowmiwriteevent). Information contained in the **EVENT\_TRACE\_HEADER** is written to the WMI log file.

## Syntax


```C++
typedef struct _EVENT_TRACE_HEADER {
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
  union {
    GUID      Guid;
    ULONGLONG GuidPtr;
  };
  union {
    struct {
      ULONG KernelTime;
      ULONG UserTime;
    };
    ULONG64 ProcessorTime;
    struct {
      ULONG ClientContext;
      ULONG Flags;
    };
  };
} EVENT_TRACE_HEADER, *PEVENT_TRACE_HEADER;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

Specifies the size, in bytes, of the buffer that is allocated to hold event tracing information. The value that is specified must include both the size of the **EVENT\_TRACE\_HEADER** structure and the size of any driver-specific data. (**EVENT\_TRACE\_HEADER** is overlaid on a [**WNODE\_HEADER**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-_wnode_header) structure, but the **Size** member of **EVENT\_TRACE\_HEADER** and the **BufferSize** member of **WNODE\_HEADER** do not specify the same size. Do not use the **BufferSize** member of **WNODE\_HEADER** to set the **Size** member.)

</dd> <dt>

**FieldTypeFlags**
</dt> <dd>

Flags to indicate which fields in the **EVENT\_TRACE\_HEADER** structure are valid.

</dd> <dt>

**HeaderType**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**MarkerFlags**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**Version**
</dt> <dd>

Drivers can use this member to store version information. This information is not interpreted by the event logger.

</dd> <dt>

**Class**
</dt> <dd>

Event class information.

<dl> <dt>

**Type**
</dt> <dd>

Trace event type. This can be one of the predefined EVENT\_TRACE\_TYPE\_*XXX* values contained in Evntrace.h or can be a driver-defined value. Callers are free to define private event types with values greater than the reserved values in Evntrace.h.

</dd> <dt>

**Level**
</dt> <dd>

Trace instrumentation level. A driver-defined value meant to represent the degree of detail of the trace instrumentation. Drivers are free to give this value meaning. This value should be 0 by default. More information about how consumers can request different levels of trace information will be provided in a future version of the documentation.

</dd> <dt>

**Version**
</dt> <dd>

Version of trace record. Version information that can be used by the driver to track different event formats.

</dd> </dl> </dd> <dt>

**ThreadId**
</dt> <dd>

Thread identifier.

</dd> <dt>

**ProcessId**
</dt> <dd>

Process identifier.

</dd> <dt>

**TimeStamp**
</dt> <dd>

The time at which the driver event occurred. This time value is expressed in absolute system time format. Absolute system time is the number of 100-nanosecond intervals since the start of the year 1601 in the Gregorian calendar. If the WNODE\_FLAG\_USE\_TIMESTAMP is set in **Flags,** the system logger will leave the value of **TimeStamp** unchanged. Otherwise, the system logger will set the value of **TimeStamp** at the time it receives the event. A driver can call **KeQuerySystemTime** to set the value of **TimeStamp**.

</dd> <dt>

**Guid**
</dt> <dd>

The GUID that identifies the data block for the event.

</dd> <dt>

**GuidPtr**
</dt> <dd>

If the WNODE\_FLAG\_USE\_GUID\_PTR flag bit is set in **Flags**, **GuidPtr** points to the GUID that identifies the data block for the event.

</dd> <dt>

**KernelTime**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**UserTime**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**ProcessorTime**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**ClientContext**
</dt> <dd>

Reserved for internal use.

</dd> <dt>

**Flags**
</dt> <dd>

Provides information about the contents of this structure. For information about **EVENT\_TRACE\_HEADER** **Flags** values, see the **Flags** description in [**WNODE\_HEADER**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-_wnode_header).

</dd> </dl>

## Remarks

A driver that supports trace events will use this structure to report events to the WMI event logger. Trace events should not be reported until the driver receives a request to enable events and the control GUID is one the driver supports. The driver should initialize an **EVENT\_TRACE\_HEADER** structure, fill in any user-defined event data at the end, and pass a pointer to the **EVENT\_TRACE\_HEADER** to **IoWMIWriteEvent**. The driver should continue reporting trace events until it receives a request to disable the control GUID for the trace events.

If the driver does not specify the WNODE\_FLAG\_USE\_MOF\_PTR flag in the **Flags** member of **EVENT\_TRACE\_HEADER**, the **EVENT\_TRACE\_HEADER** structure is followed in memory by event-specific data. In this case, the **Size** member must be **sizeof**(**EVENT\_TRACE\_HEADER**) plus the size of the event-specific data.

If the driver does specify the WNODE\_FLAG\_USE\_MOF\_PTR flag, the **EVENT\_TRACE\_HEADER** structure is followed in memory by an array of **MOF\_FIELD** structures (which are defined in Evntrace.h) that contain pointers to the data and sizes rather than the event tracing data itself. In this case, the **Size** member must be **sizeof**(**EVENT\_TRACE\_HEADER**) plus the size of the array of **MOF\_FIELD** structures.

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Evntrace.h (include Wdm.h or Ntddk.h)</dt> </dl> |



## See also

<dl> <dt>

[**IoWMIWriteEvent**](/windows-hardware/drivers/ddi/content/Wdm/nf-wdm-iowmiwriteevent)
</dt> <dt>

[**WNODE\_EVENT\_ITEM**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-tagwnode_event_item)
</dt> <dt>

[**WNODE\_HEADER**](/windows-hardware/drivers/ddi/content/wmistr/ns-wmistr-_wnode_header)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20EVENT_TRACE_HEADER%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")





