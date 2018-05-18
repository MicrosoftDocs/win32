---
title: Bluetooth and accept
description: Bluetooth uses the accept function to enable incoming connection attempts on a socket.
ms.assetid: '79708118-2f70-4759-b5d6-cf5cfc33c27e'
keywords: ["accept", "Bluetooth", "Bluetooth", "Bluetooth and accept"]
---

# Bluetooth and accept

Bluetooth uses the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function to enable incoming connection attempts on a socket. The BTH\_ADDR of the client application is obtained by reading the Bluetooth transport-specific section of the returned [**sockaddr**](https://msdn.microsoft.com/library/windows/desktop/ms740496) structure. Use of the **accept** function with Bluetooth has the following format:

-   The *addr* parameter of the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function is an optional pointer to a buffer that receives the address of the connecting entity, as known to the communications layer. A pointer to a [**SOCKADDR\_BTH**](sockaddr-bth.md) structure with the remote Bluetooth device address is returned.
-   The *addrlen* parameter of the [**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526) function is an optional pointer to an integer that contains the length, in bytes, of addr. The integer must be greater or equal to the value of **sizeof** ([**SOCKADDR\_BTH**](sockaddr-bth.md)).

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> <dt>

[**accept**](https://msdn.microsoft.com/library/windows/desktop/ms737526)
</dt> </dl>

 

 




