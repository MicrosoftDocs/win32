---
title: Texture1DArray
description: Texture1DArray
ms.assetid: 3d793423-3d79-48c1-aa78-f9d93b79e0b6
keywords:
- Texture1DArray HLSL
topic_type:
- apiref
api_name:
- Texture1DArray
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture1DArray

Texture1DArray type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                       | Description                                                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**GetDimensions**](sm5-object-texture1darray-getdimensions.md)             | Gets the resource dimensions.                                                              |
| [**Load**](texture1darray-load.md)                                          | Reads texture data.                                                                        |
| [**mips.Operator\[\]\[\]**](sm5-object-texture1darray-mipsoperatorindex.md) | Gets a read-only resource variable.                                                        |
| [**Operator\[\]**](sm5-object-texture1darray-operatorindex.md)              | Gets a read-only resource variable.                                                        |
| [**Sample**](texture1darray-sample.md)                                      | Samples a texture.                                                                         |
| [**SampleBias**](texture1darray-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                      |
| [**SampleCmp**](texture1darray-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                             |
| [**SampleCmpLevelZero**](texture1darray-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.       |
| [**SampleGrad**](texture1darray-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated. |
| [**SampleLevel**](texture1darray-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                           |



 

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

 

 




