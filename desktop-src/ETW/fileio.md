---
description: FileIo class - This class is the parent class for file I/O events. The following syntax is simplified from MOF code.
ms.assetid: 8e006a63-a061-4b62-8f90-b8c8823bb047
title: FileIo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FileIo
api_type: 
- NA
api_location: 
---

# FileIo class

This class is the parent class for file I/O events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{90cbdc39-4a3e-11d1-84f4-0000f80464e3}"), EventVersion(2)]
class FileIo : MSNT_SystemTrace
{
};
```

## Members

The **FileIo** class does not define any members.

## Remarks

To enable the File IO events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_DISK\_FILE\_IO** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify one or more of the following flags:

-   **EVENT\_TRACE\_FLAG\_FILE\_IO**
-   **EVENT\_TRACE\_FLAG\_FILE\_IO\_INIT**

Event trace consumers can implement special processing for file I/O events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**FileIoGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual event when consuming events.



| Event type             | Description                                                                                                                                                                             |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Event type value is 0  | File name event. The [**FileIo\_Name**](fileio-name.md) MOF class defines the event data for this event.                                                                               |
| Event type value is 32 | File create event. The [**FileIo\_Name**](fileio-name.md) MOF class defines the event data for this event.                                                                             |
| Event type value is 35 | File delete event. The [**FileIo\_Name**](fileio-name.md) MOF class defines the event data for this event.                                                                             |
| Event type value is 36 | File rundown event. Enumerates all open files on the computer at the end of the trace session. The [**FileIo\_Name**](fileio-name.md) MOF class defines the event data for this event. |
| Event type value is 64 | File create event. The [**FileIo\_Create**](fileio-create.md) MOF class defines the event data for this event.                                                                         |
| Event type value is 72 | Directory enumeration event. The [**FileIo\_DirEnum**](fileio-direnum.md) MOF class defines the event data for this event.                                                             |
| Event type value is 77 | Directory notification event. The [**FileIo\_DirEnum**](fileio-direnum.md) MOF class defines the event data for this event.                                                            |
| Event type value is 69 | Set information event. The [**FileIo\_Info**](fileio-info.md) MOF class defines the event data for this event.                                                                         |
| Event type value is 70 | Delete file event. The [**FileIo\_Info**](fileio-info.md) MOF class defines the event data for this event.                                                                             |
| Event type value is 71 | Rename file event. The [**FileIo\_Info**](fileio-info.md) MOF class defines the event data for this event.                                                                             |
| Event type value is 74 | Query file information event. The [**FileIo\_Info**](fileio-info.md) MOF class defines the event data for this event.                                                                  |
| Event type value is 75 | File system control event. The [**FileIo\_Info**](fileio-info.md) MOF class defines the event data for this event.                                                                     |
| Event type value is 76 | End of operation event. The [**FileIo\_OpEnd**](fileio-opend.md) MOF class defines the event data for this event.                                                                      |
| Event type value is 67 | File read event. The [**FileIo\_ReadWrite**](fileio-readwrite.md) MOF class defines the event data for this event.                                                                     |
| Event type value is 68 | File write event. The [**FileIo\_ReadWrite**](fileio-readwrite.md) MOF class defines the event data for this event.                                                                    |
| Event type value is 65 | Clean up event. The event is generated when the last handle to the file is released. The [**FileIo\_SimpleOp**](fileio-simpleop.md) MOF class defines the event data for this event.   |
| Event type value is 66 | Close event. The event is generated when the file object is freed. The [**FileIo\_SimpleOp**](fileio-simpleop.md) MOF class defines the event data for this event.                     |
| Event type value is 73 | Flush event. This event is generated when the file buffers are fully flushed to disk. The [**FileIo\_SimpleOp**](fileio-simpleop.md) MOF class defines the event data for this event.  |



 

File IO events are logged at the beginning of the operation.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**FileIo\_V0**](fileio-v0.md)
</dt> <dt>

[**FileIo\_V1**](fileio-v1.md)
</dt> </dl>

 

 
