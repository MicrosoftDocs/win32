---
description: Each physical display is represented by a monitor handle of type HMONITOR.
ms.assetid: c43c1401-52d3-485e-a418-205df5737040
title: HMONITOR and the Device Context
ms.topic: article
ms.date: 05/31/2018
---

# HMONITOR and the Device Context

Each physical display is represented by a monitor handle of type **HMONITOR**. A valid **HMONITOR** is guaranteed to be non-NULL. A physical display has the same **HMONITOR** as long as it is part of the desktop. When a **WM\_DISPLAYCHANGE** message is sent, any monitor may be removed from the desktop and thus its **HMONITOR** becomes invalid or has its settings changed. Therefore, an application should check whether all **HMONITORS** are valid when this message is sent.

Any function that returns a display device context (DC) normally returns a DC for the primary monitor. To obtain the DC for another monitor, use the [**EnumDisplayMonitors**](/windows/desktop/api/Winuser/nf-winuser-enumdisplaymonitors) function. Or, you can use the device name from the [**GetMonitorInfo**](/windows/desktop/api/Winuser/nf-winuser-getmonitorinfoa) function to create a DC with [**CreateDC**](/windows/desktop/api/Wingdi/nf-wingdi-createdca). However, if the function, such as [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc) or [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint), gets a DC for a window that spans more than one display, the DC will also span the two displays.

 

 



