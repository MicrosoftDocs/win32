---
description: IPv6 support, TCP/IP Annex, and Windows Sockets.
ms.assetid: 03e29ef1-2105-4cec-8b80-0f9acab046f6
title: IPv6 Support
ms.topic: article
ms.date: 05/31/2018
---

# IPv6 Support

In order to support both IPv4 and IPv6 on Windows XP with Service Pack 1 (SP1) and on Windows Server 2003, an application has to create two sockets, one socket for use with IPv4 and one socket for use with IPv6. These two sockets must be handled separately by the application.

If a TCP/IP service provider on Windows XP with SP1 and on Windows Server 2003 supports IPv4 and IPv6 addressing, it must create two separate sockets and listen separately on these sockets:

-   Once for IPv4.
-   Once for the IPv6 address family.

Windows Vista and later offer the ability to create a single IPv6 socket which can handle both IPv6 and IPv4 traffic. For example, a TCP listening socket for IPv6 is created, put into dual stack mode, and bound to port 5001. This dual-stack socket can accept connections from IPv6 TCP clients connecting to port 5001 and from IPv4 TCP clients connecting to port 5001. This feature allows for greatly simplified application design and reduces the resource overhead required of posting operations on two separate sockets. However, there are some restrictions that must be met in order to use a dual-stack socket. For more information, see [Dual-Stack Sockets](dual-stack-sockets.md).

[**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa) returns two [**WSAPROTOCOL\_INFO**](/windows/win32/api/winsock2/ns-winsock2-wsaprotocol_infoa) structures for each of the supported socket types (SOCK\_STREAM, SOCK\_DGRAM, SOCK\_RAW). The **iAddressFamily** must by set to AF\_INET for IPv4 addressing, and to AF\_INET6 for IPv6 addressing.

The IPv6 addresses are described in the following structures.

``` syntax
struct in_addr6 {
    u_char    s6_addr[16];             /* IPv6 address */
};

struct sockaddr_in6 {
    short             sin6_family;     /* AF_INET6 */
    u_short           sin6_port;       /* Transport level port number */
    u_long            sin6_flowinfo;   /* IPv6 flow information */
    struct in_addr6   sin6_addr;       /* IPv6 address */
    u_long            sin6_scope_id;   /* set of interfaces for a scope */
   };
```

If an application uses Windows Sockets 1.1 functions and wants to use IPv6 addresses, it may continue to use all the old functions that take the [**sockaddr**](sockaddr-2.md) structure as one of the parameters ([**bind**](/windows/desktop/api/winsock/nf-winsock-bind), [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect), [**sendto**](/windows/desktop/api/winsock/nf-winsock-sendto), and [**recvfrom**](/windows/desktop/api/winsock/nf-winsock-recvfrom), [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept), and so forth). The only change that is required is to use **sockaddr\_in6** instead of **sockaddr\_in**.

However, the name resolution functions ([**gethostbyname**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyname), [**gethostbyaddr**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyaddr), and so forth) and address conversion functions ([**inet\_addr**](/windows/win32/api/winsock2/nf-winsock2-inet_addr), [**inet\_ntoa**](/windows/win32/api/winsock2/nf-winsock2-inet_ntoa)) cannot be reused because they assume an IP address is 4 bytes in length. An application that wants to perform name resolution and address conversion for IPv6 addresses must use Windows Sockets 2-specific functions. Many new functions have been introduced to enable Windows Sockets 2 applications to take advantage of IPv6, including the [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo) and [**getnameinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getnameinfo) functions.

For more information on how to enable IPv6 capabilities in an application, see the [IPv6 Guide for Windows Sockets Applications](ipv6-guide-for-windows-sockets-applications-2.md).

 

 
