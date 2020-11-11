---
title: Bluetooth Programming with Windows Sockets
description: This section describes how to use Windows Sockets functions and structures to program a Bluetooth application.
ms.assetid: 0f15cb84-1d7a-4b64-86e8-b1b23c956c64
keywords:
- Bluetooth, tasks
- Windows Sockets
- programming
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth Programming with Windows Sockets

This section describes how to use Windows Sockets functions and structures to program a Bluetooth application. Complete reference information for the Windows Sockets API elements can be found in [Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2); this section provides only Bluetooth-specific information for each Windows Sockets programming element.

You can also download the [Bluetooth connection sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/master/Official%20Windows%20Platform%20Sample/Bluetooth%20connection%20sample) for a complete example.

As with all Windows Sockets application programming, the [**WSAStartup**](/windows/desktop/api/winsock/nf-winsock-wsastartup) function must be called to initiate Windows Sockets functionality and enable Bluetooth.

The following topics provide guidance in the use of Windows Sockets functions and structures with the Microsoft Bluetooth API:



| Topic                                                                                            | Description                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bluetooth and accept](bluetooth-and-accept.md)                                                 | Bluetooth uses the [**accept**](/windows/desktop/api/winsock2/nf-winsock2-accept) function to enable incoming connection attempts on a socket.<br/>                                                                                                                                                                                                  |
| [Bluetooth and bind](bluetooth-and-bind.md)                                                     | Bluetooth uses the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function to bind to a socket.<br/>                                                                                                                                                                                                                                     |
| [Bluetooth and BLOB](bluetooth-and-blob.md)                                                     | Bluetooth uses the [**BLOB**](/windows/desktop/api/nspapi/ns-nspapi-blob) structure to pass or receive transport-specific data to the [**WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md) structure during calls to the [**WSASetService**](bluetooth-and-wsasetservice.md) or **WSALookupService**\* functions. <br/>             |
| [Bluetooth and connect](bluetooth-and-connect.md)                                               | Bluetooth uses the [**connect**](/windows/desktop/api/winsock2/nf-winsock2-connect) function to connect to a target Bluetooth device, using a previously created Bluetooth socket.<br/>                                                                                                                                                              |
| [Bluetooth and getaddrinfo](bluetooth-and-getaddrinfo.md)                                       | The [**getaddrinfo**](/windows/desktop/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) function provides translation from host name to address for IP-based transports.<br/>                                                                                                                                                                                   |
| [Bluetooth and getpeername](bluetooth-and-getpeername.md)                                       | Used to retrieve the Bluetooth address of the peer Bluetooth device.<br/>                                                                                                                                                                                                                                            |
| [Bluetooth and getsockname](bluetooth-and-getsockname.md)                                       | Bluetooth uses the [**getsockname**](/windows/desktop/api/winsock/nf-winsock-getsockname) function to retrieve the server device address and port number allocated to a socket through a previous call to the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function.<br/>                                                                                            |
| [Bluetooth and getsockopt](bluetooth-and-getsockopt.md)                                         | Bluetooth uses the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) function to query various parameters associated with the server channel or the connection. <br/>                                                                                                                                                           |
| [Bluetooth and listen, select, and closesocket](bluetooth-and-listen-select-and-closesocket.md) | Bluetooth uses the [**listen**](/windows/desktop/api/winsock2/nf-winsock2-listen), [**select**](/windows/desktop/api/winsock2/nf-winsock2-select), and [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) functions without any modification from standard Windows Sockets programming.<br/>                                                                                                   |
| [Bluetooth and read or write operations](bluetooth-and-read-or-write-operations.md)             | Details the supported Winsock read and write operations.<br/>                                                                                                                                                                                                                                                        |
| [Bluetooth and setsockopt](bluetooth-and-setsockopt.md)                                         | Bluetooth uses the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function to set various parameters associated with the server channel or the connection.<br/>                                                                                                                                                              |
| [Bluetooth and shutdown](bluetooth-and-shutdown.md)                                             | Bluetooth uses the [**shutdown**](/windows/desktop/api/winsock/nf-winsock-shutdown) function to disconnect from the remote radio.<br/>                                                                                                                                                                                                             |
| [Bluetooth and socket](bluetooth-and-socket.md)                                                 | Bluetooth uses the [**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket) function creates a socket for incoming or outgoing connections.<br/>                                                                                                                                                                                               |
| [Bluetooth and Socket Options](bluetooth-and-socket-options.md)                                 | Details the socket options supported by Microsoft Bluetooth.<br/>                                                                                                                                                                                                                                                    |
| [Bluetooth and WSAAddressToString](bluetooth-and-wsaaddresstostring.md)                         | Used to convert a Bluetooth Device Address to a string, which is in turn provided to the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function via the [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure when retrieving device service information.<br/>                                           |
| [Bluetooth and WSALookupServiceBegin](bluetooth-and-wsalookupservicebegin.md)                   | Bluetooth uses the [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina) function to query for devices and to discover services.<br/>                                                                                                                                                                         |
| [Bluetooth and WSALookupServiceNext](bluetooth-and-wsalookupservicenext.md)                     | Bluetooth uses the [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta) function to match queries specified in a previous call to [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina).<br/>                                                                                                           |
| [Bluetooth and WSALookupServiceEnd](bluetooth-and-wsalookupserviceend.md)                       | Bluetooth uses the [**WSALookupServiceEnd**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupserviceend) function to terminate a query initiated in a previous call to [**WSALookupServiceBegin**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicebegina), and perhaps extended in subsequent calls to [**WSALookupServiceNext**](/windows/desktop/api/winsock2/nf-winsock2-wsalookupservicenexta).<br/> |
| [Bluetooth and WSAQUERYSET](bluetooth-and-wsaqueryset.md)                                       | The [**WSAQUERYSET**](/windows/desktop/api/winsock2/ns-winsock2-wsaquerysetw) structure is used in operations including device inquiry, service inquiry, and setting the service.<br/>                                                                                                                                                                |
| [Bluetooth and WSASetService](bluetooth-and-wsasetservice.md)                                   | Bluetooth uses the [**WSASetService**](/windows/desktop/api/winsock2/nf-winsock2-wsasetservicea) function to register or remove a service instance within the Bluetooth namespace (NS\_BTH) from the registry.<br/>                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> </dl>

 

