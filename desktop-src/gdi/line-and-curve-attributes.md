---
description: A device context (DC) contains attributes that affect line and curve output. The line and curve attributes include the current position, brush style, brush color, pen style, pen color, transformation, and so on.
ms.assetid: 9529b389-85f6-421f-8429-9b61cee56ef1
title: Line and Curve Attributes
ms.topic: article
ms.date: 05/31/2018
---

# Line and Curve Attributes

A device context (DC) contains attributes that affect line and curve output. The *line and curve attributes* include the current position, brush style, brush color, pen style, pen color, transformation, and so on.

The default current position for any DC is located at the point (0,0) in logical (or world) space. You can set these coordinates to a new position by calling the [**MoveToEx**](/windows/desktop/api/Wingdi/nf-wingdi-movetoex) function and passing a new set of coordinates.

> [!Note]  
> There are two sets of line- and curve-drawing functions. The first set retains the current position in a DC, and the second set alters the position. You can identify the functions that alter the current position by examining the function name. If the function name ends with the preposition "To", the function sets the current position to the ending point of the last line drawn ([**LineTo**](/windows/desktop/api/Wingdi/nf-wingdi-lineto), [**ArcTo**](/windows/desktop/api/Wingdi/nf-wingdi-arcto), [**PolylineTo**](/windows/desktop/api/Wingdi/nf-wingdi-polylineto), or [**PolyBezierTo**](/windows/desktop/api/Wingdi/nf-wingdi-polybezierto)). If the function name does not end with this preposition, it leaves the current position intact ([**Arc**](/windows/desktop/api/Wingdi/nf-wingdi-arc), [**Polyline**](/windows/desktop/api/Wingdi/nf-wingdi-polyline), or [**PolyBezier**](/windows/desktop/api/Wingdi/nf-wingdi-polybezier)).

 

The default brush is a solid white brush. An application can create a new brush by calling the [**CreateBrushIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbrushindirect) function. After creating a brush, the application can select it into its DC by calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function. Windows provides a complete set of functions to create, select, and alter the brush in an application's DC. For more information about these functions and about brushes in general, see [Brushes](brushes.md).

The default pen is a cosmetic, solid black pen that is one pixel wide. An application can create a pen by using the [**ExtCreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-extcreatepen) function. After creating a pen, your application can select it into its DC by calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function. Windows provides a complete set of functions to create, select, and alter the pen in an application's DC. For more information about these functions and about pens in general, see [Pens](pens.md).

The default transformation is the unity transformation (specified by the identity matrix). An application can specify a new transformation by calling the [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) function. Windows provides a complete set of functions to transform lines and curves by altering their width, location, and general appearance. For more information about these functions, see [Coordinate Spaces and Transformations](coordinate-spaces-and-transformations.md).

 

 



