---
Description: 'The following functions are used with painting and drawing.'
ms.assetid: 'ec18323e-c13b-4328-83bf-9e4ed4a712b8'
title: Painting and Drawing Functions
---

# Painting and Drawing Functions

The following functions are used with painting and drawing.



| Function                                       | Description                                                                                                 |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| [**BeginPaint**](beginpaint.md)               | Prepares a window for painting.                                                                             |
| [**DrawAnimatedRects**](drawanimatedrects.md) | Draws a rectangle and animates it to indicate icon or window activity.                                      |
| [**DrawCaption**](drawcaption.md)             | Draws a window caption.                                                                                     |
| [**DrawEdge**](drawedge.md)                   | Draws one or more edges of rectangle.                                                                       |
| [**DrawFocusRect**](drawfocusrect.md)         | Draws a rectangle in the style that indicates the rectangle has the focus.                                  |
| [**DrawFrameControl**](drawframecontrol.md)   | Draws a frame control.                                                                                      |
| [**DrawState**](drawstate.md)                 | Displays an image and applies a visual effect to indicate a state.                                          |
| [**DrawStateProc**](drawstateproc.md)         | A callback function that renders a complex image for [**DrawState**](drawstate.md).                        |
| [**EndPaint**](endpaint.md)                   | Marks the end of painting in a window.                                                                      |
| [**ExcludeUpdateRgn**](excludeupdatergn.md)   | Prevents drawing within invalid areas of a window.                                                          |
| [**GdiFlush**](gdiflush.md)                   | Flushes the calling thread's current batch.                                                                 |
| [**GdiGetBatchLimit**](gdigetbatchlimit.md)   | Returns the maximum number of function calls that can be accumulated in the calling thread's current batch. |
| [**GdiSetBatchLimit**](gdisetbatchlimit.md)   | Sets the maximum number of function calls that can be accumulated in the calling thread's current batch.    |
| [**GetBkColor**](getbkcolor.md)               | Returns the background color for a device context.                                                          |
| [**GetBkMode**](getbkmode.md)                 | Returns the background mix mode for a device context.                                                       |
| [**GetBoundsRect**](getboundsrect.md)         | Gets the accumulated bounding rectangle for a device context.                                               |
| [**GetROP2**](getrop2.md)                     | Gets the foreground mix mode of a device context.                                                           |
| [**GetUpdateRect**](getupdaterect.md)         | Gets the coordinates of the smallest rectangle that encloses the update region of a window.                 |
| [**GetUpdateRgn**](getupdatergn.md)           | Gets the update region of a window.                                                                         |
| [**GetWindowDC**](getwindowdc.md)             | Gets the device context for a window, including title bar, menus, and scroll bars.                          |
| [**GetWindowRgn**](getwindowrgn.md)           | Gets a copy of the window region of a window.                                                               |
| [**GetWindowRgnBox**](getwindowrgnbox.md)     | Gets the dimensions of the tightest bounding rectangle for the window region of a window.                   |
| [**GrayString**](graystring.md)               | Draws gray text at a location.                                                                              |
| [**InvalidateRect**](invalidaterect.md)       | Adds a rectangle to a window's update region.                                                               |
| [**InvalidateRgn**](invalidatergn.md)         | Invalidates the client area within a region.                                                                |
| [**LockWindowUpdate**](lockwindowupdate.md)   | Disables or enables drawing in a window.                                                                    |
| [**OutputProc**](outputproc.md)               | A callback function used with the [**GrayString**](graystring.md) function. It is used to draw a string.   |
| [**PaintDesktop**](paintdesktop.md)           | Fills the clipping region in a device context with a pattern.                                               |
| [**RedrawWindow**](redrawwindow.md)           | Updates a region in a window's client area.                                                                 |
| [**SetBkColor**](setbkcolor.md)               | Sets the background to a color value.                                                                       |
| [**SetBkMode**](setbkmode.md)                 | Sets the background mix mode of a device context.                                                           |
| [**SetBoundsRect**](setboundsrect.md)         | Controls the accumulation of bounding rectangle information for a device context.                           |
| [**SetROP2**](setrop2.md)                     | Sets the foreground mix mode.                                                                               |
| [**SetWindowRgn**](setwindowrgn.md)           | Sets the window region of a window.                                                                         |
| [**UpdateWindow**](updatewindow.md)           | Updates the client area of a window.                                                                        |
| [**ValidateRect**](validaterect.md)           | Validates the client area within a rectangle.                                                               |
| [**ValidateRgn**](validatergn.md)             | Validates the client area within a region.                                                                  |
| [**WindowFromDC**](windowfromdc.md)           | Returns a handle to the window associated with a device context.                                            |



 

 

 



