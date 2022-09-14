---
title: Bluetooth and listen, select, and closesocket
description: Bluetooth uses the listen, select, and closesocket functions without any modification from standard Windows Sockets programming.
ms.assetid: b64440de-bc63-4e3b-bfd9-5cf783f36c23
keywords:
- Bluetooth
- closesocket
- listen
- select
- Bluetooth and listen
- Bluetooth and listen,select
- Bluetooth and listen,select,and closesocket
- listen
ms.topic: article
ms.date: 05/31/2018
---

# Bluetooth and listen, select, and closesocket

Bluetooth uses the [**listen**](/windows/desktop/api/winsock2/nf-winsock2-listen), [**select**](/windows/desktop/api/winsock2/nf-winsock2-select), and [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) functions without any modification from standard Windows Sockets programming.

As with Windows Sockets, the [**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket) function frees resources associated with the socket.

When calling the [**listen**](/windows/desktop/api/winsock2/nf-winsock2-listen) function, it is strongly recommended that a low value is used for the *backlog* parameter (typically 2 to 4), since only a few client connections are accepted. This reduces the system resources that are allocated for use by the listening socket.

## Related topics

<dl> <dt>

[Windows Sockets](/windows/desktop/WinSock/windows-sockets-start-page-2)
</dt> <dt>

[**closesocket**](/windows/desktop/api/winsock/nf-winsock-closesocket)
</dt> <dt>

[**listen**](/windows/desktop/api/winsock2/nf-winsock2-listen)
</dt> <dt>

[**select**](/windows/desktop/api/winsock2/nf-winsock2-select)
</dt> </dl>

 

 