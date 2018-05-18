---
title: Asynchronous Operations
description: When RasDial is invoked as an asynchronous operation, the function returns immediately.
ms.assetid: 'f165b4a7-00fb-4888-8225-8fd106e113f2'
---

# Asynchronous Operations

When [**RasDial**](rasdial.md) is invoked as an asynchronous operation, the function returns immediately. In asynchronous mode, the **RasDial** call must specify a [notification handler](notification-handlers.md) that the Remote Access Connection Manager uses to inform the client whenever the connection operation changes states or an error occurs.

The notification handler can be a window to receive messages, or a [**RasDialFunc**](rasdialfunc.md), [**RasDialFunc1**](rasdialfunc1.md), or [**RasDialFunc2**](rasdialfunc2.md) callback function. The Remote Access Connection Manager makes its asynchronous notifications in the context of the thread that made the [**RasDial**](rasdial.md) call. For this reason, the calling thread must not terminate until the connection operation has been successfully established or an error occurs. As in synchronous mode, the client application can safely terminate once the connection has been established, and it must [shut down the connection operation](disconnecting.md) if an error occurs.

 

 




