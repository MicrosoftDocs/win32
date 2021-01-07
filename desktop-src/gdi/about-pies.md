---
description: A pie is a region bounded by the intersection of an ellipse curve and two radials. The following illustration shows a pie drawn by using the Pie function.
ms.assetid: 9ba7834e-02d2-4335-94c3-ab2f5c355619
title: About Pies
ms.topic: article
ms.date: 05/31/2018
---

# About Pies

A *pie* is a region bounded by the intersection of an ellipse curve and two radials. The following illustration shows a pie drawn by using the [**Pie**](/windows/desktop/api/Wingdi/nf-wingdi-pie) function.

![illustration showing an ellipse with a shaded pie](images/csfsh-03.png)

When calling [**Pie**](/windows/win32/api/wingdi/nf-wingdi-pie), an application supplies the coordinates of the upper-left and lower-right corners of the ellipse's bounding rectangle, as well as the coordinates of two points defining two radials.

When the system draws the curved part of the pie, it uses the current arc direction for the given device context. The default arc direction is counterclockwise. An application can reset the arc direction by calling the [**SetArcDirection**](/windows/desktop/api/Wingdi/nf-wingdi-setarcdirection) function.

 

 
