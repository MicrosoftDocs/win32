---
Description: The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.
ms.assetid: 46051bfa-b842-4e4e-bda8-e9003b5b5da4
title: The Structure of the Class-Based Interface
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# The Structure of the Class-Based Interface

The C++ interface to Windows GDI+ contains about 40 classes, 50 enumerations, and 6 structures. There are also a few functions that are not members of any class.

You must indicate that the namespace Gdiplus is being used before any GDI+ functions are called. The following statement indicates that the Gdiplus namespace is being used in the application.

`using namespace Gdiplus;`

The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class is the core of the GDI+ interface; it is the class that actually draws lines, curves, figures, images, and text.

Many classes work together with the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class. For example, the [Graphics::DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) method receives a pointer to a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object, which holds attributes (color, width, dash style, and the like) of the line to be drawn. The [Graphics::FillRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)?branch=master) method can receive a pointer to a [**LinearGradientBrush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-lineargradientbrush?branch=master) object, which works with the **Graphics** object to fill a rectangle with a gradually changing color. [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) and [**StringFormat**](/windows/win32/gdiplusstringformat/nl-gdiplusstringformat-stringformat?branch=master) objects influence the way a **Graphics** object draws text. A [**Matrix**](/windows/win32/gdiplusmatrix/nl-gdiplusmatrix-matrix?branch=master) object stores and manipulates the world transformation of a **Graphics** object, which is used to rotate, scale, and flip images.

Certain classes serve primarily as structured data types. Some of those classes (for example, [**Rect**](/windows/win32/gdiplustypes/nl-gdiplustypes-rect?branch=master), [**Point**](/windows/win32/gdiplustypes/nl-gdiplustypes-point?branch=master), and [**Size**](/windows/win32/gdiplustypes/nl-gdiplustypes-size?branch=master)) are for general purposes. Others are for specialized purposes and are considered helper classes. For example, the [**BitmapData**](/windows/win32/Gdiplusimaging/?branch=master) class is a helper for the [**Bitmap**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-bitmap?branch=master) class, and the [**PathData**](/windows/win32/gdiplustypes/nl-gdiplustypes-pathdata?branch=master) class is a helper for the [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) class. GDI+ also defines a few structures that are used for organizing data. For example, the [**ColorMap**](/windows/win32/Gdipluscolormatrix/ns-gdipluscolormatrix-colormap?branch=master) structure holds a pair of [**Color**](/windows/win32/gdipluscolor/nl-gdipluscolor-color?branch=master) objects that form one entry in a color conversion table.

GDI+ defines several enumerations, which are collections of related constants. For example, the [**LineJoin**](/windows/win32/Gdiplusenums/ne-gdiplusenums-linejoin?branch=master) enumeration contains the elements [****LineJoinBevel****](/windows/win32/Gdiplusenums/ne-gdiplusenums-linejoin?branch=master), [****LineJoinMiter****](/windows/win32/Gdiplusenums/ne-gdiplusenums-linejoin?branch=master), and [****LineJoinRound****](/windows/win32/Gdiplusenums/ne-gdiplusenums-linejoin?branch=master), which specify styles that can be used to join two lines.

GDI+ provides a few functions that are not part of any class. Two of those functions are [**GdiplusStartup**](/windows/win32/Gdiplusinit/nf-gdiplusinit-gdiplusstartup?branch=master) and [**GdiplusShutdown**](/windows/win32/Gdiplusinit/nf-gdiplusinit-gdiplusshutdown?branch=master). You must call **GdiplusStartup** before you make any other GDI+ calls, and you must call **GdiplusShutdown** when you have finished using GDI+.

 

 



