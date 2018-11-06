---
title: Porting Trimming Curves
description: OpenGL trimming curves are very similar to IRIS GL trimming curves. The following table lists the IRIS GL functions for defining trimming curves and their equivalent OpenGL functions.
ms.assetid: 9aeea9ca-5ecd-4be1-853d-45b1566b263b
keywords:
- IRIS GL porting,trimming curves
- porting from IRIS GL,trimming curves
- porting to OpenGL from IRIS GL,trimming curves
- OpenGL porting from IRIS GL,trimming curves
- trimming curves
- curves
- IRIS GL porting,curves
- porting from IRIS GL,curves
- porting to OpenGL from IRIS GL,curves
- OpenGL porting from IRIS GL,curves
ms.topic: article
ms.date: 05/31/2018
---

# Porting Trimming Curves

OpenGL trimming curves are very similar to IRIS GL trimming curves. The following table lists the IRIS GL functions for defining trimming curves and their equivalent OpenGL functions.



| IRIS GL function | OpenGL function                        | Meaning                              |
|------------------|----------------------------------------|--------------------------------------|
| **bgntrim**      | [**gluBeginTrim**](glubegintrim.md)   | Begins trimming-curve definition.    |
| **pwlcurve**     | [**gluPwlCurve**](glupwlcurve.md)     | Defines a piecewise linear curve.    |
| **nurbscurve**   | [**gluNurbsCurve**](glunurbscurve.md) | Specifies trimming-curve attributes. |
| **endtrim**      | [**gluEndTrim**](gluendtrim.md)       | Ends trimming-curve definition.      |



 

??

 

 




