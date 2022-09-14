---
title: TextureCubeArray object
description: TextureCubeArray type (as it exists in Shader Model 4) plus resource variables. This texture object supports these methods in addition to the methods in Shader Model 4.
ms.assetid: 62AAF0F9-D552-4FFA-B681-749D6DC205BD
keywords:
- TextureCubeArray object HLSL
- TextureCubeArray object HLSL , described
topic_type:
- apiref
api_name:
- TextureCubeArray
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TextureCubeArray object

**TextureCubeArray** type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports these methods in addition to the methods in Shader Model 4.

-   [Methods](#methods)

### Methods

The **TextureCubeArray** object has these methods.



| Method                                                           | Description                                                                                                                                              |
|:-----------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Gather**](texturecubearray-gather.md)                         | Returns the four texel values that would be used in a bi-linear filtering operation.<br/>                                                                |
| [**GatherAlpha**](texturecubearray-gatheralpha.md)               | Returns the alpha components of the four texel values that would be used in a bi-linear filtering operation.<br/>                                        |
| [**GatherBlue**](texturecubearray-gatherblue.md)                 | Returns the blue components of the four texel values that would be used in a bi-linear filtering operation.<br/>                                         |
| [**GatherCmp**](texturecubearray-gathercmp.md)                   | For four texel values that would be used in a bi-linear filtering operation, returns their comparison against a compare value.<br/>                      |
| [**GatherCmpAlpha**](texturecubearray-gathercmpalpha.md)         | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their alpha component against a compare value.<br/> |
| [**GatherCmpBlue**](texturecubearray-gathercmpblue.md)           | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their blue component against a compare value.<br/>  |
| [**GatherCmpGreen**](texturecubearray-gathercmpgreen.md)         | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their green component against a compare value.<br/> |
| [**GatherCmpRed**](texturecubearray-gathercmpred.md)             | For four texel values that would be used in a bi-linear filtering operation, returns a comparison of their red component against a compare value.<br/>   |
| [**GatherGreen**](texturecubearray-gathergreen.md)               | Returns the green components of the four texel values that would be used in a bi-linear filtering operation.<br/>                                        |
| [**GatherRed**](texturecubearray-gatherred.md)                   | Returns the red components of the four texel values that would be used in a bi-linear filtering operation.<br/>                                          |
| [**Sample**](texturecubearray-sample.md)                         | Samples a texture.<br/>                                                                                                                                  |
| [**SampleBias**](texturecubearray-samplebias.md)                 | Samples a texture, after applying the bias value to the mipmap level.<br/>                                                                               |
| [**SampleCmp**](texturecubearray-samplecmp.md)                   | Samples a texture, using a comparison value to reject samples.<br/>                                                                                      |
| [**SampleCmpLevelZero**](texturecubearray-samplecmplevelzero.md) | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.<br/>                                                                |
| [**SampleGrad**](texturecubearray-samplegrad.md)                 | Samples a texture using a gradient to influence the way the sample location is calculated.<br/>                                                          |
| [**SampleLevel**](texturecubearray-samplelevel.md)               | Samples a texture on the specified mipmap level.<br/>                                                                                                    |



 

## Remarks

### Minimum Shader Model

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

 

 





