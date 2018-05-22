---
Description: 'The following functions are used to create, alter, or draw paths.'
ms.assetid: '68390601-1542-41dc-bea0-78f6c3318806'
title: Path Functions
---

# Path Functions

The following functions are used to create, alter, or draw paths.



| Function                                       | Description                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortPath**](abortpath.md)                 | Closes and discards any paths in the specified device context.                                                                                                   |
| [**BeginPath**](beginpath.md)                 | Opens a path bracket in the specified device context.                                                                                                            |
| [**CloseFigure**](closefigure.md)             | Closes an open figure in a path.                                                                                                                                 |
| [**EndPath**](endpath.md)                     | Closes a path bracket and selects the path defined by the bracket into the specified device context.                                                             |
| [**FillPath**](fillpath.md)                   | Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.                                   |
| [**FlattenPath**](flattenpath.md)             | Transforms any curves in the path that is selected into the current device context (DC), turning each curve into a sequence of lines.                            |
| [**GetMiterLimit**](getmiterlimit.md)         | Retrieves the miter limit for the specified device context.                                                                                                      |
| [**GetPath**](getpath.md)                     | Retrieves the coordinates defining the endpoints of lines and the control points of curves found in the path that is selected into the specified device context. |
| [**PathToRegion**](pathtoregion.md)           | Creates a region from the path that is selected into the specified device context.                                                                               |
| [**SetMiterLimit**](setmiterlimit.md)         | Sets the limit for the length of miter joins for the specified device context.                                                                                   |
| [**StrokeAndFillPath**](strokeandfillpath.md) | Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush.                  |
| [**StrokePath**](strokepath.md)               | Renders the specified path by using the current pen.                                                                                                             |
| [**WidenPath**](widenpath.md)                 | Redefines the current path as the area that would be painted if the path were stroked using the pen currently selected into the given device context.            |



 

 

 



