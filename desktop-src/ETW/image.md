---
description: This class is the parent class for image events. The following syntax is simplified from MOF code.
ms.assetid: a719a34c-7e32-4758-9031-6ca2b2873e3e
title: Image class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Image
api_type: 
- NA
api_location: 
---

# Image class

This class is the parent class for image events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{2cb15d1d-5fc1-11d2-abe1-00a0c911f518}"), EventVersion(2)]
class Image : MSNT_SystemTrace
{
};
```

## Members

The **Image** class does not define any members.

## Remarks

To enable image events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_IMAGE\_LOAD** flag in the **EnableFlags** member of the [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for image load events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**ImageLoadGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify image load events when consuming events.



| Event type                                                          | Description                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_LOAD**(Event type value is 10)<br/>     | Image load event. Generated when a DLL or executable file is loaded. The provider generates only one event for the first time a given DLL is loaded. The [**Image\_Load**](image-load.md) MOF class defines the event data for this event.      |
| **EVENT\_TRACE\_TYPE\_END**(Event type value is 2)<br/>       | Image unload event. Generated when a DLL or executable file is unloaded. The provider generates only one event for the last time a given DLL is unloaded. The [**Image\_Load**](image-load.md) MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_DC\_START**(Event type value is 3)<br/> | Data collection start event. Enumerates all loaded images at the beginning of the trace. The [**Image\_Load**](image-load.md) MOF class defines the event data for this event.                                                                  |
| **EVENT\_TRACE\_TYPE\_DC\_END**(Event type value is 4)<br/>   | Data collection end event. Enumerates all loaded images at the end of the trace. The [**Image\_Load**](image-load.md) MOF class defines the event data for this event.                                                                          |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**Image\_Load**](image-load.md)
</dt> <dt>

[**Image\_V0**](image-v0.md)
</dt> <dt>

[**Image\_V1**](image-v1.md)
</dt> </dl>

 

 
