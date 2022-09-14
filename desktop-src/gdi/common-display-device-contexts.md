---
description: A common device context is used for drawing in the client area of the window.
ms.assetid: 63c4f775-b1a3-4f7c-808b-81c596f26353
title: Common Display Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Common Display Device Contexts

A *common device context* is used for drawing in the client area of the window. The system provides a common device context by default for any window whose window class does not explicitly specify a display device context style. Common device contexts are typically used with windows that can be drawn without extensive changes to the device context attributes. Common device contexts are convenient because they do not require additional memory or system resources, but they can be inconvenient if the application must set up many attributes before using them.

The system retrieves all common device contexts from the display device context cache. An application can retrieve a common device context immediately after the window is created. Because the common device context is from the cache, the application must always release the device context as soon as possible after drawing. After the common device context is released, it is no longer valid and the application must not attempt to draw with it. To draw again, the application must retrieve a new common device context, and continue to retrieve and release a common device context each time it draws in the window. If the application retrieves the device context handle by using the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function, it must use the [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function to release the handle. Similarly, for each [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) function, the application must use a corresponding [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) function.

When the application retrieves the device context, the system adjusts the origin so that it aligns with the upper left corner of the client area. It also sets the clipping region so that output to the device context is clipped to the client area. Any output that would otherwise appear outside the client area is clipped. If the application retrieves the common device context by using [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint), the system also includes the update region in the clipping region to further restrict the output.

When an application releases a common device context, the system restores the default values for the attributes of the device context. An application that modifies attribute values must do so each time it retrieves a common device context. Releasing the device context releases any drawing objects the application may have selected into it, so the application need not release these objects before releasing the device context. In all cases, an application must never assume that the common device context retains nondefault selections after being released.

 

 



