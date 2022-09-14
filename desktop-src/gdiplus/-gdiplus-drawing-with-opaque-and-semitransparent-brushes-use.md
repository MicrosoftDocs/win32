---
description: When you fill a shape, you must pass the address of a Brush object to one of the fill methods of the Graphics class.
ms.assetid: 42e36c32-ed20-4c5f-bcba-004d795babe3
title: Drawing with Opaque and Semitransparent Brushes
ms.topic: article
ms.date: 05/31/2018
---

# Drawing with Opaque and Semitransparent Brushes

When you fill a shape, you must pass the address of a [**Brush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-brush) object to one of the fill methods of the [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class. The one parameter of the [**SolidBrush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-solidbrush) constructor is a [**Color**](/windows/desktop/api/gdipluscolor/nl-gdipluscolor-color) object. To fill an opaque shape, set the alpha component of the color to 255. To fill a semitransparent shape, set the alpha component to any value from 1 through 254.

When you fill a semitransparent shape, the color of the shape is blended with the colors of the background. The alpha component specifies how the shape and background colors are mixed; alpha values near 0 place more weight on the background colors, and alpha values near 255 place more weigh on the shape color.

The following example draws an image and then fills three ellipses that overlap the image. The first ellipse uses an alpha component of 255, so it is opaque. The second and third ellipses use an alpha component of 128, so they are semitransparent; you can see the background image through the ellipses. The call to [**Graphics::SetCompositingQuality**](/windows/desktop/api/Gdiplusgraphics/nf-gdiplusgraphics-graphics-setcompositingquality) causes the blending for the third ellipse to be done in conjunction with gamma correction.


```
Image image(L"Texture1.jpg");
graphics.DrawImage(&image, 50, 50, image.GetWidth(), image.GetHeight());
SolidBrush opaqueBrush(Color(255, 0, 0, 255));
SolidBrush semiTransBrush(Color(128, 0, 0, 255));
graphics.FillEllipse(&opaqueBrush, 35, 45, 45, 30);
graphics.FillEllipse(&semiTransBrush, 86, 45, 45, 30);
graphics.SetCompositingQuality(CompositingQualityGammaCorrected);
graphics.FillEllipse(&semiTransBrush, 40, 90, 86, 30);
```



The following illustration shows the output of the preceding code.

![illustration showing an image overlaid by three ellipses: one opaque, one slightly transparent, one very transparent](images/compqualellipse.png)

 

 



