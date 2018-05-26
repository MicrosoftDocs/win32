---
Description: The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear.
ms.assetid: 37ef8a69-2aa0-4824-8ca9-4b84158086db
title: Transport Mapping Between API and SPI Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Transport Mapping Between API and SPI Functions

The Winsock Transport SPI is similar to the Winsock API in that all of the basic socket functions appear. When a new version of a Winsock function and the original version both exist in the API, only the new version will show up in the SPI. This is illustrated in the following list.

-   [**connect**](/windows/win32/Winsock2/nf-winsock2-connect?branch=master) and [**WSAConnect**](/windows/win32/Winsock2/nf-winsock2-wsaconnect?branch=master) both map to [**WSPConnect**](/windows/win32/Ws2spi/?branch=master)
-   [**accept**](/windows/win32/Winsock2/nf-winsock2-accept?branch=master) and [**WSAAccept**](/windows/win32/Winsock2/nf-winsock2-wsaaccept?branch=master) map to [**WSPAccept**](/windows/win32/Ws2spi/nc-ws2spi-lpwspaccept?branch=master)
-   [**socket**](/windows/win32/Winsock2/nf-winsock2-socket?branch=master) and [**WSASocket**](/windows/win32/Winsock2/nf-winsock2-wsasocketa?branch=master) map to [**WSPSocket**](/windows/win32/Ws2spi/nc-ws2spi-lpwspsocket?branch=master)

Other API functions that are collapsed into the enhanced versions in SPI include:

-   [**send**](/windows/win32/Winsock2/nf-winsock2-send?branch=master)
-   [**sendto**](/windows/win32/winsock/nf-winsock-sendto?branch=master)
-   [**recv**](/windows/win32/winsock/nf-winsock-recv?branch=master)
-   [**recvfrom**](/windows/win32/winsock/nf-winsock-recvfrom?branch=master)
-   [**ioctlsocket**](/windows/win32/winsock/nf-winsock-ioctlsocket?branch=master)

Support functions like [**htonl**](/windows/win32/winsock/nf-winsock-htonl?branch=master), [**htons**](/windows/win32/winsock/nf-winsock-htons?branch=master), [**ntohl**](/windows/win32/winsock/nf-winsock-ntohl?branch=master), and [**ntohs**](/windows/win32/winsock/nf-winsock-ntohs?branch=master) are implemented in the Ws2\_32.dll, and are not passed down to service providers. The same holds true for the WSA versions of these functions.

Windows Sockets service provider enumeration and the blocking hook-related functions are realized in the Ws2\_32.dll, thus [**WSAEnumProtocols**](/windows/win32/Winsock2/nf-winsock2-wsaenumprotocolsa?branch=master), [WSAIsBlocking](/windows/win32/winsock2/nf-winsock2-wsaisblocking?branch=master), [WSASetBlockingHook](/windows/win32/winsock2/nf-winsock2-wsasetblockinghook?branch=master), and [WSAUnhookBlockingHook](/windows/win32/winsock2/nf-winsock2-wsaunhookblockinghook?branch=master) do not appear as SPI functions.

Because error codes are returned along with SPI functions, equivalents of [**WSAGetLastError**](/windows/win32/winsock/nf-winsock-wsagetlasterror?branch=master) and [**WSASetLastError**](/windows/win32/winsock/nf-winsock-wsasetlasterror?branch=master) are not required in the SPI.

The event object manipulation and wait functions, including [**WSACreateEvent**](/windows/win32/Winsock2/nf-winsock2-wsacreateevent?branch=master), [**WSACloseEvent**](/windows/win32/Winsock2/nf-winsock2-wsacloseevent?branch=master), [**WSASetEvent**](/windows/win32/Winsock2/nf-winsock2-wsasetevent?branch=master), [**WSAResetEvent**](/windows/win32/Winsock2/nf-winsock2-wsaresetevent?branch=master), and [**WSAWaitForMultipleEvents**](/windows/win32/Winsock2/nf-winsock2-wsawaitformultipleevents?branch=master) are mapped directly to native Windows services and thus are not present in the SPI.

All the TCP/IP-specific name conversion and resolution functions in Windows Sockets 1.1 such as **GetXbyY**, **WSAAsyncGetXByY**, and [**WSACancelAsyncRequest**](/windows/win32/winsock/nf-winsock-wsacancelasyncrequest?branch=master), as well as [**gethostname**](/windows/win32/winsock/nf-winsock-gethostname?branch=master) are implemented within the Ws2\_32.dll in terms of the new name resolution facilities. For more information, see [Compatible Name Resolution for TCP/IP in the Windows Sockets 1.1 SPI](compatible-name-resolution-for-tcp-ip-in-the-windows-sockets-1-1-spi-2.md). Conversion functions such as [**inet\_addr**](/windows/win32/wsipv6ok/nf-winsock-inet_addr?branch=master) and [**inet\_ntoa**](/windows/win32/wsipv6ok/nf-winsock-inet_ntoa?branch=master) are implemented within the Ws2\_32.dll.

 

 



