---
Description: One of the properties of the Graphics class is the clipping region. All drawing done by a given Graphics object is restricted to the clipping region of that Graphics object. You can set the clipping region by calling the SetClip method.
ms.assetid: 816a5845-ca03-46c6-bdda-e6a7d02ff614
title: Clipping with a Region
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Clipping with a Region

One of the properties of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class is the clipping region. All drawing done by a given **Graphics** object is restricted to the clipping region of that **Graphics** object. You can set the clipping region by calling the **SetClip** method.

The following example constructs a path that consists of a single polygon. Then the code constructs a region based on that path. The address of the region is passed to the **SetClip** method of a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object, and then two strings are drawn.


```
// Create a path that consists of a single polygon.
Point polyPoints[] = {Point(10, 10), Point(150, 10), 
   Point(100, 75), Point(100, 150)};
GraphicsPath path;
path.AddPolygon(polyPoints, 4);
// Construct a region based on the path.
Region region(&amp;path);
// Draw the outline of the region.
Pen pen(Color(255, 0, 0, 0));
graphics.DrawPath(&amp;pen, &amp;path);
// Set the clipping region of the Graphics object.
graphics.SetClip(&amp;region);
// Draw some clipped strings.
FontFamily fontFamily(L"Arial");
Font font(&amp;fontFamily, 36, FontStyleBold, UnitPixel);
SolidBrush solidBrush(Color(255, 255, 0, 0));
graphics.DrawString(L"A Clipping Region", 20, &amp;font, 
   PointF(15, 25), &amp;solidBrush);
graphics.DrawString(L"A Clipping Region", 20, &amp;font, 
   PointF(15, 68), &amp;solidBrush);
```



The following illustration shows the clipped strings.

![illustration showing parts of two sentences appearing within a four-sided shape](images/clip1.png)

 

 



