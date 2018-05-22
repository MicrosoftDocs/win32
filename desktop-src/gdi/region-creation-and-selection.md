---
Description: 'An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.'
ms.assetid: 'e94ae371-8365-4e42-ac8c-04c3928fcffb'
title: Region Creation and Selection
---

# Region Creation and Selection

An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.



| Shape                                   | Function                                                                                                                         |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Rectangular region                      | [**CreateRectRgn**](createrectrgn.md), [**CreateRectRgnIndirect**](createrectrgnindirect.md), [**SetRectRgn**](setrectrgn.md) |
| Rectangular region with rounded corners | [**CreateRoundRectRgn**](createroundrectrgn.md)                                                                                 |
| Elliptical region                       | [**CreateEllipticRgn**](createellipticrgn.md), [**CreateEllipticRgnIndirect**](createellipticrgnindirect.md)                   |
| Polygonal region                        | [**CreatePolygonRgn**](createpolygonrgn.md), [**CreatePolyPolygonRgn**](createpolypolygonrgn.md)                               |



 

Each region creation function returns a handle that identifies the new region. An application can use this handle to select the region into a device context by calling the [**SelectObject**](selectobject.md) function and supplying this handle as the second argument. After a region is selected into a device context, the application can perform various operations on it.

 

 



