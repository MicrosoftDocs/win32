---
description: Winsock network tracing event for a socket creation operation.
ms.assetid: 59B9A570-5AEC-429D-AF71-AB6D8325C341
title: AFD_EVENT_CREATE event
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- AFD_EVENT_CREATE
api_type:
- NA
api_location: 
---

# AFD\_EVENT\_CREATE event

The **AFD\_EVENT\_CREATE** event is a Winsock network tracing event for a socket creation operation.


```C++
const EVENT_DESCRIPTOR AFD_EVENT_CREATE = {0x3e8, 0x0, 0x10, 0x4, 0xa, 0x3e8, 0x8000000000000004};
```



## Parameters

<dl> <dt>

*EnterExit* 
</dt> <dd>

Information on this event.

The following table lists the possible values for the *EnterExit* parameter:



| Value                                                                        | Meaning                                                                                              |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The start of a Winsock request.<br/>                                                           |
| <dl> <dt>1</dt> </dl> | The Winsock request completed.<br/>                                                            |
| <dl> <dt>2</dt> </dl> | The Winsock AFD driver took an internal action (aborting a connection, for example).<br/>      |
| <dl> <dt>3</dt> </dl> | The TCP/IP driver caused this event to occur. This usually indicates a data notification.<br/> |
| <dl> <dt>4</dt> </dl> | The Winsock AFD driver caused this event to occur (setting a socket option, for example).<br/> |



 

</dd> <dt>

*Location* 
</dt> <dd>

A private field used internally.

</dd> <dt>

*Process* 
</dt> <dd>

The [EPROCESS](/windows-hardware/drivers/kernel/eprocess) address of the process that owns the related socket. This is an opaque structure that serves as the process object for a process. For more information, see the Windows Driver Kit documentation for the [EPROCESS](/windows-hardware/drivers/kernel/eprocess) structure.

</dd> <dt>

*Endpoint* 
</dt> <dd>

The AFD\_ENDPOINT address of the socket.

</dd> <dt>

*AddressFamily* 
</dt> <dd>

The address family specification for the socket. Possible values for the address family are defined in the *Ws2def.h* header file. Note that the *Ws2def.h* header file is automatically included in *Winsock2.h*, and should never be used directly.

The values currently supported are AF\_INET or AF\_INET6, which are the Internet address family formats for IPv4 and IPv6. Other options for address family (AF\_NETBIOS for use with NetBIOS, for example) are supported if a Windows Sockets service provider for the address family is installed.

The table below lists common values for address family although many other values are possible.



| Af                                                                                                                                                                                                                 | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="AF_UNSPEC"></span><span id="af_unspec"></span><dl> <dt>**AF\_UNSPEC**</dt> <dt>0</dt> </dl>           | The address family is unspecified.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| <span id="AF_INET"></span><span id="af_inet"></span><dl> <dt>**AF\_INET**</dt> <dt>2</dt> </dl>                 | The Internet Protocol version 4 (IPv4) address family.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="AF_IPX"></span><span id="af_ipx"></span><dl> <dt>**AF\_IPX**</dt> <dt>6</dt> </dl>                    | The IPX/SPX address family. This address family is only supported if the NWLink IPX/SPX NetBIOS Compatible Transport protocol is installed. <br/> This address family is not supported on Windows Vista and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="AF_APPLETALK"></span><span id="af_appletalk"></span><dl> <dt>**AF\_APPLETALK**</dt> <dt>16</dt> </dl> | The AppleTalk address family. This address family is only supported if the AppleTalk protocol is installed. <br/> This address family is not supported on Windows Vista and later.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| <span id="AF_NETBIOS"></span><span id="af_netbios"></span><dl> <dt>**AF\_NETBIOS**</dt> <dt>17</dt> </dl>       | The NetBIOS address family. This address family is only supported if the Windows Sockets provider for NetBIOS is installed. <br/> The Windows Sockets provider for NetBIOS is supported on 32-bit versions of Windows. This provider is installed by default on 32-bit versions of Windows. <br/> The Windows Sockets provider for NetBIOS is not supported on 64-bit versions of windows. <br/> The Windows Sockets provider for NetBIOS only supports sockets where the *type* parameter is set to **SOCK\_DGRAM**.<br/> The Windows Sockets provider for NetBIOS is not directly related to the [NetBIOS](/previous-versions/windows/desktop/netbios/portal) programming interface. The NetBIOS programming interface is not supported on Windows Vista, Windows Server 2008, and later.<br/> |
| <span id="AF_INET6"></span><span id="af_inet6"></span><dl> <dt>**AF\_INET6**</dt> <dt>23</dt> </dl>             | The Internet Protocol version 6 (IPv6) address family.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <span id="AF_IRDA"></span><span id="af_irda"></span><dl> <dt>**AF\_IRDA**</dt> <dt>26</dt> </dl>                | The Infrared Data Association (IrDA) address family. <br/> This address family is only supported if the computer has an infrared port and driver installed.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| <span id="AF_BTH"></span><span id="af_bth"></span><dl> <dt>**AF\_BTH**</dt> <dt>32</dt> </dl>                   | The Bluetooth address family. <br/> This address family is only supported if the computer has a Bluetooth adapter and driver installed.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |



 

</dd> <dt>

*SocketType* 
</dt> <dd>

The type specification for the new socket. Possible values for the socket type are defined in the *Winsock2.h* header file.

The following table lists the possible values for the *type* parameter supported for Windows Sockets 2:



| Type                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="SOCK_STREAM"></span><span id="sock_stream"></span><dl> <dt>**SOCK\_STREAM**</dt> <dt>1</dt> </dl>          | A socket type that provides sequenced, reliable, two-way, connection-based byte streams with an OOB data transmission mechanism. This socket type uses the Transmission Control Protocol (TCP) for the Internet address family (AF\_INET or AF\_INET6).<br/>                                                                                                                                |
| <span id="SOCK_DGRAM"></span><span id="sock_dgram"></span><dl> <dt>**SOCK\_DGRAM**</dt> <dt>2</dt> </dl>             | A socket type that supports datagrams, which are connectionless, unreliable buffers of a fixed (typically small) maximum length. This socket type uses the User Datagram Protocol (UDP) for the Internet address family (AF\_INET or AF\_INET6).<br/>                                                                                                                                       |
| <span id="SOCK_RAW"></span><span id="sock_raw"></span><dl> <dt>**SOCK\_RAW**</dt> <dt>3</dt> </dl>                   | A socket type that provides a raw socket that allows an application to manipulate the next upper-layer protocol header. To manipulate the IPv4 header, the [**IP\_HDRINCL**](ipproto-ip-socket-options.md) socket option must be set on the socket. To manipulate the IPv6 header, the [**IPV6\_HDRINCL**](ipproto-ipv6-socket-options.md) socket option must be set on the socket. <br/> |
| <span id="SOCK_RDM"></span><span id="sock_rdm"></span><dl> <dt>**SOCK\_RDM**</dt> <dt>4</dt> </dl>                   | A socket type that provides a reliable message datagram. An example of this type is the Pragmatic General Multicast (PGM) multicast protocol implementation in Windows, often referred to as [reliable multicast programming](reliable-multicast-programming--pgm-.md). <br/> This *type* value is only supported if the Reliable Multicast Protocol is installed.<br/>              |
| <span id="SOCK_SEQPACKET"></span><span id="sock_seqpacket"></span><dl> <dt>**SOCK\_SEQPACKET**</dt> <dt>5</dt> </dl> | A socket type that provides a pseudo-stream packet based on datagrams. <br/>                                                                                                                                                                                                                                                                                                                |



 

</dd> <dt>

*Protocol* 
</dt> <dd>

The protocol to be used. The possible options for the *protocol* parameter are specific to the address family and socket type specified. Possible values for the *protocol* are defined in the *Wsrm.h* header file and the **IPPROTO** enumeration type defined in the *Ws2def.h* header file. Note that the *Ws2def.h* header file is automatically included in *Winsock2.h*, and should never be used directly.

If a value of 0 is specified, the caller does not wish to specify a protocol and the service provider will choose the *protocol* to use.

The table below lists common values for the *protocol* although many other values are possible.



| protocol                                                                                                                                                                                                                   | Meaning                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="IPPROTO_ICMP"></span><span id="ipproto_icmp"></span><dl> <dt>**IPPROTO\_ICMP**</dt> <dt>1</dt> </dl>          | The Internet Control Message Protocol (ICMP). This is a possible value when the *af* parameter is **AF\_UNSPEC**, **AF\_INET**, or **AF\_INET6** and the *type* parameter is **SOCK\_RAW** or unspecified.<br/>                                                                                               |
| <span id="IPPROTO_IGMP"></span><span id="ipproto_igmp"></span><dl> <dt>**IPPROTO\_IGMP**</dt> <dt>2</dt> </dl>          | The Internet Group Management Protocol (IGMP). This is a possible value when the *af* parameter is **AF\_UNSPEC**, **AF\_INET**, or **AF\_INET6** and the *type* parameter is **SOCK\_RAW** or unspecified.<br/>                                                                                              |
| <span id="BTHPROTO_RFCOMM"></span><span id="bthproto_rfcomm"></span><dl> <dt>**BTHPROTO\_RFCOMM**</dt> <dt>3</dt> </dl> | The Bluetooth Radio Frequency Communications (Bluetooth RFCOMM) protocol. This is a possible value when the *af* parameter is **AF\_BTH** and the *type* parameter is **SOCK\_STREAM**. <br/>                                                                                                                 |
| <span id="IPPROTO_TCP"></span><span id="ipproto_tcp"></span><dl> <dt>**IPPROTO\_TCP**</dt> <dt>6</dt> </dl>             | The Transmission Control Protocol (TCP). This is a possible value when the *af* parameter is **AF\_INET** or **AF\_INET6** and the *type* parameter is **SOCK\_STREAM**.<br/>                                                                                                                                 |
| <span id="IPPROTO_UDP"></span><span id="ipproto_udp"></span><dl> <dt>**IPPROTO\_UDP**</dt> <dt>17</dt> </dl>            | The User Datagram Protocol (UDP). This is a possible value when the *af* parameter is **AF\_INET** or **AF\_INET6** and the *type* parameter is **SOCK\_DGRAM**.<br/>                                                                                                                                         |
| <span id="IPPROTO_ICMPV6"></span><span id="ipproto_icmpv6"></span><dl> <dt>**IPPROTO\_ICMPV6**</dt> <dt>58</dt> </dl>   | The Internet Control Message Protocol Version 6 (ICMPv6). This is a possible value when the *af* parameter is **AF\_UNSPEC**, **AF\_INET**, or **AF\_INET6** and the *type* parameter is **SOCK\_RAW** or unspecified.<br/>                                                                                   |
| <span id="IPPROTO_RM"></span><span id="ipproto_rm"></span><dl> <dt>**IPPROTO\_RM**</dt> <dt>113</dt> </dl>              | The PGM protocol for reliable multicast. This is a possible value when the *af* parameter is **AF\_INET** and the *type* parameter is **SOCK\_RDM**. This protocol is also called **IPPROTO\_PGM**. <br/> This *protocol* value is only supported if the Reliable Multicast Protocol is installed.<br/> |



 

</dd> <dt>

*ProcessId* 
</dt> <dd>

The actual process ID or an indicator if the event was a result of Winsock code run in a system process or in a deferred procedure call (DPC) context (contexts outside the user process).

</dd> <dt>

*Status* 
</dt> <dd>

The NTSTATUS code for the operation.

</dd> </dl>

## Remarks

The **AFD\_EVENT\_CREATE** event is traced for a Winsock network operation to create a socket. The channel for this event is Winsock-AFD. The level for this event is informational.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Control of Winsock Tracing](control-of-winsock-tracing.md)
</dt> <dt>

[**EVENT\_DESCRIPTOR**](/windows/desktop/api/evntprov/ns-evntprov-event_descriptor)
</dt> <dt>

[Winsock Tracing](winsock-tracing.md)
</dt> <dt>

[Winsock Tracing Levels](winsock-tracing-levels.md)
</dt> <dt>

[Winsock Catalog Change Tracing Details](winsock-layered-service-provider-tracing-event-details.md)
</dt> </dl>

 

