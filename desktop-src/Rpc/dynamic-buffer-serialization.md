---
title: Dynamic Buffer Serialization
description: When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.
ms.assetid: 'd2c3805b-47bf-4bca-b904-9414e26dde68'
---

# Dynamic Buffer Serialization

When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.

The dynamic buffer style of serialization uses the following routines:

-   [**MesEncodeDynBufferHandleCreate**](mesencodedynbufferhandlecreate.md)
-   [**MesDecodeBufferHandleCreate**](mesdecodebufferhandlecreate.md)
-   [**MesBufferHandleReset**](mesbufferhandlereset.md)
-   [**MesHandleFree**](meshandlefree.md)

The [**MesEncodeDynBufferHandleCreate**](mesencodedynbufferhandlecreate.md) function allocates the memory needed for the encoding handle and then initializes it. The application can call [**MesBufferHandleReset**](mesbufferhandlereset.md) to reinitialize the handle. It calls [**MesHandleFree**](meshandlefree.md) to free the handle's memory. To create a decoding handle corresponding to the dynamic buffer encoding handle, use [**MesDecodeBufferHandleCreate**](mesdecodebufferhandlecreate.md).

 

 




