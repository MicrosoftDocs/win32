---
title: Bluetooth and socket
description: Creates a socket for incoming or outgoing connections.
ms.assetid: '21b9cf1f-1a85-4a4b-9557-faa4f32c3696'
keywords: ["Bluetooth Bluetooth", "socket Bluetooth", "Bluetooth and socket Bluetooth"]
---

# Bluetooth and socket

The [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function creates a socket for incoming or outgoing connections.:

To create a socket using Bluetooth, use the following settings:

-   The *af* parameter of the [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function is always set to **AF\_BTH** for Bluetooth sockets.
-   The *type* parameter of the [**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506) function is always **SOCK\_STREAM**; **SOCK\_DGRAM** sockets are not supported by Bluetooth.
-   For the *protocol* parameter, **BTHPROTO\_RFCOMM** is the supported protocol.

For more information, see [Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673).

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> <dt>

[**socket**](https://msdn.microsoft.com/library/windows/desktop/ms740506)
</dt> </dl>

 

 




