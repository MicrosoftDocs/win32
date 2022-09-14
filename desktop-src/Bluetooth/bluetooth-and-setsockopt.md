---
title: Bluetooth and setsockopt
description: Bluetooth uses the setsockopt function to set various parameters associated with the server channel or the connection.
ms.assetid: ab78baed-5556-4d7b-88a6-e3ceb93afa8c
keywords:
- Bluetooth
- setsockopt
- Bluetooth and setsockopt
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and setsockopt

Bluetooth uses the [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) function to set various parameters associated with the server channel or the connection. Use of **setsockopt** with Bluetooth has the following requirements:

-   The *s* parameter of [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) must be a valid Bluetooth socket.
-   The *level* parameter of [**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt) must be SOL\_RFCOMM.

For a listing of available Bluetooth socket options, see [Bluetooth and Socket Options](bluetooth-and-socket-options.md).

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**setsockopt**](/windows/desktop/api/winsock/nf-winsock-setsockopt)
</dt> </dl>

 

 