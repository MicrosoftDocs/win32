---
title: Image Rendering
description: Image Rendering
ms.assetid: 'de87f288-f1bd-471c-b594-e9dbde3cff0a'
keywords: ["DrawDib,image rendering", "DrawDib,drawing DIBs", "DrawDibDraw function", "DrawDibGetBuffer function", "DrawDibUpdate function"]
---

# Image Rendering

After you call [**DrawDibOpen**](drawdibopen.md) to create a DrawDib DC (see [DrawDib Operations](drawdib-operations.md)), you can draw a DIB to the screen by using the [**DrawDibDraw**](drawdibdraw.md) function. **DrawDibDraw** dithers true-color bitmaps when displaying them with 8-bit display adapters.

[**DrawDibDraw**](drawdibdraw.md) also supports video compressors transparently when displaying compressed bitmaps. You can access the buffer that contains the decompressed image by using the [**DrawDibGetBuffer**](drawdibgetbuffer.md) function. **DrawDibGetBuffer** returns **NULL** when drawing an uncompressed bitmap. You should prepare your application to handle compressed and uncompressed bitmaps.

You can refresh an image or a portion of an image displayed by your application by using the [**DrawDibUpdate**](drawdibupdate.md) macro.

## Related topics

<dl> <dt>

[About the DrawDib Functions](about-the-drawdib-functions.md)
</dt> </dl>

 

 




