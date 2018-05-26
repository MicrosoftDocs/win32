---
Description: The topic Drawing a Line shows how to write a Windows application that uses Windows GDI+ to draw a line.
ms.assetid: fcf45b19-456c-4551-8901-d587a73a5638
title: Drawing a String
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Drawing a String

The topic [Drawing a Line](-gdiplus-drawing-a-line-use.md) shows how to write a Windows application that uses Windows GDI+ to draw a line. To draw a string, replace the **OnPaint** function shown in that topic with the following **OnPaint** function:


```
VOID OnPaint(HDC hdc)
{
   Graphics    graphics(hdc);
   SolidBrush  brush(Color(255, 0, 0, 255));
   FontFamily  fontFamily(L"Times New Roman");
   Font        font(&amp;fontFamily, 24, FontStyleRegular, UnitPixel);
   PointF      pointF(10.0f, 20.0f);
   
   graphics.DrawString(L"Hello World!", -1, &amp;font, pointF, &amp;brush);
}
```



The previous code creates several GDI+ objects. The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object provides the [DrawString Methods](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) method, which does the actual drawing. The [**SolidBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-solidbrush?branch=master) object specifies the color of the string.

The [**FontFamily**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-fontfamily?branch=master) constructor receives a single, string argument that identifies the font family. The address of the **FontFamily** object is the first argument passed to the [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) constructor. The second argument passed to the [Font](/windows/win32/gdiplusheaders/nf-gdiplusheaders-font-font(const font &)?branch=master) constructor specifies the font size, and the third argument specifies the style. The value **FontStyleRegular** is a member of the [**FontStyle**](/windows/win32/Gdiplusenums/ne-gdiplusenums-fontstyle?branch=master) enumeration, which is declared in Gdiplusenums.h. The last argument to the **Font** constructor indicates that the size of the font (24 in this case) is measured in pixels. The value **UnitPixel** is a member of the [**Unit**](/windows/win32/Gdiplusenums/ne-gdiplusenums-unit?branch=master) enumeration.

The first argument passed to the [DrawString Methods](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) method is the address of a wide-character string. The second argument, –1, specifies that the string is null terminated. (If the string is not null terminated, the second argument should specify the number of wide characters in the string.) The third argument is the address of the [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) object. The fourth argument is a reference to a [**PointF**](/windows/win32/gdiplustypes/nl-gdiplustypes-pointf?branch=master) object that specifies the location where the string will be drawn. The last argument is the address of the [**Brush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-brush?branch=master) object, which specifies the color of the string.

 

 



