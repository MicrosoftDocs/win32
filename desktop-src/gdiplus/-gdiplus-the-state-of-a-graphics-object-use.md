---
Description: The Graphics class is at the heart of Windows GDI+. To draw anything, you create a Graphics object, set its properties, and call its methods ( DrawLine, DrawImage, DrawString, and the like).
ms.assetid: 7d70f9fe-c0b2-4d65-815d-483d06df96ad
title: The State of a Graphics Object
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The State of a Graphics Object

The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class is at the heart of Windows GDI+. To draw anything, you create a **Graphics** object, set its properties, and call its methods ( [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master), [DrawImage](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawimage(in image,in const point &)?branch=master), [DrawString](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master), and the like).

The following example constructs a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object and then calls the [**Graphics::DrawRectangle**](/windows/win32/Gdiplusgraphics/?branch=master) method of the **Graphics** object:


```
HDC          hdc;
PAINTSTRUCT  ps;

hdc = BeginPaint(hWnd, &amp;ps);
{
   Graphics graphics(hdc);
   Pen pen(Color(255, 0, 0, 255));  // opaque blue
   graphics.DrawRectangle(&amp;pen, 10, 10, 200, 100);
}
EndPaint(hWnd, &amp;ps);
```



In the preceding code, the [BeginPaint](http://msdn.microsoft.com/library/en-us/gdi/pantdraw_7b78.asp) method returns a handle to a device context, and that handle is passed to the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) constructor. A device context is a structure (maintained by Windows) that holds information about the particular display device being used.

## Graphics State

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object does more than provide drawing methods, such as [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) and [DrawRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &)?branch=master). A **Graphics** object also maintains graphics state, which can be divided into the following categories:

-   A link to a device context
-   Quality settings
-   Transformations
-   A clipping region

### Device Context

As an application programmer, you don't have to think about the interaction between a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and its device context. This interaction is handled by GDI+ behind the scenes.

### Quality Settings

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object has several properties that influence the quality of the items that are drawn on the screen. You can view and manipulate these properties by calling get and set methods. For example, you can call the [**Graphics::SetTextRenderingHint**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-settextrenderinghint?branch=master) method to specify the type of antialiasing (if any) applied to text. Other set methods that influence quality are [**Graphics::SetSmoothingMode**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-setsmoothingmode?branch=master), [**Graphics::SetCompositingMode**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-setcompositingmode?branch=master), [**Graphics::SetCompositingQuality**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-setcompositingquality?branch=master), and [**Graphics::SetInterpolationMode**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-setinterpolationmode?branch=master).

The following example draws two ellipses, one with the smoothing mode set to [****SmoothingModeAntiAlias****](/windows/win32/Gdiplusenums/ne-gdiplusenums-smoothingmode?branch=master) and one with the smoothing mode set to [****SmoothingModeHighSpeed****](/windows/win32/Gdiplusenums/ne-gdiplusenums-smoothingmode?branch=master):


```
Graphics graphics(hdc);
Pen pen(Color(255, 0, 255, 0));  // opaque green

graphics.SetSmoothingMode(SmoothingModeAntiAlias);
graphics.DrawEllipse(&amp;pen, 0, 0, 200, 100);
graphics.SetSmoothingMode(SmoothingModeHighSpeed);
graphics.DrawEllipse(&amp;pen, 0, 150, 200, 100);
```



### Transformations

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object maintains two transformations (world and page) that are applied to all items drawn by that **Graphics** object. Any affine transformation can be stored in the world transformation. Affine transformations include scaling, rotating, reflecting, skewing, and translating. The page transformation can be used for scaling and for changing units (for example, pixels to inches). For more information on transformations, see [Coordinate Systems and Transformations](-gdiplus-coordinate-systems-and-transformations-about.md).

The following example sets the world and page transformations of a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object. The world transformation is set to a 30-degree rotation. The page transformation is set so that the coordinates passed to the second [**Graphics::DrawEllipse**](/windows/win32/Gdiplusgraphics/?branch=master) will be treated as millimeters instead of pixels. The code makes two identical calls to the **Graphics::DrawEllipse** method. The world transformation is applied to the first **Graphics::DrawEllipse** call, and both transformations (world and page) are applied to the second **Graphics::DrawEllipse** call.


```
Graphics graphics(hdc);
Pen pen(Color(255, 255, 0, 0));

graphics.ResetTransform();
graphics.RotateTransform(30.0f);            // World transformation
graphics.DrawEllipse(&amp;pen, 30, 0, 50, 25);
graphics.SetPageUnit(UnitMillimeter);       // Page transformation
graphics.DrawEllipse(&amp;pen, 30, 0, 50, 25);
```



The following illustration shows the two ellipses. Note that the 30-degree rotation is about the origin of the coordinate system (upper-left corner of the client area), not about the centers of the ellipses. Also note that the pen width of 1 means 1 pixel for the first ellipse and 1 millimeter for the second ellipse.

![screen shot of a window containing a small, thin ellipse and a large, thicker ellipse](images/graphicsascon1.png)

 

### Clipping Region

A [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object maintains a clipping region that applies to all items drawn by that **Graphics** object. You can set the clipping region by calling the [SetClip](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-setclip(in const graphicspath,in combinemode)?branch=master) method.

The following example creates a plus-shaped region by forming the union of two rectangles. That region is designated as the clipping region of a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object. Then the code draws two lines that are restricted to the interior of the clipping region.


```
Graphics graphics(hdc);
Pen pen(Color(255, 255, 0, 0), 5);  // opaque red, width 5
SolidBrush brush(Color(255, 180, 255, 255));  // opaque aqua

// Create a plus-shaped region by forming the union of two rectangles.
Region region(Rect(50, 0, 50, 150));
region.Union(Rect(0, 50, 150, 50));
graphics.FillRegion(&amp;brush, &amp;region);

// Set the clipping region.
graphics.SetClip(&amp;region);

// Draw two clipped lines.
graphics.DrawLine(&amp;pen, 0, 30, 150, 160);
graphics.DrawLine(&amp;pen, 40, 20, 190, 150);
```



The following illustration shows the clipped lines.

![illustration showing a colored shape crossed by two diagonal red lines](images/graphicsascon2.png)

 

 



