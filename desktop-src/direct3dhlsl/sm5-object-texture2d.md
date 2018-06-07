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
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Texture2D

Texture2D type ([as it exists in Shader Model 4](dx-graphics-hlsl-to-type.md)) plus resource variables. This texture object supports the following methods in addition to the methods in Shader Model 4.



| Method                                                                  | Description                                                                                |
|-------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [**Gather**](texture2d-gather.md)                                      | Samples a texture and returns all components.                                              |
| [**GatherRed**](texture2d-gatherred.md)                                | Samples a texture and returns the red component.                                           |
| [**GatherGreen**](texture2d-gathergreen.md)                            | Samples a texture and returns the green component.                                         |
| [**GatherBlue**](texture2d-gatherblue.md)                              | Samples a texture and returns the blue component.                                          |
| [**GatherAlpha**](texture2d-gatheralpha.md)                            | Samples a texture and returns the alpha component.                                         |
| [**GatherCmp**](texture2d-gathercmp.md)                                | Samples and compares a texture and returns all components.                                 |
| [**GatherCmpRed**](texture2d-gathercmpred.md)                          | Samples and compares a texture and returns the red component.                              |
| [**GatherCmpGreen**](texture2d-gathercmpgreen.md)                      | Samples and compares a texture and returns the green component.                            |
| [**GatherCmpBlue**](texture2d-gathercmpblue.md)                        | Samples and compares a texture and returns the blue component.                             |
| [**GatherCmpAlpha**](texture2d-gathercmpalpha.md)                      | Samples and compares a texture and returns the alpha component.                            |
| [**GetDimensions**](sm5-object-texture2d-getdimensions.md)             | Gets the resource dimensions.                                                              |
| [**Load**](texture2d-load.md)                                          | Reads texture data.                                                                        |
| [**mips.Operator\[\]\[\]**](sm5-object-texture2d-mipsoperatorindex.md) | Gets a read-only resource variable.                                                        |
| [**Operator\[\]**](sm5-object-texture2d-operatorindex.md)              | Gets a read-only resource variable.                                                        |
| [**Sample**](texture-sample-overload.md)                               | Samples a texture.                                                                         |
| [**SampleBias**](texture2d-samplebias.md)                              | Samples a texture, after applying the bias value to the mipmap level.                      |
| [**SampleCmp**](texture2d-samplecmp.md)                                | Samples a texture, using a comparison value to reject samples.                             |
| [**SampleCmpLevelZero**](texture2d-samplecmplevelzero.md)              | Samples a texture (mipmap level 0 only), using a comparison value to reject samples.       |
| [**SampleGrad**](texture2d-samplegrad.md)                              | Samples a texture using a gradient to influence the way the sample location is calculated. |
| [**SampleLevel**](texture2d-samplelevel.md)                            | Samples a texture on the specified mipmap level.                                           |



 

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

 

 




