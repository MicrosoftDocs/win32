---
description: Nearly all applications use the screen to display the data they manipulate.
ms.assetid: 97d606a0-11d3-49c3-b045-8397f4bcfa54
title: About Painting and Drawing
ms.topic: article
ms.date: 05/31/2018
---

# About Painting and Drawing

Nearly all applications use the screen to display the data they manipulate. An application paints images, draws figures, and writes text so that the user can view data as it is created, edited, and printed. Microsoft Windows provides rich support for painting and drawing, but, because of the nature of multitasking operating systems, applications must cooperate with one another when accessing the screen.

To keep all applications functioning smoothly and cooperatively, the system manages all output to the screen. Applications use windows as their primary output device rather than the screen itself. The system supplies display device contexts that uniquely correspond to the windows. Applications use display device contexts to direct their output to the specified windows. Drawing in a window (directing output to it) prevents an application from interfering with the output of other applications and allows applications to coexist with one another while still taking full advantage of the graphics capabilities of the system.

-   [When to Draw in a Window](when-to-draw-in-a-window.md)
-   [The WM\_PAINT Message](the-wm-paint-message.md)
-   [Drawing Without the WM\_PAINT Message](drawing-without-the-wm-paint-message.md)
-   [Window Coordinate System](window-coordinate-system.md)
-   [Window Regions](window-regions.md)
-   [Window Background](window-background.md)
-   [Minimized Windows](minimized-windows.md)
-   [Resized Windows](resized-windows.md)
-   [Nonclient Area](nonclient-area.md)
-   [Child Window Update Region](child-window-update-region.md)
-   [Display Devices](display-devices.md)
-   [Window Update Lock](window-update-lock.md)
-   [Accumulated Bounding Rectangle](accumulated-bounding-rectangle.md)

 

 



