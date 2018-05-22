---
Description: 'A private device context enables an application to avoid retrieving and initializing a display device context each time the application must draw in a window.'
ms.assetid: '8de5a14b-a8b3-42a5-81f3-bf3c357052cb'
title: Private Display Device Contexts
---

# Private Display Device Contexts

A *private device context* enables an application to avoid retrieving and initializing a display device context each time the application must draw in a window. Private device contexts are useful for windows that require many changes to the values of the attributes of the device context to prepare it for drawing. Private device contexts reduce the time required to prepare the device context and therefore the time needed to carry out drawing in the window.

An application directs the system to create a private device context for a window by specifying the CS\_OWNDC style in the window class. The system creates a unique private device context each time it creates a new window belonging to the class. Initially, the private device context has the same default values for attributes as a common device context, but the application can modify these at any time. The system preserves changes to the device context for the life of the window or until the application makes additional changes.

An application can retrieve a handle to the private device context by using the [**GetDC**](getdc.md) function any time after the window is created. The application must retrieve the handle only once. Thereafter, it can keep and use the handle any number of times. Because a private device context is not part of the display device context cache, an application need never release the device context by using the [**ReleaseDC**](releasedc.md) function.

The system automatically adjusts the device context to reflect changes to the window, such as moving or sizing. This ensures that any overlapping windows are always properly clipped; that is, no action is required by the application to ensure clipping. However, the system does not revise the device context to include the update region. Therefore, when processing a [**WM\_PAINT**](wm-paint.md) message, the application must incorporate the update region either by calling [**BeginPaint**](beginpaint.md) or by retrieving the update region and intersecting it with the current clipping region. If the application does not call **BeginPaint**, it must explicitly validate the update region by using the [**ValidateRect**](validaterect.md) or [**ValidateRgn**](validatergn.md) function. If the application does not validate the update region, the window receives an endless series of **WM\_PAINT** messages.

Because [**BeginPaint**](beginpaint.md) hides the caret if a window is showing it, an application that calls **BeginPaint** should also call the [**EndPaint**](endpaint.md) function to restore the caret. **EndPaint** has no other effect on a private device context.

Although a private device context is convenient to use, it is memory-intensive in terms of system resources, requiring 800 or more bytes to store. Private device contexts are recommended when performance considerations outweigh storage costs.

The system includes the private device context when sending the [**WM\_ERASEBKGND**](_win32_wm_erasebkgnd_cpp) message to the application. The current selections of the private device context, including mapping mode, are in effect when the application or the system processes these messages. To avoid undesirable effects, the system uses logical coordinates when erasing the background; for example, it uses the [**GetClipBox**](getclipbox.md) function to retrieve the logical coordinates of the area to erase and passes these coordinates to the [**FillRect**](fillrect.md) function. Applications that process these messages can use similar techniques.

An application can use the [**GetDCEx**](getdcex.md) function to force the system to return a common device context for the window that has a private device context. This is useful for carrying out quick touch-ups to a window without changing the current values of the attributes of the private device context.

 

 



