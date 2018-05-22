---
Description: 'Smooth shading is a method of shading a region with a color gradient.'
ms.assetid: '94f26d15-fb76-47ec-b805-f04975d41b43'
title: Smooth Shading
---

# Smooth Shading

*Smooth shading* is a method of shading a region with a color gradient. Including color information, along with the bounds of drawing primitive, specifies the color gradient. GDI linearly interpolates the color of the inside of the primitive passed on the color endpoints. Color and vertex information is included with position information in the [**TRIVERTEX**](trivertex.md) structure.

Use the [**GradientFill**](gradientfill.md) function to fill a triangle or rectangle structure. To fill a triangle with smooth shading, call **GradientFill** with the three triangle endpoints. To fill a rectangle with smooth shading, call **GradientFill** with the upper-left and lower-right rectangle coordinates. **GradientFill** references the [**TRIVERTEX**](trivertex.md), [**GRADIENT\_RECT**](gradient-rect.md), and [**GRADIENT\_TRIANGLE**](gradient-triangle.md) structures.

For an example, see [Drawing a Shaded Triangle](drawing-a-shaded-triangle.md).

 

 



