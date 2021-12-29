---
description: WorldToObject4x3 - A matrix for transforming from world-space to object-space.
ms.assetid: 
title: WorldToObject4x3
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WorldToObject4x3
api_type: 
- NA
---

# WorldToObject4x3

A matrix for transforming from world-space to object-space. Object-space refers to the space of the current bottom-level acceleration structure.

## Syntax

```
void WorldToObject4x3();

```




## Remarks

The matrix is a transposition of **WorldToObject3x4** matrix.

This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




