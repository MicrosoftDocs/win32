---
description: Ordinarily, the system palette entries that the system reserves for static colors cannot be changed.
ms.assetid: be258151-36cc-42ba-8005-ff9d8e59b894
title: System Palette and Static Colors
ms.topic: article
ms.date: 05/31/2018
---

# System Palette and Static Colors

Ordinarily, the system palette entries that the system reserves for static colors cannot be changed. An application can override this default behavior by using the [**SetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-setsystempaletteuse) function to reduce the number of static color entries and, thereby, increase the number of unused system palette entries. However, because changing the static colors can have an immediate and dramatic effect on all windows on the display, an application should not call **SetSystemPaletteUse**, unless it has a maximized window and the input focus.

When an application calls [**SetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-setsystempaletteuse) with the SYSPAL\_NOSTATIC value, the system frees all but two of the reserved entries, allowing those entries to receive new color values when the application subsequently realizes its logical palette. The remaining two static color entries remain reserved and are set to white and black. An application can restore the reserved entries by calling **SetSystemPaletteUse** with the SYSPAL\_STATIC value. It can discover the current system palette usage by using the [**GetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-getsystempaletteuse) function.

Furthermore, after setting the system palette usage to SYSPAL\_NOSTATIC, the application must immediately realize its logical palette, call the [**GetSysColor**](/windows/win32/api/winuser/nf-winuser-getsyscolor) function to save the current system color settings, call the [**SetSysColors**](/windows/win32/api/winuser/nf-winuser-setsyscolors) function to set the system colors to reasonable values using black and white, and finally send the [**WM\_SYSCOLORCHANGE**](wm-syscolorchange.md) message to other top-level windows to allow them to be redrawn with the new system colors. When setting system colors using black and white, the application should make sure adjacent or overlapping items, such as window frames and borders, are set to black and white, respectively.

Before the application loses the input focus, closes its window, or terminates, it must immediately call [**SetSystemPaletteUse**](/windows/desktop/api/Wingdi/nf-wingdi-setsystempaletteuse) with the SYSPAL\_STATIC value, realize its logical palette, restore the system colors to their previous values, and send the [**WM\_SYSCOLORCHANGE**](wm-syscolorchange.md) message. The system sends a [**WM\_PAINT**](wm-paint.md) message to any window that is affected by a system color change. Applications that have brushes using the existing system colors should delete those brushes and re-create them using the new system colors.

 

 
