---
Description: 'The topic Using a Color Matrix to Set Alpha Values in Images shows a nondestructive method for changing the alpha values of an image.'
ms.assetid: '38c6254d-5191-4948-804a-1a4427aab7c6'
title: Setting the Alpha Values of Individual Pixels
---

# Setting the Alpha Values of Individual Pixels

The topic [Using a Color Matrix to Set Alpha Values in Images](-gdiplus-using-a-color-matrix-to-set-alpha-values-in-images-use.md) shows a nondestructive method for changing the alpha values of an image. The example in that topic renders an image semitransparently, but the pixel data in the bitmap is not changed. The alpha values are altered only during rendering.

The following example shows how to change the alpha values of individual pixels. The code in the example actually changes the alpha information in a [**Bitmap**](-gdiplus-class-bitmap-class.md) object. The approach is much slower than using a color matrix and an [**ImageAttributes**](-gdiplus-class-imageattributes-class.md) object but gives you control over the individual pixels in the bitmap.


```
INT iWidth = bitmap.GetWidth();
INT iHeight = bitmap.GetHeight();
Color color, colorTemp;
for(INT iRow = 0; iRow < iHeight; iRow++)
{
   for(INT iColumn = 0; iColumn < iWidth; iColumn++)
   {
      bitmap.GetPixel(iColumn, iRow, &amp;color);
      colorTemp.SetValue(color.MakeARGB(
         (BYTE)(255 * iColumn / iWidth), 
         color.GetRed(),
         color.GetGreen(),
         color.GetBlue()));
      bitmap.SetPixel(iColumn, iRow, colorTemp);
   }
}
// First draw a wide black line.
Pen pen(Color(255, 0, 0, 0), 25);
graphics.DrawLine(&amp;pen, 10, 35, 200, 35);
// Now draw the modified bitmap.
graphics.DrawImage(&amp;bitmap, 30, 0, iWidth, iHeight);
```



The following illustration shows the resulting image.

![illustration showing an image that gets more opaque from left to right, over a black rectangle](images/image3.png)

The preceding code example uses nested loops to change the alpha value of each pixel in the bitmap. For each pixel, [**Bitmap::GetPixel**](-gdiplus-class-bitmap-getpixel-x-y-color-.md) gets the existing color, [**Color::SetValue**](-gdiplus-class-color-setvalue-argb-.md) creates a temporary color that contains the new alpha value, and then [**Bitmap::SetPixel**](-gdiplus-class-bitmap-setpixel-x-y-color-.md) sets the new color. The alpha value is set based on the column of the bitmap. In the first column, alpha is set to 0. In the last column, alpha is set to 255. So the resulting image goes from fully transparent (on the left edge) to fully opaque (on the right edge).

[**Bitmap::GetPixel**](-gdiplus-class-bitmap-getpixel-x-y-color-.md) and [**Bitmap::SetPixel**](-gdiplus-class-bitmap-setpixel-x-y-color-.md) give you control of the individual pixel values. However, using **Bitmap::GetPixel** and **Bitmap::SetPixel** is not nearly as fast as using the [**ImageAttributes**](-gdiplus-class-imageattributes-class.md) class and the [**ColorMatrix**](-gdiplus-struc-colormatrix.md) structure.

 

 



