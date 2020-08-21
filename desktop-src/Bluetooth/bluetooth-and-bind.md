---
title: Bluetooth and bind
description: Bluetooth uses the bind function to bind to a socket.
ms.assetid: 308d2680-de51-49e6-a0da-7aba494d9572
keywords:
- bind
- Bluetooth
- Bluetooth
- Bluetooth and bind
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and bind

Bluetooth uses the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function to bind to a socket. To bind a Bluetooth socket, call the **bind** function using the [**SOCKADDR\_BTH**](/windows/desktop/api/Ws2bth/ns-ws2bth-sockaddr_bth) structure. Use the **SOCKADDR\_BTH** structure with the following settings:

``` syntax
name.addressFamily = AF_BTH;
name.btAddr = 0;
name.serviceClassId = GUID_NULL;
name.port = number of service channel, 0 or BT_PORT_ANY;
```

On client applications, the port member must be zero to enable an appropriate local endpoint to be assigned. On server applications, the port member must be a valid port number or BT\_PORT\_ANY; ports automatically assigned using BT\_PORT\_ANY may be queried subsequently with a call to the [**getsockname**](bluetooth-and-getsockname.md) function. The valid range for requesting a specific RFCOMM port is 1 through 30. Server channels are global resource, and only 30 server channels are available for RFCOMM on any Bluetooth device, which must be shared by all Windows Sockets that belong to the Bluetooth address family. If no server channel is available, or if the specified server channel is already reserved, the [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) call fails.

Upon successful return from bind, the server channel is reserved until the socket is closed. Use the [**getsockname**](bluetooth-and-getsockname.md) function to retrieve the channel number for SDP registration.

Applications should use auto-allocation for the server channel.

The [**bind**](/windows/desktop/api/winsock/nf-winsock-bind) function does not automatically advertise the server application using the Bluetooth SDP; applications must call the [**WSASetService**](/windows/desktop/api/winsock2/nf-winsock2-wsasetservicea) function to be found by remote Bluetooth applications.

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**bind**](/windows/desktop/api/winsock/nf-winsock-bind)
</dt> </dl>

 

 