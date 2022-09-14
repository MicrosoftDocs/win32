---
title: bufinfo (sm5 - asm)
description: Query the element count on a buffer (but not the constant buffer).
ms.assetid: 3A5C28F3-FE59-4C67-92AC-66B10E1D9692
ms.topic: reference
ms.date: 05/31/2018
---

# bufinfo (sm5 - asm)

Query the element count on a buffer (but not the constant buffer).



| bufinfo dest\[.mask\], srcResource |
|------------------------------------|



 



| Item                                                                                                               | Description                                                                           |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <span id="dest"></span><span id="DEST"></span>*dest*<br/>                                                    | \[in\] The address of the results.<br/>                                         |
| <span id="srcResource"></span><span id="srcresource"></span><span id="SRCRESOURCE"></span>*srcResource*<br/> | \[in\] Buffer, other than a constant Buffer, in an SRV (t\#) or UAV (u\#).<br/> |



 

## Remarks

All components in *dest* receive the integer number of elements in the buffer s shader resource view. The number of elements depends on the view parameters such as memory format.

For a typed buffer SRV or UAV, the return value is the number of elements in the view (where an element is one unit of the typed format).

For a raw buffer SRV or UAV, the return value is the number of bytes in the view.

For a structured buffer SRV or UAV, the return value is the number of structures in the view.

This instruction applies to the following shader stages:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| X      | X    | X      | X        | X     | X       |



 

## Minimum Shader Model

This instruction is supported in the following shader models:



| Shader Model                                              | Supported |
|-----------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md)        | yes       |
| [Shader Model 4.1](dx-graphics-hlsl-sm4.md)              | no        |
| [Shader Model 4](dx-graphics-hlsl-sm4.md)                | no        |
| [Shader Model 3 (DirectX HLSL)](dx-graphics-hlsl-sm3.md) | no        |
| [Shader Model 2 (DirectX HLSL)](dx-graphics-hlsl-sm2.md) | no        |
| [Shader Model 1 (DirectX HLSL)](dx-graphics-hlsl-sm1.md) | no        |



 

## Related topics

<dl> <dt>

[Shader Model 5 Assembly (DirectX HLSL)](shader-model-5-assembly--directx-hlsl-.md)
</dt> </dl>

 

 





