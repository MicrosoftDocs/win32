---
description: The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear.
ms.assetid: 37ef8a69-2aa0-4824-8ca9-4b84158086db
title: Transport Mapping Between API and SPI Functions
ms.topic: article
ms.date: 05/31/2018
---

# Transport Mapping Between API and SPI Functions

The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear. When a new version of a Winsock function and the original version both exist in the API, only the new version will show up in the SPI. This is illustrated in the following list.

-   [**connect**](/windows/desktop/api/Winsock2/nf-winsock2-connect) and [**WSAConnect**](/windows/desktop/api/Winsock2/nf-winsock2-wsaconnect) both map to [**WSPConnect**](/previous-versions/windows/hardware/network/ff566275(v=vs.85))
-   [**accept**](/windows/desktop/api/Winsock2/nf-winsock2-accept) and [**WSAAccept**](/windows/desktop/api/Winsock2/nf-winsock2-wsaaccept) map to [**WSPAccept**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspaccept)
-   [**socket**](/windows/desktop/api/Winsock2/nf-winsock2-socket) and [**WSASocket**](/windows/desktop/api/Winsock2/nf-winsock2-wsasocketa) map to [**WSPSocket**](/windows/desktop/api/Ws2spi/nc-ws2spi-lpwspsocket)

Other API functions that are collapsed into the enhanced versions in SPI include:

-   [**send**](/windows/desktop/api/Winsock2/nf-winsock2-send)
-   [**sendto**](/windows/desktop/api/winsock/nf-winsock-sendto)
-   [**recv**](/windows/desktop/api/winsock/nf-winsock-recv)
-   [**recvfrom**](/windows/desktop/api/winsock/nf-winsock-recvfrom)
-   [**ioctlsocket**](/windows/desktop/api/winsock/nf-winsock-ioctlsocket)

Support functions like [**htonl**](/windows/desktop/api/winsock/nf-winsock-htonl), [**htons**](/windows/desktop/api/winsock/nf-winsock-htons), [**ntohl**](/windows/desktop/api/winsock/nf-winsock-ntohl), and [**ntohs**](/windows/desktop/api/winsock/nf-winsock-ntohs) are implemented in the Ws2\_32.dll, and are not passed down to service providers. The same holds true for the WSA versions of these functions.

Windows Sockets service provider enumeration and the blocking hook-related functions are realized in the Ws2\_32.dll, thus [**WSAEnumProtocols**](/windows/desktop/api/Winsock2/nf-winsock2-wsaenumprotocolsa), [WSAIsBlocking](/windows/desktop/api/winsock2/nf-winsock2-wsaisblocking), [WSASetBlockingHook](/windows/desktop/api/winsock2/nf-winsock2-wsasetblockinghook), and [WSAUnhookBlockingHook](/windows/desktop/api/winsock2/nf-winsock2-wsaunhookblockinghook) do not appear as SPI functions.

Because error codes are returned along with SPI functions, equivalents of [**WSAGetLastError**](/windows/desktop/api/winsock/nf-winsock-wsagetlasterror) and [**WSASetLastError**](/windows/desktop/api/winsock/nf-winsock-wsasetlasterror) are not required in the SPI.

The event object manipulation and wait functions, including [**WSACreateEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacreateevent), [**WSACloseEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsacloseevent), [**WSASetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsasetevent), [**WSAResetEvent**](/windows/desktop/api/Winsock2/nf-winsock2-wsaresetevent), and [**WSAWaitForMultipleEvents**](/windows/desktop/api/Winsock2/nf-winsock2-wsawaitformultipleevents) are mapped directly to native Windows services and thus are not present in the SPI.

All the TCP/IP-specific name conversion and resolution functions in Windows Sockets 1.1 such as **GetXbyY**, **WSAAsyncGetXByY**, and [**WSACancelAsyncRequest**](/windows/desktop/api/winsock/nf-winsock-wsacancelasyncrequest), as well as [**gethostname**](/windows/desktop/api/winsock/nf-winsock-gethostname) are implemented within the Ws2\_32.dll in terms of the new name resolution facilities. For more information, see [Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-spi-2.md). Conversion functions such as [**inet\_addr**](/windows/win32/api/winsock2/nf-winsock2-inet_addr) and [**inet\_ntoa**](/windows/win32/api/winsock2/nf-winsock2-inet_ntoa) are implemented within the Ws2\_32.dll.

 

 
