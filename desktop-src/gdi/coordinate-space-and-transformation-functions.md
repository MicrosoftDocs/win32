---
description: The following functions are used with coordinate spaces and transformations.
ms.assetid: 3ebcabf2-9718-47b2-aba0-7cc28fa42e5a
title: Coordinate Space and Transformation Functions
ms.topic: article
ms.date: 05/31/2018
---

# Coordinate Space and Transformation Functions

The following functions are used with coordinate spaces and transformations.



| Function                                                                       | Description                                                                                                                      |
|--------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [**ClientToScreen**](/windows/desktop/api/Winuser/nf-winuser-clienttoscreen)                                       | Converts the client-area coordinates of a specified point to screen coordinates.                                                 |
| [**CombineTransform**](/windows/desktop/api/Wingdi/nf-wingdi-combinetransform)                                   | Concatenates two world-space to page-space transformations.                                                                      |
| [**DPtoLP**](/windows/desktop/api/Wingdi/nf-wingdi-dptolp)                                                       | Converts device coordinates into logical coordinates.                                                                            |
| [**GetCurrentPositionEx**](/windows/desktop/api/Wingdi/nf-wingdi-getcurrentpositionex)                           | Retrieves the current position in logical coordinates.                                                                           |
| [**GetDisplayAutoRotationPreferences**](/previous-versions//dn376360(v=vs.85)) | Gets the orientation preferences of the display.                                                                                 |
| [**GetGraphicsMode**](/windows/desktop/api/Wingdi/nf-wingdi-getgraphicsmode)                                     | Retrieves the current graphics mode for the specified device context.                                                            |
| [**GetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-getmapmode)                                               | Retrieves the current mapping mode.                                                                                              |
| [**GetViewportExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-getviewportextex)                                   | Retrieves the x-extent and y-extent of the current viewport for the specified device context.                                    |
| [**GetViewportOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-getviewportorgex)                                   | Retrieves the x-coordinates and y-coordinates of the viewport origin for the specified device context.                           |
| [**GetWindowExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-getwindowextex)                                       | Retrieves the x-extent and y-extent of the window for the specified device context.                                              |
| [**GetWindowOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-getwindoworgex)                                       | Retrieves the x-coordinates and y-coordinates of the window origin for the specified device context.                             |
| [**GetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-getworldtransform)                                 | Retrieves the current world-space to page-space transformation.                                                                  |
| [**LPtoDP**](/windows/desktop/api/Wingdi/nf-wingdi-lptodp)                                                       | Converts logical coordinates into device coordinates.                                                                            |
| [**MapWindowPoints**](/windows/desktop/api/Winuser/nf-winuser-mapwindowpoints)                                     | Converts (maps) a set of points from a coordinate space relative to one window to a coordinate space relative to another window. |
| [**ModifyWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-modifyworldtransform)                           | Changes the world transformation for a device context using the specified mode.                                                  |
| [**OffsetViewportOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-offsetviewportorgex)                             | Modifies the viewport origin for a device context using the specified horizontal and vertical offsets.                           |
| [**OffsetWindowOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-offsetwindoworgex)                                 | Modifies the window origin for a device context using the specified horizontal and vertical offsets.                             |
| [**ScaleViewportExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-scaleviewportextex)                               | Modifies the viewport for a device context using the ratios formed by the specified multiplicands and divisors.                  |
| [**ScaleWindowExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-scalewindowextex)                                   | Modifies the window for a device context using the ratios formed by the specified multiplicands and divisors.                    |
| [**ScreenToClient**](/windows/desktop/api/Winuser/nf-winuser-screentoclient)                                       | Converts the screen coordinates of a specified point on the screen to client coordinates.                                        |
| [**SetDisplayAutoRotationPreferences**](/previous-versions//dn376361(v=vs.85)) | Sets the orientation preferences of the display.                                                                                 |
| [**SetGraphicsMode**](/windows/desktop/api/Wingdi/nf-wingdi-setgraphicsmode)                                     | Sets the graphics mode for the specified device context.                                                                         |
| [**SetMapMode**](/windows/desktop/api/Wingdi/nf-wingdi-setmapmode)                                               | Sets the mapping mode of the specified device context.                                                                           |
| [**SetViewportExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-setviewportextex)                                   | Sets the horizontal and vertical extents of the viewport for a device context by using the specified values.                     |
| [**SetViewportOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-setviewportorgex)                                   | Specifies which device point maps to the window origin (0,0).                                                                    |
| [**SetWindowExtEx**](/windows/desktop/api/Wingdi/nf-wingdi-setwindowextex)                                       | Sets the horizontal and vertical extents of the window for a device context by using the specified values.                       |
| [**SetWindowOrgEx**](/windows/desktop/api/Wingdi/nf-wingdi-setwindoworgex)                                       | Specifies which window point maps to the viewport origin (0,0).                                                                  |
| [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform)                                 | Sets a two-dimensional linear transformation between world space and page space for the specified device context.                |



 

 

 
