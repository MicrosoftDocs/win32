---
description: The system sends a WM\_NCPAINT message to the window whenever a part of the nonclient area of the window, such as the title bar, menu bar, or window frame, must be updated.
ms.assetid: e4dc61f3-6a9f-4ed4-8685-62eb4ceb85f1
title: Nonclient Area
ms.topic: article
ms.date: 05/31/2018
---

# Nonclient Area

The system sends a [**WM\_NCPAINT**](wm-ncpaint.md) message to the window whenever a part of the nonclient area of the window, such as the title bar, menu bar, or window frame, must be updated. The system may also send other messages to direct a window to update a portion of its client area; for example, when a window becomes active or inactive, it sends the [**WM\_NCACTIVATE**](../winmsg/wm-ncactivate.md) message to update its title bar. In general, processing these messages for standard windows is not recommended, because the application must be able to draw all the required parts of the nonclient area for the window. For this reason, most applications pass these messages to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca) for default processing.

An application that creates custom nonclient areas for its windows must process these messages. When doing so, the application must use a window device context to carry out drawing in the window. The *window device context* enables the application to draw in all portions of the window, including the nonclient area. An application retrieves a window device context by using the [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc) or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function and, when drawing is complete, must release the window device context by using the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function.

The system maintains an update region for the nonclient area. When an application receives a [**WM\_NCPAINT**](wm-ncpaint.md) message, the *wParam* parameter contains a handle to a region defining the dimensions of the update region. The application can use the handle to combine the update region with the clipping region for the window device context. The system does not automatically combine the update region when retrieving the window device context unless the application uses [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) and specifies both the region handle and the DCX\_INTERSECTRGN flag. If the application does not combine the update region, only drawing operations that would otherwise extend outside the window are clipped. The application is not responsible for clearing the update region, regardless of whether it uses the region.

If an application processes the [**WM\_NCACTIVATE**](../winmsg/wm-ncactivate.md) message, after processing it must return **TRUE** to direct the system to complete the change of active window. If the window is minimized when the application receives the **WM\_NCACTIVATE** message, it should pass the message to [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca). In such cases, the default function redraws the label for the icon.

 

 
