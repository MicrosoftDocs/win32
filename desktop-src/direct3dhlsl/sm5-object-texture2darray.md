---
title: Texture2DArray
description: Texture2DArray
ms.assetid: 78ab2feb-4d67-4f6f-bffe-48d55183ce28
keywords:
- Texture2DArray HLSL
topic_type:
- apiref
api_name:
- Texture2DArray
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# Texture2DArray

Texture2DArray type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                      | Description                                                                                                                                         |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Gather**](texture2darray-gather.md)                                      | Returns the four texel values that would be used in a bi-linear filtering operation.                                                                |
| [**GatherRed**](texture2darray-gatherred.md)                                | Returns the red components of the four texel values that would be used in a bi-linear filtering operation.                                          |
| [**GatherGreen**](texture2darray-gathergreen.md)                            | Returns the green components of the four texel values that would be used in a bi-linear filtering operation.                                        |
| [**GatherBlue**](texture2darray-gatherblue.md)                              | Returns the blue components of the four texel values that would be used in a bi-linear filtering operation.                                         |
| [**GatherAlpha**](texture2darray-gatheralpha.md)                            | Returns the alpha components of the four texel values that would be used in a bi-linear filtering operation.                                        |
| [**GatherCmp**](texture2darray-gathercmp.md)                                | For four texel values that would be used in a bi-linear filtering operation, returns their comparison against a compare value.                      |
| [**GatherCmpRed**](texture2darray-gathercmpred.md)                          | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their red component against a compare value.   |
| [**GatherCmpGreen**](texture2darray-gathercmpgreen.md)                      | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value. |
| [**GatherCmpBlue**](texture2darray-gathercmpblue.md)                        | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their blue component against a compare value.  |
| [**GatherCmpAlpha**](texture2darray-gathercmpalpha.md)                      | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their alpha component against a compare value. |
| [**GetDimensions**](sm5-object-texture2darray-getdimensions.md)             | Gets the resource dimensions.                                                                                                                       |
| [**Load**](texture2darray-load.md)                                          | Reads texture data.                                                                                                                                 |
| [**mips.Operator\[\]\[\]**](sm5-object-texture2darray-mipsoperatorindex.md) | Gets a read-only resource variable.                                                                                                                 |
| [**Operator\[\]**](sm5-object-texture2darray-operatorindex.md)              | Gets a read-only resource variable.                                                                                                                 |
| [**Sample**](texture2darray-sample.md)                                      | Samples a texture.                                                                                                                                  |
| [**SampleBias**](texture2darray-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                                                                               |
| [**SampleCmp**](texture2darray-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                                                                                      |
| [**SampleCmpLevelZero**](texture2darray-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.                                                                |
| [**SampleGrad**](texture2darray-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated.                                                          |
| [**SampleLevel**](texture2darray-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                                                                                    |



 

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

 

 




