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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
api_location: 
---

# TextureCubeArray object

**TextureCubeArray** type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports these methods in addition to the methods in Shader Model 4.

-   [Methods](#methods)

### Methods

The **TextureCubeArray** object has these methods.



| Method                                                            | Description                                                                                           |
|:------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------|
| [**Gather**](texturecubearray-gather.md)                         | Samples a texture and returns all components.<br/>                                              |
| [**GatherAlpha**](texturecubearray-gatheralpha.md)               | Samples a texture and returns the alpha component.<br/>                                         |
| [**GatherBlue**](texturecubearray-gatherblue.md)                 | Samples a texture and returns the blue component.<br/>                                          |
| [**GatherCmp**](texturecubearray-gathercmp.md)                   | Samples and compares a texture and returns all components.<br/>                                 |
| [**GatherCmpAlpha**](texturecubearray-gathercmpalpha.md)         | Samples and compares a texture and returns the alpha component.<br/>                            |
| [**GatherCmpBlue**](texturecubearray-gathercmpblue.md)           | Samples and compares a texture and returns the blue component.<br/>                             |
| [**GatherCmpGreen**](texturecubearray-gathercmpgreen.md)         | Samples and compares a texture and returns the green component.<br/>                            |
| [**GatherCmpRed**](texturecubearray-gathercmpred.md)             | Samples and compares a texture and returns the red component.<br/>                              |
| [**GatherGreen**](texturecubearray-gathergreen.md)               | Samples a texture and returns the green component.<br/>                                         |
| [**GatherRed**](texturecubearray-gatherred.md)                   | Samples a texture and returns the red component.<br/>                                           |
| [**Sample**](texturecubearray-sample.md)                         | Samples a texture.<br/>                                                                         |
| [**SampleBias**](texturecubearray-samplebias.md)                 | Samples a texture, after applying the bias value to the mipmap level.<br/>                      |
| [**SampleCmp**](texturecubearray-samplecmp.md)                   | Samples a texture, using a comparison value to reject samples.<br/>                             |
| [**SampleCmpLevelZero**](texturecubearray-samplecmplevelzero.md) | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.<br/>       |
| [**SampleGrad**](texturecubearray-samplegrad.md)                 | Samples a texture using a gradient to influence the way the sample location is calculated.<br/> |
| [**SampleLevel**](texturecubearray-samplelevel.md)               | Samples a texture on the specified mipmap level.<br/>                                           |



 

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

 

 





