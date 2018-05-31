---
Description: The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.
ms.assetid: 46051bfa-b842-4e4e-bda8-e9003b5b5da4
title: The Structure of the Class-Based Interface
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# The Structure of the Class-Based Interface

The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.

You must indicate that the namespace Gdiplus is being used before any GDI+ functions are called. The following statement indicates that the Gdiplus namespace is being used in the application.

`using namespace Gdiplus;`

The [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class is the core of the GDI+ interface; it is the class that actually draws lines, curves, figures, images, and text.

Many classes work together with the [**Graphics**](/windows/desktop/api/gdiplusgraphics/nl-gdiplusgraphics-graphics) class. For example, the [Graphics::DrawLine](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)) method receives a pointer to a [**Pen**](/windows/desktop/api/gdipluspen/nl-gdipluspen-pen) object, which holds attributes (color, width, dash style, and the like) of the line to be drawn. The [Graphics::FillRectangle](/windows/desktop/api/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)) method can receive a pointer to a [**LinearGradientBrush**](/windows/desktop/api/gdiplusbrush/nl-gdiplusbrush-lineargradientbrush) object, which works with the **Graphics** object to fill a rectangle with a gradually changing color. [**Font**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-font) and [**StringFormat**](/windows/desktop/api/gdiplusstringformat/nl-gdiplusstringformat-stringformat) objects influence the way a **Graphics** object draws text. A [**Matrix**](/windows/desktop/api/gdiplusmatrix/nl-gdiplusmatrix-matrix) object stores and manipulates the world transformation of a **Graphics** object, which is used to rotate, scale, and flip images.

Certain classes serve primarily as structured data types. Some of those classes (for example, [**Rect**](/windows/desktop/api/gdiplustypes/nl-gdiplustypes-rect), [**Point**](/windows/desktop/api/gdiplustypes/nl-gdiplustypes-point), and [**Size**](/windows/desktop/api/gdiplustypes/nl-gdiplustypes-size)) are for general purposes. Others are for specialized purposes and are considered helper classes. For example, the [**BitmapData**](/windows/desktop/api/Gdiplusimaging/) class is a helper for the [**Bitmap**](/windows/desktop/api/gdiplusheaders/nl-gdiplusheaders-bitmap) class, and the [**PathData**](/windows/desktop/api/gdiplustypes/nl-gdiplustypes-pathdata) class is a helper for the [**GraphicsPath**](/windows/desktop/api/gdipluspath/nl-gdipluspath-graphicspath) class. GDI+ also defines a few structures that are used for organizing data. For example, the [**ColorMap**](/windows/desktop/api/Gdipluscolormatrix/ns-gdipluscolormatrix-colormap) structure holds a pair of [**Color**](/windows/desktop/api/gdipluscolor/nl-gdipluscolor-color) objects that form one entry in a color conversion table.

GDI+ defines several enumerations, which are collections of related constants. For example, the [**LineJoin**](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-linejoin) enumeration contains the elements [****LineJoinBevel****](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-linejoin), [****LineJoinMiter****](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-linejoin), and [****LineJoinRound****](/windows/desktop/api/Gdiplusenums/ne-gdiplusenums-linejoin), which specify styles that can be used to join two lines.

GDI+ provides a few functions that are not part of any class. Two of those functions are [**GdiplusStartup**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusstartup) and [**GdiplusShutdown**](/windows/desktop/api/Gdiplusinit/nf-gdiplusinit-gdiplusshutdown). You must call **GdiplusStartup** before you make any other GDI+ calls, and you must call **GdiplusShutdown** when you have finished using GDI+.

 

 



