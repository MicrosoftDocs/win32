---
title: Dynamic Buffer Serialization
description: When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.
ms.assetid: d2c3805b-47bf-4bca-b904-9414e26dde68
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Buffer Serialization

When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.

The dynamic buffer style of serialization uses the following routines:

-   [**MesEncodeDynBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesencodedynbufferhandlecreate)
-   [**MesDecodeBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodebufferhandlecreate)
-   [**MesBufferHandleReset**](/windows/desktop/api/Midles/nf-midles-mesbufferhandlereset)
-   [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree)

The [**MesEncodeDynBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesencodedynbufferhandlecreate) function allocates the memory needed for the encoding handle and then initializes it. The application can call [**MesBufferHandleReset**](/windows/desktop/api/Midles/nf-midles-mesbufferhandlereset) to reinitialize the handle. It calls [**MesHandleFree**](/windows/desktop/api/Midles/nf-midles-meshandlefree) to free the handle's memory. To create a decoding handle corresponding to the dynamic buffer encoding handle, use [**MesDecodeBufferHandleCreate**](/windows/desktop/api/Midles/nf-midles-mesdecodebufferhandlecreate).

 

 




