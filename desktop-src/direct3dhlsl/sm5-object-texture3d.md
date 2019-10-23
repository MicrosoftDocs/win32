---
title: Texture3D
description: Texture3D
ms.assetid: a3640aac-b503-4716-8bc6-105e96bea03c
keywords:
- Texture3D HLSL
topic_type:
- apiref
api_name:
- Texture3D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture3D

Texture3D type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                  | Description                                                                                |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**GetDimensions**](sm5-object-texture3d-getdimensions.md)             | Gets the resource dimensions.                                                              |
| [**Load**](texture3d-load.md)                                          | Reads texture data.                                                                        |
| [**mips.Operator\[\]\[\]**](sm5-object-texture3d-mipsoperatorindex.md) | Gets a read-only resource variable.                                                        |
| [**Operator\[\]**](sm5-object-texture3d-operatorindex.md)              | Gets a read-only resource variable.                                                        |
| [**Sample**](texture3d-sample.md)                                      | Samples a texture.                                                                         |
| [**SampleBias**](texture3d-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                      |
| [**SampleGrad**](texture3d-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated. |
| [**SampleLevel**](texture3d-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                           |



 

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

 




