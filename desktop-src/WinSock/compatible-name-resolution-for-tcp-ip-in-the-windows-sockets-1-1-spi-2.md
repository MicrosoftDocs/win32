---
Description: Windows Sockets 1.1 defined a number of routines that were used for IPv4 name resolution with TCP/IP networks. These are customarily called the GetXbyY functions and include the following.
ms.assetid: 7a3ff7f3-d4b9-4900-8fd8-708a89c78c0a
title: Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI

Windows Sockets 1.1 defined a number of routines that were used for IPv4 name resolution with TCP/IP networks. These are customarily called the **GetXbyY** functions and include the following.

[**gethostname**](/windows/win32/winsock/nf-winsock-gethostname?branch=master)

[**gethostbyaddr**](/windows/win32/wsipv6ok/nf-winsock-gethostbyaddr?branch=master)

[**gethostbyname**](/windows/win32/wsipv6ok/nf-winsock-gethostbyname?branch=master)

[**getprotobyname**](/windows/win32/winsock/nf-winsock-getprotobyname?branch=master)

[**getprotobynumber**](/windows/win32/winsock/nf-winsock-getprotobynumber?branch=master)

[**getservbyname**](/windows/win32/winsock/nf-winsock-getservbyname?branch=master)

[**getservbyport**](/windows/win32/winsock/nf-winsock-getservbyport?branch=master)

Asynchronous versions of these functions were also defined.

[**WSAAsyncGetHostByAddr**](/windows/win32/wsipv6ok/nf-winsock-wsaasyncgethostbyaddr?branch=master)

[**WSAAsyncGetHostByName**](/windows/win32/wsipv6ok/nf-winsock-wsaasyncgethostbyname?branch=master)

[**WSAAsyncGetProtoByName**](/windows/win32/winsock/nf-winsock-wsaasyncgetprotobyname?branch=master)

[**WSAAsyncGetProtoByNumber**](/windows/win32/winsock/nf-winsock-wsaasyncgetprotobynumber?branch=master)

[**WSAAsyncGetServByName**](/windows/win32/winsock/nf-winsock-wsaasyncgetservbyname?branch=master)

[**WSAAsyncGetServByPort**](/windows/win32/winsock/nf-winsock-wsaasyncgetservbyport?branch=master)

These functions are specific to TCP/IP networks; developers of protocol-independent applications are discouraged from continuing to utilize these transport-specific functions. However, to retain strict backward compatibility with Windows Sockets 1.1, the preceding functions continue to be supported as long as at least one namespace provider is present that supports the AF\_INET address family.

The *Ws2\_32.dll* implements these compatibility functions in terms of the new, protocol-independent name resolution facilities using an appropriate sequence of [**WSALookupServiceBegin**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicebegina?branch=master), [**WSALookupServiceNext**](/windows/win32/Winsock2/nf-winsock2-wsalookupservicenexta?branch=master), [**WSALookupServiceEnd**](/windows/win32/Winsock2/nf-winsock2-wsalookupserviceend?branch=master) function calls. The details of how the **GetXbyY** functions are mapped to name resolution functions are provided below. The Ws2\_32.dll handles the differences between the asynchronous and synchronous versions of the **GetXbyY** functions, so that only the implementation of the synchronous **GetXbyY** functions are discussed.

 

 



