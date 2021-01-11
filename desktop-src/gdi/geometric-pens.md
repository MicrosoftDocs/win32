---
description: The dimensions of a geometric pen are specified in logical units.
ms.assetid: e7030490-d10c-4d1c-87ae-5b4cc4858ee1
title: Geometric Pens
ms.topic: article
ms.date: 05/31/2018
---

# Geometric Pens

The dimensions of a geometric pen are specified in logical units. Therefore, lines drawn with a geometric pen can be scaled that is, they may appear wider or narrower, depending on the current world transformation. For more information about world transformation, see [Coordinate Spaces and Transformations](coordinate-spaces-and-transformations.md).

In addition to the three attributes shared with cosmetic pens (width, style, and color), geometric pens possess the following four attributes: pattern, optional hatch, end style, and join style. For more information about these attributes, see [Pen Attributes](pen-attributes.md).

To create a geometric pen, an application uses the [**ExtCreatePen**](/windows/desktop/api/Wingdi/nf-wingdi-extcreatepen) function. As with cosmetic pens, the [**SelectObject**](/windows/desktop/api/Wingdi/nf-wingdi-selectobject) function selects a geometric pen into the application's DC.

 

 



