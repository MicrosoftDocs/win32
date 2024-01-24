---
description: The following functions are used with painting and drawing.
ms.assetid: ec18323e-c13b-4328-83bf-9e4ed4a712b8
title: Painting and Drawing Functions
ms.topic: article
ms.date: 05/31/2018
---

# Painting and Drawing Functions

The following functions are used with painting and drawing.



| Function                                       | Description                                                                                                 |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**BeginPaint**](/windows/desktop/api/Winuser/nf-winuser-beginpaint)               | Prepares a window for painting.                                                                             |
| [**DrawAnimatedRects**](/windows/desktop/api/Winuser/nf-winuser-drawanimatedrects) | Draws a rectangle and animates it to indicate icon or window activity.                                      |
| [**DrawCaption**](/windows/desktop/api/Winuser/nf-winuser-drawcaption)             | Draws a window caption.                                                                                     |
| [**DrawEdge**](/windows/desktop/api/Winuser/nf-winuser-drawedge)                   | Draws one or more edges of rectangle.                                                                       |
| [**DrawFocusRect**](/windows/desktop/api/Winuser/nf-winuser-drawfocusrect)         | Draws a rectangle in the style that indicates the rectangle has the focus.                                  |
| [**DrawFrameControl**](/windows/desktop/api/Winuser/nf-winuser-drawframecontrol)   | Draws a frame control.                                                                                      |
| [**DrawState**](/windows/desktop/api/Winuser/nf-winuser-drawstatea)                 | Displays an image and applies a visual effect to indicate a state.                                          |
| [**DrawStateProc**](/windows/desktop/api/Winuser/nc-winuser-drawstateproc)         | A callback function that renders a complex image for [**DrawState**](/windows/desktop/api/Winuser/nf-winuser-drawstatea).                        |
| [**EndPaint**](/windows/desktop/api/Winuser/nf-winuser-endpaint)                   | Marks the end of painting in a window.                                                                      |
| [**ExcludeUpdateRgn**](/windows/desktop/api/Winuser/nf-winuser-excludeupdatergn)   | Prevents drawing within invalid areas of a window.                                                          |
| [**GdiFlush**](/windows/desktop/api/Wingdi/nf-wingdi-gdiflush)                   | Flushes the calling thread's current batch.                                                                 |
| [**GdiGetBatchLimit**](/windows/desktop/api/Wingdi/nf-wingdi-gdigetbatchlimit)   | Returns the maximum number of function calls that can be accumulated in the calling thread's current batch. |
| [**GdiSetBatchLimit**](/windows/desktop/api/Wingdi/nf-wingdi-gdisetbatchlimit)   | Sets the maximum number of function calls that can be accumulated in the calling thread's current batch.    |
| [**GetBkColor**](/windows/desktop/api/Wingdi/nf-wingdi-getbkcolor)               | Returns the background color for a device context.                                                          |
| [**GetBkMode**](/windows/desktop/api/Wingdi/nf-wingdi-getbkmode)                 | Returns the background mix mode for a device context.                                                       |
| [**GetBoundsRect**](/windows/desktop/api/Wingdi/nf-wingdi-getboundsrect)         | Gets the accumulated bounding rectangle for a device context.                                               |
| [**GetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-getrop2)                     | Gets the foreground mix mode of a device context.                                                           |
| [**GetUpdateRect**](/windows/desktop/api/Winuser/nf-winuser-getupdaterect)         | Gets the coordinates of the smallest rectangle that encloses the update region of a window.                 |
| [**GetUpdateRgn**](/windows/desktop/api/Winuser/nf-winuser-getupdatergn)           | Gets the update region of a window.                                                                         |
| [**GetWindowDC**](/windows/desktop/api/Winuser/nf-winuser-getwindowdc)             | Gets the device context for a window, including title bar, menus, and scroll bars.                          |
| [**GetWindowRgn**](/windows/desktop/api/Winuser/nf-winuser-getwindowrgn)           | Gets a copy of the window region of a window.                                                               |
| [**GetWindowRgnBox**](/windows/desktop/api/Winuser/nf-winuser-getwindowrgnbox)     | Gets the dimensions of the tightest bounding rectangle for the window region of a window.                   |
| [**GrayString**](/windows/desktop/api/Winuser/nf-winuser-graystringa)               | Draws gray text at a location.                                                                              |
| [**InvalidateRect**](/windows/desktop/api/Winuser/nf-winuser-invalidaterect)       | Adds a rectangle to a window's update region.                                                               |
| [**InvalidateRgn**](/windows/desktop/api/Winuser/nf-winuser-invalidatergn)         | Invalidates the client area within a region.                                                                |
| [**LockWindowUpdate**](/windows/desktop/api/Winuser/nf-winuser-lockwindowupdate)   | Disables or enables drawing in a window.                                                                    |
| [**OutputProc**](/windows/desktop/api/Winuser/nc-winuser-graystringproc)               | A callback function used with the [**GrayString**](/windows/desktop/api/Winuser/nf-winuser-graystringa) function. It is used to draw a string.   |
| [**PaintDesktop**](/windows/desktop/api/Winuser/nf-winuser-paintdesktop)           | Fills the clipping region in a device context with a pattern.                                               |
| [**RedrawWindow**](/windows/desktop/api/Winuser/nf-winuser-redrawwindow)           | Updates a region in a window's client area.                                                                 |
| [**SetBkColor**](/windows/desktop/api/Wingdi/nf-wingdi-setbkcolor)               | Sets the background to a color value.                                                                       |
| [**SetBkMode**](/windows/desktop/api/Wingdi/nf-wingdi-setbkmode)                 | Sets the background mix mode of a device context.                                                           |
| [**SetBoundsRect**](/windows/desktop/api/Wingdi/nf-wingdi-setboundsrect)         | Controls the accumulation of bounding rectangle information for a device context.                           |
| [**SetROP2**](/windows/desktop/api/Wingdi/nf-wingdi-setrop2)                     | Sets the foreground mix mode.                                                                               |
| [**SetWindowRgn**](/windows/desktop/api/Winuser/nf-winuser-setwindowrgn)           | Sets the window region of a window.                                                                         |
| [**UpdateWindow**](/windows/desktop/api/Winuser/nf-winuser-updatewindow)           | Updates the client area of a window.                                                                        |
| [**ValidateRect**](/windows/desktop/api/Winuser/nf-winuser-validaterect)           | Validates the client area within a rectangle.                                                               |
| [**ValidateRgn**](/windows/desktop/api/Winuser/nf-winuser-validatergn)             | Validates the client area within a region.                                                                  |
| [**WindowFromDC**](/windows/desktop/api/Winuser/nf-winuser-windowfromdc)           | Returns a handle to the window associated with a device context.                                            |



 

 

 



