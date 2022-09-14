---
title: Bluetooth and socket
description: Creates a socket for incoming or outgoing connections.
ms.assetid: 21b9cf1f-1a85-4a4b-9557-faa4f32c3696
keywords:
- Bluetooth Bluetooth
- socket Bluetooth
- Bluetooth and socket Bluetooth
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and socket

The [**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket) function creates a socket for incoming or outgoing connections.:

To create a socket using Bluetooth, use the following settings:

-   The *af* parameter of the [**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket) function is always set to **AF\_BTH** for Bluetooth sockets.
-   The *type* parameter of the [**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket) function is always **SOCK\_STREAM**; **SOCK\_DGRAM** sockets are not supported by Bluetooth.
-   For the *protocol* parameter, **BTHPROTO\_RFCOMM** is the supported protocol.

For more information, see [Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2).

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**socket**](/windows/desktop/api/winsock2/nf-winsock2-socket)
</dt> </dl>

 

 