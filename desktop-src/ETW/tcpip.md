---
description: TcpIp class - This class is the parent class for TCP/IP events. The following syntax is simplified from MOF code.
ms.assetid: f9d6ea8f-c777-4747-89f4-f389c6eeac35
title: TcpIp class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- TcpIp
api_type: 
- NA
api_location: 
---

# TcpIp class

This class is the parent class for TCP/IP events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[Guid("{9a280ac0-c8e0-11d1-84e2-00c04fb998a2}"), EventVersion(2)]
class TcpIp : MSNT_SystemTrace
{
};
```

## Members

The **TcpIp** class does not define any members.

## Remarks

To enable TCP/IP events in an NT Kernel logging session, specify the **EVENT\_TRACE\_FLAG\_NETWORK\_TCPIP** flag in the **EnableFlags** member of an [**EVENT\_TRACE\_PROPERTIES**](/windows/win32/api/evntrace/ns-evntrace-event_trace_properties) structure when calling the [**StartTrace**](/windows/win32/api/evntrace/nf-evntrace-starttracea) function.

Event trace consumers can implement special processing for TCP/IP events by calling the [**SetTraceCallback**](/windows/win32/api/evntrace/nf-evntrace-settracecallback) function and specifying [**TcpIpGuid**](nt-kernel-logger-constants.md) as the *pGuid* parameter. Use the following event types to identify the actual network (TCP/IP) event when consuming events.



| Event type                                                            | Description                                                                                                                                                                                   |
|-----------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **EVENT\_TRACE\_TYPE\_ACCEPT**(Event type value is 15)<br/>     | Accept event for IPv4 protocol. The [**TcpIp\_TypeGroup2**](tcpip-typegroup2.md) MOF class defines the event data for this event.                                                            |
| **EVENT\_TRACE\_TYPE\_CONNECT**(Event type value is 12)<br/>    | Connect event for IPv4 protocol. The [**TcpIp\_TypeGroup2**](tcpip-typegroup2.md) MOF class defines the event data for this event.                                                           |
| **EVENT\_TRACE\_TYPE\_DISCONNECT**(Event type value is 13)<br/> | Disconnect event for IPv4 protocol. The [**TcpIp\_TypeGroup1**](tcpip-typegroup1.md) MOF class defines the event data for this event.                                                        |
| **EVENT\_TRACE\_TYPE\_RECEIVE**(Event type value is 11)<br/>    | Receive event for IPv4 protocol. The [**TcpIp\_TypeGroup1**](tcpip-typegroup1.md) MOF class defines the event data for this event.                                                           |
| **EVENT\_TRACE\_TYPE\_RECONNECT**(Event type value is 16)<br/>  | Reconnect event for IPv4 protocol. (A connect attempt failed and another attempt is made.) The [**TcpIp\_TypeGroup1**](tcpip-typegroup1.md) MOF class defines the event data for this event. |
| **EVENT\_TRACE\_TYPE\_RETRANSMIT**(Event type value is 14)<br/> | Retransmit event for IPv4 protocol. The [**TcpIp\_TypeGroup1**](tcpip-typegroup1.md) MOF class defines the event data for this event.                                                        |
| **EVENT\_TRACE\_TYPE\_SEND**(Event type value is 10)<br/>       | Send event for IPv4 protocol. The [**TcpIp\_SendIPV4**](tcpip-sendipv4.md) MOF class defines the event data for this event.                                                                  |
| Event type value, 17                                                  | Fail event. The [**TcpIp\_Fail**](tcpip-fail.md) MOF class defines the event data for this event.                                                                                            |
| Event type value, 18                                                  | TCP copy event for IPv4 protocol. The [**TcpIp\_TypeGroup1**](tcpip-typegroup1.md) MOF class defines the event data for this event.                                                          |
| Event type value, 26                                                  | Send event for IPv6 protocol. The [**TcpIp\_SendIPV6**](tcpip-sendipv6.md) MOF class defines the event data for this event.                                                                  |
| Event type value, 27                                                  | Receive event for IPv6 protocol. The [**TcpIp\_TypeGroup3**](tcpip-typegroup3.md) MOF class defines the event data for this event.                                                           |
| Event type value, 28                                                  | Connect event for IPv6 protocol. The [**TcpIp\_TypeGroup4**](tcpip-typegroup4.md) MOF class defines the event data for this event.                                                           |
| Event type value, 29                                                  | Disconnect event for IPv6 protocol. The [**TcpIp\_TypeGroup3**](tcpip-typegroup3.md) MOF class defines the event data for this event.                                                        |
| Event type value, 30                                                  | Retransmit event for IPv6 protocol. The [**TcpIp\_TypeGroup3**](tcpip-typegroup3.md) MOF class defines the event data for this event.                                                        |
| Event type value, 31                                                  | Accept event for IPv6 protocol. The [**TcpIp\_TypeGroup4**](tcpip-typegroup4.md) MOF class defines the event data for this event.                                                            |
| Event type value, 32                                                  | Reconnect event for IPv6 protocol. (A connect attempt failed and another attempt is made.) The [**TcpIp\_TypeGroup3**](tcpip-typegroup3.md) MOF class defines the event data for this event. |
| Event type value, 34                                                  | TCP copy event for IPv6 protocol. The [**TcpIp\_TypeGroup3**](tcpip-typegroup3.md) MOF class defines the event data for this event.                                                          |



 

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

[**TcpIp\_Fail**](tcpip-fail.md)
</dt> <dt>

[**TcpIp\_SendIPV4**](tcpip-sendipv4.md)
</dt> <dt>

[**TcpIp\_SendIPV6**](tcpip-sendipv6.md)
</dt> <dt>

[**TcpIp\_TypeGroup1**](tcpip-typegroup1.md)
</dt> <dt>

[**TcpIp\_TypeGroup2**](tcpip-typegroup2.md)
</dt> <dt>

[**TcpIp\_TypeGroup3**](tcpip-typegroup3.md)
</dt> <dt>

[**TcpIp\_TypeGroup4**](tcpip-typegroup4.md)
</dt> <dt>

[**TcpIp\_V0**](tcpip-v0.md)
</dt> <dt>

[**TcpIp\_V1**](tcpip-v1.md)
</dt> </dl>

 

 
