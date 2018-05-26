---
Description: You can use the DrawString method of the Graphics class to draw text at a specified location or within a specified rectangle.
ms.assetid: a873c132-f232-4144-bcc3-ca200055074c
title: Drawing Text
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing Text

You can use the [DrawString](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class to draw text at a specified location or within a specified rectangle.

-   [Drawing Text at a Specified Location](#drawing-text-at-a-specified-location)
-   [Drawing Text in a Rectangle](#drawing-text-in-a-rectangle)

## Drawing Text at a Specified Location

To draw text at a specified location, you need [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master), [**FontFamily**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-fontfamily?branch=master), [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master), [**PointF**](/windows/win32/gdiplustypes/nl-gdiplustypes-pointf?branch=master), and [**Brush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-brush?branch=master) objects.

The following example draws the string "Hello" at location (30, 10). The font family is Times New Roman. The font, which is an individual member of the font family, is Times New Roman, size 24 pixels, regular style. Assume that **graphics** is an existing [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object.


```
FontFamily  fontFamily(L"Times New Roman");
Font        font(&amp;fontFamily, 24, FontStyleRegular, UnitPixel);
PointF      pointF(30.0f, 10.0f);
SolidBrush  solidBrush(Color(255, 0, 0, 255));

graphics.DrawString(L"Hello", -1, &amp;font, pointF, &amp;solidBrush);
            
```



The following illustration shows the output of the preceding code.

![screen shot of a small window containing the text "hello"](images/fontstext1.png)

In the preceding example, the [**FontFamily**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-fontfamily?branch=master) constructor receives a string that identifies the font family. The address of the **FontFamily** object is passed as the first argument to the [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) constructor. The second argument passed to the **Font** constructor specifies the size of the font measured in units given by the fourth argument. The third argument specifies the style (regular, bold, italic, and so on) of the font.

The [DrawString](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) method receives five arguments. The first argument is the string to be drawn, and the second argument is the length (in characters, not bytes) of that string. If the string is null-terminated, you can pass –1 for the length. The third argument is the address of the [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) object that was constructed previously. The fourth argument is a [**PointF**](/windows/win32/gdiplustypes/nl-gdiplustypes-pointf?branch=master) object that contains the coordinates of the upper-left corner of the string. The fifth argument is the address of a [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) object that will be used to fill the characters of the string.

## Drawing Text in a Rectangle

One of the [**DrawString**](/windows/win32/Gdiplusgraphics/?branch=master) methods of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class has a *RectF* parameter. By calling that **DrawString** method, you can draw text that wraps in a specified rectangle. To draw text in a rectangle, you need **Graphics**, [**FontFamily**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-fontfamily?branch=master), [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master), [**RectF**](/windows/win32/gdiplustypes/nl-gdiplustypes-rectf?branch=master), and [**Brush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-brush?branch=master) objects.

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

In the preceding example, the fourth argument passed to the [**DrawString**](/windows/win32/Gdiplusgraphics/?branch=master) method is a [**RectF**](/windows/win32/gdiplustypes/nl-gdiplustypes-rectf?branch=master) object that specifies the bounding rectangle for the text. The fifth parameter is of type [**StringFormat**](/windows/win32/gdiplusstringformat/nl-gdiplusstringformat-stringformat?branch=master)— the argument is **NULL** because no special string formatting is required.

 

 



