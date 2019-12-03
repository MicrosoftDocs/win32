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



| Method                                                                       | Description                                                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**Gather**](texture2darray-gather.md)                                      | Samples a texture and returns all components.                                              |
| [**GatherRed**](texture2darray-gatherred.md)                                | Samples a texture and returns the red component.                                           |
| [**GatherGreen**](texture2darray-gathergreen.md)                            | Samples a texture and returns the green component.                                         |
| [**GatherBlue**](texture2darray-gatherblue.md)                              | Samples a texture and returns the blue component.                                          |
| [**GatherAlpha**](texture2darray-gatheralpha.md)                            | Samples a texture and returns the alpha component.                                         |
| [**GatherCmp**](texture2darray-gathercmp.md)                                | Samples and compares a texture and returns all components.                                 |
| [**GatherCmpRed**](texture2darray-gathercmpred.md)                          | Samples and compares a texture and returns the red component.                              |
| [**GatherCmpGreen**](texture2darray-gathercmpgreen.md)                      | Samples and compares a texture and returns the green component.                            |
| [**GatherCmpBlue**](texture2darray-gathercmpblue.md)                        | Samples and compares a texture and returns the blue component.                             |
| [**GatherCmpAlpha**](texture2darray-gathercmpalpha.md)                      | Samples and compares a texture and returns the alpha component.                            |
| [**GetDimensions**](sm5-object-texture2darray-getdimensions.md)             | Gets the resource dimensions.                                                              |
| [**Load**](texture2darray-load.md)                                          | Reads texture data.                                                                        |
| [**mips.Operator\[\]\[\]**](sm5-object-texture2darray-mipsoperatorindex.md) | Gets a read-only resource variable.                                                        |
| [**Operator\[\]**](sm5-object-texture2darray-operatorindex.md)              | Gets a read-only resource variable.                                                        |
| [**Sample**](texture2darray-sample.md)                                      | Samples a texture.                                                                         |
| [**SampleBias**](texture2darray-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                      |
| [**SampleCmp**](texture2darray-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                             |
| [**SampleCmpLevelZero**](texture2darray-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.       |
| [**SampleGrad**](texture2darray-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated. |
| [**SampleLevel**](texture2darray-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                           |



 

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

 

 




