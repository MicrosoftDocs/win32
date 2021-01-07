---
description: A window device context enables an application to draw anywhere in a window, including the nonclient area.
ms.assetid: 7b3c6352-51d5-4fdf-82c2-7a28194f607f
title: Window Display Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Window Display Device Contexts

A *window device context* enables an application to draw anywhere in a window, including the nonclient area. Window device contexts are typically used by applications that process the [**WM\_NCPAINT**](wm-ncpaint.md) and [**WM\_NCACTIVATE**](../winmsg/wm-ncactivate.md) messages for windows with custom nonclient areas. Using a window device context is not recommended for any other purpose.

An application can retrieve a window device context by using the [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc) or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function with the DCX\_WINDOW option specified. The function retrieves a window device context from the display device context cache. A window that uses a window device context must release it after drawing by using the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function as soon as possible. Window device contexts are always from the cache; the CS\_OWNDC and CS\_CLASSDC class styles do not affect the device context.

When an application retrieves a window device context, the system sets the device origin to the upper left corner of the window instead of the upper left corner of the client area. It also sets the clipping region to include the entire window, not just the client area. The system sets the current attribute values of a window device context to the same default values as a common device context. An application can change the attribute values, but the system does not preserve any changes when the device context is released.

 

 
