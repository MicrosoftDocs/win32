---
description: This topic lists the SetClip methods of the Graphics class. For a complete list of methods for the Graphics class, see Graphics.
ms.assetid: e8348373-da79-4d33-8bea-d594985493d4
title: Graphics.SetClip methods
ms.date: 07/02/2019
ms.topic: reference
---

# Graphics.SetClip methods

This topic lists the SetClip methods of the [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class. For a complete list of methods for the **Graphics** class, see [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics).

### Overload list



| Method                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**SetClip(HRGN,CombineMode)**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inhrgn_incombinemode))                     | The [**Graphics::SetClip**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inhrgn_incombinemode)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and a GDI region.<br/>                                                                                                                                                                                                          |
| [**SetClip(Rect&,CombineMode)**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstrect__incombinemode))   | The [**Graphics::SetClip**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstrect__incombinemode)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and a rectangle.<br/>                                                                                                                                                                                          |
| [**SetClip(RectF&,CombineMode)**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstrectf__incombinemode)) | The [**Graphics::SetClip**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstrectf__incombinemode)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and a rectangle.<br/>                                                                                                                                                                                         |
| [**SetClip(Region\*,CombineMode)**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstregion_incombinemode))               | The [**Graphics::SetClip**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstregion_incombinemode)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and the region specified by a [**Region**](/windows/win32/api/gdiplusheaders/nl-gdiplusheaders-region) object.<br/>                                                                                                                                      |
| [**SetClip(Graphics\*,CombineMode)**](/previous-versions//ms535823(v=vs.85))                  | The [**Graphics::SetClip**](/previous-versions//ms535823(v=vs.85)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and the clipping region of another **Graphics** object.<br/>                                                                                                                                                                       |
| [**SetClip(GraphicsPath\*,CombineMode)**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstgraphicspath_incombinemode))           | The [**Graphics::SetClip**](/windows/win32/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(inconstgraphicspath_incombinemode)) method updates the clipping region of this [**Graphics**](/windows/win32/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) object to a region that is the combination of itself and the region specified by a graphics path. If a figure in the path is not closed, this method treats the nonclosed figure as if it were closed by a straight line that connects the figure's starting and ending points.<br/> |



 

 
