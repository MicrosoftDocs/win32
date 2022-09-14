---
description: In order to support both IPv4 and IPv6 on Windows XP with Service Pack 1 (SP1) and on Windows Server 2003, an application has to create two sockets, one socket for use with IPv4 and one socket for use with IPv6.
ms.assetid: 7ae49081-ffb5-4eee-b488-2541398e7acc
title: Dual-Stack Sockets for IPv6 Winsock Applications
ms.topic: article
ms.date: 05/31/2018
---

# Dual-Stack Sockets for IPv6 Winsock Applications

In order to support both IPv4 and IPv6 on Windows XP with Service Pack 1 (SP1) and on Windows Server 2003, an application has to create two sockets, one socket for use with IPv4 and one socket for use with IPv6. These two sockets must be handled separately by the application.

Windows Vista and later offer the ability to create a single IPv6 socket which can handle both IPv6 and IPv4 traffic. For example, a TCP listening socket for IPv6 is created, put into dual stack mode, and bound to port 5001. This dual-stack socket can accept connections from IPv6 TCP clients connecting to port 5001 and from IPv4 TCP clients connecting to port 5001. This feature allows for greatly simplified application design and reduces the resource overhead required of posting operations on two separate sockets.

## Creating a Dual-Stack Socket

By default, an IPv6 socket created on Windows Vista and later only operates over the IPv6 protocol. In order to make an IPv6 socket into a dual-stack socket, the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function must be called with the **IPV6\_V6ONLY** socket option to set this value to zero before the socket is bound to an IP address. When the **IPV6\_V6ONLY** socket option is set to zero, a socket created for the **AF\_INET6** address family can be used to send and receive packets to and from an IPv6 address or an IPv4 mapped address.

## IP Addresses with a Dual-Stack Socket

Dual-stack sockets always require IPv6 addresses. The ability to interact with an IPv4 address requires the use of the IPv4-mapped IPv6 address format. Any IPv4 addresses must be represented in the IPv4-mapped IPv6 address format which enables an IPv6 only application to communicate with an IPv4 node. The IPv4-mapped IPv6 address format allows the IPv4 address of an IPv4 node to be represented as an IPv6 address. The IPv4 address is encoded into the low-order 32 bits of the IPv6 address, and the high-order 96 bits hold the fixed prefix 0:0:0:0:0:FFFF. The IPv4-mapped IPv6 address format is specified in RFC 4291. For more information, see [www.ietf.org/rfc/rfc4291.txt](https://tools.ietf.org/html/rfc4291). The IN6ADDR\_SETV4MAPPED macro in *Mstcpip.h* can be used to convert an IPv4 address to the required IPv4-mapped IPv6 address format.

If the underlying protocol is actually IPv4, then the IPv4 address is mapped into an IPv4-mapped IPv6 address format. That is the, family field in the [SOCKADDR](sockaddr-2.md) structure indicates AF\_INET6, but an IPv4-mapped IPv6 address is encoded in the IPv6 address structure. For a dual-stack socket in listening mode, this means that any accepted IPv4 connections will return an IPv4-mapped IPv6 address. For a dual-stack socket that is connecting to an IPv4 destination, the SOCKADDR structure passed to connect must be an IPv4-mapped IPv6 address. Applications must take care to handle these IPv4-mapped IPv6 addresses appropriately and only use them with dual stack sockets. If an IP address is to be passed to a regular IPv4 socket, the address must be a regular IPv4 address not a IPv4-mapped IPv6 address.

## Potential Issues using a Dual-Stack Socket

A potential pitfall for applications is getting an IPv4-mapped IPv6 address on a dual-stack socket and then trying to use the returned IP address on a different IPv6 only socket. For example, the [**getsockname**](/windows/desktop/api/winsock/nf-winsock-getsockname) or [**getpeername**](/windows/desktop/api/winsock/nf-winsock-getpeername) functions can return an IPv4-mapped IPv6 address when used on a dual-stack socket. If the returned IPv4-mapped IPv6 address is then subsequently used on a different socket that was not set to dual-stack (an IPv6 only socket which is the default behavior when a socket is created), any use of this IPv6 only socket with an IPv4-mapped IPv6 address will fail. The IPv4-mapped IPv6 address format can only be used on a dual-stack socket.

On a dual-stack datagram socket, if an application requires the [**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg) function to return packet information in a [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure for datagrams received over IPv4, then [IP\_PKTINFO](ip-pktinfo.md) socket option must be set to true on the socket. If only the [IPV6\_PKTINFO](ipv6-pktinfo.md) option is set to true on the socket, packet information will be provided for datagrams received over IPv6 but may not be provided for datagrams received over IPv4.

If an application tries to set the [IP\_PKTINFO](ip-pktinfo.md) socket option on a dual-stack datagram socket and IPv4 is disabled on the system, then the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function will fail and [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) will return with an error of [WSAEINVAL](windows-sockets-error-codes-2.md). This same error is also returned by the **setsockopt** function as a result of other errors. If an application tries to set an IPPROTO\_IP level socket option on a dual-stack socket and it fails with [WSAEINVAL](windows-sockets-error-codes-2.md), then the application should determine if IPv4 is disabled on the local computer. One method that can be used to detect if IPv4 is enabled or disabled is to call the [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) function with the *af* parameter set to AF\_INET to try and create an IPv4 socket. If the **socket** function fails and **WSAGetLastError** returns an error of [WSAEAFNOSUPPORT](windows-sockets-error-codes-2.md), then it means IPv4 is not enabled. In this case, a **setsockopt** function failure when attempting to set the IP\_PKTINFO socket option can be ignored by the application. Otherwise a failure when attempting to set the IP\_PKTINFO socket option should be treated as an unexpected error.

For a dual-stack socket when sending datagrams with the [**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg) function and an application wants to specify a specific local IP source address to be used, the method to handle this depends on the destination IP address. When sending to an IPv4 destination address or an IPv4-mapped IPv6 destination address, one of the control data objects passed in the [**WSAMSG**](/windows/desktop/api/Ws2def/ns-ws2def-wsamsg) structure pointed to by the *lpMsg* parameter should contain an [**in\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in_pktinfo) structure containing the local IPv4 source address to use for sending. When sending to an IPv6 destination address that is not a an IPv4-mapped IPv6 address, one of the control data objects passed in the **WSAMSG** structure pointed to by the *lpMsg* parameter should contain an [**in6\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in6_pktinfo) structure containing the local IPv6 source address to use for sending.

## Related topics

<dl> <dt>

[IPv6 Guide for Windows Sockets Applications](ipv6-guide-for-windows-sockets-applications-2.md)
</dt> <dt>

[Changing Data Structures for IPv6 Winsock Appications](changing-data-structures-2.md)
</dt> <dt>

[Function Calls for IPv6 Winsock Applications](function-calls-2.md)
</dt> <dt>

[Use of Hardcoded IPv4 Addresses](use-of-hardcoded-ipv4-addresses-2.md)
</dt> <dt>

[User Interface Issues for IPv6 Winsock Applications](user-interface-issues-2.md)
</dt> <dt>

[Underlying Protocols for IPv6 Winsock Applications](underlying-protocols-2.md)
</dt> <dt>

[**getpeername**](/windows/desktop/api/winsock/nf-winsock-getpeername)
</dt> <dt>

[**getsockname**](/windows/desktop/api/winsock/nf-winsock-getsockname)
</dt> <dt>

[**in\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in_pktinfo)
</dt> <dt>

[**in6\_pktinfo**](/windows/desktop/api/Ws2ipdef/ns-ws2ipdef-in6_pktinfo)
</dt> <dt>

[IP\_PKTINFO](ip-pktinfo.md)
</dt> <dt>

[IPV6\_PKTINFO](ipv6-pktinfo.md)
</dt> <dt>

[**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt)
</dt> <dt>

[**LPFN_WSARECVMSG (WSARecvMsg)**](/windows/win32/api/mswsock/nc-mswsock-lpfn_wsarecvmsg)
</dt> <dt>

[**WSASendMsg**](/windows/desktop/api/winsock2/nf-winsock2-wsasendmsg)
</dt> </dl>

 

 
