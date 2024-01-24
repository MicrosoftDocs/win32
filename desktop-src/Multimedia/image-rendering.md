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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Image Rendering

\[The feature associated with this page, [DrawDib](/windows/win32/multimedia/drawdib), is a legacy feature. It has been superseded by [MediaComposition class](/uwp/api/Windows.Media.Editing.MediaComposition). **MediaComposition class** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaComposition class** instead of **DrawDib**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

After you call [**DrawDibOpen**](/windows/desktop/api/Vfw/nf-vfw-drawdibopen) to create a DrawDib DC (see [DrawDib Operations](drawdib-operations.md)), you can draw a DIB to the screen by using the [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) function. **DrawDibDraw** dithers true-color bitmaps when displaying them with 8-bit display adapters.

[**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) also supports video compressors transparently when displaying compressed bitmaps. You can access the buffer that contains the decompressed image by using the [**DrawDibGetBuffer**](/windows/desktop/api/Vfw/nf-vfw-drawdibgetbuffer) function. **DrawDibGetBuffer** returns **NULL** when drawing an uncompressed bitmap. You should prepare your application to handle compressed and uncompressed bitmaps.

You can refresh an image or a portion of an image displayed by your application by using the [**DrawDibUpdate**](/windows/desktop/api/Vfw/nf-vfw-drawdibupdate) macro.

## Related topics

<dl> <dt>

[About the DrawDib Functions](about-the-drawdib-functions.md)
</dt> </dl>

 

 




