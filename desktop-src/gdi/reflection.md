---
description: Some applications provide features that reflect (or mirror) objects drawn in the client area.
ms.assetid: 2205dc3c-ca4b-4a0a-be3e-0332ce8467a0
title: Reflection
ms.topic: article
ms.date: 05/31/2018
---

# Reflection

Some applications provide features that reflect (or mirror) objects drawn in the client area. Applications that contain reflection capabilities use the [**SetWorldTransform**](/windows/desktop/api/Wingdi/nf-wingdi-setworldtransform) function to set the appropriate values in the world-space to page-space transformation. This function receives a pointer to an [**XFORM**](/windows/win32/api/wingdi/ns-wingdi-xform) structure containing the appropriate values. The eM11 and eM22 members of XFORM specify the horizontal and vertical reflection components, respectively.

The *reflection transformation* creates a mirror image of an object with respect to either the x- or y-axis. In short, reflection is just negative scaling. To produce a horizontal reflection, x-coordinates are multiplied by -1. To produce a vertical reflection, y-coordinates are multiplied by -1.

Horizontal reflection can be represented by the following algorithm:

``` syntax
x' = -x 
```

where x is the x-coordinate and x' is the result of the reflection.

The 2-by-2 matrix that produced horizontal reflection contains the following values:

``` syntax
|-1    0| 
|0     1| 
```

Vertical reflection can be represented by the following algorithm:

``` syntax
y' = -y 
```

where y is the y-coordinate and y' is the result of the reflection.

The 2-by-2 matrix that produced vertical reflection contains the following values:

``` syntax
|1    0| 
|0   -1| 
```

The horizontal-reflection and vertical-reflection operations can be combined into a single operation by using the following 2-by-2 matrix:

``` syntax
|-1    0| 
|0    -1| 
```

 

 



