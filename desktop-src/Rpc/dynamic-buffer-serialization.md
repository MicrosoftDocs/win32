---
title: Dynamic Buffer Serialization
description: When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.
ms.assetid: d2c3805b-47bf-4bca-b904-9414e26dde68
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dynamic Buffer Serialization

When using the dynamic buffer style of serialization, the marshalling buffer is allocated by the stub, and the data is encoded into this buffer and passed back to you. When unmarshaling, you supply the buffer that contains the data.

The dynamic buffer style of serialization uses the following routines:

-   [**MesEncodeDynBufferHandleCreate**](/windows/win32/Midles/nf-midles-mesencodedynbufferhandlecreate?branch=master)
-   [**MesDecodeBufferHandleCreate**](/windows/win32/Midles/nf-midles-mesdecodebufferhandlecreate?branch=master)
-   [**MesBufferHandleReset**](/windows/win32/Midles/nf-midles-mesbufferhandlereset?branch=master)
-   [**MesHandleFree**](/windows/win32/Midles/nf-midles-meshandlefree?branch=master)

The [**MesEncodeDynBufferHandleCreate**](/windows/win32/Midles/nf-midles-mesencodedynbufferhandlecreate?branch=master) function allocates the memory needed for the encoding handle and then initializes it. The application can call [**MesBufferHandleReset**](/windows/win32/Midles/nf-midles-mesbufferhandlereset?branch=master) to reinitialize the handle. It calls [**MesHandleFree**](/windows/win32/Midles/nf-midles-meshandlefree?branch=master) to free the handle's memory. To create a decoding handle corresponding to the dynamic buffer encoding handle, use [**MesDecodeBufferHandleCreate**](/windows/win32/Midles/nf-midles-mesdecodebufferhandlecreate?branch=master).

 

 




