---
title: TextureCube object
description: TextureCube type (as it exists in Shader Model 4) plus resource variables. This texture object supports these methods in addition to the methods in Shader Model 4.
ms.assetid: BC96D7BB-992E-48CC-A774-E211E1BB1720
keywords:
- TextureCube object HLSL
- TextureCube object HLSL , described
topic_type:
- apiref
api_name:
- TextureCube
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# TextureCube object

**TextureCube** type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports these methods in addition to the methods in Shader Model 4.

-   [Methods](#methods)

### Methods

The **TextureCube** object has these methods.



| Method                                                       | Description                                                                                           |
|:-------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**Gather**](texturecube-gather.md)                         | Samples a texture and returns all components.<br/>                                              |
| [**GatherAlpha**](texturecube-gatheralpha.md)               | Samples a texture and returns the alpha component.<br/>                                         |
| [**GatherBlue**](texturecube-gatherblue.md)                 | Samples a texture and returns the blue component.<br/>                                          |
| [**GatherCmp**](texturecube-gathercmp.md)                   | Samples and compares a texture and returns all components.<br/>                                 |
| [**GatherCmpAlpha**](texturecube-gathercmpalpha.md)         | Samples and compares a texture and returns the alpha component.<br/>                            |
| [**GatherCmpBlue**](texturecube-gathercmpblue.md)           | Samples and compares a texture and returns the blue component.<br/>                             |
| [**GatherCmpGreen**](texturecube-gathercmpgreen.md)         | Samples and compares a texture and returns the green component.<br/>                            |
| [**GatherCmpRed**](texturecube-gathercmpred.md)             | Samples and compares a texture and returns the red component.<br/>                              |
| [**GatherGreen**](texturecube-gathergreen.md)               | Samples a texture and returns the green component.<br/>                                         |
| [**GatherRed**](texturecube-gatherred.md)                   | Samples a texture and returns the red component.<br/>                                           |
| [**Sample**](texturecube-sample.md)                         | Samples a texture.<br/>                                                                         |
| [**SampleBias**](texturecube-samplebias.md)                 | Samples a texture, after applying the bias value to the mipmap level.<br/>                      |
| [**SampleCmp**](texturecube-samplecmp.md)                   | Samples a texture, using a comparison value to reject samples.<br/>                             |
| [**SampleCmpLevelZero**](texturecube-samplecmplevelzero.md) | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.<br/>       |
| [**SampleGrad**](texturecube-samplegrad.md)                 | Samples a texture using a gradient to influence the way the sample location is calculated.<br/> |
| [**SampleLevel**](texturecube-samplelevel.md)               | Samples a texture on the specified mipmap level.<br/>                                           |



 

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

 

 





