---
title: Adding Palette Message Handlers
description: Adding Palette Message Handlers
ms.assetid: bfd77f42-6a9d-4195-b1a0-1688e44358e3
keywords:
- DrawDib,palettes
- DrawDibRealize function
- DrawDibDraw function
ms.topic: article
ms.date: 05/31/2018
---

# Adding Palette Message Handlers

The following example illustrates simple message handlers for the [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged) and [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) messages. The example uses the [**DrawDibRealize**](/windows/desktop/api/Vfw/nf-vfw-drawdibrealize) function to process the **WM\_QUERYNEWPALETTE** message.

Your application should respond to the [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) message by invalidating the destination window to let the [**DrawDibDraw**](/windows/desktop/api/Vfw/nf-vfw-drawdibdraw) function redraw an image. You should respond to the [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged) message by using the [**DrawDibRealize**](/windows/desktop/api/Vfw/nf-vfw-drawdibrealize) function to realize the palette.


```C++
case WM_PALETTECHANGED: 
    if ((HWND)wParam == hwnd) 
        break; 
case WM_QUERYNEWPALETTE: 
    hdc = GetDC(hwnd); 
    f = DrawDibRealize(hdd, hdc, FALSE) > 0; 
    ReleaseDC(hwnd, hdc); 
    if (f) 
        InvalidateRect(hwnd, NULL, TRUE); 
    break; 

```



## Related topics

<dl> <dt>

[Using DrawDib](using-drawdib.md)
</dt> </dl>

 

 