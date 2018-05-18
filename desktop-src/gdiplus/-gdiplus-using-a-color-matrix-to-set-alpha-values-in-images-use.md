---
Description: 'The Bitmap class (which inherits from the Image class) and the ImageAttributes class provide functionality for getting and setting pixel values.'
ms.assetid: 'e3d67431-6098-4b2a-8910-5695a8473216'
title: Using a Color Matrix to Set Alpha Values in Images
---

# Using a Color Matrix to Set Alpha Values in Images

The [**Bitmap**](-gdiplus-class-bitmap-class.md) class (which inherits from the [**Image**](-gdiplus-class-image-class.md) class) and the [**ImageAttributes**](-gdiplus-class-imageattributes-class.md) class provide functionality for getting and setting pixel values. You can use the **ImageAttributes** class to modify the alpha values for an entire image, or you can call the [**Bitmap::SetPixel**](-gdiplus-class-bitmap-setpixel-x-y-color-.md) method of the **Bitmap** class to modify individual pixel values. For more information on setting individual pixel values, see [Setting the Alpha Values of Individual Pixels](-gdiplus-setting-the-alpha-values-of-individual-pixels-use.md).

The following example draws a wide black line and then displays an opaque image that covers part of that line.


```
Bitmap bitmap(L"Texture1.jpg");
Pen pen(Color(255, 0, 0, 0), 25);
// First draw a wide black line.
graphics.DrawLine(&amp;pen, Point(10, 35), Point(200, 35));
// Now draw an image that covers part of the black line.
graphics.DrawImage(&amp;bitmap,
   Rect(30, 0, bitmap.GetWidth(), bitmap.GetHeight()));
```



The following illustration shows the resulting image, which is drawn at (30, 0). Note that the wide black line doesn't show through the image.

![illustration showing an opaque image overlapping a thin, wide, black rectangle](images/image1.png)

The [**ImageAttributes**](-gdiplus-class-imageattributes-class.md) class has many properties that you can use to modify images during rendering. In the following example, an **ImageAttributes** object is used to set all the alpha values to 80 percent of what they were. This is done by initializing a color matrix and setting the alpha scaling value in the matrix to 0.8. The address of the color matrix is passed to the [**ImageAttributes::SetColorMatrix**](-gdiplus-class-imageattributes-setcolormatrix-colormatrix-mode-type-.md) method of the **ImageAttributes** object, and the address of the **ImageAttributes** object is passed to the [DrawImage](-gdiplus-class-graphics-drawimage-methods.md) method of a [**Graphics**](-gdiplus-class-graphics-class.md) object.


```
// Create a Bitmap object and load it with the texture image.
Bitmap bitmap(L"Texture1.jpg");
Pen pen(Color(255, 0, 0, 0), 25);
// Initialize the color matrix.
// Notice the value 0.8 in row 4, column 4.
ColorMatrix colorMatrix = {1.0f, 0.0f, 0.0f, 0.0f, 0.0f,
                           0.0f, 1.0f, 0.0f, 0.0f, 0.0f,
                           0.0f, 0.0f, 1.0f, 0.0f, 0.0f,
                           0.0f, 0.0f, 0.0f, 0.8f, 0.0f,
                           0.0f, 0.0f, 0.0f, 0.0f, 1.0f};
// Create an ImageAttributes object and set its color matrix.
ImageAttributes imageAtt;
imageAtt.SetColorMatrix(&amp;colorMatrix, ColorMatrixFlagsDefault,
   ColorAdjustTypeBitmap);
// First draw a wide black line.
graphics.DrawLine(&amp;pen, Point(10, 35), Point(200, 35));
// Now draw the semitransparent bitmap image.
INT iWidth = bitmap.GetWidth();
INT iHeight = bitmap.GetHeight();
graphics.DrawImage(
   &amp;bitmap, 
   Rect(30, 0, iWidth, iHeight),  // Destination rectangle
   0,                             // Source rectangle X 
   0,                             // Source rectangle Y
   iWidth,                        // Source rectangle width
   iHeight,                       // Source rectangle height
   UnitPixel, 
   &amp;imageAtt);
```



During rendering, the alpha values in the bitmap are converted to 80 percent of what they were. This results in an image that is blended with the background. As the following illustration shows, the bitmap image looks transparent; you can see the solid black line through it.

![illustration similar to the previous one, but the image is sem-transparent](images/image2.png)

Where the image is over the white portion of the background, the image has been blended with the color white. Where the image crosses the black line, the image is blended with the color black.

 

 



