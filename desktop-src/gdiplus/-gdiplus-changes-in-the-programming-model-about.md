---
Description: The following sections describe several ways that programming with Windows GDI+ is different from programming with Windows Graphics Device Interface (GDI).
ms.assetid: 89a154c1-6a49-45d6-a73c-94b0b1567408
title: Changes in the Programming Model
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Changes in the Programming Model

The following sections describe several ways that programming with Windows GDI+ is different from programming with Windows Graphics Device Interface (GDI).

-   [Device Contexts, Handles, and Graphics Objects](#device-contexts-handles-and-graphics-objects)
-   [Two Ways to Draw a Line](#two-ways-to-draw-a-line)
    -   [Drawing a line with GDI](#drawing-a-line-with-gdi)
    -   [Drawing a line with GDI+ and the C++ class interface](#drawing-a-line-with-gdi-and-the-c-class-interface)
-   [Pens, Brushes, Paths, Images, and Fonts as Parameters](#pens-brushes-paths-images-and-fonts-as-parameters)
-   [Method Overloading](#method-overloading)
-   [No More Current Position](#no-more-current-position)
-   [Separate Methods for Draw and Fill](#separate-methods-for-draw-and-fill)
-   [Constructing Regions](#constructing-regions)

## Device Contexts, Handles, and Graphics Objects

If you have written programs using GDI (the graphics device interface included in previous versions of Windows), you are familiar with the idea of a device context (DC). A device context is a structure used by Windows to store information about the capabilities of a particular display device and attributes that specify how items will be drawn on that device. A device context for a video display is also associated with a particular window on the display. First you obtain a handle to a device context (HDC), and then you pass that handle as an argument to GDI functions that actually do the drawing. You also pass the handle as an argument to GDI functions that obtain or set the attributes of the device context.

When you use GDI+, you don't have to be as concerned with handles and device contexts as you do when you use GDI. You simply create a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and then invoke its methods in the familiar object-oriented style — myGraphicsObject.DrawLine(*parameters*). The **Graphics** object is at the core of GDI+ just as the device context is at the core of GDI. The device context and the **Graphics** object play similar roles, but there are some fundamental differences between the handle-based programming model used with device contexts (GDI) and the object-oriented model used with **Graphics** objects (GDI+).

The [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object, like the device context, is associated with a particular window on the screen and contains attributes (for example, smoothing mode and text rendering hint) that specify how items are to be drawn. However, the **Graphics** object is not tied to a pen, brush, path, image, or font as a device context is. For example, in GDI, before you can use a device context to draw a line, you must call [SelectObject](http://msdn.microsoft.com/library/en-us/gdi/devcons_9v3o.asp) to associate a pen object with the device context. This is referred to as selecting the pen into the device context. All lines drawn in the device context will use that pen until you select a different pen. With GDI+, you pass a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object as an argument to the [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) method of the **Graphics** class. You can use a different **Pen** object in each of a series of DrawLine calls without having to associate a given **Pen** object with a **Graphics** object.

## Two Ways to Draw a Line

The following two examples each draw a red line of width 3 from location (20, 10) to location (200,100). The first example calls GDI, and the second calls GDI+ through the C++ class interface.

-   [Drawing a line with GDI](#drawing-a-line-with-gdi)
-   [Drawing a line with GDI+ and the C++ class interface](#drawing-a-line-with-gdi-and-the-c-class-interface)

### Drawing a line with GDI

To draw a line with GDI, you need two objects: a device context and a pen. You get a handle to a device context by calling [**BeginPaint**](gdi.beginpaint), and a handle to a pen by calling [CreatePen](http://msdn.microsoft.com/library/en-us/gdi/pens_9wha.asp). Next, you call [SelectObject](http://msdn.microsoft.com/library/en-us/gdi/devcons_9v3o.asp) to select the pen into the device context. You set the pen position to (20, 10) by calling [MoveToEx](http://msdn.microsoft.com/library/en-us/gdi/linecurv_4660.asp) and then draw a line from that pen position to (200, 100) by calling **LineTo**. Note that MoveToEx and [LineTo](http://msdn.microsoft.com/library/en-us/gdi/linecurv_7567.asp) both receive **hdc** as an argument.


```
HDC          hdc;
PAINTSTRUCT  ps;
HPEN         hPen;
HPEN         hPenOld;
hdc = BeginPaint(hWnd, &amp;ps);
   hPen = CreatePen(PS_SOLID, 3, RGB(255, 0, 0));
   hPenOld = (HPEN)SelectObject(hdc, hPen);
   MoveToEx(hdc, 20, 10, NULL);
   LineTo(hdc, 200, 100);
   SelectObject(hdc, hPenOld);
   DeleteObject(hPen);
EndPaint(hWnd, &amp;ps);
```



### Drawing a line with GDI+ and the C++ class interface

To draw a line with GDI+ and the C++ class interface, you need a [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object and a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object. Note that you don't ask Windows for handles to these objects. Instead, you use constructors to create an instance of the **Graphics** class (a **Graphics** object) and an instance of the **Pen** class (a **Pen** object). Drawing a line involves calling the [**Graphics::DrawLine**](/windows/win32/Gdiplusgraphics/?branch=master) method of the **Graphics** class. The first parameter of the **Graphics::DrawLine** method is a pointer to your **Pen** object. This is a simpler and more flexible scheme than selecting a pen into a device context as shown in the preceding GDI example.


```
HDC          hdc;
PAINTSTRUCT  ps;
Pen*         myPen;
Graphics*    myGraphics;
hdc = BeginPaint(hWnd, &amp;ps);
   myPen = new Pen(Color(255, 255, 0, 0), 3);
   myGraphics = new Graphics(hdc);
   myGraphics->DrawLine(myPen, 20, 10, 200, 100);
   delete myGraphics;
   delete myPen;
EndPaint(hWnd, &amp;ps);
```



## Pens, Brushes, Paths, Images, and Fonts as Parameters

The preceding examples show that [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) objects can be created and maintained separately from the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) object, which supplies the drawing methods. [**Brush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-brush?branch=master), [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master), [**Image**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-image?branch=master), and [**Font**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-font?branch=master) objects can also be created and maintained separately from the **Graphics** object. Many of the drawing methods provided by the **Graphics** class receive a **Brush**, **GraphicsPath**, **Image**, or **Font** object as an argument. For example, the address of a **Brush** object is passed as an argument to the [FillRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)?branch=master) method, and the address of a **GraphicsPath** object is passed as an argument to the [**Graphics::DrawPath**](/windows/win32/Gdiplusgraphics/nf-gdiplusgraphics-graphics-drawpath?branch=master) method. Similarly, addresses of **Image** and **Font** objects are passed to the [DrawImage](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawimage(in image,in const point &)?branch=master) and [DrawString](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawstring(const wchar,int,const font,const pointf &,const brush)?branch=master) methods. This is in contrast to GDI where you select a brush, path, image, or font into the device context and then pass a handle to the device context as an argument to a drawing function.

## Method Overloading

Many of the GDI+ methods are overloaded; that is, several methods share the same name but have different parameter lists. For example, the [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class comes in the following forms:


```
Status DrawLine(IN const Pen* pen,
                IN REAL x1,
                IN REAL y1,
                IN REAL x2,
                IN REAL y2);
Status DrawLine(IN const Pen* pen,
                IN const PointF&amp; pt1,
                IN const PointF&amp; pt2);
Status DrawLine(IN const Pen* pen,
                IN INT x1,
                IN INT y1,
                IN INT x2,
                IN INT y2);
    
Status DrawLine(IN const Pen* pen,
                IN const Point&amp; pt1,
                IN const Point&amp; pt2);
```



All four of the [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) variations above receive a pointer to a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object, the coordinates of the starting point, and the coordinates of the ending point. The first two variations receive the coordinates as floating point numbers, and the last two variations receive the coordinates as integers. The first and third variations receive the coordinates as a list of four separate numbers, while the second and fourth variations receive the coordinates as a pair of [**Point**](/windows/win32/gdiplustypes/nl-gdiplustypes-point?branch=master) (or [**PointF**](/windows/win32/gdiplustypes/nl-gdiplustypes-pointf?branch=master)) objects.

## No More Current Position

Note that in the [DrawLine](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawline(in const pen,in const point &,in const point &)?branch=master) methods shown previously both the starting point and the ending point of the line are received as arguments. This is a departure from the GDI scheme where you call to set the current pen position followed by to draw a line starting at (**x1**, **y1**) and ending at (**x2**, **y2**). GDI+ as a whole has abandoned the notion of current position.

## Separate Methods for Draw and Fill

GDI+ is more flexible than GDI when it comes to drawing the outlines and filling the interiors of shapes like rectangles. GDI has a [Rectangle](http://msdn.microsoft.com/library/en-us/gdi/fillshap_6kth.asp) function that draws the outline and fills the interior of a rectangle all in one step. The outline is drawn with the currently selected pen, and the interior is filled with the currently selected brush.


```
hBrush = CreateHatchBrush(HS_CROSS, RGB(0, 0, 255));
hPen = CreatePen(PS_SOLID, 3, RGB(255, 0, 0));
SelectObject(hdc, hBrush);
SelectObject(hdc, hPen);
Rectangle(hdc, 100, 50, 200, 80);
```



GDI+ has separate methods for drawing the outline and filling the interior of a rectangle. The [DrawRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &)?branch=master) method of the [**Graphics**](/windows/win32/gdiplusgraphics/nl-gdiplusgraphics-graphics?branch=master) class has the address of a [**Pen**](/windows/win32/gdipluspen/nl-gdipluspen-pen?branch=master) object as one of its parameters, and the [FillRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)?branch=master) method has the address of a [**Brush**](/windows/win32/gdiplusbrush/nl-gdiplusbrush-brush?branch=master) object as one of its parameters.


```
HatchBrush* myHatchBrush = new HatchBrush(
   HatchStyleCross,
   Color(255, 0, 255, 0),
   Color(255, 0, 0, 255));
Pen* myPen = new Pen(Color(255, 255, 0, 0), 3);
myGraphics.FillRectangle(myHatchBrush, 100, 50, 100, 30);
myGraphics.DrawRectangle(myPen, 100, 50, 100, 30);
```



Note that the [FillRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-fillrectangle(in const brush,in const rect &)?branch=master) and [DrawRectangle](/windows/win32/gdiplusgraphics/nf-gdiplusgraphics-graphics-drawrectangle(in const pen,in const rect &)?branch=master) methods in GDI+ receive arguments that specify the rectangle's left edge, top, width, and height. This is in contrast to the GDI[Rectangle](http://msdn.microsoft.com/library/en-us/gdi/fillshap_6kth.asp) function, which takes arguments that specify the rectangle's left edge, right edge, top, and bottom. Also note that the constructor for the [**Color**](/windows/win32/gdipluscolor/nl-gdipluscolor-color?branch=master) class in GDI+ has four parameters. The last three parameters are the usual red, green, and blue values; the first parameter is the alpha value, which specifies the extent to which the color being drawn is blended with the background color.

## Constructing Regions

GDI provides several functions for creating regions: CreateRectRgn, CreateEllpticRgn, CreateRoundRectRgn, CreatePolygonRgn, and CreatePolyPolygonRgn. You might expect the [**Region**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-region?branch=master) class in GDI+ to have analogous constructors that take rectangles, ellipses, rounded rectangles, and polygons as arguments, but that is not the case. The **Region** class in GDI+ provides a constructor that receives a [**Rect**](/windows/win32/gdiplustypes/nl-gdiplustypes-rect?branch=master) object reference and another constructor that receives the address of a [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object. If you want to construct a region based on an ellipse, rounded rectangle, or polygon, you can easily do so by creating a **GraphicsPath** object (that contains an ellipse, for example) and then passing the address of that **GraphicsPath** object to a **Region** constructor.

GDI+ makes it easy to form complex regions by combining shapes and paths. The [**Region**](/windows/win32/gdiplusheaders/nl-gdiplusheaders-region?branch=master) class has [Union](/windows/win32/gdiplusheaders/nf-gdiplusheaders-region-union(in const graphicspath)?branch=master) and [Intersect](/windows/win32/gdiplusheaders/nf-gdiplusheaders-region-intersect(in const graphicspath)?branch=master) methods that you can use to augment an existing region with a path or another region. One nice feature of the GDI+ scheme is that a [**GraphicsPath**](/windows/win32/gdipluspath/nl-gdipluspath-graphicspath?branch=master) object is not destroyed when it is passed as an argument to a **Region** constructor. In GDI, you can convert a path to a region with the [PathToRegion](http://msdn.microsoft.com/library/en-us/gdi/paths_56lq.asp) function, but the path is destroyed in the process. Also, a **GraphicsPath** object is not destroyed when its address is passed as an argument to a Union or Intersect method, so you can use a given path as a building block for several separate regions. This is shown in the following example. Assume that **onePath** is a pointer to a **GraphicsPath** object (simple or complex) that has already been initialized.


```
Region  region1(rect1);
Region  region2(rect2);
region1.Union(onePath);
region2.Intersect(onePath);
```



 

 



