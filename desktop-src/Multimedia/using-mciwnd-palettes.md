---
title: Using MCIWnd Palettes
description: Using MCIWnd Palettes
ms.assetid: 2b99ca57-f321-4286-8ebf-ae3344d8d2c9
keywords:
- MCIWndGetPalette macro
- MCIWndSetPalette macro
- MCIWndRealize macro
ms.topic: article
ms.date: 05/31/2018
---

# Using MCIWnd Palettes

Playing video clips with 8-bit color depth (256-color capacity) requires a palette to define the colors being used. Sometimes, the palette included with a video clip is not the most appropriate palette to use during playback. In this case, MCIWnd provides three ways to manage palettes for playback:

-   Retrieve a handle to the palette associated with an MCIWnd window by using the [**MCIWndGetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndgetpalette) macro. The palette is not necessarily associated exclusively with the MCIWnd window. Other applications can access, and even invalidate, the palette handle. Consequently, your application should anticipate the global use of the palette and, when finished with the palette, should not free it.
-   Specify a new palette to use with the video clip associated with an MCIWnd window by using the [**MCIWndSetPalette**](/windows/desktop/api/Vfw/nf-vfw-mciwndsetpalette) macro.
-   Realize the palette associated with an MCIWnd window to the system palette by using the [**MCIWndRealize**](/windows/desktop/api/Vfw/nf-vfw-mciwndrealize) macro. This macro calls the [**RealizePalette**](/windows/desktop/api/wingdi/nf-wingdi-realizepalette) function with the palette associated with the MCIWnd window. If your application message handlers for [**WM\_PALETTECHANGED**](/windows/desktop/gdi/wm-palettechanged) and [**WM\_QUERYNEWPALETTE**](/windows/desktop/gdi/wm-querynewpalette) call only **RealizePalette** or **MCIWndRealize**, you must forward these messages to MCIWnd if you do not handle them yourself.

> [!Note]  
> When a video clip with 8-bit color depth is loaded into the MCIWnd window, the palette included with that clip replaces the palette associated with the MCIWnd window.

 

## Related topics

<dl> <dt>

[Playback Enhancements](playback-enhancements.md)
</dt> </dl>

 

 