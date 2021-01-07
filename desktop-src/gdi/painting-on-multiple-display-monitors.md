---
description: The system automatically handles painting into a device context (DC) that spans more than one monitor, even when the monitors have different color depths.
ms.assetid: 2f03f612-293a-4a42-a13b-1e08e49d9e54
title: Painting on Multiple Display Monitors
ms.topic: article
ms.date: 05/31/2018
---

# Painting on Multiple Display Monitors

The system automatically handles painting into a device context (DC) that spans more than one monitor, even when the monitors have different color depths. Usually this produces good results, but it may not be optimal. For example, a window on two monitors of vastly different color depths could have poor color rendition. Also, monitors with the same color depth may have different color formatsfor example, colors could be encoded with different numbers of bits, or be located in different places in a pixel's color value.

To get the best results for each of the monitors in a DC that spans more than one display, call [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors) to enumerate the monitors that intersect your DC and paint the intersecting area in each of them separately according to the display attributes for that monitor. See the example in [Painting on a DC That Spans Multiple Displays](painting-on-a-dc-that-spans-multiple-displays.md).

If you do all of your drawing in your **WM\_PAINT** code and if your **WM\_PAINT** code handles all of the various video modes, then you should be able to place your **WM\_PAINT** code in the **MonitorEnumProc** of [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors) with only a few modifications.

 

 



