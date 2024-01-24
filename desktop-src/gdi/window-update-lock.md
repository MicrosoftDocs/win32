---
description: A window update lock is a temporary suspension of drawing in a window.
ms.assetid: 92b1ba04-ff79-4a37-9633-99412cdafe95
title: Window Update Lock
ms.topic: article
ms.date: 05/31/2018
---

# Window Update Lock

A *window update lock* is a temporary suspension of drawing in a window. The system uses the lock to prevent other windows from drawing over the tracking rectangle whenever the user moves or sizes a window. Applications can use the lock to prevent drawing if they carry out similar moving or sizing operations with their own windows.

An application uses the [**LockWindowUpdate**](/windows/desktop/api/Winuser/nf-winuser-lockwindowupdate) function to set or clear a window update lock, specifying the window to lock. The lock applies to the specified window and all of its child windows. When the lock is set, the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) and [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) functions return a display device context with a visible region that is empty. Given this, the application can continue to draw in the window, but all output is clipped. The lock persists until the application clears it by calling **LockWindowUpdate**, specifying **NULL** for the window. Although **LockWindowUpdate** forces a window's visible region to be empty, the function does not make the specified window invisible and does not clear the WS\_VISIBLE style bit.

After the lock is set, the application can use the [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function, with the DCX\_LOCKWINDOWUPDATE value, to retrieve a display device context to draw over the locked window. This allows the application to draw a tracking rectangle when processing keyboard or mouse messages. The system uses this method when the user moves and sizes windows. **GetDCEx** retrieves the display device context from the display device context cache, so the application must release the device context as soon as possible after drawing.

While a window update lock is set, the system creates an accumulated bounding rectangle for each locked window. When the lock is cleared, the system uses this bounding rectangle to set the update region for the window and its child windows, forcing an eventual [**WM\_PAINT**](wm-paint.md) message. If the accumulated bounding rectangle is empty (that is, if no drawing has occurred while the lock was set), the update region is not set.

 

 



