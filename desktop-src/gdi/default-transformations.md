---
description: Whenever an application creates a DC and immediately begins calling GDI drawing or output functions, it takes advantage of the default page-space to device-space, and device-space to client-area transformations.
ms.assetid: 64465eb4-d23a-44e7-ad0d-060b195d37b3
title: Default Transformations
ms.topic: article
ms.date: 05/31/2018
---

# Default Transformations

Whenever an application creates a DC and immediately begins calling GDI drawing or output functions, it takes advantage of the default page-space to device-space, and device-space to client-area transformations. A world-to-page space transformation cannot happen until the application first calls the [**SetGraphicsMode**](/windows/desktop/api/Wingdi/nf-wingdi-setgraphicsmode) function to set the mode to GM\_ADVANCED and then calls the [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) function.

Use of MM\_TEXT (the default page-space to device-space transformation) results in a one-to-one mapping; that is, a given point in page space maps to the same point in device space. As previously mentioned, this transformation is not specified by a matrix. Instead, it is obtained by dividing the width of the viewport by the width of the window and the height of the viewport by the height of the window. In the default case, the viewport dimensions are 1-pixel by 1-pixel and the window dimensions are 1-page unit by 1-page unit.

The device-space to physical-device (client area, desktop, or printer paper) transformation always results in a one-to-one mapping; that is, one unit in device space is always equivalent to one unit in the client area, on the desktop, or on a page. The sole purpose of this transformation is translation; it ensures that output appears correctly in an application's window no matter where that window is moved on the desktop.

The one unique aspect of MM\_TEXT is the orientation of the y-axis in page space. In MM\_TEXT, the positive y-axis extends downward and the negative y-axis extends upward.

 

 



