---
description: Note  All of the Windows Sockets 1.1 functions for name resolution are specific to IPv4 TCP/IP networks.
ms.assetid: 5a2a37f3-85c5-4b27-9ce3-f5b707b1564a
title: Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API
ms.topic: article
ms.date: 05/31/2018
---

# Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 API

> [!Note]  
> All of the Windows Sockets 1.1 functions for name resolution are specific to IPv4 TCP/IP networks. Application developers are strongly discouraged from continuing to utilize these transport-specific functions that only support IPv4.

 

Application developers should be using the following functions that are protocol-independent and support both IPv6 and IPv4 name resolution.

-   [**getaddrinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfo)
-   [**GetAddrInfoEx**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfoexa)
-   [**GetAddrInfoW**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getaddrinfow)
-   [**getnameinfo**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getnameinfo)
-   [**GetNameInfoW**](/windows/desktop/api/Ws2tcpip/nf-ws2tcpip-getnameinfow)

Windows Sockets 1.1 defined a number of routines used for name resolution with TCP/IP (IP version 4) networks. These are sometimes called the **getXbyY** functions and include the following:

<dl>

[**gethostname**](/windows/desktop/api/winsock/nf-winsock-gethostname)  
[**gethostbyaddr**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyaddr)  
[**gethostbyname**](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyname)  
[**getprotobyname**](/windows/desktop/api/winsock/nf-winsock-getprotobyname)  
[**getprotobynumber**](/windows/desktop/api/winsock/nf-winsock-getprotobynumber)  
[**getservbyname**](/windows/desktop/api/winsock/nf-winsock-getservbyname)  
[**getservbyport**](/windows/desktop/api/winsock/nf-winsock-getservbyport)  
</dl>

Asynchronous versions of these functions were also defined.

<dl>

[**WSAAsyncGetHostByAddr**](/windows/win32/api/winsock/nf-winsock-wsaasyncgethostbyaddr)  
[**WSAAsyncGetHostByName**](/windows/win32/api/winsock/nf-winsock-wsaasyncgethostbyname)  
[**WSAAsyncGetProtoByName**](/windows/desktop/api/winsock/nf-winsock-wsaasyncgetprotobyname)  
[**WSAAsyncGetProtoByNumber**](/windows/desktop/api/winsock/nf-winsock-wsaasyncgetprotobynumber)  
[**WSAAsyncGetServByName**](/windows/desktop/api/winsock/nf-winsock-wsaasyncgetservbyname)  
[**WSAAsyncGetServByPort**](/windows/desktop/api/winsock/nf-winsock-wsaasyncgetservbyport)  
</dl>

There are also two functions, now implemented in the Winsock2.dll, used to convert dotted Ipv4 address notation to and from string and binary representations, respectively.

<dl>

[**inet\_addr**](/windows/win32/api/winsock2/nf-winsock2-inet_addr)  
[**inet\_ntoa**](/windows/win32/api/winsock2/nf-winsock2-inet_ntoa)  
</dl>

In order to retain strict backward compatibility with Windows Sockets 1.1, all of the older IPv4-only functions continue to be supported as long as at least one namespace provider is present that supports the AF\_INET address family (these functions are not relevant to IP version 6, denoted by AF\_INET6).

The Ws2\_32.dll implements these compatibility functions in terms of the new, protocol-independent name resolution facilities using an appropriate sequence of [**WSALookupServiceBegin**](/windows/desktop/api/Winsock2/nf-winsock2-wsalookupservicebegina)/**Next**/**End** function calls. The details of how the **getXbyY** functions are mapped to name resolution functions are provided below. The WSs2\_32.dll handles the differences between the asynchronous and synchronous versions of the **getXbyY** functions, so only the implementation of the synchronous **getXbyY** functions are discussed.

This section describes compatible name resolution for TCP/IP in the Windows Sockets 1.1 API. The following list describes the topics in this section:

-   [Basic Approach for GetXbyY in the API](basic-approach-for-getxbyy-in-the-api-2.md)
-   [getprotobyname and getprotobynumber Functions in the API](getprotobyname-and-getprotobynumber-functions-in-the-api-2.md)
-   [getservbyname and getservbyport Functions in the API](getservbyname-and-getservbyport-functions-in-the-api-2.md)
-   [gethostbyname Function in the API](gethostbyname-function-in-the-api-2.md)
-   [gethostbyaddr Function in the API](gethostbyaddr-function-in-the-api-2.md)
-   [gethostname Function in the API](gethostname-function-in-the-api-2.md)

## Related topics

<dl> <dt>

[Protocol-Independent Name Resolution](protocol-independent-name-resolution-2.md)
</dt> <dt>

[Registration and Name Resolution](registration-and-name-resolution-2.md)
</dt> </dl>

 

 
