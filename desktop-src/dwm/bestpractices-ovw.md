---
title: Performance Considerations and Best Practices
description: This topic presents a set of best practices for using the Desktop Window Manager (DWM) APIs.
ms.assetid: 5b1f6ff8-1d3f-4a70-8efd-90f8802e8532
keywords:
- Desktop Window Manager (DWM),best practices
- DWM (Desktop Window Manager),best practices
- Desktop Window Manager (DWM),application practices
- DWM (Desktop Window Manager),application practices
- Desktop Window Manager (DWM),drawing practices
- DWM (Desktop Window Manager),drawing practices
- Desktop Window Manager (DWM),blur behind effect
- DWM (Desktop Window Manager),blur behind effect
- application practices
- drawing practices
- blur behind effect
ms.topic: article
ms.date: 05/31/2018
---

# Performance Considerations and Best Practices

This topic presents a set of best practices for using the Desktop Window Manager (DWM) APIs.

This topic contains the following sections:

-   [Application Practices for DWM](#application-practices-for-dwm)
-   [Drawing Practices for DWM](#drawing-practices-for-dwm)
-   [DWM Blur-Behind Client Region](#dwm-blur-behind-client-region)

## Application Practices for DWM

If your application handles dots per inch (dpi) scaling, you can declare an application as dpi-aware and prevent automatic scaling by setting the dpi-aware flag in the program's manifest or by calling the [**SetProcessDPIAware**](/windows/desktop/api/winuser/nf-winuser-setprocessdpiaware) function during program initialization.

With DWM composition turned on, obscured applications no longer receive [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) messages and are not asked to re-render. Each window's content is already available to compose the screen image.

Top-level [**WS\_EX\_TRANSPARENT**](/windows/desktop/api/winuser/nf-winuser-createwindowexa) windows should be combined with a **WS\_EX\_LAYERED** style for the purposes of hit testing. **WS\_EX\_TRANSPARENT** in the classic sense, without redirection, is useful for child windows in a hierarchy of windows that belong to the same thread, but is not intended for top-level windows.

Use regions or layering to create shaped or blended windows. Note that in Windows Vista and later versions of Windows, custom drawing only part of a top-level window will not provide the desired stale content in undrawn regions.

APIs such as [**GetDCOrgEx**](/windows/desktop/api/wingdi/nf-wingdi-getdcorgex) can be used to determine certain actual values. If you have a device context (DC) for a redirected window, the origin returned by **GetDCOrgEx** will not match the origin of your window on the screen. The origin will instead be the origin of the back-buffer surface for your window: (0, 0).

When all else fails, disable window rendering by calling the [**DwmSetWindowAttribute**](/windows/desktop/api/Dwmapi/nf-dwmapi-dwmsetwindowattribute) function.

## Drawing Practices for DWM

Avoid drawing directly to the primary display surface. Doing so will force the DWM to disable composition until your application releases the primary device surface.

Evaluate whether your application must provide its own double buffering. The DWM effectively double buffers content and presents the window in a single frame.

Avoid reading from or writing to a display DC. Although supported by DWM, we do not recommend it because of decreased performance.

Avoid drawing in the non-client area. Although this area can be accessed by the application, and drawing there is supported by the Microsoft Win32 API, doing this can cause the window to lose any glass border it has.

Avoid mixing Windows Graphics Device Interface (GDI) and Microsoft DirectX unless they do not overlap. If mixing is necessary, either draw the GDI content into a DirectX software surface and combine them before composing to the screen, or else draw them in separate windows.

Use [**BitBlt**](/windows/desktop/api/wingdi/nf-wingdi-bitblt) or [**StretchBlt**](/windows/desktop/api/wingdi/nf-wingdi-stretchblt) function instead of Windows GDI+ to present your drawing for rendering. GDI+ renders one scan line at a time with software rendering. This can cause flickering in your applications.

## DWM Blur-Behind Client Region

Rendering the blur-behind effect is a resource-intensive operation for both the CPU and the graphics processing unit (GPU). Application developers are urged to consider the implications of using client-area blur so that it does not consume excessive resources. You should use particular caution in the following cases:

-   When you expect the size of the client-area blur to be significant, even if no updates will occur in the blurred area itself. The blur has to be rendered in case any updates occur under the blurred area of the window, which incurs CPU and GPU costs. In addition, window operations on the window (move/resize/transitions) will incur more costs.
-   When you expect significant updates in the blurred client area. This will require a repaint of the blur on every update and consume excessive resources.
-   If the blur is expected to cover a significant area, and updates to that area are also expected, we strongly recommended that you do not blur the client area.

 

 