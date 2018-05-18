---
Description: 'Windows Sockets 1.1 defined a number of routines that were used for IPv4 name resolution with TCP/IP networks. These are customarily called the GetXbyY functions and include the following.'
ms.assetid: '7a3ff7f3-d4b9-4900-8fd8-708a89c78c0a'
title: 'Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI'
---

# Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI

Windows Sockets 1.1 defined a number of routines that were used for IPv4 name resolution with TCP/IP networks. These are customarily called the **GetXbyY** functions and include the following.

[**gethostname**](gethostname-2.md)

[**gethostbyaddr**](gethostbyaddr-2.md)

[**gethostbyname**](gethostbyname-2.md)

[**getprotobyname**](getprotobyname-2.md)

[**getprotobynumber**](getprotobynumber-2.md)

[**getservbyname**](getservbyname-2.md)

[**getservbyport**](getservbyport-2.md)

Asynchronous versions of these functions were also defined.

[**WSAAsyncGetHostByAddr**](wsaasyncgethostbyaddr-2.md)

[**WSAAsyncGetHostByName**](wsaasyncgethostbyname-2.md)

[**WSAAsyncGetProtoByName**](wsaasyncgetprotobyname-2.md)

[**WSAAsyncGetProtoByNumber**](wsaasyncgetprotobynumber-2.md)

[**WSAAsyncGetServByName**](wsaasyncgetservbyname-2.md)

[**WSAAsyncGetServByPort**](wsaasyncgetservbyport-2.md)

These functions are specific to TCP/IP networks; developers of protocol-independent applications are discouraged from continuing to utilize these transport-specific functions. However, to retain strict backward compatibility with Windows Sockets 1.1, the preceding functions continue to be supported as long as at least one namespace provider is present that supports the AF\_INET address family.

The *Ws2\_32.dll* implements these compatibility functions in terms of the new, protocol-independent name resolution facilities using an appropriate sequence of [**WSALookupServiceBegin**](wsalookupservicebegin-2.md), [**WSALookupServiceNext**](wsalookupservicenext-2.md), [**WSALookupServiceEnd**](wsalookupserviceend-2.md) function calls. The details of how the **GetXbyY** functions are mapped to name resolution functions are provided below. The Ws2\_32.dll handles the differences between the asynchronous and synchronous versions of the **GetXbyY** functions, so that only the implementation of the synchronous **GetXbyY** functions are discussed.

 

 



