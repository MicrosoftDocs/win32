---
Description: After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory.
ms.assetid: 73657a66-9415-4db0-a800-463c3d639240
title: Operations on Graphic Objects
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Operations on Graphic Objects

After an application creates a display or printer DC, it can begin drawing on the associated device or, in the case of the memory DC, it can begin drawing on the bitmap stored in memory. However, before drawing begins, and sometimes while drawing is in progress, it is often necessary to replace the default objects with new objects.

An application can examine a default object's attributes by calling the [**GetCurrentObject**](/windows/win32/Wingdi/nf-wingdi-getcurrentobject?branch=master) and [**GetObject**](/windows/win32/Wingdi/nf-wingdi-getobject?branch=master) functions. The **GetCurrentObject** function returns a handle identifying the current pen, brush, palette, bitmap, or font, and the **GetObject** function initializes a structure containing that object's attributes.

Some printers provide resident pens, brushes, and fonts that can be used to improve drawing speed in an application. Two functions can be used to enumerate these objects: [**EnumObjects**](/windows/win32/Wingdi/nf-wingdi-enumobjects?branch=master) and [**EnumFontFamilies**](/windows/win32/Wingdi/nf-wingdi-enumfontfamiliesa?branch=master). If the application must enumerate resident pens or brushes, it can call the **EnumObjects** function to examine the corresponding attributes. If the application must enumerate resident fonts, it can call the **EnumFontFamilies** function (which can also enumerate GDI fonts).

Once an application determines that a default object needs replacing, it creates a new object by calling one of the following creation functions.



| Graphic object | Function                                                                                                                                                                                                                                                                                                                                                             |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Bitmap         | [**CreateBitmap**](/windows/win32/Wingdi/nf-wingdi-createbitmap?branch=master), [**CreateBitmapIndirect**](/windows/win32/Wingdi/nf-wingdi-createbitmapindirect?branch=master), [**CreateCompatibleBitmap**](/windows/win32/Wingdi/nf-wingdi-createcompatiblebitmap?branch=master), [**CreateDiscardableBitmap**](/windows/win32/Wingdi/nf-wingdi-creatediscardablebitmap?branch=master), [**CreateDIBitmap**](/windows/win32/Wingdi/nf-wingdi-createdibitmap?branch=master)                                                                                                           |
| Brush          | [**CreateBrushIndirect**](/windows/win32/Wingdi/nf-wingdi-createbrushindirect?branch=master), [**CreateDIBPatternBrush**](/windows/win32/Wingdi/nf-wingdi-createdibpatternbrush?branch=master), [**CreateDIBPatternBrushPt**](/windows/win32/Wingdi/nf-wingdi-createdibpatternbrushpt?branch=master), [**CreateHatchBrush**](/windows/win32/Wingdi/nf-wingdi-createhatchbrush?branch=master), [**CreatePatternBrush**](/windows/win32/Wingdi/nf-wingdi-createpatternbrush?branch=master), [**CreateSolidBrush**](/windows/win32/Wingdi/nf-wingdi-createsolidbrush?branch=master)                                                 |
| Color Palette  | [**CreatePalette**](/windows/win32/Wingdi/nf-wingdi-createpalette?branch=master)                                                                                                                                                                                                                                                                                                                               |
| Font           | [**CreateFont**](/windows/win32/Wingdi/nf-wingdi-createfonta?branch=master), [**CreateFontIndirect**](/windows/win32/Wingdi/nf-wingdi-createfontindirecta?branch=master)                                                                                                                                                                                                                                                                                   |
| Pen            | [**CreatePen**](/windows/win32/Wingdi/nf-wingdi-createpen?branch=master), [**CreatePenIndirect**](/windows/win32/Wingdi/nf-wingdi-createpenindirect?branch=master), [**ExtCreatePen**](/windows/win32/Wingdi/nf-wingdi-extcreatepen?branch=master)                                                                                                                                                                                                                                                 |
| Region         | [**CreateEllipticRgn**](/windows/win32/Wingdi/nf-wingdi-createellipticrgn?branch=master), [**CreateEllipticRgnIndirect**](/windows/win32/Wingdi/nf-wingdi-createellipticrgnindirect?branch=master), [**CreatePolygonRgn**](/windows/win32/Wingdi/nf-wingdi-createpolygonrgn?branch=master), [**CreatePolyPolygonRgn**](/windows/win32/Wingdi/nf-wingdi-createpolypolygonrgn?branch=master), [**CreateRectRgn**](/windows/win32/Wingdi/nf-wingdi-createrectrgn?branch=master), [**CreateRectRgnIndirect**](/windows/win32/Wingdi/nf-wingdi-createrectrgnindirect?branch=master), [**CreateRoundRectRgn**](/windows/win32/Wingdi/nf-wingdi-createroundrectrgn?branch=master) |



 

Each of these functions returns a handle identifying a new object. After an application retrieves a handle, it must call the [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master) function to replace the default object. However, the application should save the handle identifying the default object and use this handle to replace the new object when it is no longer needed. When the application finishes drawing with the new object, it must restore the default object by calling the **SelectObject** function and then delete the new object by calling the [**DeleteObject**](/windows/win32/Wingdi/nf-wingdi-deleteobject?branch=master) function. Failing to delete objects causes serious performance problems.

 

 



