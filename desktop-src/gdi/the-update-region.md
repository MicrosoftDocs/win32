---
description: The update region identifies the portion of a window that is out-of-date or invalid and in need of redrawing.
ms.assetid: '21228620-9491-4e1b-8658-15e9605951f2'
title: The Update Region
ms.topic: article
ms.date: 05/31/2018
---

# The Update Region

The *update region* identifies the portion of a window that is out-of-date or invalid and in need of redrawing. The system uses the update region to generate [**WM\_PAINT**](wm-paint.md) messages for applications and to minimize the time applications spend bringing the contents of their windows up to date. The system adds only the invalid portion of the window to the update region, requiring only that portion to be drawn.

When the system determines that a window needs updating, it sets the dimensions of the update region to the invalid portion of the window. Setting the update region does not immediately cause the application to draw. Instead, the application continues retrieving messages from the application message queue until no messages remain. The system then checks the update region, and if the region is not empty (non-NULL), it sends a [**WM\_PAINT**](wm-paint.md) message to the window procedure.

An application can use the update region to generate its [**WM\_PAINT**](wm-paint.md) messages. For example, an application that loads data from open files typically sets the update region while loading so that new data is drawn during processing of the next **WM\_PAINT** message. In general, an application should not draw at the time its data changes, but route all drawing operations through the **WM\_PAINT** message.

 

 



