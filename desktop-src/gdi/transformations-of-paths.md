---
description: Paths are defined using logical units and current transformations.
ms.assetid: a5a426ec-25e8-4fe1-985c-d078227e8aba
title: Transformations of Paths
ms.topic: article
ms.date: 05/31/2018
---

# Transformations of Paths

Paths are defined using logical units and current transformations. (If the [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) function has been called, the logical units are world units; otherwise, the logical units are page units.) An application can use world transformations to scale, rotate, shear, translate, and reflect the lines and Bézier curves that define a path.

> [!Note]  
> A world transformation within a path bracket only affects those lines and curves drawn after the transformation was set. It will have no affect on those lines and curves that were drawn before it was set. For a description of the world transformation, see [Coordinate Spaces and Transformations](coordinate-spaces-and-transformations.md).

 

An application can also use [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) to outline the shape of the pen used to outline a path if the pen is a geometric pen. For a description of geometric pens, see [Pens](pens.md).

 

 



