---
Description: 'The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.'
ms.assetid: '46051bfa-b842-4e4e-bda8-e9003b5b5da4'
title: 'The Structure of the Class-Based Interface'
---

# The Structure of the Class-Based Interface

The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.

You must indicate that the namespace Gdiplus is being used before any GDI+ functions are called. The following statement indicates that the Gdiplus namespace is being used in the application.

`using namespace Gdiplus;`

The [**Graphics**](-gdiplus-class-graphics-class.md) class is the core of the GDI+ interface; it is the class that actually draws lines, curves, figures, images, and text.

Many classes work together with the [**Graphics**](-gdiplus-class-graphics-class.md) class. For example, the [Graphics::DrawLine](-gdiplus-class-graphics-drawline-methods.md) method receives a pointer to a [**Pen**](-gdiplus-class-pen-class.md) object, which holds attributes (color, width, dash style, and the like) of the line to be drawn. The [Graphics::FillRectangle](-gdiplus-class-graphics-fillrectangle-methods.md) method can receive a pointer to a [**LinearGradientBrush**](-gdiplus-class-lineargradientbrush-class.md) object, which works with the **Graphics** object to fill a rectangle with a gradually changing color. [**Font**](-gdiplus-class-font-class.md) and [**StringFormat**](-gdiplus-class-stringformat-class.md) objects influence the way a **Graphics** object draws text. A [**Matrix**](-gdiplus-class-matrix-class.md) object stores and manipulates the world transformation of a **Graphics** object, which is used to rotate, scale, and flip images.

Certain classes serve primarily as structured data types. Some of those classes (for example, [**Rect**](-gdiplus-class-rect-class.md), [**Point**](-gdiplus-class-point-class.md), and [**Size**](-gdiplus-class-size-class.md)) are for general purposes. Others are for specialized purposes and are considered helper classes. For example, the [**BitmapData**](-gdiplus-class-bitmapdata-class.md) class is a helper for the [**Bitmap**](-gdiplus-class-bitmap-class.md) class, and the [**PathData**](-gdiplus-class-pathdata-class.md) class is a helper for the [**GraphicsPath**](-gdiplus-class-graphicspath-class.md) class. GDI+ also defines a few structures that are used for organizing data. For example, the [**ColorMap**](-gdiplus-struc-colormap.md) structure holds a pair of [**Color**](-gdiplus-class-color-class.md) objects that form one entry in a color conversion table.

GDI+ defines several enumerations, which are collections of related constants. For example, the [**LineJoin**](-gdiplus-enum-linejoin.md) enumeration contains the elements [****LineJoinBevel****](-gdiplus-enum-linejoin.md), [****LineJoinMiter****](-gdiplus-enum-linejoin.md), and [****LineJoinRound****](-gdiplus-enum-linejoin.md), which specify styles that can be used to join two lines.

GDI+ provides a few functions that are not part of any class. Two of those functions are [**GdiplusStartup**](-gdiplus-func-gdiplusstartup-token-input-output-.md) and [**GdiplusShutdown**](-gdiplus-func-gdiplusshutdown-.md). You must call **GdiplusStartup** before you make any other GDI+ calls, and you must call **GdiplusShutdown** when you have finished using GDI+.

 

 



