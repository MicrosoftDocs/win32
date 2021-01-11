---
description: By using a class device context, an application can use a single display device context for every window belonging to a specified class.
ms.assetid: fc76abbf-68da-47f2-8145-4fad806297b4
title: Class Display Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Class Display Device Contexts

By using a *class device context*, an application can use a single display device context for every window belonging to a specified class. Class device contexts are often used with control windows that are drawn using the same attribute values. Like private device contexts, class device contexts minimize the time required to prepare a device context for drawing.

The system supplies a class device context for a window if it belongs to a window class having the CS\_CLASSDC style. The system creates the device context when creating the first window belonging to the class and then uses the same device context for all subsequently created windows in the class. Initially, the class device context has the same default values for attributes as a common device context, but the application can modify these at any time. The system preserves all changes, except for the clipping region and device origin, until the last window in the class has been destroyed. A change made for one window applies to all windows in that class.

An application can retrieve the handle to the class device context by using the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc) function any time after the first window has been created. The application can keep and use the handle without releasing it because the class device context is not part of the display device context cache. If the application creates another window in the same window class, the application must retrieve the class device context again. Retrieving the device context sets the correct device origin and clipping region for the new window. After the application retrieves the class device context for a new window in the class, the device context can no longer be used to draw in the original window without again retrieving it for that window. In general, each time it must draw in a window, an application must explicitly retrieve the class device context for the window.

Applications that use class device contexts should always call [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) when processing a [**WM\_PAINT**](wm-paint.md) message. The function sets the correct device origin and clipping region for the window, and incorporates the update region. The application should also call [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) to restore the caret if **BeginPaint** hid it. **EndPaint** has no other effect on a class device context.

The system passes the class device context when sending the [**WM\_ERASEBKGND**](../winmsg/wm-erasebkgnd.md) message to the application, permitting the current attribute values to affect any drawing carried out by the application or the system when processing this message. As it could with a window having a private device context, an application can use [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) to force the system to return a common device context for the window that has a class device context.

Using class device contexts is not recommended.

 

 
