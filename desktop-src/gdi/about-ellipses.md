---
Description: An ellipse is a closed curve defined by two fixed points (f1 and f2 ) such that the sum of the distances (d1 +d2 ) from any point on the curve to the two fixed points is constant.
ms.assetid: c4aab4cf-9575-4817-b51f-aed4e3c27d2f
title: About Ellipses
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Ellipses

An ellipse is a closed curve defined by two fixed points (f1 and f2 ) such that the sum of the distances (d1 +d2 ) from any point on the curve to the two fixed points is constant. The following illustration shows an ellipse drawn by using the [**Ellipse**](/windows/win32/Wingdi/nf-wingdi-ellipse?branch=master) function.

![illustration showing an ellipse, two fixed points, two distances, and a bounding rectangle](images/csfsh-01.png)

When calling [**Ellipse**](/windows/win32/Wingdi/nf-wingdi-ellipse?branch=master), an application supplies the coordinates of the upper-left and lower-right corners of the ellipse's bounding rectangle. A *bounding rectangle* is the smallest rectangle completely surrounding the ellipse. When the system draws the ellipse, it excludes the right and lower sides if no world transformations are set. Therefore, for any rectangle measuring x units wide by y units high, the associated ellipse measures x1 units wide by y1 units high. If the application sets a world transformation by calling the [**SetWorldTransform**](/windows/win32/Wingdi/nf-wingdi-setworldtransform?branch=master) or [**ModifyWorldTransform**](/windows/win32/Wingdi/nf-wingdi-modifyworldtransform?branch=master) function, the system includes the right and lower sides.

 

 



