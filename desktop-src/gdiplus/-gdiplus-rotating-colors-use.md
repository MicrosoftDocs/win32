---
description: Rotation in a four-dimensional color space is difficult to visualize.
ms.assetid: 099f76a3-2da3-4f2b-8f8d-557d144451dc
title: Rotating Colors
ms.topic: article
ms.date: 05/31/2018
---

# Rotating Colors

Rotation in a four-dimensional color space is difficult to visualize. We can make it easier to visualize rotation by agreeing to keep one of the color components fixed. Suppose we agree to keep the alpha component fixed at 1 (fully opaque). Then we can visualize a three-dimensional color space with red, green, and blue axes as shown in the following illustration.

![illustration of a perspective view of a three-dimensional color space with axes labeled red, green, and blue](images/recoloring03.png)

A color can be thought of as a point in 3-D space. For example, the point (1, 0, 0) in space represents the color red, and the point (0, 1, 0) in space represents the color green.

The following illustration shows what it means to rotate the color (1, 0, 0) through an angle of 60 degrees in the Red-Green plane. Rotation in a plane parallel to the Red-Green plane can be thought of as rotation about the blue axis.

![illustration showing the point (1, 0, 0) rotated 60 degrees to (0.5, 0.866, 0)](images/recoloring04.png)

The following illustration shows how to initialize a color matrix to perform rotations about each of the three coordinate axes (red, green, blue).

![illustration showing color matrices that performing rotations about each of the three coordinate axes](images/recoloring05.png)

The following example takes an image that is all one color (1, 0, 0.6) and applies a 60-degree rotation about the blue axis. The angle of the rotation is swept out in a plane that is parallel to the Red-Green plane.


```
Image            image(L"RotationInput.bmp");
ImageAttributes  imageAttributes;
UINT             width = image.GetWidth();
UINT             height = image.GetHeight();
REAL             degrees = 60;
REAL             pi = acos(-1);  // the angle whose cosine is -1.
REAL             r = degrees * pi / 180;  // degrees to radians

ColorMatrix colorMatrix = {
   cos(r),  sin(r), 0.0f, 0.0f, 0.0f,
   -sin(r), cos(r), 0.0f, 0.0f, 0.0f,
   0.0f,    0.0f,   1.0f, 0.0f, 0.0f,
   0.0f,    0.0f,   0.0f, 1.0f, 0.0f,
   0.0f,    0.0f,   0.0f, 0.0f, 1.0f};
   
imageAttributes.SetColorMatrix(
   &colorMatrix, 
   ColorMatrixFlagsDefault,
   ColorAdjustTypeBitmap);
   
graphics.DrawImage(&image, 10, 10, width, height);

graphics.DrawImage(
   &image, 
   Rect(130, 10, width, height),  // destination rectangle 
   0, 0,        // upper-left corner of source rectangle 
   width,       // width of source rectangle
   height,      // height of source rectangle
   UnitPixel,
   &imageAttributes);
```



The following illustration shows the original image on the left and the color-rotated image on the right.

![illustration showing rectangles filled with the original image (violet red) and color-rotated image (sea green)](images/colortrans5.png)

The color rotation performed in the preceding code example can be visualized as follows.

![illustration showing a 3-d color space, and the point (1, 0, 0.6) rotated 60 degrees to (0.5, 0.866, 0.6)](images/recoloring06.png)

 

 



