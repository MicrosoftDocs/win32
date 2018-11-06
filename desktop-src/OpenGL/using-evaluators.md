---
title: Using Evaluators
description: Using Evaluators
ms.assetid: a5a99d0a-526e-4492-90c4-a6b9fdbdff16
keywords:
- OpenGL,evaluators
- evaluators OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Using Evaluators

The OpenGL evaluator functions allow you to use a polynomial mapping to produce vertices, normals, texture coordinates, and colors. These calculated values are then passed on to the processing pipeline as if they had been directly specified. The evaluator functions are also the basis for the NURBS (Non-Uniform Rational B-Spline) functions, which allow you to define curves and surfaces, as described under [OpenGL Utility library](opengl-utility-library.md).

The first step in using evaluators is to define the appropriate one- or two-dimensional polynomial mapping using [**glMap\***](glmap1.md). You can then specify and evaluate the domain values for this map in one of two ways:

-   Define a series of evenly spaced domain values to be mapped using [**glMapGrid**](glmapgrid-functions.md) and then evaluate a rectangular subset of that grid with [**glEvalMesh**](glevalmesh-functions.md). A single point of the grid can be evaluated using [**glEvalPoint**](glevalpoint.md).
-   Explicitly specify a desired domain value as an argument, which evaluates the maps at that value.

## Related topics

<dl> <dt>

[Evaluators Reference](evaluators-reference.md)
</dt> </dl>

 

 




