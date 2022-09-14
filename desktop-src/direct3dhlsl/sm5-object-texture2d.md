---
title: Texture2D
description: Texture2D
ms.assetid: e4f9cfd8-65e6-4375-8f87-736bca32cad4
keywords:
- Texture2D HLSL
topic_type:
- apiref
api_name:
- Texture2D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2D

Texture2D type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                 | Description                                                                                                                                        |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Gather**](texture2d-gather.md)                                      | Returns the four texel values that would be used in a bi-linear filtering operation.                                                                |
| [**GatherRed**](texture2d-gatherred.md)                                | Returns the red components of the four texel values that would be used in a bi-linear filtering operation.                                          |
| [**GatherGreen**](texture2d-gathergreen.md)                            | Returns the green components of the four texel values that would be used in a bi-linear filtering operation.                                        |
| [**GatherBlue**](texture2d-gatherblue.md)                              | Returns the blue components of the four texel values that would be used in a bi-linear filtering operation.                                         |
| [**GatherAlpha**](texture2d-gatheralpha.md)                            | Returns the alpha components of the four texel values that would be used in a bi-linear filtering operation.                                        |
| [**GatherCmp**](texture2d-gathercmp.md)                                | For four texel values that would be used in a bi-linear filtering operation, returns their comparison against a compare value.                      |
| [**GatherCmpRed**](texture2d-gathercmpred.md)                          | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their red component against a compare value.   |
| [**GatherCmpGreen**](texture2d-gathercmpgreen.md)                      | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value. |
| [**GatherCmpBlue**](texture2d-gathercmpblue.md)                        | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their blue component against a compare value.  |
| [**GatherCmpAlpha**](texture2d-gathercmpalpha.md)                      | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their alpha component against a compare value. |
| [**GetDimensions**](sm5-object-texture2d-getdimensions.md)             | Gets the resource dimensions.                                                                                                                       |
| [**Load**](texture2d-load.md)                                          | Reads texture data.                                                                                                                                 |
| [**mips.Operator\[\]\[\]**](sm5-object-texture2d-mipsoperatorindex.md) | Gets a read-only resource variable.                                                                                                                 |
| [**Operator\[\]**](sm5-object-texture2d-operatorindex.md)              | Gets a read-only resource variable.                                                                                                                 |
| [**Sample**](texture-sample-overload.md)                               | Samples a texture.                                                                                                                                  |
| [**SampleBias**](texture2d-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                                                                               |
| [**SampleCmp**](texture2d-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                                                                                      |
| [**SampleCmpLevelZero**](texture2d-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.                                                                |
| [**SampleGrad**](texture2d-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated.                                                          |
| [**SampleLevel**](texture2d-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                                                                                    |



 

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

 

 




