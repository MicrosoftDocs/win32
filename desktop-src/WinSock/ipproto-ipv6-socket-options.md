---
description: The following tables describe IPPROTO\_IPV6 socket options that apply to sockets created for the IPv6 address family (AF\_INET6). See the getsockopt and setsockopt function reference pages for more information on getting and setting socket options.
ms.assetid: 65f8f7a4-757b-43a3-9d47-b115754c89d6
title: IPPROTO_IPV6 socket options
ms.topic: article
ms.date: 10/07/2019
---

# IPPROTO\_IPV6 socket options

The following tables describe **IPPROTO\_IPV6** socket options that apply to sockets created for the IPv6 address family (AF\_INET6). See the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) and [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function reference pages for more information on getting and setting socket options.

To enumerate protocols and discover supported properties for each installed protocol, use the [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [**WSCEnumProtocols**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols), or [**WSCEnumProtocols32**](/windows/desktop/api/Ws2spi/nf-ws2spi-wscenumprotocols32) function.

Some socket options require more explanation than these tables can convey; such options contain links to additional information.

## Options

| Option | get | set | Optval type | Description |
|-|-|-|-|-|
| IP\_ORIGINAL\_ARRIVAL\_IF | yes | yes | DWORD (boolean) | Indicates if the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function should return optional control data containing the original arrival interface where the packet was received for datagram sockets. This option is used with IPv6 transition technologies (6to4, ISATAP, and Teredo tunnels, for example) that provide address assignment and host-to-host automatic tunneling for unicast IPv6 traffic when IPv6 hosts must traverse IP4 networks to reach other IPv6 networks. IPv6 packets are sent tunneled as IPv4 packets. This option allows the original IPv4 interface where the packet was received to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure.  |
| IPV6_ADD_IFLIST | | yes | DWORD (IF_INDEX) | Adds an interface index to the IFLIST associated with the **IP_IFLIST** option. |
| IPV6\_ADD\_MEMBERSHIP | | yes | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) | Join the socket to the supplied multicast group on the specified interface.  This option is only valid on datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IPV6_DEL_IFLIST | | yes | DWORD (IF_INDEX) | Removes an interface index from the IFLIST associated with the **IP_IFLIST** option. Entries can be removed only by the application, so be aware that entries might go stale once an interface is removed. |
| IPV6\_DROP\_MEMBERSHIP | | yes | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) | Leave the supplied multicast group from the given interface.  This option is only valid on datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IPV6_GET_IFLIST | yes | | DWORD[] (IF_INDEX[]) | Gets the current IFLIST associated with the **IP_IFLIST** option. Returns error if **IP_IFLIST** is not enabled. |
| IPV6\_HDRINCL | yes | yes | DWORD(boolean) | Indicates the application provides the IPv6 header on all outgoing data. If the *optval* parameter is set to **1** on the call to [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt), the option is enabled. If *optval* is set to **0**, the option is disabled. The default value is disabled. This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). A TCP/IP service provider that supports SOCK\_RAW should also support IPV6\_HDRINCL. |
| IPV6\_HOPLIMIT | yes | yes | DWORD (boolean) | Indicates that hop (TTL) information should be returned in the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function. If *optval* is set to **1** on the call to [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt), the option is enabled. If set to **0**, the option is disabled.  This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IPV6_IFLIST | yes | yes | DWORD (boolean) | Gets or sets the **IP_IFLIST** state of the socket. When this option is set to true, Datagram reception is restricted to interfaces that are in the IFLIST. Datagrams received on any other interfaces are ignored. IFLIST starts empty. Use **IP_ADD_IFLIST** and **IP_DEL_IFLIST** to edit the IFLIST. |
| IPV6\_JOIN\_GROUP | | yes | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) | Same as IPV6\_ADD\_MEMBERSHIP |
| IPV6\_LEAVE\_GROUP | | yes | [**ipv6\_mreq**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-ipv6_mreq) | Same as IPV6\_DROP\_MEMBERSHIP |
| IPV6\_MTU | yes | | DWORD | Gets the system's estimate of the path MTU. Socket must be connected. |
| IPV6\_MTU\_DISCOVER | yes | yes | DWORD (**PMTUD\_STATE**) | Gets or sets the path MTU discovery state for the socket. The default value is **IP\_PMTUDISC\_NOT\_SET**. For stream sockets, **IP\_PMTUDISC\_NOT\_SET** and **IP\_PMTUDISC\_DO** will perform path MTU discovery. **IP\_PMTUDISC\_DONT** and **IP\_PMTUDISC\_PROBE** will turn off path MTU discovery. For datagram sockets, if set to **IP\_PMTUDISC\_DO** , attempts to send packets larger than path MTU will result in an error. If set to **IP\_PMTUDISC\_DONT**, packets will be fragmented according to interface MTU. If set to **IP\_PMTUDISC\_PROBE**, attempts to send packets larger than interface MTU will result in an error.  |
| IPV6\_MULTICAST\_HOPS | yes | yes | DWORD | Gets or sets the TTL value associated with IPv6 multicast traffic on the socket. It is illegal to set the TTL to a value greater than 255.  This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IPV6\_MULTICAST\_IF | yes | yes | DWORD | Gets or sets the outgoing interface for sending IPv6 multicast traffic. This option does not change the default interface for receiving IPv6 multicast traffic. This option is important for multihomed computers.  The input value for setting this option is a 4-byte interface index of the desired outgoing interface in host byte order. The [**GetAdaptersAddresses**](/windows/win32/api/iphlpapi/nf-iphlpapi-getadaptersaddresses) function can be used to obtain the interface index information. If *optval* is set to **NULL** on call to [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt), the default IPv6 interface is used. If *optval* is zero , the default interface for receiving multicast is specified for sending multicast traffic.  When getting this option, the *optval* returns the current default interface index for sending multicast IPv6 traffic in host byte order. |
| IPV6\_MULTICAST\_LOOP | yes | yes | DWORD (boolean) | Indicates multicast data sent on the socket will be echoed to the sockets receive buffer if it is also joined on the destination multicast group. If *optval* is set to **1** on the call to [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt), the option is enabled. If set to **0**, the option is disabled.  This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| [IPV6\_PKTINFO](ipv6-pktinfo.md) | yes | yes | DWORD (boolean) | Indicates that packet information should be returned by the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function. |
| [IPV6\_PROTECTION\_LEVEL](ipv6-protection-level.md) | yes | yes | INT | Enables restriction of a socket to a specified scope, such as addresses with the same link local or site local prefix. Provides various restriction levels and default settings. See [IPV6\_PROTECTION\_LEVEL](ipv6-protection-level.md) for more information. |
| IPV6\_RECVIF | yes | yes | DWORD (boolean) | Indicates whether the IP stack should populate the control buffer with details about which interface received a packet with a datagram socket. When this value is true, the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function will return optional control data containing the interface where the packet was received for datagram sockets. This option allows the IPv6 interface where the packet was received to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure.  This option is only valid for datagram and raw sockets (the socket type must be SOCK\_DGRAM or SOCK\_RAW). |
| IPV6\_RECVTCLASS | yes | yes | DWORD (boolean) | Indicates whether the IP stack should populate the control buffer with a message containing the Traffic Class IPv6 header field on a received datagram. When this value is true, the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function will return optional control data containing the Traffic Class IPv6 header field value of the received datagram.  This option allows the Traffic Class IPv6 header field of the received datagram to be returned in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure. The returned message type will be IPV6\_TCLASS. All DSCP and ECN bits of the Traffic Class field will be returned.  This option is only valid on datagram sockets (the socket type must be SOCK\_DGRAM).  |
| IPV6\_UNICAST\_HOPS | yes | yes | DWORD | Gets or sets the current TTL value associated with IPv6 socket for unicast traffic. It is illegal to set the TTL to a value greater than 255. |
| IPV6\_UNICAST\_IF | yes | yes | DWORD (IF\_INDEX) | Gets or sets the outgoing interface for sending IPv6 traffic. This option does not change the default interface for receiving IPv6 traffic. This option is important for multihomed computers.  The input value for setting this option is a 4-byte interface index of the desired outgoing interface in host byte order. The [**GetAdaptersAddresses**](/windows/win32/api/iphlpapi/nf-iphlpapi-getadaptersaddresses) function can be used to obtain the interface index information. If *optval* is zero, the default interface for sending IPv6 traffic is set to unspecified.  When getting this option, the *optval* returns the current default interface index for sending IPv6 traffic in host byte order. |
| IPV6_USER_MTU | yes | yes | DWORD | Gets or sets an upper bound on the IP layer MTU (in bytes) for the given socket. If the value is higher than the system's estimate of the path MTU (which you can retrieve on a connected socket by querying the **IPV6_MTU** socket option), then the option has no effect. If the value is lower, then outbound packets larger than this will be fragmented, or will fail to send, depending on the value of **IPV6_DONTFRAG**. Default value is **IP_UNSPECIFIED_USER_MTU** (MAXULONG). For type-safety, you should use the [**WSAGetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsagetipusermtu) and [**WSASetIPUserMtu**](/windows/win32/api/ws2tcpip/nf-ws2tcpip-wsasetipusermtu) functions instead of using the socket option directly. |
| IPV6\_V6ONLY | yes | yes | DWORD (boolean) | Indicates if a socket created for the AF\_INET6 address family is restricted to IPv6 communications only. Sockets created for the AF\_INET6 address family may be used for both IPv6 and IPv4 communications. Some applications may want to restrict their use of a socket created for the AF\_INET6 address family to IPv6 communications only. When this value is nonzero (the default on Windows), a socket created for the AF\_INET6 address family can be used to send and receive IPv6 packets only. When this value is zero, a socket created for the AF\_INET6 address family can be used to send and receive packets to and from an IPv6 address or an IPv4 address. Note that the ability to interact with an IPv4 address requires the use of IPv4 mapped addresses. This socket option is supported on Windows Vista or later. |

## Windows support for IPPROTO\_IPV6 socket options

| Option | Windows 8 | Windows Server 2012 | Windows 7 | Windows Server 2008 | Windows Vista |
|-|-|-|-|-|-|
| IP\_ORIGINAL\_ARRIVAL\_IF | x | x | x | | |
| IPV6_ADD_IFLIST | Starting with Windows 10, version 1803 | | | | | |
| IPV6\_ADD\_MEMBERSHIP | x | x | x | x | x |
| IPV6_DEL_IFLIST | Starting with Windows 10, version 1803 | | | | | |
| IPV6\_DROP\_MEMBERSHIP | x | x | x | x | x |
| IPV6_GET_IFLIST | Starting with Windows 10, version 1803 | | | | | |
| IPV6\_HDRINCL | x | x | x | x | x |
| IPV6\_HOPLIMIT | x | x | x | x | x |
| IPV6_IFLIST | Starting with Windows 10, version 1803 | | | | | |
| IPV6\_JOIN\_GROUP | x | x | x | x | x |
| IPV6\_LEAVE\_GROUP | x | x | x | x | x |
| IPV6\_MULTICAST\_HOPS | x | x | x | x | x |
| IPV6\_MULTICAST\_IF | x | x | x | x | x |
| IPV6\_MULTICAST\_LOOP | x | x | x | x | x |
| IPV6\_PKTINFO | x | x | x | x | x |
| [IPV6\_PROTECTION\_LEVEL](ipv6-protection-level.md) | x | x | x | x | x |
| IPV6\_RECVIF | x | x | x | x | x |
| IPV6\_UNICAST\_HOPS | x | x | x | x | x |
| IPV6\_UNICAST\_IF | x | x | x | x | x |
| IPV6\_V6ONLY | x | x | x | x | x |

<br/>

| Option | Windows Server 2003 | Windows XP |
|-|-|-|
| IP\_ORIGINAL\_ARRIVAL\_IF | | |
| IPV6_ADD_IFLIST | | |
| IPV6\_ADD\_MEMBERSHIP | x | x |
| IPV6_DEL_IFLIST | | |
| IPV6\_DROP\_MEMBERSHIP | x | x |
| IPV6_GET_IFLIST | | |
| IPV6\_HDRINCL  x | x |
| IPV6\_HOPLIMIT  x | x |
| IPV6_IFLIST | | |
| IPV6\_JOIN\_GROUP | x | x |
| IPV6\_LEAVE\_GROUP | x | x |
| IPV6\_MULTICAST\_HOPS | x | x |
| IPV6\_MULTICAST\_IF | x | x |
| IPV6\_MULTICAST\_LOOP | x | x |
| IPV6\_PKTINFO | x | x |
| [IPV6\_PROTECTION\_LEVEL](ipv6-protection-level.md) | x | x |
| IPV6\_RECVIF | | |
| IPV6\_UNICAST\_HOPS | x | x |
| IPV6\_UNICAST\_IF | | |
| IPV6\_V6ONLY | | |

## Remarks

On the Microsoft Windows Software Development Kit (SDK) released for Windows Vista and later, the organization of header files has changed and **IPPROTO\_IPV6** level is defined in the *Ws2def.h* header file which is automatically included in the *Winsock2.h* header file. The **IPPROTO\_IPV6** socket options are defined in the *Ws2ipdef.h* header file which is automatically included in the *Ws2tcpip.h* header file. The *Ws2def.h* and *Ws2ipdef.h* header files should never be used directly.

The IP\_ORIGINAL\_ARRIVAL\_IF socket option is supported on Windows Server 2008 R2 as well as on Windows 7.

## Requirements

| Requirement | Value |
|-|-|
| Header | <dl> <dt>Ws2def.h (include Winsock2.h); </dt> <dt>Winsock2.h on Windows Server 2003 and Windows XP</dt> </dl> |
