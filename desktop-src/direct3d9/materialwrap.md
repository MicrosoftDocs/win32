---
description: Defines a set of two Boolean values used in the MeshFaceWraps template to define the texture topology of an individual face. Use instead of Boolean2d when the texture coordinates (u, v) span the range of 0 to 2 instead of 0 to 1.
ms.assetid: 0d1755fc-66cb-4372-b9d0-fb320c55d6a7
title: MaterialWrap
ms.topic: reference
ms.date: 05/31/2018
---

# MaterialWrap

Defines a set of two Boolean values used in the [**MeshFaceWraps**](meshfacewraps.md) template to define the texture topology of an individual face. Use instead of [**Boolean2d**](boolean2d.md) when the texture coordinates (u, v) span the range of 0 to 2 instead of 0 to 1.

``` syntax
template MaterialWrap
{
    < 4885ae60-78e8-11cf-8f52-0040333594a3 >
    Boolean u;
    Boolean v;
} 
```

Where:

-   u - Boolean value. See [**Boolean**](boolean.md).
-   v - Boolean value. See [**Boolean**](boolean.md).

> [!Note]  
> The [**MeshFaceWraps**](meshfacewraps.md) template is no longer used.

 

## See also

<dl> <dt>

[Templates](dx9-graphics-reference-x-file-format-templates.md)
</dt> </dl>

 

 



