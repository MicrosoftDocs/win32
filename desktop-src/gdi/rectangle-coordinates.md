---
description: An application must use a RECT structure to define a rectangle.
ms.assetid: 93c63dcb-6c8e-4c8b-aa19-6f8952d75e2e
title: Rectangle Coordinates
ms.topic: article
ms.date: 05/31/2018
---

# Rectangle Coordinates

An application must use a [**RECT**](/windows/win32/api/windef/ns-windef-rect) structure to define a rectangle. The structure specifies the coordinates of two points: the upper left and lower right corners of the rectangle. The sides of the rectangle extend from these two points and are parallel to the x-axis and y-axis.

The coordinate values for a rectangle are expressed as signed integers. The coordinate value of a rectangle's right side must be greater than that of its left side. Likewise, the coordinate value of the bottom must be greater than that of the top.

Because applications can use rectangles for many different purposes, the rectangle functions do not use an explicit unit of measure. Instead, all rectangle coordinates and dimensions are given in signed, logical values. The mapping mode and the function in which the rectangle is used determine the units of measure. For more information about coordinates and mapping modes, see [Coordinate Spaces and Transformations](coordinate-spaces-and-transformations.md).

 

 
