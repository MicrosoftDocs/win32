---
description: Each monitor can have its own color depth.
ms.assetid: 8d1ba8d2-b43d-498d-be5a-100fe9fc0f61
title: Colors on Multiple Display Monitors
ms.topic: article
ms.date: 05/31/2018
---

# Colors on Multiple Display Monitors

Each monitor can have its own color depth. The system automatically adjusts colors as windows move across monitors with different color depths. In general, this produces good results. However, this is not always optimal. To take advantage of the color capabilities of different monitors, see the [Painting on Multiple Display Monitors](painting-on-multiple-display-monitors.md) section that follows.

To determine if all monitors have the same color format, call [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) with SM\_SAMEDISPLAYFORMAT.

If the primary monitor is palettized, [**SelectPalette**](/windows/desktop/api/Wingdi/nf-wingdi-selectpalette) and [**RealizePalette**](/windows/desktop/api/Wingdi/nf-wingdi-realizepalette) work the same as before, but across all monitors. In addition, the palettes of all palettized devices are synchronized. If the primary monitor is not palettized, **SelectPalette** and **RealizePalette** will select the palette into the background and palettized devices will not be synchronized.

 

 
