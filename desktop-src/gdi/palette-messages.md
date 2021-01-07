---
description: Changes to the system palette for the display device can have dramatic and sometimes undesirable effects on the colors used in windows on the desktop.
ms.assetid: 9c470b6f-c0d3-462e-9649-1f39b06bd543
title: Palette Messages
ms.topic: article
ms.date: 05/31/2018
---

# Palette Messages

Changes to the system palette for the display device can have dramatic and sometimes undesirable effects on the colors used in windows on the desktop. To minimize the impact of these changes, the system provides a set of messages that help applications manage their logical palettes while ensuring that colors in the active window are as close as possible to the colors intended.

The system sends a [**WM\_QUERYNEWPALETTE**](wm-querynewpalette.md) message to a top-level or overlapped window just before activating the window. This message gives an application the opportunity to select and realize its logical palette so that it receives the best possible mapping of colors for its logical palette. When the application receives the message, it should use the [**SelectPalette**](/windows/desktop/api/Wingdi/nf-wingdi-selectpalette), [**UnrealizeObject**](/windows/desktop/api/Wingdi/nf-wingdi-unrealizeobject), and [**RealizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-realizepalette) functions to select and realize the logical palette. Doing so directs the system to update colors in the system palette so that its colors match as many colors in the logical palette as possible.

When an application causes changes to the system palette as a result of realizing its logical palette, the system sends a [**WM\_PALETTECHANGED**](wm-palettechanged.md) message to all top-level and overlapped windows. This message gives applications the opportunity to update the colors in the client areas of their windows, replacing colors that have changed with colors that more closely match the intended colors. An application that receives the **WM\_PALETTECHANGED** message should use [**UnrealizeObject**](/windows/desktop/api/Wingdi/nf-wingdi-unrealizeobject) and [**RealizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-realizepalette) to reset the logical palettes associated with all inactive windows and then update the colors in the client area for each inactive window by using the [**UpdateColors**](/windows/desktop/api/Wingdi/nf-wingdi-updatecolors) function. This technique does not guarantee the greatest number of exact color matches; however, it does ensure that colors in the logical palette are mapped to reasonable colors in the system palette.

> [!Note]  
> To avoid creating an infinite loop, an application should never realize the palette for the window whose handle matches the handle passed in the *wParam* parameter of the [**WM\_PALETTECHANGED**](wm-palettechanged.md) message.

 

The [**UpdateColors**](/windows/desktop/api/Wingdi/nf-wingdi-updatecolors) function typically updates a client area of an inactive window faster than redrawing the area. However, because **UpdateColors** performs color translation based on the color of each pixel before the system palette changed, each call to this function results in the loss of some color accuracy. This means **UpdateColors** cannot be used to update colors when the window becomes active. In such cases, the application should redraw the client area.

The system may send the [**WM\_QUERYNEWPALETTE**](wm-querynewpalette.md) message when changes to the logical palette are made. Also, the system may send the [**WM\_PALETTEISCHANGING**](wm-paletteischanging.md) message to all top-level and overlapped windows when the system palette is about to change.

 

 



