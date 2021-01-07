---
description: An application obtains a display DC by calling the BeginPaint, GetDC, or GetDCEx function and identifying the window in which the corresponding output will appear.
ms.assetid: '8f952d68-ee52-4e63-9f09-80a14c755d31'
title: Display Device Contexts
ms.topic: article
ms.date: 05/31/2018
---

# Display Device Contexts

An application obtains a display DC by calling the [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint), [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc), or [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex) function and identifying the window in which the corresponding output will appear. Typically, an application obtains a display DC only when it must draw in the client area. However, one may obtain a [window device context](#window-device-contexts) by calling the [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc) function. When the application is finished drawing, it must release the DC by calling the [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint) or [**ReleaseDC**](/windows/desktop/api/Winuser/nf-winuser-releasedc) function.

There are five types of DCs for video displays:

-   Class
-   Common
-   Private
-   Window
-   Parent

## Class Device Contexts

*Class device contexts* are supported strictly for compatibility with 16-bit versions of Windows. When writing your application, avoid using the class device context; use a private device context instead.

## Common Device Contexts

*Common device contexts* are display DCs maintained in a special cache by the system. Common device contexts are used in applications that perform infrequent drawing operations. Before the system returns the DC handle, it initializes the common device context with default objects, attributes, and modes. Any drawing operations performed by the application use these defaults unless one of the GDI functions is called to select a new object, change the attributes of an existing object, or select a new mode.

Because only a limited number of common device contexts exist, an application should release them after it has finished drawing. When the application releases a common device context, any changes to the default data are lost.

## Private Device Contexts

*Private device contexts* are display DCs that, unlike common device contexts, retain any changes to the default data even after an application releases them. Private device contexts are used in applications that perform numerous drawing operations such as computer-aided design (CAD) applications, desktop-publishing applications, drawing and painting applications, and so on. Private device contexts are not part of the system cache and therefore need not be released after use. The system automatically removes a private device context after the last window of that class has been destroyed.

An application creates a private device context by first specifying the CS\_OWNDC window-class style when it initializes the **style** member of the [**WNDCLASS**](/windows/win32/api/winuser/ns-winuser-wndclassa) structure and calls the [**RegisterClass**](/windows/win32/api/winuser/nf-winuser-registerclassa) function. (For more information about window classes, see [Window Classes](../winmsg/window-classes.md).)

After creating a window with the CS\_OWNDC style, an application can call the [**GetDC**](/windows/desktop/api/Winuser/nf-winuser-getdc), [**GetDCEx**](/windows/desktop/api/Winuser/nf-winuser-getdcex), or [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint) function once to obtain a handle identifying a private device context. The application can continue using this handle (and the associated DC) until it deletes the window created with this class. Any changes to graphic objects and their attributes, or graphic modes are retained by the system until the window is deleted.

## Window Device Contexts

A *window device context* enables an application to draw anywhere in a window, including the nonclient area. Window device contexts are typically used by applications that process the [**WM\_NCPAINT**](wm-ncpaint.md) and [**WM\_NCACTIVATE**](../winmsg/wm-ncactivate.md) messages for windows with custom nonclient areas. Using a window device context is not recommended for any other purpose. For more information; see [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc).

## Parent Device Contexts

A *parent device context* enables an application to minimize the time necessary to set up the clipping region for a window. An application typically uses parent device contexts to speed up drawing for control windows without requiring a private or class device context. For example, the system uses parent device contexts for push button and edit controls. Parent device contexts are intended for use with child windows only, never with top-level or pop-up windows. For more information; see [Parent Display Device Contexts](parent-display-device-contexts.md).

 

 
