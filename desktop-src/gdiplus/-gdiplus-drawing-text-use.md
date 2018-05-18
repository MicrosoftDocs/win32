---
Description: 'You can use the DrawString method of the Graphics class to draw text at a specified location or within a specified rectangle.'
ms.assetid: 'a873c132-f232-4144-bcc3-ca200055074c'
title: Drawing Text
---

# Drawing Text

You can use the [DrawString](-gdiplus-class-graphics-drawstring-methods.md) method of the [**Graphics**](-gdiplus-class-graphics-class.md) class to draw text at a specified location or within a specified rectangle.

-   [Drawing Text at a Specified Location](#drawing-text-at-a-specified-location)
-   [Drawing Text in a Rectangle](#drawing-text-in-a-rectangle)

## Drawing Text at a Specified Location

To draw text at a specified location, you need [**Graphics**](-gdiplus-class-graphics-class.md), [**FontFamily**](-gdiplus-class-fontfamily-class.md), [**Font**](-gdiplus-class-font-class.md), [**PointF**](-gdiplus-class-pointf-class.md), and [**Brush**](-gdiplus-class-brush-class.md) objects.

The following example draws the string "Hello" at location (30, 10). The font family is Times New Roman. The font, which is an individual member of the font family, is Times New Roman, size 24 pixels, regular style. Assume that **graphics** is an existing [**Graphics**](-gdiplus-class-graphics-class.md) object.


```
FontFamily  fontFamily(L"Times New Roman");
Font        font(&amp;fontFamily, 24, FontStyleRegular, UnitPixel);
PointF      pointF(30.0f, 10.0f);
SolidBrush  solidBrush(Color(255, 0, 0, 255));

graphics.DrawString(L"Hello", -1, &amp;font, pointF, &amp;solidBrush);
            
```



The following illustration shows the output of the preceding code.

![screen shot of a small window containing the text "hello"](images/fontstext1.png)

In the preceding example, the [**FontFamily**](-gdiplus-class-fontfamily-class.md) constructor receives a string that identifies the font family. The address of the **FontFamily** object is passed as the first argument to the [**Font**](-gdiplus-class-font-class.md) constructor. The second argument passed to the **Font** constructor specifies the size of the font measured in units given by the fourth argument. The third argument specifies the style (regular, bold, italic, and so on) of the font.

The [DrawString](-gdiplus-class-graphics-drawstring-methods.md) method receives five arguments. The first argument is the string to be drawn, and the second argument is the length (in characters, not bytes) of that string. If the string is null-terminated, you can pass –1 for the length. The third argument is the address of the [**Font**](-gdiplus-class-font-class.md) object that was constructed previously. The fourth argument is a [**PointF**](-gdiplus-class-pointf-class.md) object that contains the coordinates of the upper-left corner of the string. The fifth argument is the address of a [**SolidBrush**](-gdiplus-class-solidbrush-class.md) object that will be used to fill the characters of the string.

## Drawing Text in a Rectangle

One of the [**DrawString**](-gdiplus-class-graphics-drawstring-string-length-font-layoutrect-stringformat-brush-.md) methods of the [**Graphics**](-gdiplus-class-graphics-class.md) class has a *RectF* parameter. By calling that **DrawString** method, you can draw text that wraps in a specified rectangle. To draw text in a rectangle, you need **Graphics**, [**FontFamily**](-gdiplus-class-fontfamily-class.md), [**Font**](-gdiplus-class-font-class.md), [**RectF**](-gdiplus-class-rectf-class.md), and [**Brush**](-gdiplus-class-brush-class.md) objects.

The following example creates a rectangle with upper-left corner (30, 10), width 100, and height 122. Then the code draws a string inside that rectangle. The string is restricted to the rectangle and wraps in such a way that individual words are not broken.


```
WCHAR string[] = 
   L"Draw text in a rectangle by passing a RectF to the DrawString method.";
                       
FontFamily   fontFamily(L"Arial");
Font         font(&amp;fontFamily, 12, FontStyleBold, UnitPoint);
RectF        rectF(30.0f, 10.0f, 100.0f, 122.0f);
SolidBrush   solidBrush(Color(255, 0, 0, 255));

graphics.DrawString(string, -1, &amp;font, rectF, NULL, &amp;solidBrush);

Pen pen(Color(255, 0, 0, 0));
graphics.DrawRectangle(&amp;pen, rectF);
            
```



The following illustration shows the text drawn in the rectangle.

![screen shot of a small window containing a recangle, within which appears the first part of a sentence](images/fontstext2.png)

In the preceding example, the fourth argument passed to the [**DrawString**](-gdiplus-class-graphics-drawstring-string-length-font-layoutrect-stringformat-brush-.md) method is a [**RectF**](-gdiplus-class-rectf-class.md) object that specifies the bounding rectangle for the text. The fifth parameter is of type [**StringFormat**](-gdiplus-class-stringformat-class.md)— the argument is **NULL** because no special string formatting is required.

 

 



