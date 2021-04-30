---
description: ObjectToWorld3x4 - A matrix for transforming from object-space to world-space.
ms.assetid: 
title: ObjectToWorld3x4
ms.localizationpriority: low
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ObjectToWorld3x4
api_type: 
- NA
---

# ObjectToWorld3x4

A matrix for transforming from object-space to world-space. Object-space refers to the space of the current bottom-level acceleration structure.

## Syntax

```
void ObjectToWorld3x4();

```




## Remarks

The matrix is a transposition of **ObjectToWorld4x3** matrix.

This function can be called from the following raytracing shader types:

* [**Any Hit Shader**](any-hit-shader.md)
* [**Closest Hit Shader**](closest-hit-shader.md)
* [**Intersection Shader**](intersection-shader.md)





## See also

<dl> <dt>

[Direct3D 12 Raytracing HLSL Reference](direct3d-12-raytracing-hlsl-reference.md)
</dt> </dl>

 

 




