---
Description: 'After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory.'
ms.assetid: '73657a66-9415-4db0-a800-463c3d639240'
title: Operations on Graphic Objects
---

# Operations on Graphic Objects

After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory. However, before drawing begins, and sometimes while drawing is in progress, it is often necessary to replace the default objects with new objects.

An application can examine a default object's attributes by calling the [**GetCurrentObject**](getcurrentobject.md) and [**GetObject**](getobject.md) functions. The **GetCurrentObject** function returns a handle identifying the current pen, brush, palette, bitmap, or font, and the **GetObject** function initializes a structure containing that object's attributes.

Some printers provide resident pens, brushes, and fonts that can be used to improve drawing speed in an application. Two functions can be used to enumerate these objects: [**EnumObjects**](enumobjects.md) and [**EnumFontFamilies**](enumfontfamilies.md). If the application must enumerate resident pens or brushes, it can call the **EnumObjects** function to examine the corresponding attributes. If the application must enumerate resident fonts, it can call the **EnumFontFamilies** function (which can also enumerate GDI fonts).

Once an application determines that a default object needs replacing, it creates a new object by calling one of the following creation functions.



| Graphic object | Function                                                                                                                                                                                                                                                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bitmap         | [**CreateBitmap**](createbitmap.md), [**CreateBitmapIndirect**](createbitmapindirect.md), [**CreateCompatibleBitmap**](createcompatiblebitmap.md), [**CreateDiscardableBitmap**](creatediscardablebitmap.md), [**CreateDIBitmap**](createdibitmap.md)                                                                                                           |
| Brush          | [**CreateBrushIndirect**](createbrushindirect.md), [**CreateDIBPatternBrush**](createdibpatternbrush.md), [**CreateDIBPatternBrushPt**](createdibpatternbrushpt.md), [**CreateHatchBrush**](createhatchbrush.md), [**CreatePatternBrush**](createpatternbrush.md), [**CreateSolidBrush**](createsolidbrush.md)                                                 |
| Color Palette  | [**CreatePalette**](createpalette.md)                                                                                                                                                                                                                                                                                                                               |
| Font           | [**CreateFont**](createfont.md), [**CreateFontIndirect**](createfontindirect.md)                                                                                                                                                                                                                                                                                   |
| Pen            | [**CreatePen**](createpen.md), [**CreatePenIndirect**](createpenindirect.md), [**ExtCreatePen**](extcreatepen.md)                                                                                                                                                                                                                                                 |
| Region         | [**CreateEllipticRgn**](createellipticrgn.md), [**CreateEllipticRgnIndirect**](createellipticrgnindirect.md), [**CreatePolygonRgn**](createpolygonrgn.md), [**CreatePolyPolygonRgn**](createpolypolygonrgn.md), [**CreateRectRgn**](createrectrgn.md), [**CreateRectRgnIndirect**](createrectrgnindirect.md), [**CreateRoundRectRgn**](createroundrectrgn.md) |



 

Each of these functions returns a handle identifying a new object. After an application retrieves a handle, it must call the [**SelectObject**](selectobject.md) function to replace the default object. However, the application should save the handle identifying the default object and use this handle to replace the new object when it is no longer needed. When the application finishes drawing with the new object, it must restore the default object by calling the **SelectObject** function and then delete the new object by calling the [**DeleteObject**](deleteobject.md) function. Failing to delete objects causes serious performance problems.

 

 



