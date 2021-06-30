---
title: Data Types (HLSL)
description: HLSL supports many different intrinsic data types. This table shows which types to use to define shader variables.
ms.assetid: e4b7738d-e865-4151-a204-0a5b88a913b3
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Data Types (HLSL)

HLSL supports many different intrinsic data types. This table shows which types to use to define shader variables.



| Use this intrinsic type                                                                                                                         | To define this shader variable                                            |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| [Scalar](dx-graphics-hlsl-scalar.md)                                                                                   | One-component scalar                       |
| [Vector](dx-graphics-hlsl-vector.md), [Matrix](dx-graphics-hlsl-matrix.md)                                            | Multiple-component vector or matrix        |
| [Sampler](dx-graphics-hlsl-sampler.md), [Texture](dx-graphics-hlsl-texture.md) or [Buffer](dx-graphics-hlsl-buffer.md)   | Sampler, texture, or buffer object         |
| [Struct](dx-graphics-hlsl-struct.md), [User Defined](dx-graphics-hlsl-user-defined.md)                                | Custom structure or typedef                |
| Array                                                                                   | Literal scalar expressions declared containing most other types                       |
| [State Object](dx-graphics-hlsl-state-object.md) | HLSL representations of state objects |


 

To help you better understand how to use vectors and matrices in HLSL, you may want to read this background information on how HLSL uses [per-component](dx-graphics-hlsl-per-component-math.md) math.

## Related topics

<dl> <dt>

[Variables (DirectX HLSL)](dx-graphics-hlsl-variables.md)
</dt> </dl>

 

 




