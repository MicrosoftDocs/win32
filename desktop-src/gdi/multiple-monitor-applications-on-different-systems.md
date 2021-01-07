---
description: To have your multiple monitoraware application work both on systems with and without multiple monitor support, link your application with Multimon.h.
ms.assetid: 8667305e-ca76-49cb-878e-07814431e6db
title: Multiple Monitor Applications on Different Systems
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Monitor Applications on Different Systems

To have your multiple monitoraware application work both on systems with and without multiple monitor support, link your application with Multimon.h. You must also define COMPILE\_MULTIMON\_STUBS in exactly one C file. If the system does not support multiple monitors, this returns default values from [**GetSystemMetrics**](/windows/win32/api/winuser/nf-winuser-getsystemmetrics) , and the multiple monitor functions act as if there is only one display. On multiple monitor systems, your application will work normally.

Because negative coordinates can happen easily in a multimonitor system, you should retrieve coordinates that are packed in the lParam by using the **GET\_X\_LPARAM** and **GET\_Y\_LPARAM** macros.

Do not use negative coordinates or coordinates larger than SM\_CXSCREEN and SM\_CYSCREEN to hide a window. Windows that use these limits to hide may appear on another monitor. Likewise, do not use these limits to keep a window visible because this can cause a window to snap to the primary monitor. It is best to reexamine existing applications for these problems. However, you can minimize problems in existing applications by running the application on the primary monitor or by keeping the primary monitor in the upper-left corner of the virtual screen.

Note that SM\_CXMAXTRACK and SM\_CYMAXTRACK are defined for the desktop, not just one monitor. Windows using these limits may need to be redefined.

A parent or related window might not be on the same monitor as a child window. To locate the monitor of a window, applications should use the [**MonitorFromWindow**](/windows/desktop/api/Winuser/nf-winuser-monitorfromwindow) function.

To have a screen saver display on all monitors, link with the latest version of Scrnsave.lib. Otherwise, the screen saver may only appear on the primary monitor and leave the other monitors untouched. Screen savers linked with the latest Scrnsave.lib will work on both single and multiple monitor systems. To have a different screen saver on each monitor, use the multiple monitor functions to handle each monitor separately.

Input devices that deliver coordinates to the system in absolute coordinates, such as tablets, have their cursor input restricted to the primary monitor. To switch tablet input between monitors, see the instructions from the OEM.

To map mouse input that is sent in absolute coordinates to the entire virtual screen, use the [**INPUT**](/windows/win32/api/winuser/ns-winuser-input) structure with MOUSEEVENTF\_ABSOLUTE and MOUSEEVENTF\_VIRTUALDESKTOP.

The [**BitBlt**](/windows/desktop/api/Wingdi/nf-wingdi-bitblt) function works well for multiple monitor systems. However, the [**MaskBlt**](/windows/desktop/api/Wingdi/nf-wingdi-maskblt), [**PlgBlt**](/windows/desktop/api/Wingdi/nf-wingdi-plgblt), [**StretchBlt**](/windows/desktop/api/Wingdi/nf-wingdi-stretchblt), and [**TransparentBlt**](/windows/desktop/api/WinGdi/nf-wingdi-transparentblt) functions will fail if the source and destination device contexts are different.

 

 
