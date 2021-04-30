---
description: An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.
ms.assetid: e94ae371-8365-4e42-ac8c-04c3928fcffb
title: Region Creation and Selection
ms.topic: article
ms.date: 05/31/2018
---

# Region Creation and Selection

An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.



| Shape                                   | Function                                                                                                                         |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Rectangular region                      | [**CreateRectRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createrectrgn), [**CreateRectRgnIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createrectrgnindirect), [**SetRectRgn**](/windows/desktop/api/Wingdi/nf-wingdi-setrectrgn) |
| Rectangular region with rounded corners | [**CreateRoundRectRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createroundrectrgn)                                                                                 |
| Elliptical region                       | [**CreateEllipticRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createellipticrgn), [**CreateEllipticRgnIndirect**](/windows/desktop/api/Wingdi/nf-wingdi-createellipticrgnindirect)                   |
| Polygonal region                        | [**CreatePolygonRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createpolygonrgn), [**CreatePolyPolygonRgn**](/windows/desktop/api/Wingdi/nf-wingdi-createpolypolygonrgn)                               |



 

Each region creation function returns a handle that identifies the new region. An application can use this handle to select the region into a device context by calling the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function and supplying this handle as the second argument. After a region is selected into a device context, the application can perform various operations on it.

 

 



