---
Description: A function is the building block for a shader created in the high-level language. If you prefer to write shaders in a C-style language instead of in assembly language, you will want to write functions.
ms.assetid: e9243c05-e943-4a42-ab73-e684900fc81d
title: Effect Function Syntax (Direct3D 9)
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Effect Function Syntax (Direct3D 9)

A function is the building block for a shader created in the high-level language. If you prefer to write shaders in a C-style language instead of in assembly language, you will want to write functions.

## Syntax


```
type id ( [ parameters ] )  
    { body }
```



Functions do not change parameter values in an effect.

-   type - Any valid [Reference for HLSL](direct3dhlsl.dx_graphics_hlsl_reference) type.
-   id - A unique name.
-   parameters - Function parameters.
-   body - The body of the function.

Functions are built from the high-level language. See [Reference for HLSL](direct3dhlsl.dx_graphics_hlsl_reference).

## Related topics

<dl> <dt>

[Effect Format](dx9-graphics-reference-effects-file-format.md)
</dt> </dl>

 

 



