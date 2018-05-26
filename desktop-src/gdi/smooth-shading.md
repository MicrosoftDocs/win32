---
Description: Smooth shading is a method of shading a region with a color gradient.
ms.assetid: 94f26d15-fb76-47ec-b805-f04975d41b43
title: Smooth Shading
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Smooth Shading

*Smooth shading* is a method of shading a region with a color gradient. Including color information, along with the bounds of drawing primitive, specifies the color gradient. GDI linearly interpolates the color of the inside of the primitive passed on the color endpoints. Color and vertex information is included with position information in the [**TRIVERTEX**](/windows/win32/Wingdi/ns-wingdi-_trivertex?branch=master) structure.

Use the [**GradientFill**](/windows/win32/WinGdi/nf-wingdi-gradientfill?branch=master) function to fill a triangle or rectangle structure. To fill a triangle with smooth shading, call **GradientFill** with the three triangle endpoints. To fill a rectangle with smooth shading, call **GradientFill** with the upper-left and lower-right rectangle coordinates. **GradientFill** references the [**TRIVERTEX**](/windows/win32/Wingdi/ns-wingdi-_trivertex?branch=master), [**GRADIENT\_RECT**](/windows/win32/Wingdi/ns-wingdi-_gradient_rect?branch=master), and [**GRADIENT\_TRIANGLE**](/windows/win32/Wingdi/ns-wingdi-_gradient_triangle?branch=master) structures.

For an example, see [Drawing a Shaded Triangle](drawing-a-shaded-triangle.md).

 

 



