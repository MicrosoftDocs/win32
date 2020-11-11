---
title: Thread Safety
description: All functions in this API are safe to call concurrently from different threads. However, each object passed as a parameter to the functions have specific threading behavior, as described below.
ms.assetid: 712d6750-884e-421a-8ecf-efcd4ec9b21d
keywords:
- Thread Safety Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Thread Safety

All functions in this API are safe to call concurrently from different threads. However, each object passed as a parameter to the functions have specific threading behavior, as described below.


The following handles are single threaded and do not support concurrent operations for a particular instance:

-   [WS\_HEAP](ws-heap.md)
-   [WS\_MESSAGE](ws-message.md)
-   [WS\_XML\_BUFFER](ws-xml-buffer.md)
-   [WS\_XML\_READER](ws-xml-reader.md)
-   [WS\_XML\_WRITER](ws-xml-writer.md)
-   [WS\_ERROR](ws-error.md)
-   [WS\_OPERATION\_CONTEXT](ws-operation-context.md)
-   [WS\_POLICY](ws-policy.md)
-   [WS\_METADATA](ws-metadata.md)
-   [WS\_SECURITY\_TOKEN](ws-security-token.md)
-   [WS\_SECURITY\_CONTEXT](ws-security-context.md)

The following handles are free threaded and do support concurrent operations for a particular instance:

-   [WS\_CHANNEL](ws-channel.md)
-   [WS\_LISTENER](ws-listener.md)
-   [WS\_SERVICE\_HOST](ws-service-host.md)
-   [WS\_SERVICE\_PROXY](ws-service-proxy.md)

For all these handles, threading is defined in terms of operations (not function calls). An operation is defined differently for functions invoked synchronously versus functions invoked asynchronously:

-   For functions invoked synchronously, the operation is pending during the execution of the function.
-   For functions invoked asynchronously, if the function returns a return code other than **WS\_S\_ASYNC** the operation is pending during the execution of the function. If the function returns **WS\_S\_ASYNC** , however, the operation is pending until the [**WS\_ASYNC\_CALLBACK**](/windows/desktop/api/WebServices/nc-webservices-ws_async_callback) is invoked. For more information about invoking functions asynchronously, see the [Asynchronous Model](asynchronous-model.md) topic. For error codes, see [Windows Web Services Return Values](windows-web-services-return-values.md).

Failure to follow the threading contract for an object will result in undefined behavior.

 

 




