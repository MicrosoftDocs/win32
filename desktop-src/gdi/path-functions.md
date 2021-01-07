---
description: The following functions are used to create, alter, or draw paths.
ms.assetid: 68390601-1542-41dc-bea0-78f6c3318806
title: Path Functions (Windows GDI)
ms.topic: article
ms.date: 05/31/2018
---

# Path Functions (Windows GDI)

The following functions are used to create, alter, or draw paths.



| Function                                       | Description                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortPath**](/windows/desktop/api/Wingdi/nf-wingdi-abortpath)                 | Closes and discards any paths in the specified device context.                                                                                                   |
| [**BeginPath**](/windows/desktop/api/Wingdi/nf-wingdi-beginpath)                 | Opens a path bracket in the specified device context.                                                                                                            |
| [**CloseFigure**](/windows/desktop/api/Wingdi/nf-wingdi-closefigure)             | Closes an open figure in a path.                                                                                                                                 |
| [**EndPath**](/windows/desktop/api/Wingdi/nf-wingdi-endpath)                     | Closes a path bracket and selects the path defined by the bracket into the specified device context.                                                             |
| [**FillPath**](/windows/desktop/api/Wingdi/nf-wingdi-fillpath)                   | Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.                                   |
| [**FlattenPath**](/windows/desktop/api/Wingdi/nf-wingdi-flattenpath)             | Transforms any curves in the path that is selected into the current device context (DC), turning each curve into a sequence of lines.                            |
| [**GetMiterLimit**](/windows/desktop/api/Wingdi/nf-wingdi-getmiterlimit)         | Retrieves the miter limit for the specified device context.                                                                                                      |
| [**GetPath**](/windows/desktop/api/Wingdi/nf-wingdi-getpath)                     | Retrieves the coordinates defining the endpoints of lines and the control points of curves found in the path that is selected into the specified device context. |
| [**PathToRegion**](/windows/desktop/api/Wingdi/nf-wingdi-pathtoregion)           | Creates a region from the path that is selected into the specified device context.                                                                               |
| [**SetMiterLimit**](/windows/desktop/api/Wingdi/nf-wingdi-setmiterlimit)         | Sets the limit for the length of miter joins for the specified device context.                                                                                   |
| [**StrokeAndFillPath**](/windows/desktop/api/Wingdi/nf-wingdi-strokeandfillpath) | Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush.                  |
| [**StrokePath**](/windows/desktop/api/Wingdi/nf-wingdi-strokepath)               | Renders the specified path by using the current pen.                                                                                                             |
| [**WidenPath**](/windows/desktop/api/Wingdi/nf-wingdi-widenpath)                 | Redefines the current path as the area that would be painted if the path were stroked using the pen currently selected into the given device context.            |



 

 

 



