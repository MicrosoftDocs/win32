---
Description: The following functions are used with coordinate spaces and transformations.
ms.assetid: 3ebcabf2-9718-47b2-aba0-7cc28fa42e5a
title: Coordinate Space and Transformation Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Coordinate Space and Transformation Functions

The following functions are used with coordinate spaces and transformations.



| Function                                                                       | Description                                                                                                                      |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**ClientToScreen**](/windows/win32/Winuser/nf-winuser-clienttoscreen?branch=master)                                       | Converts the client-area coordinates of a specified point to screen coordinates.                                                 |
| [**CombineTransform**](/windows/win32/Wingdi/nf-wingdi-combinetransform?branch=master)                                   | Concatenates two world-space to page-space transformations.                                                                      |
| [**DPtoLP**](/windows/win32/Wingdi/nf-wingdi-dptolp?branch=master)                                                       | Converts device coordinates into logical coordinates.                                                                            |
| [**GetCurrentPositionEx**](/windows/win32/Wingdi/nf-wingdi-getcurrentpositionex?branch=master)                           | Retrieves the current position in logical coordinates.                                                                           |
| [**GetDisplayAutoRotationPreferences**](/windows/win32/Winuser/?branch=master) | Gets the orientation preferences of the display.                                                                                 |
| [**GetGraphicsMode**](/windows/win32/Wingdi/nf-wingdi-getgraphicsmode?branch=master)                                     | Retrieves the current graphics mode for the specified device context.                                                            |
| [**GetMapMode**](/windows/win32/Wingdi/nf-wingdi-getmapmode?branch=master)                                               | Retrieves the current mapping mode.                                                                                              |
| [**GetViewportExtEx**](/windows/win32/Wingdi/nf-wingdi-getviewportextex?branch=master)                                   | Retrieves the x-extent and y-extent of the current viewport for the specified device context.                                    |
| [**GetViewportOrgEx**](/windows/win32/Wingdi/nf-wingdi-getviewportorgex?branch=master)                                   | Retrieves the x-coordinates and y-coordinates of the viewport origin for the specified device context.                           |
| [**GetWindowExtEx**](/windows/win32/Wingdi/nf-wingdi-getwindowextex?branch=master)                                       | Retrieves the x-extent and y-extent of the window for the specified device context.                                              |
| [**GetWindowOrgEx**](/windows/win32/Wingdi/nf-wingdi-getwindoworgex?branch=master)                                       | Retrieves the x-coordinates and y-coordinates of the window origin for the specified device context.                             |
| [**GetWorldTransform**](/windows/win32/Wingdi/nf-wingdi-getworldtransform?branch=master)                                 | Retrieves the current world-space to page-space transformation.                                                                  |
| [**LPtoDP**](/windows/win32/Wingdi/nf-wingdi-lptodp?branch=master)                                                       | Converts logical coordinates into device coordinates.                                                                            |
| [**MapWindowPoints**](/windows/win32/Winuser/nf-winuser-mapwindowpoints?branch=master)                                     | Converts (maps) a set of points from a coordinate space relative to one window to a coordinate space relative to another window. |
| [**ModifyWorldTransform**](/windows/win32/Wingdi/nf-wingdi-modifyworldtransform?branch=master)                           | Changes the world transformation for a device context using the specified mode.                                                  |
| [**OffsetViewportOrgEx**](/windows/win32/Wingdi/nf-wingdi-offsetviewportorgex?branch=master)                             | Modifies the viewport origin for a device context using the specified horizontal and vertical offsets.                           |
| [**OffsetWindowOrgEx**](/windows/win32/Wingdi/nf-wingdi-offsetwindoworgex?branch=master)                                 | Modifies the window origin for a device context using the specified horizontal and vertical offsets.                             |
| [**ScaleViewportExtEx**](/windows/win32/Wingdi/nf-wingdi-scaleviewportextex?branch=master)                               | Modifies the viewport for a device context using the ratios formed by the specified multiplicands and divisors.                  |
| [**ScaleWindowExtEx**](/windows/win32/Wingdi/nf-wingdi-scalewindowextex?branch=master)                                   | Modifies the window for a device context using the ratios formed by the specified multiplicands and divisors.                    |
| [**ScreenToClient**](/windows/win32/Winuser/nf-winuser-screentoclient?branch=master)                                       | Converts the screen coordinates of a specified point on the screen to client coordinates.                                        |
| [**SetDisplayAutoRotationPreferences**](/windows/win32/Winuser/?branch=master) | Sets the orientation preferences of the display.                                                                                 |
| [**SetGraphicsMode**](/windows/win32/Wingdi/nf-wingdi-setgraphicsmode?branch=master)                                     | Sets the graphics mode for the specified device context.                                                                         |
| [**SetMapMode**](/windows/win32/Wingdi/nf-wingdi-setmapmode?branch=master)                                               | Sets the mapping mode of the specified device context.                                                                           |
| [**SetViewportExtEx**](/windows/win32/Wingdi/nf-wingdi-setviewportextex?branch=master)                                   | Sets the horizontal and vertical extents of the viewport for a device context by using the specified values.                     |
| [**SetViewportOrgEx**](/windows/win32/Wingdi/nf-wingdi-setviewportorgex?branch=master)                                   | Specifies which device point maps to the window origin (0,0).                                                                    |
| [**SetWindowExtEx**](/windows/win32/Wingdi/nf-wingdi-setwindowextex?branch=master)                                       | Sets the horizontal and vertical extents of the window for a device context by using the specified values.                       |
| [**SetWindowOrgEx**](/windows/win32/Wingdi/nf-wingdi-setwindoworgex?branch=master)                                       | Specifies which window point maps to the viewport origin (0,0).                                                                  |
| [**SetWorldTransform**](/windows/win32/Wingdi/nf-wingdi-setworldtransform?branch=master)                                 | Sets a two-dimensional linear transformation between world space and page space for the specified device context.                |



 

 

 



