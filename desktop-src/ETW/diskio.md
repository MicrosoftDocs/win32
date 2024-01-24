---
description: This class is the parent class for disk I/O events. The following syntax is simplified from MOF code.
ms.assetid: 630fb6c6-b505-4384-ab7b-ee898d95bd41
title: DiskIo class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskIo
api_type: 
- NA
api_location: 
---

# DiskIo class

This class is the parent class for disk I/O events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{3d6fa8d4-fe05-11d0-9dda-00c04fd7ba7c}")]
class DiskIo : MSNT_SystemTrace
{
};
```

## Members

The **DiskIo** class does not define any members.

## Remarks

To enable disk I/0 events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_DISK\_IO** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function. You can also specify one or more of the following flags:

-   **EVENT\_TRACE\_FLAG\_DISK\_IO\_INIT**
-   **EVENT\_TRACE\_FLAG\_DRIVER**

Event trace consumers can implement special processing for disk I/O events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**DiskIoGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual disk I/O event when consuming events.



| Event type                                                                      | Description                                                                                                                                                   |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_IO\_READ**(Event type value is 10)<br/>             | Read event. The [**DiskIo\_TypeGroup1**](diskio-typegroup1.md) MOF class defines the event data for this event.                                              |
| **EVENT\_TRACE\_TYPE\_IO\_WRITE**(Event type value is 11)<br/>            | Write event. The [**DiskIo\_TypeGroup1**](diskio-typegroup1.md) MOF class defines the event data for this event.                                             |
| **EVENT\_TRACE\_TYPE\_IO\_READ\_INIT**(Event type value is 12)<br/>       | Initialize read event. The [**DiskIo\_TypeGroup2**](diskio-typegroup2.md) MOF class defines the event data for this event.                                   |
| **EVENT\_TRACE\_TYPE\_IO\_WRITE\_INIT**(Event type value is 13)<br/>      | Initialize write event. The [**DiskIo\_TypeGroup2**](diskio-typegroup2.md) MOF class defines the event data for this event.                                  |
| **EVENT\_TRACE\_TYPE\_IO\_FLUSH**(Event type value is 14)<br/>            | Initialize write event. The [**DiskIo\_TypeGroup3**](diskio-typegroup3.md) MOF class defines the event data for this event.                                  |
| **EVENT\_TRACE\_TYPE\_IO\_FLUSH\_INIT**(Event type value is 15)<br/>      | Initialize flush event. The [**DiskIo\_TypeGroup2**](diskio-typegroup2.md) MOF class defines the event data for this event.                                  |
| **EVENT\_TRACE\_TYPE\_IO\_REDIRECTED\_INIT**(Event type value is 16)<br/> | Initialize redirected event. Redirected IO events are used to map disk IOs to a Windows Imaging Format (WIM) to the filename within the WIM.                  |
| Event type value is 52<br/>                                               | Driver complete request event. The [**DriverCompleteRequest**](drivercompleterequest.md) MOF class defines the event data for this event.                    |
| Event type value is 53<br/>                                               | Driver complete request return event. The [**DriverCompleteRequestReturn**](drivercompleterequestreturn.md) MOF class defines the event data for this event. |
| Event type value is 37<br/>                                               | Driver completion routine event. The [**DriverCompletionRoutine**](drivercompletionroutine.md) MOF class defines the event data for this event.              |
| Event type value is 34<br/>                                               | Driver major function call event. The [**DriverMajorFunctionCall**](drivermajorfunctioncall.md) MOF class defines the event data for this event.             |
| Event type value is 35<br/>                                               | Driver major function call return event. The [**DriverMajorFunctionReturn**](drivermajorfunctionreturn.md) MOF class defines the event data for this event.  |



 

The disk I/0 provider cannot identify which file is read or written during a disk I/O event. To retrieve the name of the file associated with the disk I/O event, enable the file I/0 event provider.

Disk I/O events are recorded at the I/O completion time. To determine when the I/O operation began, use the initialization events, for example, EVENT\_TRACE\_TYPE\_IO\_READ\_INIT.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DiskIo\_TypeGroup1**](diskio-typegroup1.md)
</dt> <dt>

[**DiskIo\_TypeGroup2**](diskio-typegroup2.md)
</dt> <dt>

[**DiskIo\_TypeGroup3**](diskio-typegroup3.md)
</dt> <dt>

[**DriverCompleteRequest**](drivercompleterequest.md)
</dt> <dt>

[**DriverCompleteRequestReturn**](drivercompleterequestreturn.md)
</dt> <dt>

[**DriverCompletionRoutine**](drivercompletionroutine.md)
</dt> <dt>

[**DriverMajorFunctionCall**](drivermajorfunctioncall.md)
</dt> <dt>

[**DriverMajorFunctionReturn**](drivermajorfunctionreturn.md)
</dt> </dl>

 

 
