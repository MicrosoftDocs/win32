---
Description: The following functions are used with painting and drawing.
ms.assetid: ec18323e-c13b-4328-83bf-9e4ed4a712b8
title: Painting and Drawing Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Painting and Drawing Functions

The following functions are used with painting and drawing.



| Function                                       | Description                                                                                                 |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**BeginPaint**](/windows/win32/Winuser/nf-winuser-beginpaint?branch=master)               | Prepares a window for painting.                                                                             |
| [**DrawAnimatedRects**](/windows/win32/Winuser/nf-winuser-drawanimatedrects?branch=master) | Draws a rectangle and animates it to indicate icon or window activity.                                      |
| [**DrawCaption**](/windows/win32/Winuser/nf-winuser-drawcaption?branch=master)             | Draws a window caption.                                                                                     |
| [**DrawEdge**](/windows/win32/Winuser/nf-winuser-drawedge?branch=master)                   | Draws one or more edges of rectangle.                                                                       |
| [**DrawFocusRect**](/windows/win32/Winuser/nf-winuser-drawfocusrect?branch=master)         | Draws a rectangle in the style that indicates the rectangle has the focus.                                  |
| [**DrawFrameControl**](/windows/win32/Winuser/nf-winuser-drawframecontrol?branch=master)   | Draws a frame control.                                                                                      |
| [**DrawState**](/windows/win32/Winuser/nf-winuser-drawstatea?branch=master)                 | Displays an image and applies a visual effect to indicate a state.                                          |
| [**DrawStateProc**](/windows/win32/Winuser/nc-winuser-drawstateproc?branch=master)         | A callback function that renders a complex image for [**DrawState**](/windows/win32/Winuser/nf-winuser-drawstatea?branch=master).                        |
| [**EndPaint**](/windows/win32/Winuser/nf-winuser-endpaint?branch=master)                   | Marks the end of painting in a window.                                                                      |
| [**ExcludeUpdateRgn**](/windows/win32/Winuser/nf-winuser-excludeupdatergn?branch=master)   | Prevents drawing within invalid areas of a window.                                                          |
| [**GdiFlush**](/windows/win32/Wingdi/nf-wingdi-gdiflush?branch=master)                   | Flushes the calling thread's current batch.                                                                 |
| [**GdiGetBatchLimit**](/windows/win32/Wingdi/nf-wingdi-gdigetbatchlimit?branch=master)   | Returns the maximum number of function calls that can be accumulated in the calling thread's current batch. |
| [**GdiSetBatchLimit**](/windows/win32/Wingdi/nf-wingdi-gdisetbatchlimit?branch=master)   | Sets the maximum number of function calls that can be accumulated in the calling thread's current batch.    |
| [**GetBkColor**](/windows/win32/Wingdi/nf-wingdi-getbkcolor?branch=master)               | Returns the background color for a device context.                                                          |
| [**GetBkMode**](/windows/win32/Wingdi/nf-wingdi-getbkmode?branch=master)                 | Returns the background mix mode for a device context.                                                       |
| [**GetBoundsRect**](/windows/win32/Wingdi/nf-wingdi-getboundsrect?branch=master)         | Gets the accumulated bounding rectangle for a device context.                                               |
| [**GetROP2**](/windows/win32/Wingdi/nf-wingdi-getrop2?branch=master)                     | Gets the foreground mix mode of a device context.                                                           |
| [**GetUpdateRect**](/windows/win32/Winuser/nf-winuser-getupdaterect?branch=master)         | Gets the coordinates of the smallest rectangle that encloses the update region of a window.                 |
| [**GetUpdateRgn**](/windows/win32/Winuser/nf-winuser-getupdatergn?branch=master)           | Gets the update region of a window.                                                                         |
| [**GetWindowDC**](/windows/win32/Winuser/nf-winuser-getwindowdc?branch=master)             | Gets the device context for a window, including title bar, menus, and scroll bars.                          |
| [**GetWindowRgn**](/windows/win32/Winuser/nf-winuser-getwindowrgn?branch=master)           | Gets a copy of the window region of a window.                                                               |
| [**GetWindowRgnBox**](/windows/win32/Winuser/nf-winuser-getwindowrgnbox?branch=master)     | Gets the dimensions of the tightest bounding rectangle for the window region of a window.                   |
| [**GrayString**](/windows/win32/Winuser/nf-winuser-graystringa?branch=master)               | Draws gray text at a location.                                                                              |
| [**InvalidateRect**](/windows/win32/Winuser/nf-winuser-invalidaterect?branch=master)       | Adds a rectangle to a window's update region.                                                               |
| [**InvalidateRgn**](/windows/win32/Winuser/nf-winuser-invalidatergn?branch=master)         | Invalidates the client area within a region.                                                                |
| [**LockWindowUpdate**](/windows/win32/Winuser/nf-winuser-lockwindowupdate?branch=master)   | Disables or enables drawing in a window.                                                                    |
| [**OutputProc**](/windows/win32/Winuser/nc-winuser-graystringproc?branch=master)               | A callback function used with the [**GrayString**](/windows/win32/Winuser/nf-winuser-graystringa?branch=master) function. It is used to draw a string.   |
| [**PaintDesktop**](/windows/win32/Winuser/nf-winuser-paintdesktop?branch=master)           | Fills the clipping region in a device context with a pattern.                                               |
| [**RedrawWindow**](/windows/win32/Winuser/nf-winuser-redrawwindow?branch=master)           | Updates a region in a window's client area.                                                                 |
| [**SetBkColor**](/windows/win32/Wingdi/nf-wingdi-setbkcolor?branch=master)               | Sets the background to a color value.                                                                       |
| [**SetBkMode**](/windows/win32/Wingdi/nf-wingdi-setbkmode?branch=master)                 | Sets the background mix mode of a device context.                                                           |
| [**SetBoundsRect**](/windows/win32/Wingdi/nf-wingdi-setboundsrect?branch=master)         | Controls the accumulation of bounding rectangle information for a device context.                           |
| [**SetROP2**](/windows/win32/Wingdi/nf-wingdi-setrop2?branch=master)                     | Sets the foreground mix mode.                                                                               |
| [**SetWindowRgn**](/windows/win32/Winuser/nf-winuser-setwindowrgn?branch=master)           | Sets the window region of a window.                                                                         |
| [**UpdateWindow**](/windows/win32/Winuser/nf-winuser-updatewindow?branch=master)           | Updates the client area of a window.                                                                        |
| [**ValidateRect**](/windows/win32/Winuser/nf-winuser-validaterect?branch=master)           | Validates the client area within a rectangle.                                                               |
| [**ValidateRgn**](/windows/win32/Winuser/nf-winuser-validatergn?branch=master)             | Validates the client area within a region.                                                                  |
| [**WindowFromDC**](/windows/win32/Winuser/nf-winuser-windowfromdc?branch=master)           | Returns a handle to the window associated with a device context.                                            |



 

 

 



