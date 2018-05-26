---
Description: The following functions are used to create, alter, or draw paths.
ms.assetid: 68390601-1542-41dc-bea0-78f6c3318806
title: Path Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Path Functions

The following functions are used to create, alter, or draw paths.



| Function                                       | Description                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AbortPath**](/windows/win32/Wingdi/nf-wingdi-abortpath?branch=master)                 | Closes and discards any paths in the specified device context.                                                                                                   |
| [**BeginPath**](/windows/win32/Wingdi/nf-wingdi-beginpath?branch=master)                 | Opens a path bracket in the specified device context.                                                                                                            |
| [**CloseFigure**](/windows/win32/Wingdi/nf-wingdi-closefigure?branch=master)             | Closes an open figure in a path.                                                                                                                                 |
| [**EndPath**](/windows/win32/Wingdi/nf-wingdi-endpath?branch=master)                     | Closes a path bracket and selects the path defined by the bracket into the specified device context.                                                             |
| [**FillPath**](/windows/win32/Wingdi/nf-wingdi-fillpath?branch=master)                   | Closes any open figures in the current path and fills the path's interior by using the current brush and polygon-filling mode.                                   |
| [**FlattenPath**](/windows/win32/Wingdi/nf-wingdi-flattenpath?branch=master)             | Transforms any curves in the path that is selected into the current device context (DC), turning each curve into a sequence of lines.                            |
| [**GetMiterLimit**](/windows/win32/Wingdi/nf-wingdi-getmiterlimit?branch=master)         | Retrieves the miter limit for the specified device context.                                                                                                      |
| [**GetPath**](/windows/win32/Wingdi/nf-wingdi-getpath?branch=master)                     | Retrieves the coordinates defining the endpoints of lines and the control points of curves found in the path that is selected into the specified device context. |
| [**PathToRegion**](/windows/win32/Wingdi/nf-wingdi-pathtoregion?branch=master)           | Creates a region from the path that is selected into the specified device context.                                                                               |
| [**SetMiterLimit**](/windows/win32/Wingdi/nf-wingdi-setmiterlimit?branch=master)         | Sets the limit for the length of miter joins for the specified device context.                                                                                   |
| [**StrokeAndFillPath**](/windows/win32/Wingdi/nf-wingdi-strokeandfillpath?branch=master) | Closes any open figures in a path, strokes the outline of the path by using the current pen, and fills its interior by using the current brush.                  |
| [**StrokePath**](/windows/win32/Wingdi/nf-wingdi-strokepath?branch=master)               | Renders the specified path by using the current pen.                                                                                                             |
| [**WidenPath**](/windows/win32/Wingdi/nf-wingdi-widenpath?branch=master)                 | Redefines the current path as the area that would be painted if the path were stroked using the pen currently selected into the given device context.            |



 

 

 



