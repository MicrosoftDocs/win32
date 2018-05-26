---
title: Using MCIWnd Palettes
description: Using MCIWnd Palettes
ms.assetid: 2b99ca57-f321-4286-8ebf-ae3344d8d2c9
keywords:
- MCIWndGetPalette macro
- MCIWndSetPalette macro
- MCIWndRealize macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using MCIWnd Palettes

Playing video clips with 8-bit color depth (256-color capacity) requires a palette to define the colors being used. Sometimes, the palette included with a video clip is not the most appropriate palette to use during playback. In this case, MCIWnd provides three ways to manage palettes for playback:

-   Retrieve a handle to the palette associated with an MCIWnd window by using the [**MCIWndGetPalette**](/windows/win32/Vfw/nf-vfw-mciwndgetpalette?branch=master) macro. The palette is not necessarily associated exclusively with the MCIWnd window. Other applications can access, and even invalidate, the palette handle. Consequently, your application should anticipate the global use of the palette and, when finished with the palette, should not free it.
-   Specify a new palette to use with the video clip associated with an MCIWnd window by using the [**MCIWndSetPalette**](/windows/win32/Vfw/nf-vfw-mciwndsetpalette?branch=master) macro.
-   Realize the palette associated with an MCIWnd window to the system palette by using the [**MCIWndRealize**](/windows/win32/Vfw/nf-vfw-mciwndrealize?branch=master) macro. This macro calls the [**RealizePalette**](https://msdn.microsoft.com/library/windows/desktop/dd162896) function with the palette associated with the MCIWnd window. If your application message handlers for [**WM\_PALETTECHANGED**](https://msdn.microsoft.com/library/windows/desktop/dd145214) and [**WM\_QUERYNEWPALETTE**](https://msdn.microsoft.com/library/windows/desktop/dd145218) call only **RealizePalette** or **MCIWndRealize**, you must forward these messages to MCIWnd if you do not handle them yourself.

> [!Note]  
> When a video clip with 8-bit color depth is loaded into the MCIWnd window, the palette included with that clip replaces the palette associated with the MCIWnd window.

 

## Related topics

<dl> <dt>

[Playback Enhancements](playback-enhancements.md)
</dt> </dl>

 

 




