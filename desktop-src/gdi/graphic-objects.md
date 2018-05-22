---
Description: 'The pen, brush, bitmap, palette, region, and path associated with a DC are referred to as its graphic objects. The following attributes are associated with each of these objects.'
ms.assetid: '95c82efa-257e-4718-9853-7ef10cdfd76c'
title: Graphic Objects
---

# Graphic Objects

The pen, brush, bitmap, palette, region, and path associated with a DC are referred to as its graphic objects. The following attributes are associated with each of these objects.



| Graphic object | Associated attributes                                                               |
|----------------|-------------------------------------------------------------------------------------|
| Bitmap         | Size, in bytes; dimensions, in pixels; color-format; compression scheme; and so on. |
| Brush          | Style, color, pattern, and origin.                                                  |
| Palette        | Colors and size (or number of colors).                                              |
| Font           | Typeface name, width, height, weight, character set, and so on.                     |
| Path           | Shape.                                                                              |
| Pen            | Style, width, and color.                                                            |
| Region         | Location and dimensions.                                                            |



 

When an application creates a DC, the system automatically stores a set of default objects in it (there is no default bitmap or path). An application can examine the attributes of the default objects by calling the [**GetCurrentObject**](getcurrentobject.md) and [**GetObject**](getobject.md) functions. The application can change these defaults by creating a new object and selecting it into the DC. An object is selected into a DC by calling the [**SelectObject**](selectobject.md) function.

An application can set the current brush color to a specified color value with [**SetDCBrushColor**](setdcbrushcolor.md).

The [**GetDCBrushColor**](getdcbrushcolor.md) function returns the DC brush color. The [**SetDCPenColor**](setdcpencolor.md) function sets the pen color to a specified color value. The [**GetDCPenColor**](getdcpencolor.md) function returns the DC pen color.

 

 



