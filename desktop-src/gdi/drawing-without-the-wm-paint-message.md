---
description: Although applications carry out most drawing operations while the WM\_PAINT message is processing, it is sometimes more efficient for an application to draw directly in a window without relying on the WM\_PAINT message.
ms.assetid: 2d015879-58d2-4cbe-b1cc-445f2e8fd316
title: Drawing Without the WM_PAINT Message
ms.topic: article
ms.date: 05/31/2018
---

# Drawing Without the WM\_PAINT Message

Although applications carry out most drawing operations while the [**WM\_PAINT**](wm-paint.md) message is processing, it is sometimes more efficient for an application to draw directly in a window without relying on the **WM\_PAINT** message. This can be useful when the user needs immediate feedback, such as when selecting text and dragging or sizing an object. In such cases, the application usually draws while processing keyboard or mouse messages.

To draw in a window without using a [**WM\_PAINT**](wm-paint.md) message, the application uses the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function to retrieve a display device context for the window. With the display device context, the application can draw in the window and avoid intruding into other windows. When the application has finished drawing, it calls the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function to release the display device context for use by other applications.

When drawing without using a [**WM\_PAINT**](wm-paint.md) message, the application usually does not invalidate the window. Instead, it draws in such a fashion that it can easily restore the window and remove the drawing. For example, when the user selects text or an object, the application typically draws the selection by inverting whatever is already in the window. The application can remove the selection and restore the original contents of the window by simply inverting again.

The application is responsible for carefully managing any changes it makes to the window. In particular, if an application draws a selection and an intervening [**WM\_PAINT**](wm-paint.md) message occurs, the application must ensure that any drawing done during the message does not corrupt the selection. To avoid this, many applications remove the selection, carry out usual drawing operations, and then restore the selection when drawing is complete.

 

 



