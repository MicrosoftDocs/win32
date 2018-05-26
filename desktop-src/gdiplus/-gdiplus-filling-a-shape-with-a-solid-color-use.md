---
Description: To fill a shape with a solid color, create a SolidBrush object, and then pass the address of that SolidBrush object as an argument to one of the fill methods of the Graphics class.
ms.assetid: cedef138-5047-4a72-8b89-5a95062a351c
title: Filling a Shape with a Solid Color
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Filling a Shape with a Solid Color

To fill a shape with a solid color, create a [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) object, and then pass the address of that **SolidBrush** object as an argument to one of the fill methods of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class. The following example shows how to fill an ellipse with the color red:


```
SolidBrush solidBrush(Color(255, 255, 0, 0));
stat = graphics.FillEllipse(&amp;solidBrush, 0, 0, 100, 60);
```



In the preceding example, the [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) constructor takes a [**Color**](/windows/win32/gdipluscolor/nl-gdipluscolor-color?branch=master) object reference as its only argument. The values used by the **Color** constructor represent the alpha, red, green, and blue components of the color. Each of these values must be in the range 0 through 255. The first 255 indicates that the color is fully opaque, and the second 255 indicates that the red component is at full intensity. The two zeros indicate that the green and blue components both have an intensity of 0.

The four numbers (0, 0, 100, 60) passed to the [**Graphics::FillEllipse**](/windows/win32/Gdiplusgraphics/?branch=master) method specify the location and size of the bounding rectangle for the ellipse. The rectangle has an upper-left corner of (0, 0), a width of 100, and a height of 60.

 

 



