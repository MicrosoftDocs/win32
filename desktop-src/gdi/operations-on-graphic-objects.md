---
description: After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory.
ms.assetid: 73657a66-9415-4db0-a800-463c3d639240
title: Operations on Graphic Objects
ms.topic: article
ms.date: 05/31/2018
---

# Operations on Graphic Objects

After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory. However, before drawing begins, and sometimes while drawing is in progress, it is often necessary to replace the default objects with new objects.

An application can examine a default object's attributes by calling the [**GetCurrentObject**](/windows/desktop/api/Wingdi/nf-wingdi-getcurrentobject) and [**GetObject**](/windows/desktop/api/Wingdi/nf-wingdi-getobject) functions. The **GetCurrentObject** function returns a handle identifying the current pen, brush, palette, bitmap, or font, and the **GetObject** function initializes a structure containing that object's attributes.

Some printers provide resident pens, brushes, and fonts that can be used to improve drawing speed in an application. Two functions can be used to enumerate these objects: [**EnumObjects**](/windows/desktop/api/Wingdi/nf-wingdi-enumobjects) and [**EnumFontFamilies**](/windows/desktop/api/Wingdi/nf-wingdi-enumfontfamiliesa). If the application must enumerate resident pens or brushes, it can call the **EnumObjects** function to examine the corresponding attributes. If the application must enumerate resident fonts, it can call the **EnumFontFamilies** function (which can also enumerate GDI fonts).

Once an application determines that a default object needs replacing, it creates a new object by calling one of the following creation functions.



| Graphic object | Function                                                                                                                                                                                                                                                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bitmap         | [**CreateBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmap), [**CreateBitmapIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbitmapindirect), [**CreateCompatibleBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createcompatiblebitmap), [**CreateDiscardableBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-creatediscardablebitmap), [**CreateDIBitmap**](/windows/desktop/api/Wingdi/nf-wingdi-createdibitmap)                                                                                                           |
| Brush          | [**CreateBrushIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createbrushindirect), [**CreateDIBPatternBrush**](/windows/desktop/api/Wingdi/nf-wingdi-createdibpatternbrush), [**CreateDIBPatternBrushPt**](/windows/desktop/api/Wingdi/nf-wingdi-createdibpatternbrushpt), [**CreateHatchBrush**](/windows/desktop/api/Wingdi/nf-wingdi-createhatchbrush), [**CreatePatternBrush**](/windows/desktop/api/Wingdi/nf-wingdi-createpatternbrush), [**CreateSolidBrush**](/windows/desktop/api/Wingdi/nf-wingdi-createsolidbrush)                                                 |
| Color Palette  | [**CreatePalette**](/windows/desktop/api/Wingdi/nf-wingdi-createpalette)                                                                                                                                                                                                                                                                                                                               |
| Font           | [**CreateFont**](/windows/desktop/api/Wingdi/nf-wingdi-createfonta), [**CreateFontIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createfontindirecta)                                                                                                                                                                                                                                                                                   |
| Pen            | [**CreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-createpen), [**CreatePenIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createpenindirect), [**ExtCreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-extcreatepen)                                                                                                                                                                                                                                                 |
| Region         | [**CreateEllipticRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createellipticrgn), [**CreateEllipticRgnIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createellipticrgnindirect), [**CreatePolygonRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createpolygonrgn), [**CreatePolyPolygonRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createpolypolygonrgn), [**CreateRectRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createrectrgn), [**CreateRectRgnIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createrectrgnindirect), [**CreateRoundRectRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createroundrectrgn) |



 

Each of these functions returns a handle identifying a new object. After an application retrieves a handle, it must call the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function to replace the default object. However, the application should save the handle identifying the default object and use this handle to replace the new object when it is no longer needed. When the application finishes drawing with the new object, it must restore the default object by calling the **SelectObject** function and then delete the new object by calling the [**DeleteObject**](/windows/desktop/api/Wingdi/nf-wingdi-deleteobject) function. Failing to delete objects causes serious performance problems.

 

 



