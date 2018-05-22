---
Description: 'An application retrieves the dimensions of a region''s bounding rectangle by calling the GetRgnBox function.'
ms.assetid: '3851d0f4-33ec-44db-9cb8-c2afb03ffc25'
title: Retrieving a Bounding Rectangle
---

# Retrieving a Bounding Rectangle

An application retrieves the dimensions of a region's bounding rectangle by calling the [**GetRgnBox**](getrgnbox.md) function. If the region is rectangular, **GetRgnBox** returns the dimensions of the region. If the region is elliptical, the function returns the dimensions of the smallest rectangle that can be drawn around the ellipse. The long sides of the rectangle are the same length as the ellipse's major axis, and the short sides of the rectangle are the same length as the ellipse's minor axis. If the region is polygonal, **GetRgnBox** returns the dimensions of the smallest rectangle that can be drawn around the entire polygon.

 

 



