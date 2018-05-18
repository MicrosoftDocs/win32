---
title: Bluetooth and listen, select, and closesocket
description: Bluetooth uses the listen, select, and closesocket functions without any modification from standard Windows Sockets programming.
ms.assetid: 'b64440de-bc63-4e3b-bfd9-5cf783f36c23'
keywords: ["Bluetooth", "closesocket", "listen", "select", "Bluetooth and listen", "Bluetooth and listen,select", "Bluetooth and listen,select,and closesocket", "listen"]
---

# Bluetooth and listen, select, and closesocket

Bluetooth uses the [**listen**](https://msdn.microsoft.com/library/windows/desktop/ms739168), [**select**](https://msdn.microsoft.com/library/windows/desktop/ms740141), and [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) functions without any modification from standard Windows Sockets programming.

As with Windows Sockets, the [**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582) function frees resources associated with the socket.

When calling the [**listen**](https://msdn.microsoft.com/library/windows/desktop/ms739168) function, it is strongly recommended that a low value is used for the *backlog* parameter (typically 2 to 4), since only a few client connections are accepted. This reduces the system resources that are allocated for use by the listening socket.

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> <dt>

[**closesocket**](https://msdn.microsoft.com/library/windows/desktop/ms737582)
</dt> <dt>

[**listen**](https://msdn.microsoft.com/library/windows/desktop/ms739168)
</dt> <dt>

[**select**](https://msdn.microsoft.com/library/windows/desktop/ms740141)
</dt> </dl>

 

 




