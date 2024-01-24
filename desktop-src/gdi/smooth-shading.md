---
description: Smooth shading is a method of shading a region with a color gradient.
ms.assetid: 94f26d15-fb76-47ec-b805-f04975d41b43
title: Smooth Shading
ms.topic: article
ms.date: 05/31/2018
---

# Smooth Shading

*Smooth shading* is a method of shading a region with a color gradient. Including color information, along with the bounds of drawing primitive, specifies the color gradient. GDI linearly interpolates the color of the inside of the primitive passed on the color endpoints. Color and vertex information is included with position information in the [**TRIVERTEX**](/windows/desktop/api/Wingdi/ns-wingdi-trivertex) structure.

Use the [**GradientFill**](/windows/desktop/api/WinGdi/nf-wingdi-gradientfill) function to fill a triangle or rectangle structure. To fill a triangle with smooth shading, call **GradientFill** with the three triangle endpoints. To fill a rectangle with smooth shading, call **GradientFill** with the upper-left and lower-right rectangle coordinates. **GradientFill** references the [**TRIVERTEX**](/windows/desktop/api/Wingdi/ns-wingdi-trivertex), [**GRADIENT\_RECT**](/windows/desktop/api/Wingdi/ns-wingdi-gradient_rect), and [**GRADIENT\_TRIANGLE**](/windows/desktop/api/Wingdi/ns-wingdi-gradient_triangle) structures.

For an example, see [Drawing a Shaded Triangle](drawing-a-shaded-triangle.md).

 

 



