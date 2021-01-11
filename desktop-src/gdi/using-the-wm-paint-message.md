---
description: You can use the WM\_PAINT message to carry out the drawing necessary for displaying information.
ms.assetid: cc56745f-95d0-4607-a206-1e7ed7109bf0
title: Using the WM_PAINT Message
ms.topic: article
ms.date: 05/31/2018
---

# Using the WM\_PAINT Message

You can use the [**WM\_PAINT**](wm-paint.md) message to carry out the drawing necessary for displaying information. Because the system sends WM\_PAINT messages to your application when your window must be updated or when you explicitly request an update, you can consolidate the code for drawing in your application's window procedure. You can then use this code whenever your application must draw either new or existing information.

The following sections show a variety of ways to use the WM\_PAINT message to draw in a window:

-   [Drawing in the Client Area](drawing-in-the-client-area.md)
-   [Redrawing the Entire Client Area](redrawing-the-entire-client-area.md)
-   [Redrawing in the Update Region](redrawing-in-the-update-region.md)
-   [Invalidating the Client Area](invalidating-the-client-area.md)
-   [Drawing a Minimized Window](drawing-a-minimized-window.md)
-   [Drawing a Custom Window Background](drawing-a-custom-window-background.md)

 

 



