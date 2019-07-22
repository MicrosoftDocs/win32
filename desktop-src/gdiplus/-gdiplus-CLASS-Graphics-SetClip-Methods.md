---
Description: This topic lists the SetClip methods of the Graphics class. For a complete list of methods for the Graphics class, see Graphics.
ms.assetid: e8348373-da79-4d33-8bea-d594985493d4
title: Graphics.SetClip methods
ms.date: 07/02/2019
ms.topic: reference
---

# Graphics.SetClip methods

This topic lists the SetClip methods of the [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) class. For a complete list of methods for the **Graphics** class, see [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx).

### Overload list



| Method                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetClip(HRGN,CombineMode)**](https://msdn.microsoft.com/library/ms535827(v=VS.85).aspx)                     | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535827(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and a GDI region.<br/>                                                                                                                                                                                                          |
| [**SetClip(Rect&,CombineMode)**](https://msdn.microsoft.com/library/ms535826(v=VS.85).aspx)   | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535826(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and a rectangle.<br/>                                                                                                                                                                                          |
| [**SetClip(RectF&,CombineMode)**](https://msdn.microsoft.com/library/ms535828(v=VS.85).aspx) | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535828(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and a rectangle.<br/>                                                                                                                                                                                         |
| [**SetClip(Region\*,CombineMode)**](https://msdn.microsoft.com/library/ms535825(v=VS.85).aspx)               | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535825(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and the region specified by a [**Region**](https://msdn.microsoft.com/library/ms534501(v=VS.85).aspx) object.<br/>                                                                                                                                      |
| [**SetClip(Graphics\*,CombineMode)**](https://msdn.microsoft.com/library/ms535823(v=VS.85).aspx)                  | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535823(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and the clipping region of another **Graphics** object.<br/>                                                                                                                                                                       |
| [**SetClip(GraphicsPath\*,CombineMode)**](https://msdn.microsoft.com/library/ms535824(v=VS.85).aspx)           | The [**Graphics::SetClip**](https://msdn.microsoft.com/library/ms535824(v=VS.85).aspx) method updates the clipping region of this [**Graphics**](https://msdn.microsoft.com/library/ms534453(v=VS.85).aspx) object to a region that is the combination of itself and the region specified by a graphics path. If a figure in the path is not closed, this method treats the nonclosed figure as if it were closed by a straight line that connects the figure's starting and ending points.<br/> |



 

 




