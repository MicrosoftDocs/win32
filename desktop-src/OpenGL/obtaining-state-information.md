---
title: Obtaining State Information
description: Obtaining State Information
ms.assetid: 86fc8503-92b9-4b5b-8a28-4c9783983ac6
keywords:
- OpenGL,state information
- OpenGL,state variables
- state information OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining State Information

OpenGL maintains many state variables that affect the behavior of many functions. Some of these variables have specialized query functions.

:::row:::
    :::column:::
        [**glGetClipPlane**](glgetclipplane.md)
    :::column-end:::
    :::column:::
        [**glGetPixelMap**](glgetpixelmap.md)
    :::column-end:::
    :::column:::
        [**glGetTexImage**](glgetteximage.md)
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        [**glGetLight**](glgetlight.md)
    :::column-end:::
    :::column:::
        [**glGetPolygonStipple**](glgetpolygonstipple.md)
    :::column-end:::
    :::column:::
        [**glGetTexLevelParameter**](glgettexlevelparameter.md)
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        [**glGetMap**](glgetmap.md)
    :::column-end:::
    :::column:::
        [**glGetTexEnv**](glgettexenv.md)
    :::column-end:::
    :::column:::
        [**glGetTexParameter**](glgettexparameter.md)
    :::column-end:::
:::row-end:::

:::row:::
    :::column:::
        [**glGetMaterial**](glgetmaterial.md)
    :::column-end:::
    :::column:::
        [**glGetTexGen**](glgettexgen.md)
    :::column-end:::
    :::column:::

    :::column-end:::
:::row-end:::

To obtain the value of other state variables, use [**glGetBooleanv**](glgetbooleanv.md), [**glGetDoublev**](glgetdoublev.md), [**glGetFloatv**](glgetfloatv.md), or [**glGetIntegerv**](glgetintegerv.md), as appropriate. See [**glGet**](glgetbooleanv--glgetdoublev--glgetfloatv--glgetintegerv.md) for information about how to use these functions. Other query functions you might want to use are [**glGetError**](glgeterror.md), [**glGetString**](glgetstring.md), and [**glIsEnabled**](glisenabled.md). (See [Handling Errors](handling-errors.md) for more information about functions related to error handling.) To save and restore sets of state variables, use [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md).

-   [Using the Query Functions](using-the-query-functions.md)
-   [Error Handling](error-handling.md)
-   [OpenGL Error Codes](opengl-error-codes.md)
-   [Saving and Restoring Sets of State Variables](saving-and-restoring-sets-of-state-variables.md)
-   [OpenGL State Variables](opengl-state-variables.md)
-   [State Information Reference](state-information-reference.md)

 

 




