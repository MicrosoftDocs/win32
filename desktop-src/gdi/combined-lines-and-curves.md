---
description: In addition to drawing lines or curves, applications can draw combinations of line and curve output by calling a single function. For example, an application can draw the outline of a pie chart by calling the AngleArc function.
ms.assetid: 0abcc20c-ba89-4eb4-bbd1-7ea27d367fb8
title: Combined Lines and Curves
ms.topic: article
ms.date: 05/31/2018
---

# Combined Lines and Curves

In addition to drawing lines or curves, applications can draw combinations of line and curve output by calling a single function. For example, an application can draw the outline of a pie chart by calling the [**AngleArc**](/windows/desktop/api/Wingdi/nf-wingdi-anglearc) function.

The [**AngleArc**](/windows/desktop/api/Wingdi/nf-wingdi-anglearc) function draws an arc along a circle's perimeter and draws a line connecting the starting point of the arc to the circle's center. In addition to using the **AngleArc** function, an application can also combine line and irregular curve output by using the [**PolyDraw**](/windows/desktop/api/Wingdi/nf-wingdi-polydraw) function.

 

 



