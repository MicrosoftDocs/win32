---
description: UdpIp class - This class is the parent class for UDP/IP events. The following syntax is simplified from MOF code.
ms.assetid: 0fbecad2-0221-408e-9f43-859547efa803
title: UdpIp class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UdpIp
api_type: 
- NA
api_location: 
---

# UdpIp class

This class is the parent class for UDP/IP events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{bf3a50c5-a9c9-4988-a005-2df0b7c80f80}"), EventVersion(2)]
class UdpIp : MSNT_SystemTrace
{
};
```

## Members

The **UdpIp** class does not define any members.

## Remarks

To enable UDP/IP events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_NETWORK\_TCPIP** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for UDP/IP events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**UdpIpGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual network (UDP/IP) event when consuming events.



| Event type                                                         | Description                                                                                                                         |
|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_RECEIVE**(Event type value is 11)<br/> | Receive event for IPv4 protocol. The [**UdpIp\_TypeGroup1**](udpip-typegroup1.md) MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_SEND**(Event type value is 10)<br/>    | Send event for IPv4 protocol. The [**UdpIp\_TypeGroup1**](udpip-typegroup1.md) MOF class defines the event data for this event.    |
| Event type value, 17                                               | Fail event. The [**UdpIp\_Fail**](udpip-fail.md) MOF class defines the event data for this event.                                  |
| Event type value, 26                                               | Send event for IPv6 protocol. The [**UdpIp\_TypeGroup2**](udpip-typegroup2.md) MOF class defines the event data for this event.    |
| Event type value, 27                                               | Receive event for IPv6 protocol. The [**UdpIp\_TypeGroup2**](udpip-typegroup2.md) MOF class defines the event data for this event. |



 

You can trace network events to a source and destination process using the **ProcessId** property. Because some network events are logged by separate threads, you may not be able to use the **ProcessId** and **ThreadId** members of [**EVENT\_TRACE\_HEADER**](/windows/win32/api/evntrace/ns-evntrace-event_trace_header) to identify the process or thread that originated the network activities.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**MSNT\_SystemTrace**](msnt-systemtrace.md)
</dt> <dt>

[**UdpIp\_Fail**](udpip-fail.md)
</dt> <dt>

[**UdpIp\_TypeGroup1**](udpip-typegroup1.md)
</dt> <dt>

[**UdpIp\_TypeGroup2**](udpip-typegroup2.md)
</dt> <dt>

[**UdpIp\_V0**](udpip-v0.md)
</dt> <dt>

[**UdpIp\_V1**](udpip-v1.md)
</dt> </dl>

 

 
