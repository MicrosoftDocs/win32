---
Description: 'The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear.'
ms.assetid: '37ef8a69-2aa0-4824-8ca9-4b84158086db'
title: Transport Mapping Between API and SPI Functions
---

# Transport Mapping Between API and SPI Functions

The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear. When a new version of a Winsock function and the original version both exist in the API, only the new version will show up in the SPI. This is illustrated in the following list.

-   [**connect**](connect-2.md) and [**WSAConnect**](wsaconnect-2.md) both map to [**WSPConnect**](wspconnect-2.md)
-   [**accept**](accept-2.md) and [**WSAAccept**](wsaaccept-2.md) map to [**WSPAccept**](wspaccept-2.md)
-   [**socket**](socket-2.md) and [**WSASocket**](wsasocket-2.md) map to [**WSPSocket**](wspsocket-2.md)

Other API functions that are collapsed into the enhanced versions in SPI include:

-   [**send**](send-2.md)
-   [**sendto**](sendto-2.md)
-   [**recv**](recv-2.md)
-   [**recvfrom**](recvfrom-2.md)
-   [**ioctlsocket**](ioctlsocket-2.md)

Support functions like [**htonl**](htonl-2.md), [**htons**](htons-2.md), [**ntohl**](ntohl-2.md), and [**ntohs**](ntohs-2.md) are implemented in the Ws2\_32.dll, and are not passed down to service providers. The same holds true for the WSA versions of these functions.

Windows Sockets service provider enumeration and the blocking hook-related functions are realized in the Ws2\_32.dll, thus [**WSAEnumProtocols**](wsaenumprotocols-2.md), [WSAIsBlocking](wsaisblocking-2.md), [WSASetBlockingHook](wsasetblockinghook-2.md), and [WSAUnhookBlockingHook](wsaunhookblockinghook-2.md) do not appear as SPI functions.

Because error codes are returned along with SPI functions, equivalents of [**WSAGetLastError**](wsagetlasterror-2.md) and [**WSASetLastError**](wsasetlasterror-2.md) are not required in the SPI.

The event object manipulation and wait functions, including [**WSACreateEvent**](wsacreateevent-2.md), [**WSACloseEvent**](wsacloseevent-2.md), [**WSASetEvent**](wsasetevent-2.md), [**WSAResetEvent**](wsaresetevent-2.md), and [**WSAWaitForMultipleEvents**](wsawaitformultipleevents-2.md) are mapped directly to native Windows services and thus are not present in the SPI.

All the TCP/IP-specific name conversion and resolution functions in Windows Sockets 1.1 such as **GetXbyY**, **WSAAsyncGetXByY**, and [**WSACancelAsyncRequest**](wsacancelasyncrequest-2.md), as well as [**gethostname**](gethostname-2.md) are implemented within the Ws2\_32.dll in terms of the new name resolution facilities. For more information, see [Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-spi-2.md). Conversion functions such as [**inet\_addr**](inet-addr-2.md) and [**inet\_ntoa**](inet-ntoa-2.md) are implemented within the Ws2\_32.dll.

 

 



