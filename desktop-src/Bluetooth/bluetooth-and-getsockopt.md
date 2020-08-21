---
title: Bluetooth and getsockopt
description: Bluetooth uses the getsockopt function to query various parameters associated with the server channel or the connection.
ms.assetid: 9593fd6c-b55d-45d8-a9d9-87ebcd09d1bd
keywords:
- Bluetooth
- getsockopt
- Bluetooth and getsockopt
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and getsockopt

Bluetooth uses the [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) function to query various parameters associated with the server channel or the connection. Use of **getsockopt** with Bluetooth has the following requirements:

-   The *s* parameter of [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) must be a valid Bluetooth socket.
-   The *level* parameter of [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) must be SOL\_RFCOMM.

For a listing of available Bluetooth socket options, see [Bluetooth and Socket Options](bluetooth-and-socket-options.md).

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt)
</dt> </dl>

 

 