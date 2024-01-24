---
description: Typically, an application draws in a window in response to a WM\_PAINT message.
ms.assetid: 'b2317ce9-e775-450e-91f5-00f735f256a3'
title: The WM_PAINT Message
ms.topic: article
ms.date: 05/31/2018
---

# The WM\_PAINT Message

Typically, an application draws in a window in response to a [**WM\_PAINT**](wm-paint.md) message. The system sends this message to a window procedure when changes to the window have altered the content of the client area. The system sends the message only if there are no other messages in the application message queue.

Upon receiving a [**WM\_PAINT**](wm-paint.md) message, an application can call [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) to retrieve the display device context for the client area and use it in calls to GDI functions to carry out whatever drawing operations are necessary to update the client area. After completing the drawing operations, the application calls the [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) function to release the display device context.

Before [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) returns the display device context, the system prepares the device context for the specified window. It first sets the clipping region for the device context to be equal to the intersection of the portion of the window that needs updating and the portion that is visible to the user. Only those portions of the window that have changed are redrawn. Attempts to draw outside this region are clipped and do not appear on the screen.

The system can also send [**WM\_NCPAINT**](wm-ncpaint.md) and [**WM\_ERASEBKGND**](../winmsg/wm-erasebkgnd.md) messages to the window procedure before [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) returns. These messages direct the application to draw the nonclient area and window background. The *nonclient area* is the part of a window that is outside of the client area. The area includes features such as the title bar, window menu (also known as the **System** menu), and scroll bars. Most applications rely on the default window function, [**DefWindowProc**](/windows/desktop/api/winuser/nf-winuser-defwindowproca), to draw this area and therefore pass the **WM\_NCPAINT** message to this function. The *window background* is the color or pattern that a window is filled with before other drawing operations begin. The background covers any images previously in the window or on the screen under the window. If a window belongs to a window class having a class background brush, the **DefWindowProc** function draws the window background automatically.

[**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) fills a [**PAINTSTRUCT**](/windows/win32/api/winuser/ns-winuser-paintstruct) structure with information such as the dimensions of the portion of the window to be updated and a flag indicating whether the window background has been drawn. The application can use this information to optimize drawing. For example, it can use the dimensions of the update region, specified by the **rcPaint** member, to limit drawing to only those portions of the window that need updating. If an application has very simple output, it can ignore the update region and draw in the entire window, relying on the system to discard (clip) any unneeded output. Because the system clips drawing that extends outside the clipping region, only drawing that is in the update region is visible.

[**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) sets the update region of a window to **NULL**. This clears the region, preventing it from generating subsequent [**WM\_PAINT**](wm-paint.md) messages. If an application processes a **WM\_PAINT** message but does not call **BeginPaint** or otherwise clear the update region, the application continues to receive **WM\_PAINT** messages as long as the region is not empty. In all cases, an application must clear the update region before returning from the **WM\_PAINT** message.

After the application finishes drawing, it should call [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint). For most windows, **EndPaint** releases the display device context, making it available to other windows. **EndPaint** also shows the caret, if it was previously hidden by [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint). **BeginPaint** hides the caret to prevent drawing operations from corrupting it.

-   [The Update Region](the-update-region.md)
-   [Invalidating and Validating the Update Region](invalidating-and-validating-the-update-region.md)
-   [Retrieving the Update Region](retrieving-the-update-region.md)
-   [Excluding the Update Region](excluding-the-update-region.md)
-   [Synchronous and Asynchronous Drawing](synchronous-and-asynchronous-drawing.md)

 

 
