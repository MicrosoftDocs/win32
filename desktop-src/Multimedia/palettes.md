---
title: Palettes
description: Palettes
ms.assetid: ee048f9a-3036-40dc-a6d7-f612b9ef767c
keywords:
- DrawDib,palettes
- DrawDibRealize function
- DrawDibDraw function
- DrawDibSetPalette function
- DrawDibGetPalette function
- DrawDibChangePalette function
ms.topic: article
ms.date: 05/31/2018
---

# Palettes

The DrawDib functions require that an application respond to two palette-oriented messages: [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) and [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged). If your application is not palette-aware, you will need to add a handler for each of these messages. For more information about processing the **WM\_QUERYNEWPALETTE** and **WM\_PALETTECHANGED** messages, see [Adding Palette Message Handlers](adding-palette-message-handlers.md).

You can realize the current DrawDib palette to the DC by using the [**DrawDibRealize**](/windows/desktop/api/Vfw/nf-vfw-drawdibrealize) function. You should realize the palette in response to the [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) or [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged) message, or when you prepare to display an image sequence by using the [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) function.

You can draw an image mapped to another palette by using the [**DrawDibSetPalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibsetpalette) function. This function forces the DrawDib DC to use the specified palette, which can affect the image quality. For example, an application that is palette-aware might have realized a palette and needs to prevent DrawDib from realizing its own palette. The application can use **DrawDibSetPalette** to notify DrawDib of the palette to use.

You can obtain a handle of the current foreground palette by using the [**DrawDibGetPalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibgetpalette) function. If your application uses the current foreground palette, it does not have exclusive use of the palette and another application can invalidate the palette handle. Your application should not free the palette when you finish using it. Freeing the palette could invalidate the palette handle for another application.

You can prepare DrawDib to receive new color values for its palette by using the [**DrawDibChangePalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibchangepalette) function. In the code following **DrawDibChangePalette**, you assign new values for the palette color table. If the **DDF\_ANIMATE** flag is not set in the DrawDib DC when you call **DrawDibChangePalette**, you can enact the palette changes by using [**DrawDibRealize**](/windows/desktop/api/Vfw/nf-vfw-drawdibrealize) to realize the palette. You can then use [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) to redraw the image. If the **DDF\_ANIMATE** flag is set in the DrawDib DC, you can animate the palette and the colors of the displayed bitmap by using **DrawDibDraw** or **DrawDibRealize**. You can update the **DDF\_ANIMATE** flag by using the [**DrawDibEnd**](/windows/desktop/api/Vfw/nf-vfw-drawdibend) and [**DrawDibBegin**](/windows/desktop/api/Vfw/nf-vfw-drawdibbegin) functions.

> [!Note]  
> If you free the DrawDib palette while it is selected by a DC, a graphics device interface (GDI) error can result when the DC uses the palette. Instead, your application should use [**DrawDibSetPalette**](/windows/desktop/api/Vfw/nf-vfw-drawdibsetpalette) to change the DrawDib DC to use the default palette or another palette.

 

The [**DrawDibEnd**](/windows/desktop/api/Vfw/nf-vfw-drawdibend), [**DrawDibClose**](/windows/desktop/api/Vfw/nf-vfw-drawdibclose), and [**DrawDibBegin**](/windows/desktop/api/Vfw/nf-vfw-drawdibbegin) functions can free the DrawDib palette. However, these functions should be used only when the palette has not been selected by the DC. The DrawDibDraw function can also free the palette when it uses the same DrawDib DC, but specifies different drawing parameters (*lpbi*, *dxDst*, *dyDst*, *dxSrc*, or *dySrc*) or a different format.

## Related topics

<dl> <dt>

[Image Rendering](image-rendering.md)
</dt> </dl>

 

 