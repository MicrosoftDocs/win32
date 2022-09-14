---
description: The system changes the size of a window when the user chooses window menu commands, such as Size and Maximize, or when the application calls functions, such as the SetWindowPos function.
ms.assetid: 6f997cba-e4c9-4e27-8309-42b9892ec620
title: Resized Windows
ms.topic: article
ms.date: 05/31/2018
---

# Resized Windows

The system changes the size of a window when the user chooses window menu commands, such as Size and Maximize, or when the application calls functions, such as the [**SetWindowPos**](/windows/win32/api/winuser/nf-winuser-setwindowpos) function. When a window changes size, the system assumes that the contents of the previously exposed portion of the window are not affected and need not be redrawn. The system invalidates only the newly exposed portion of the window, which saves time when the eventual [**WM\_PAINT**](wm-paint.md) message is processed by the application. In this case, **WM\_PAINT** is not generated when the size of the window is reduced.

For some windows, any change to the size of the window invalidates the contents. For example, a clock application that adapts the face of the clock to fit neatly within its window must redraw the clock whenever the window changes size. To force the system to invalidate the entire client area of the window when a vertical, horizontal, or both vertical and horizontal change is made, an application must specify the CS\_VREDRAW or CS\_HREDRAW style, or both, when registering the window class. Any window belonging to a window class having these styles is invalidated each time the user or the application changes the size of the window.

 

 
