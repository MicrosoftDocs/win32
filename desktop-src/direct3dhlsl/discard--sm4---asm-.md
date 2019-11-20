---
title: discard (sm4 - asm)
description: Conditionally flag results of Pixel Shader to be discarded when the end of the program is reached.
ms.assetid: 566C4A9A-B32A-4AA6-A888-70F6965B1B5A
ms.topic: reference
ms.date: 05/31/2018
---

# discard (sm4 - asm)

Conditionally flag results of Pixel Shader to be discarded when the end of the program is reached.



| discard{\_z\|\_nz} src0.select\_component |
|-------------------------------------------|



 



| Item                                                            | Description                                                                                       |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <span id="src0"></span><span id="SRC0"></span>*src0*<br/> | \[in\] The value that determines whether to discard the current pixel being processed.<br/> |



 

## Remarks

This instruction flags the current pixel as terminated, while continuing execution, so that other pixels executing in parallel may obtain derivatives if necessary. Even though execution continues, all Pixel Shader output writes before or after the **discard** instruction are discarded.

For **discard\_z**, if all bits in *src0.select\_component* are zero, then the pixel is discarded.

For **discard\_nz**, if any bits in *src0.select\_component* are nonzero, then the pixel is discarded.

In addition, the **discard** instruction can be present inside any flow control construct.

Multiple **discard** instructions may be present in a Shader, and if any is executed, the pixel is terminated.

This instruction applies to the following shader stages:



| Vertex Shader | Geometry Shader | Pixel Shader |
|---------------|-----------------|--------------|
|               |                 | x            |



 

## Minimum Shader Model

This function is supported in the following shader models.



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | yes       |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | yes       |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 4 Assembly (DirectX HLSL)](dx-graphics-hlsl-sm4-asm.md)
</dt> </dl>

 

 





