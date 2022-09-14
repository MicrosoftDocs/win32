---
description: The coordinate system for a window is based on the coordinate system of the display device.
ms.assetid: 8590fc59-d7ad-4149-9a77-242037a11188
title: Window Coordinate System
ms.topic: article
ms.date: 05/31/2018
---

# Window Coordinate System

The coordinate system for a window is based on the coordinate system of the display device. The basic unit of measure is the device unit (typically, the pixel). Points on the screen are described by x- and y-coordinate pairs. The x-coordinates increase to the right; y-coordinates increase from top to bottom. The origin (0,0) for the system depends on the type of coordinates being used.

The system and applications specify the position of a window on the screen in *screen coordinates*. For screen coordinates, the origin is the upper-left corner of the screen. The full position of a window is often described by a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure containing the screen coordinates of two points that define the upper-left and lower-right corners of the window.

The system and applications specify the position of points in a window by using *client coordinates*. The origin in this case is the upper-left corner of the window or client area. Client coordinates ensure that an application can use consistent coordinate values while drawing in the window, regardless of the position of the window on the screen.

The dimensions of the client area are also described by a [**RECT**](/previous-versions//dd162897(v=vs.85)) structure that contains client coordinates for the area. In all cases, the upper-left coordinate of the rectangle is included in the window or client area, while the lower-right coordinate is excluded. Graphics operations in a window or client area are excluded from the right and lower edges of the enclosing rectangle.

Occasionally, applications may be required to map coordinates in one window to those of another window. An application can map coordinates by using the [**MapWindowPoints**](/windows/desktop/api/Winuser/nf-winuser-mapwindowpoints) function. If one of the windows is the desktop window, the function effectively converts screen coordinates to client coordinates and vice versa; the desktop window is always specified in screen coordinates.

 

 
