---
title: Bluetooth and setsockopt
description: Bluetooth uses the setsockopt function to set various parameters associated with the server channel or the connection.
ms.assetid: 'ab78baed-5556-4d7b-88a6-e3ceb93afa8c'
keywords: ["Bluetooth", "setsockopt", "Bluetooth and setsockopt"]
---

# Bluetooth and setsockopt

Bluetooth uses the [**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476) function to set various parameters associated with the server channel or the connection. Use of **setsockopt** with Bluetooth has the following requirements:

-   The *s* parameter of [**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476) must be a valid Bluetooth socket.
-   The *level* parameter of [**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476) must be SOL\_RFCOMM.

For a listing of available Bluetooth socket options, see [Bluetooth and Socket Options](bluetooth-and-socket-options.md).

## Related topics

<dl> <dt>

[Windows Sockets](https://msdn.microsoft.com/library/windows/desktop/ms740673)
</dt> <dt>

[**setsockopt**](https://msdn.microsoft.com/library/windows/desktop/ms740476)
</dt> </dl>

 

 




