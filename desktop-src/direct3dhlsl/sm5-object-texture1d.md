---
title: Texture1D
description: Texture1D
ms.assetid: 5f6fd0e4-a73e-4d13-b3a0-c884b7912581
keywords:
- Texture1D HLSL
topic_type:
- apiref
api_name:
- Texture1D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture1D

A 1D texture type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                  | Description                                                                                |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**GetDimensions**](sm5-object-texture1d-getdimensions.md)             | Gets the resource dimensions.                                                              |
| [**Load**](texture1d-load.md)                                          | Reads texture data.                                                                        |
| [**Operator\[\]**](sm5-object-texture1d-operatorindex.md)              | Gets a read-only resource variable.                                                        |
| [**mips.Operator\[\]\[\]**](sm5-object-texture1d-mipsoperatorindex.md) | Gets a read-only resource variable.                                                        |
| [**Sample**](texture1d-sample.md)                                      | Samples a texture.                                                                         |
| [**SampleBias**](texture1d-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                      |
| [**SampleCmp**](texture1d-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                             |
| [**SampleCmpLevelZero**](texture1d-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.       |
| [**SampleGrad**](texture1d-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated. |
| [**SampleLevel**](texture1d-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                           |



 

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

 

 




