---
description: This class is the parent class for advanced local procedure call events. The following syntax is simplified from MOF code.
ms.assetid: 5380fada-50e7-4eb2-8549-6d738a56d2cd
title: ALPC class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ALPC
api_type: 
- NA
api_location: 
---

# ALPC class

This class is the parent class for advanced local procedure call events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{45d8cccd-539f-4b72-a8b7-5c683142609a}")]
class ALPC : MSNT_SystemTrace
{
};
```

## Members

The **ALPC** class does not define any members.

## Remarks

To enable advanced local procedure call events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_ALPC** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for ALPC events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**ALPCGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual ALPC event when consuming events.



| Event type           | Description                                                                                                                                         |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Event type value, 33 | Send message event. The [**ALPC\_Send\_Message**](alpc-send-message.md) MOF class defines the event data for this event.                           |
| Event type value, 34 | Receive message event. The [**ALPC\_Receive\_Message**](alpc-receive-message.md) MOF class defines the event data for this event.                  |
| Event type value, 35 | Wait for reply event. The [**ALPC\_Wait\_For\_Reply**](alpc-wait-for-reply.md) MOF class defines the event data for this event.                    |
| Event type value, 36 | Wait for new message event. The [**ALPC\_Wait\_For\_New\_Message**](alpc-wait-for-new-message.md) MOF class defines the event data for this event. |
| Event type value, 37 | Stop waiting event. The [**ALPC\_Unwait**](alpc-unwait.md) MOF class defines the event data for this event.                                        |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

