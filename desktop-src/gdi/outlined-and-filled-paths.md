---
description: An application can draw the outline of a path by calling the StrokePath function, it can fill the interior of a path by calling the FillPath function, and it can both outline and fill the path by calling the StrokeAndFillPath function.
ms.assetid: e3e82676-3095-43f0-9fb4-959f925e66c2
title: Outlined and Filled Paths
ms.topic: article
ms.date: 05/31/2018
---

# Outlined and Filled Paths

An application can draw the outline of a path by calling the [**StrokePath**](/windows/desktop/api/Wingdi/nf-wingdi-strokepath) function, it can fill the interior of a path by calling the [**FillPath**](/windows/desktop/api/Wingdi/nf-wingdi-fillpath) function, and it can both outline and fill the path by calling the [**StrokeAndFillPath**](/windows/desktop/api/Wingdi/nf-wingdi-strokeandfillpath) function.

Whenever an application fills a path, the system uses the DC's current fill mode. An application can retrieve this mode by calling the [**GetPolyFillMode**](/windows/desktop/api/Wingdi/nf-wingdi-getpolyfillmode) function, and it can set a new fill mode by calling the [**SetPolyFillMode**](/windows/desktop/api/Wingdi/nf-wingdi-setpolyfillmode) function. For a description of the two fill modes, see [Regions](regions.md).

The following illustration shows the cross-section of an object created by a computer-aided design (CAD) application using paths that were both outlined and filled.

![illustration showing the cross-sectional view of an object, with various parts indicated by different fill patterns](images/cspth-01.png)

 

 



