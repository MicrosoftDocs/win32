---
title: Bluetooth Programming with Windows Sockets
description: This section describes how to use Windows Sockets functions and structures to program a Bluetooth application.
ms.assetid: '0f15cb84-1d7a-4b64-86e8-b1b23c956c64'
keywords: ["Bluetooth, tasks", "Windows Sockets", "programming"]
---

# Bluetooth Programming with Windows Sockets

This section describes how to use Windows Sockets functions and structures to program a Bluetooth application. Complete reference information for the Windows Sockets API elements can be found in [Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673); this section provides only Bluetooth-specific information for each Windows Sockets programming element.

You can also download the [Bluetooth connection sample](http://go.microsoft.com/fwlink/p/?LinkID=331652) for a complete example.

As with all Windows Sockets application programming, the [**WSAStartup**](https://msdn.microsoft.com/library/windows/desktop/ms742213) function must be called to initiate Windows Sockets functionality and enable Bluetooth.

The following topics provide guidance in the use of Windows Sockets functions and structures with the Microsoft Bluetooth API:



| Topic                                                                                            | Description                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Bluetooth and accept](bluetooth-and-accept.md)                                                 | Bluetooth uses the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function to enable incoming connection attempts on a socket.<br/>                                                                                                                                                                                                  |
| [Bluetooth and bind](bluetooth-and-bind.md)                                                     | Bluetooth uses the [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function to bind to a socket.<br/>                                                                                                                                                                                                                                     |
| [Bluetooth and BLOB](bluetooth-and-blob.md)                                                     | Bluetooth uses the [**BLOB**](https://msdn.microsoft.com/library/windows/desktop/ms737551) structure to pass or receive transport-specific data to the [**WSAQUERYSET**](bluetooth-and-wsaqueryset-for-set-service.md) structure during calls to the [**WSASetService**](bluetooth-and-wsasetservice.md) or **WSALookupService**\* functions. <br/>             |
| [Bluetooth and connect](bluetooth-and-connect.md)                                               | Bluetooth uses the [**connect**](https://msdn.microsoft.com/library/windows/desktop/ms737625) function to connect to a target Bluetooth device, using a previously created Bluetooth socket.<br/>                                                                                                                                                              |
| [Bluetooth and getaddrinfo](bluetooth-and-getaddrinfo.md)                                       | The [**getaddrinfo**](https://msdn.microsoft.com/library/windows/desktop/ms738520) function provides translation from host name to address for IP-based transports.<br/>                                                                                                                                                                                   |
| [Bluetooth and getpeername](bluetooth-and-getpeername.md)                                       | Used to retrieve the Bluetooth address of the peer Bluetooth device.<br/>                                                                                                                                                                                                                                            |
| [Bluetooth and getsockname](bluetooth-and-getsockname.md)                                       | Bluetooth uses the [**getsockname**](https://msdn.microsoft.com/library/windows/desktop/ms738543) function to retrieve the server device address and port number allocated to a socket through a previous call to the [**bind**](https://msdn.microsoft.com/library/windows/desktop/ms737550) function.<br/>                                                                                            |
| [Bluetooth and getsockopt](bluetooth-and-getsockopt.md)                                         | Bluetooth uses the [**getsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms738544) function to query various parameters associated with the server channel or the connection. <br/>                                                                                                                                                           |
| [Bluetooth and listen, select, and closesocket](bluetooth-and-listen-select-and-closesocket.md) | Bluetooth uses the [**listen**](https://msdn.microsoft.com/library/windows/desktop/ms739168), [**select**](https://msdn.microsoft.com/library/windows/desktop/ms740141), and [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) functions without any modification from standard Windows Sockets programming.<br/>                                                                                                   |
| [Bluetooth and read or write operations](bluetooth-and-read-or-write-operations.md)             | Details the supported Winsock read and write operations.<br/>                                                                                                                                                                                                                                                        |
| [Bluetooth and setsockopt](bluetooth-and-setsockopt.md)                                         | Bluetooth uses the [**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476) function to set various parameters associated with the server channel or the connection.<br/>                                                                                                                                                              |
| [Bluetooth and shutdown](bluetooth-and-shutdown.md)                                             | Bluetooth uses the [**shutdown**](https://msdn.microsoft.com/library/windows/desktop/ms740481) function to disconnect from the remote radio.<br/>                                                                                                                                                                                                             |
| [Bluetooth and socket](bluetooth-and-socket.md)                                                 | Bluetooth uses the [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function creates a socket for incoming or outgoing connections.<br/>                                                                                                                                                                                               |
| [Bluetooth and Socket Options](bluetooth-and-socket-options.md)                                 | Details the socket options supported by Microsoft Bluetooth.<br/>                                                                                                                                                                                                                                                    |
| [Bluetooth and WSAAddressToString](bluetooth-and-wsaaddresstostring.md)                         | Used to convert a Bluetooth Device Address to a string, which is in turn provided to the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function via the [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure when retrieving device service information.<br/>                                           |
| [Bluetooth and WSALookupServiceBegin](bluetooth-and-wsalookupservicebegin.md)                   | Bluetooth uses the [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633) function to query for devices and to discover services.<br/>                                                                                                                                                                         |
| [Bluetooth and WSALookupServiceNext](bluetooth-and-wsalookupservicenext.md)                     | Bluetooth uses the [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641) function to match queries specified in a previous call to [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633).<br/>                                                                                                           |
| [Bluetooth and WSALookupServiceEnd](bluetooth-and-wsalookupserviceend.md)                       | Bluetooth uses the [**WSALookupServiceEnd**](https://msdn.microsoft.com/library/windows/desktop/ms741637) function to terminate a query initiated in a previous call to [**WSALookupServiceBegin**](https://msdn.microsoft.com/library/windows/desktop/ms741633), and perhaps extended in subsequent calls to [**WSALookupServiceNext**](https://msdn.microsoft.com/library/windows/desktop/ms741641).<br/> |
| [Bluetooth and WSAQUERYSET](bluetooth-and-wsaqueryset.md)                                       | The [**WSAQUERYSET**](https://msdn.microsoft.com/library/windows/desktop/ms741679) structure is used in operations including device inquiry, service inquiry, and setting the service.<br/>                                                                                                                                                                |
| [Bluetooth and WSASetService](bluetooth-and-wsasetservice.md)                                   | Bluetooth uses the [**WSASetService**](https://msdn.microsoft.com/library/windows/desktop/ms742211) function to register or remove a service instance within the Bluetooth namespace (NS\_BTH) from the registry.<br/>                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> </dl>

 

 





