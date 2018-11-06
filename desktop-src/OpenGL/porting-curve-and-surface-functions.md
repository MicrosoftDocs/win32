---
title: Porting Curve and Surface Functions
description: Porting Curve and Surface Functions
ms.assetid: 2e80f742-6665-4e7c-a8a1-c43c4764ccc8
keywords:
- IRIS GL porting,curves
- porting from IRIS GL,curves
- porting to OpenGL from IRIS GL,curves
- OpenGL porting from IRIS GL,curves
- IRIS GL porting,surface patches
- porting from IRIS GL,surface patches
- porting to OpenGL from IRIS GL,surface patches
- OpenGL porting from IRIS GL,surface patches
- curves
- surface patches
ms.topic: article
ms.date: 05/31/2018
---

# Porting Curve and Surface Functions

OpenGL doesn't support equivalents to the IRIS GL functions for curves and surface patches. You'll need to rewrite your code if it includes any of the following calls:

-   **defbasis**
-   **curvebasis**, **curveprecision**, **crv**, **crvn**, **rcrv**, **rcrvn**, and **curveit**
-   **patchbasis**, **patchcurves**, **patchprecision**, **patch**, and **rpatch**

This topic includes information on the following.

-   [Porting NURBS Objects](porting-nurbs-objects.md)
-   [Porting NURBS Curves](porting-nurbs-curves.md)
-   [Porting Trimming Curves](porting-trimming-curves.md)
-   [Porting NURBS Surfaces](porting-nurbs-surfaces.md)

 

 




