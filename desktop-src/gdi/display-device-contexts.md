---
Description: 'An application obtains a display DC by calling the BeginPaint, GetDC, or GetDCEx function and identifying the window in which the corresponding output will appear.'
ms.assetid: 'fc76abbf-68da-47f2-8145-4fad806297b4'
title: Display Device Contexts
---

# Display Device Contexts

An application obtains a display DC by calling the [**BeginPaint**](beginpaint.md), [**GetDC**](getdc.md), or [**GetDCEx**](getdcex.md) function and identifying the window in which the corresponding output will appear. Typically, an application obtains a display DC only when it must draw in the client area. However, one may obtain a [window device context](#window-device-contexts) by calling the [**GetWindowDC**](getwindowdc.md) function. When the application is finished drawing, it must release the DC by calling the [**EndPaint**](endpaint.md) or [**ReleaseDC**](releasedc.md) function.

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

An application creates a private device context by first specifying the CS\_OWNDC window-class style when it initializes the **style** member of the [**WNDCLASS**](_win32_wndclass_str_cpp) structure and calls the [**RegisterClass**](_win32_registerclass_cpp) function. (For more information about window classes, see [Window Classes](_win32_window_classes_cpp).)

After creating a window with the CS\_OWNDC style, an application can call the [**GetDC**](getdc.md), [**GetDCEx**](getdcex.md), or [**BeginPaint**](beginpaint.md) function once to obtain a handle identifying a private device context. The application can continue using this handle (and the associated DC) until it deletes the window created with this class. Any changes to graphic objects and their attributes, or graphic modes are retained by the system until the window is deleted.

## Window Device Contexts

A *window device context* enables an application to draw anywhere in a window, including the nonclient area. Window device contexts are typically used by applications that process the [**WM\_NCPAINT**](wm-ncpaint.md) and [**WM\_NCACTIVATE**](_win32_wm_ncactivate_cpp) messages for windows with custom nonclient areas. Using a window device context is not recommended for any other purpose. For more information; see [**GetWindowDC**](getwindowdc.md).

## Parent Device Contexts

A *parent device context* enables an application to minimize the time necessary to set up the clipping region for a window. An application typically uses parent device contexts to speed up drawing for control windows without requiring a private or class device context. For example, the system uses parent device contexts for push button and edit controls. Parent device contexts are intended for use with child windows only, never with top-level or pop-up windows. For more information; see [Parent Display Device Contexts](parent-display-device-contexts.md).

 

 



