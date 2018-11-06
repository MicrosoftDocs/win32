---
title: OpenGL State Variables
description: The following topics list the names of state variables that can be queried
ms.assetid: f4bc4ec1-a529-4b9e-84af-94caa0ef7131
keywords:
- OpenGL state variables
- state variables, OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# OpenGL State Variables

The following topics list the names of state variables that can be queried:

-   [**State Variables for Current Values and Associated Data**](state-variables-for-current-values-and-associated-data.md)
-   [**Transformation State Variables**](transformation-state-variables.md)
-   [**Coloring State Variables**](coloring-state-variables.md)
-   [**Lighting State Variables**](lighting-state-variables.md)
-   [**Rasterization State Variables**](rasterization-state-variables.md)
-   [**Texturing State Variables**](texturing-state-variables.md)
-   [**Pixel Operations**](pixel-operations.md)
-   [**Framebuffer Control State Variables**](framebuffer-control-state-variables.md)
-   [**Pixel State Variables**](pixel-state-variables.md)
-   [**Evaluator State Variables**](evaluator-state-variables.md)
-   [**Hint State Variables**](hint-state-variables.md)
-   [**Implementation-Dependent State Variables**](implementation-dependent-state-variables.md)
-   [**Implementation-Dependent Pixel-Depth State Variables**](implementation-dependent-pixel-depth-state-variables.md)
-   [**Miscellaneous State Variables**](miscellaneous-state-variables.md)

For each variable, the topic lists a description, attribute group, initial or minimum value, and the suggested [**glGet\***](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) function to use for obtaining it.

State variables that you can obtain using [**glGetBooleanv**](glgetbooleanv.md), [**glGetIntegerv**](glgetintegerv.md), [**glGetFloatv**](glgetfloatv.md), or [**glGetDoublev**](glgetdoublev.md) are listed with just one of these functionsthe one that is most appropriate for the type of data to be returned. You cannot obtain these state variables using [**glIsEnabled**](glisenabled.md). However, you can obtain state variables for which **glIsEnabled** is listed as the query function with **glGetBooleanv**, **glGetIntegerv**, **glGetFloatv**, and **glGetDoublev**. You can obtain state variables for which any other function is listed as the query function only by using that function. If no attribute group is listed, the variable doesn't belong to any group. All state variables that you can query, except those that are implementation dependent, have initial values. To determine the initial value of a variable for which no initial value is listed, see that variable's reference or the

*OpenGL Reference Manual*.

 

 




