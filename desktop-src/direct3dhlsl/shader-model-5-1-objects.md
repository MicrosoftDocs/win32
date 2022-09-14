---
title: Shader Model 5.1 Objects
description: The following objects have been added to shader model 5.1.
ms.assetid: 2958618D-54C6-4860-9910-B45AAB73CCFD
ms.topic: article
ms.date: 05/31/2018
---

# Shader Model 5.1 Objects

The following objects have been added to shader model 5.1.

For the [Rasterizer Order Views](/windows/desktop/direct3d11/rasterizer-order-views) (available in D3D11.3 and D3D12), the following objects are new, and are only allowed in the pixel shader. Note that the methods they support are identical to the corresponding UAV objects.



| Rasterizer object                                   | UAV object                                                              |
|------------------------------------|---------------------------------------------------------------|
| RasterizerOrderedBuffer            | [**RWBuffer**](sm5-object-rwbuffer.md)                       |
| RasterizerOrderedByteAddressBuffer | [**RWByteAddressBuffer**](sm5-object-rwbyteaddressbuffer.md) |
| RasterizerOrderedStructuredBuffer  | [**RWStructuredBuffer**](sm5-object-rwstructuredbuffer.md)   |
| RasterizerOrderedTexture1D         | [**RWTexture1D**](sm5-object-rwtexture1d.md)                 |
| RasterizerOrderedTexture1DArray    | [**RWTexture1DArray**](sm5-object-rwtexture1darray.md)       |
| RasterizerOrderedTexture2D         | [**RWTexture2D**](sm5-object-rwtexture2d.md)                 |
| RasterizerOrderedTexture2DArray    | [**RWTexture2DArray**](sm5-object-rwtexture2darray.md)       |
| RasterizerOrderedTexture3D         | [**RWTexture3D**](sm5-object-rwtexture3d.md)                 |



 

## Related topics

<dl> <dt>

[Shader Model 5.1](shader-model-5-1.md)
</dt> <dt>

[HLSL Shader Model 5.1 Features for Direct3D 12](hlsl-shader-model-5-1-features-for-direct3d-12.md)
</dt> </dl>

 

 
