---
Description: An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.
ms.assetid: e94ae371-8365-4e42-ac8c-04c3928fcffb
title: Region Creation and Selection
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Region Creation and Selection

An application creates a region by calling a function associated with a specific shape. The following table shows the function(s) associated with each of the standard shapes.



| Shape                                   | Function                                                                                                                         |
|-----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Rectangular region                      | [**CreateRectRgn**](/windows/win32/Wingdi/nf-wingdi-createrectrgn?branch=master), [**CreateRectRgnIndirect**](/windows/win32/Wingdi/nf-wingdi-createrectrgnindirect?branch=master), [**SetRectRgn**](/windows/win32/Wingdi/nf-wingdi-setrectrgn?branch=master) |
| Rectangular region with rounded corners | [**CreateRoundRectRgn**](/windows/win32/Wingdi/nf-wingdi-createroundrectrgn?branch=master)                                                                                 |
| Elliptical region                       | [**CreateEllipticRgn**](/windows/win32/Wingdi/nf-wingdi-createellipticrgn?branch=master), [**CreateEllipticRgnIndirect**](/windows/win32/Wingdi/nf-wingdi-createellipticrgnindirect?branch=master)                   |
| Polygonal region                        | [**CreatePolygonRgn**](/windows/win32/Wingdi/nf-wingdi-createpolygonrgn?branch=master), [**CreatePolyPolygonRgn**](/windows/win32/Wingdi/nf-wingdi-createpolypolygonrgn?branch=master)                               |



 

Each region creation function returns a handle that identifies the new region. An application can use this handle to select the region into a device context by calling the [**SelectObject**](/windows/win32/Wingdi/nf-wingdi-selectobject?branch=master) function and supplying this handle as the second argument. After a region is selected into a device context, the application can perform various operations on it.

 

 



