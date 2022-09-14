---
title: Image Rendering
description: Image Rendering
ms.assetid: de87f288-f1bd-471c-b594-e9dbde3cff0a
keywords:
- DrawDib,image rendering
- DrawDib,drawing DIBs
- DrawDibDraw function
- DrawDibGetBuffer function
- DrawDibUpdate function
ms.topic: article
ms.date: 05/31/2018
---

# Image Rendering

After you call [**DrawDibOpen**](/windows/desktop/api/Vfw/nf-vfw-drawdibopen) to create a DrawDib DC (see [DrawDib Operations](drawdib-operations.md)), you can draw a DIB to the screen by using the [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) function. **DrawDibDraw** dithers true-color bitmaps when displaying them with 8-bit display adapters.

[**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) also supports video compressors transparently when displaying compressed bitmaps. You can access the buffer that contains the decompressed image by using the [**DrawDibGetBuffer**](/windows/desktop/api/Vfw/nf-vfw-drawdibgetbuffer) function. **DrawDibGetBuffer** returns **NULL** when drawing an uncompressed bitmap. You should prepare your application to handle compressed and uncompressed bitmaps.

You can refresh an image or a portion of an image displayed by your application by using the [**DrawDibUpdate**](/windows/desktop/api/Vfw/nf-vfw-drawdibupdate) macro.

## Related topics

<dl> <dt>

[About the DrawDib Functions](about-the-drawdib-functions.md)
</dt> </dl>

 

 




