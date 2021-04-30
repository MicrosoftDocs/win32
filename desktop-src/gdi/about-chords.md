---
description: A chord is a region bounded by the intersection of an ellipse and a line segment called a secant. The following illustration shows a chord drawn by using the Chord function.
ms.assetid: 9aa35b39-06f2-48bf-b32c-3e3e32fab68b
title: About Chords
ms.topic: article
ms.date: 05/31/2018
---

# About Chords

A *chord* is a region bounded by the intersection of an ellipse and a line segment called a *secant*. The following illustration shows a chord drawn by using the [**Chord**](/windows/desktop/api/Wingdi/nf-wingdi-chord) function.

![illustration of an elipse, showing two radials, a secant, and a chord](images/csfsh-02.png)

When calling [**Chord**](/windows/win32/api/wingdi/nf-wingdi-chord), an application supplies the coordinates of the upper-left and lower-right corners of the ellipse's bounding rectangle, as well as the coordinates of two points defining two radials. A radial is a line drawn from the center of an ellipse's bounding rectangle to a point on the ellipse.

When the system draws the curved part of the chord, it does so by using the current arc direction for the specified device context. The default arc direction is counterclockwise. You can have your application reset the arc direction by calling the [**SetArcDirection**](/windows/desktop/api/Wingdi/nf-wingdi-setarcdirection) function.

 

 
