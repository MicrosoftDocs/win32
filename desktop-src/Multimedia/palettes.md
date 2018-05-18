---
title: Palettes
description: Palettes
ms.assetid: 'ee048f9a-3036-40dc-a6d7-f612b9ef767c'
keywords: ["DrawDib,palettes", "DrawDibRealize function", "DrawDibDraw function", "DrawDibSetPalette function", "DrawDibGetPalette function", "DrawDibChangePalette function"]
---

# Palettes

The DrawDib functions require that an application respond to two palette-oriented messages: [**WM\_QUERYNEWPALETTE**](https://msdn.microsoft.com/library/windows/desktop/dd145218) and [**WM\_PALETTECHANGED**](https://msdn.microsoft.com/library/windows/desktop/dd145214). If your application is not palette-aware, you will need to add a handler for each of these messages. For more information about processing the **WM\_QUERYNEWPALETTE** and **WM\_PALETTECHANGED** messages, see [Adding Palette Message Handlers](adding-palette-message-handlers.md).

You can realize the current DrawDib palette to the DC by using the [**DrawDibRealize**](drawdibrealize.md) function. You should realize the palette in response to the [**WM\_QUERYNEWPALETTE**](https://msdn.microsoft.com/library/windows/desktop/dd145218) or [**WM\_PALETTECHANGED**](https://msdn.microsoft.com/library/windows/desktop/dd145214) message, or when you prepare to display an image sequence by using the [**DrawDibDraw**](drawdibdraw.md) function.

You can draw an image mapped to another palette by using the [**DrawDibSetPalette**](drawdibsetpalette.md) function. This function forces the DrawDib DC to use the specified palette, which can affect the image quality. For example, an application that is palette-aware might have realized a palette and needs to prevent DrawDib from realizing its own palette. The application can use **DrawDibSetPalette** to notify DrawDib of the palette to use.

You can obtain a handle of the current foreground palette by using the [**DrawDibGetPalette**](drawdibgetpalette.md) function. If your application uses the current foreground palette, it does not have exclusive use of the palette and another application can invalidate the palette handle. Your application should not free the palette when you finish using it. Freeing the palette could invalidate the palette handle for another application.

You can prepare DrawDib to receive new color values for its palette by using the [**DrawDibChangePalette**](drawdibchangepalette.md) function. In the code following **DrawDibChangePalette**, you assign new values for the palette color table. If the **DDF\_ANIMATE** flag is not set in the DrawDib DC when you call **DrawDibChangePalette**, you can enact the palette changes by using [**DrawDibRealize**](drawdibrealize.md) to realize the palette. You can then use [**DrawDibDraw**](drawdibdraw.md) to redraw the image. If the **DDF\_ANIMATE** flag is set in the DrawDib DC, you can animate the palette and the colors of the displayed bitmap by using **DrawDibDraw** or **DrawDibRealize**. You can update the **DDF\_ANIMATE** flag by using the [**DrawDibEnd**](drawdibend.md) and [**DrawDibBegin**](drawdibbegin.md) functions.

> [!Note]  
> If you free the DrawDib palette while it is selected by a DC, a graphics device interface (GDI) error can result when the DC uses the palette. Instead, your application should use [**DrawDibSetPalette**](drawdibsetpalette.md) to change the DrawDib DC to use the default palette or another palette.

 

The [**DrawDibEnd**](drawdibend.md), [**DrawDibClose**](drawdibclose.md), and [**DrawDibBegin**](drawdibbegin.md) functions can free the DrawDib palette. However, these functions should be used only when the palette has not been selected by the DC. The DrawDibDraw function can also free the palette when it uses the same DrawDib DC, but specifies different drawing parameters (*lpbi*, *dxDst*, *dyDst*, *dxSrc*, or *dySrc*) or a different format.

## Related topics

<dl> <dt>

[Image Rendering](image-rendering.md)
</dt> </dl>

 

 




