---
Description: The following tables describe IPPROTO\_IP socket options that apply to sockets created for the IPv4 address family (AF\_INET). See the getsockopt and setsockopt function reference pages for more information on getting and setting socket options.
ms.assetid: 6b06a29e-59cd-4446-bd2f-131dc25bf571
title: IPPROTO_IP socket options
ms.topic: article
ms.date: 10/02/2019
---

## Options

| Option | Get | Set | Optval type | Description |
|-|-|-|-|-|
| IP\_ADD\_MEMBERSHIP | | yes | [**ip\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq) | Join the socket to the supplied multicast group on the specified interface. |
| IP\_ADD\_SOURCE\_MEMBERSHIP | | yes | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) | Join the supplied multicast group on the given interface and accept data sourced from the supplied source address. |
| IP\_BLOCK\_SOURCE | | yes | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) | Removes the given source as a sender to the supplied multicast group and interface. |
| IP\_DONTFRAGMENT | yes | yes | DWORD (boolean) | Indicates that data should not be fragmented regardless of the local MTU. Valid only for message oriented protocols. Microsoft TCP/IP providers respect this option for UDP and ICMP. |
| IP\_DROP\_MEMBERSHIP | | yes | [**ip\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq) | Leaves the specified multicast group from the specified interface. Service providers must support this option when multicast is supported. Support is indicated in the [**WSAPROTOCOL\_INFO**](https://msdn.microsoft.com/library/ms741675(v=VS.85).aspx) structure returned by a [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa) function call with the following: XPI\_SUPPORT\_MULTIPOINT=1, XP1\_MULTIPOINT\_CONTROL\_PLANE=0, XP1\_MULTIPOINT\_DATA\_PLANE=0. |
| IP\_DROP\_SOURCE\_MEMBERSHIP | | yes | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) | Drops membership to the given multicast group, interface, and source address. |
| IP\_HDRINCL | yes | yes | DWORD (boolean) | When set to **TRUE**, indicates the application provides the IP header. Applies only to SOCK\_RAW sockets. The TCP/IP service provider may set the ID field, if the value supplied by the application is zero.  The IP\_HDRINCL option is applied only to the SOCK\_RAW type of protocol. A TCP/IP service provider that supports SOCK\_RAW should also support IP\_HDRINCL.  |
| IP\_MTU | yes | | DWORD | Gets the system's estimate of the path MTU. Socket must be connected. |
| IP\_MTU\_DISCOVER | yes | yes | DWORD (**PMTUD\_STATE**) | Gets or sets the path MTU discovery state for the socket. The default value is **IP\_PMTUDISC\_NOT\_SET**. For stream sockets, **IP\_PMTUDISC\_NOT\_SET** and **IP\_PMTUDISC\_DO** will perform path MTU discovery. **IP\_PMTUDISC\_DONT** and **IP\_PMTUDISC\_PROBE** will turn off path MTU discovery. For datagram sockets, **IP\_PMTUDISC\_DO** will force all outgoing packets to have the DF bit set and an attempt to send packets larger than path MTU will result in an error. **IP\_PMTUDISC\_DONT** will force all outgoing packets to have the DF bit not set, and packets will be fragmented according to interface MTU. **IP\_PMTUDISC\_PROBE** will force all outgoing packets to have the DF bit set, and an attempt to send packets larger than interface MTU will result in an error. |
| IP\_MULTICAST\_IF | yes | yes | DWORD | Gets or sets the outgoing interface for sending IPv4 multicast traffic. This option does not change the default interface for receiving IPv4 multicast traffic.  The input value for setting this option is a 4-byte IPv4 address in network byte order. This DWORD parameter can also be an interface index in network byte order. Any IP address in the 0.x.x.x block (first octet of 0) except IPv4 address 0.0.0.0 is treated as an interface index. An interface index is a 24-bit number, and the 0.0.0.0/8 IPv4 address block is not used (this range is reserved). The interface index can be used to specify the default interface for multicast traffic for IPv4. If *optval* is zero , the default interface for receiving multicast is specified for sending multicast traffic.  When getting this option, the *optval* returns the current default interface index for sending multicast IPv4 traffic in host byte order. |
| IP\_MULTICAST\_LOOP | yes | yes | DWORD (boolean) | Controls whether data sent by an application on the local computer (not necessarily by the same socket) in a multicast session will be received by a socket joined to the multicast destination group on the loopback interface. A value of **TRUE** causes multicast data sent by an application on the local computer to be delivered to a listening socket on the loopback interface. A value of **FALSE** prevents multicast data sent by an application on the local computer from being delivered to a listening socket on the loopback interface. By default, **IP\_MULTICAST\_LOOPBACK** is enabled. |
| IP\_MULTICAST\_TTL | yes | yes | DWORD | Sets/gets the TTL value associated with IP multicast traffic on the socket. |
| IP\_OPTIONS | yes | yes | char \[\] | Specifies IP options to be inserted into outgoing packets. Setting new options overwrites all previously specified options. Setting optval to zero removes all previously specified options. IP\_OPTIONS support is not required; to check whether IP\_OPTIONS is supported, use [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) to get current options. If **getsockopt** fails, IP\_OPTIONS is not supported. |
| IP\_ORIGINAL\_ARRIVAL\_IF | yes | yes | DWORD (boolean) | Indicates if the [**WSARecvMsg**](https://msdn.microsoft.com/library/ms741687(v=VS.85).aspx) function should return optional control data containing the arrival interface where the packet was received for datagram sockets. This option allows the IPv4 interface where the packet was received to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure.  This option is only valid on datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| [IP\_PKTINFO](ip-pktinfo.md) | yes | yes | DWORD | Indicates that packet information should be returned by the **WSARecvMsg** function. |
| IP\_RECEIVE\_BROADCAST | yes | yes | DWORD (boolean) | Allows or blocks broadcast reception. |
| IP\_RECVIF | yes | yes | DWORD (boolean) | Indicates whether the IP stack should populate the control buffer with details about which interface received a packet with a datagram socket. When this value is true, the [**WSARecvMsg**](https://msdn.microsoft.com/library/ms741687(v=VS.85).aspx) function will return optional control data containing the interface where the packet was received for datagram sockets. This option allows the IPv4 interface where the packet was received to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure.  This option is only valid on datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IP\_RECVTOS | yes | yes | DWORD (boolean) | Indicates whether the IP stack should populate the control buffer with a message containing the Type of Service (TOS) IPv4 header field on a received datagram. When this value is true, the [**WSARecvMsg**](https://msdn.microsoft.com/library/ms741687(v=VS.85).aspx) function will return optional control data containing the TOS IPv4 header field value of the received datagram.  This option allows the TOS IPv4 header field of the received datagram to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure. The returned message type will be IP\_TOS. All DSCP and ECN bits of the TOS field will be returned.  This option is only valid on datagram sockets (the socket type must be SOCK\_DGRAM).  |
| IP\_RECVTTL | yes | yes | DWORD (boolean) | Indicates that hop (TTL) information should be returned in the [**WSARecvMsg**](https://msdn.microsoft.com/library/ms741687(v=VS.85).aspx) function. If *optval* is set to **1** on the call to [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt), the option is enabled. If set to **0**, the option is disabled.  This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IP\_TOS | yes | yes | DWORD (boolean) | Do not use. Type of Service (TOS) settings should only be set using the Quality of Service API. See [Differentiated Services](https://msdn.microsoft.com/library/Aa373439(v=VS.80).aspx) in the Quality of Service section of the Platform SDK for more information. |
| IP\_TTL | yes | yes | DWORD (boolean) | Changes the default value set by the TCP/IP service provider in the TTL field of the IP header in outgoing datagrams. IP\_TTL support is not required; to check whether IP\_TTL is supported, use [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) to get current options. If **getsockopt** fails, IP\_TTL is not supported. |
| IP\_UNBLOCK\_SOURCE | | yes | [**ip\_mreq\_source**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ip_mreq_source) | Adds the given source as a sender to the supplied multicast group and interface. |
| IP\_UNICAST\_IF | yes | yes | DWORD (IF\_INDEX) | Gets or sets the outgoing interface for sending IPv4 traffic. This option does not change the default interface for receiving IPv4 traffic. This option is important for multihomed computers.  The input value for setting this option is a 4-byte IPv4 address in network byte order. This DWORD parameter must be an interface index in network byte order. Any IP address in the 0.x.x.x block (first octet of 0) except IPv4 address 0.0.0.0 is treated as an interface index. An interface index is a 24-bit number, and the 0.0.0.0/8 IPv4 address block is not used (this range is reserved). The interface index can be used to specify the default interface for sending traffic for IPv4. The [**GetAdaptersAddresses**](https://msdn.microsoft.com/library/Aa365915(v=VS.85).aspx) function can be used to obtain the interface index information. If *optval* is zero , the default interface for sending traffic is set to unspecified.  When getting this option, the *optval* returns the current default interface index for sending IPv4 traffic in host byte order. |
| IP_USER_MTU | yes | yes | DWORD | Gets or sets an upper bound on the IP layer MTU (in bytes) for the given socket. If the value is higher than the system's estimate of the path MTU (which you can retrieve on a connected socket by querying the **IP_MTU** socket option), then the option has no effect. If the value is lower, then outbound packets larger than this will be fragmented, or will fail to send, depending on the value of **IP_DONTFRAGMENT**. Default value is **IP_UNSPECIFIED_USER_MTU** (MAXULONG). For type-safety, you should use the [**WSAGetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetipusermtu) and [**WSASetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetipusermtu) functions instead of using the socket option directly. |
| IP\_WFP\_REDIRECT\_CONTEXT | yes | yes | WSACMSGHDR with control data | A datagram socket ancillary data type (cmsg\_type) to indicate the redirect context for a UDP socket used by a user mode Windows Filtering Platform (WFP) redirect service. |
| IP\_WFP\_REDIRECT\_RECORDS | yes | yes | WSACMSGHDR with control data | A datagram socket ancillary data type (cmsg\_type) to indicate the redirect record for a UDP socket used by a user mode Windows Filtering Platform (WFP) redirect service. |

## Windows support for IP\_PROTO options

| Option | Windows 10 | Windows 8 | Windows Server 2012 | Windows 7 | Windows Server 2008 | Windows Vista |
|-|-|-|-|-|-|-|
| IP\_ADD\_MEMBERSHIP | x | x | x | x | x | x |
| IP\_ADD\_SOURCE\_MEMBERSHIP | x | x | x | x | x | x |
| IP\_BLOCK\_SOURCE | x | x | x | x | x | x |
| IP\_DONTFRAGMENT | x | x | x | x | x | x |
| IP\_DROP\_MEMBERSHIP | x | x | x | x | x | x |
| IP\_DROP\_SOURCE\_MEMBERSHIP | x | x | x | x | x | x |
| IP\_HDRINCL | x | x | x | x | x | x |
| IP\_MULTICAST\_IF | x | x | x | x | x | x |
| IP\_MULTICAST\_LOOP | x | x | x | x | x | x |
| IP\_MULTICAST\_TTL | x | x | x | x | x | x |
| IP\_OPTIONS | x | x | x | x | x | x |
| IP\_ORIGINAL\_ARRIVAL\_IF | x | x | x | x | | |
| IP\_PKTINFO | x | x | x | x | x | x |
| IP\_RECEIVE\_BROADCAST | x | x | x | x | x | x |
| IP\_RECVIF | Starting with Windows 10, version 1703 | x | x | x | x | x |
| IP\_RECVTTL | x | | | | | |
| IP\_TOS | x | x | x | | | |
| IP\_TTL | x | x | x | x | x | x |
| IP\_UNBLOCK\_SOURCE | x | x | x | x | x | x |
| IP\_UNICAST\_IF | x | x | x | x | x | x |
| IP\_WFP\_REDIRECT\_CONTEXT | x | x | x | | | |
| IP\_WFP\_REDIRECT\_RECORDS | x | x | x | | | |

<br/>

| Option | Windows Server 2003 | Windows XP |
|-|-|-|
| IP\_ADD\_MEMBERSHIP | x | x |
| IP\_ADD\_SOURCE\_MEMBERSHIP | x | x |
| IP\_BLOCK\_SOURCE | x | x |
| IP\_DONTFRAGMENT | x | x |
| IP\_DROP\_MEMBERSHIP | x | x |
| IP\_DROP\_SOURCE\_MEMBERSHIP | x | x |
| IP\_HDRINCL | x | x |
| IP\_MULTICAST\_IF | x | x |
| IP\_MULTICAST\_LOOP | x | x |
| IP\_MULTICAST\_TTL | x | x |
| IP\_OPTIONS | x | x |
| IP\_ORIGINAL\_ARRIVAL\_IF | | |
| IP\_PKTINFO | x | x |
| IP\_RECEIVE\_BROADCAST | x | x |
| IP\_RECVIF | | |
| IP\_RECVTTL | | |
| IP\_TOS | | |
| IP\_TTL | x | x |
| IP\_UNBLOCK\_SOURCE | x | x |
| IP\_UNICAST\_IF | | |
| IP\_WFP\_REDIRECT\_CONTEXT | | |
| IP\_WFP\_REDIRECT\_RECORDS | | |