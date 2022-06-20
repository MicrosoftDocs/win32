---
title: StructuredBuffer
description: A read-only buffer, which can take a T type that is a structure.
ms.assetid: fe2ec0b8-0e19-42b6-9dad-c992ecdeb19e
keywords:
- StructuredBuffer HLSL
topic_type:
- apiref
api_name:
- StructuredBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# StructuredBuffer

A read-only buffer, which can take a T type that is a structure.

| Method                                                             | Description                            |
|--------------------------------------------------------------------|----------------------------------------|
| [**GetDimensions**](sm5-object-structuredbuffer-getdimensions.md) | Gets the resource dimensions.          |
| [**Load**](structuredbuffer-load.md)                              | Reads buffer data.                     |
| [**Operator\[\]**](sm5-object-structuredbuffer-operatorindex.md)  | Returns a read-only resource variable. |

The SRV format bound to this resource needs to be created with the **DXGI_FORMAT_UNKNOWN** format.

To find out more about [structured buffers](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources), see the overview material.

## Minimum Shader Model

This object is supported in the following shader models.

| Shader Model                                                                                                                                                                                                            | Supported |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models [Shader Model 4](dx-graphics-hlsl-sm4.md) (Available for compute and pixel shaders in Direct3D 11 on some Direct3D 10 devices.)<br/> | yes       |

This object is supported for the following types of shaders.

| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>
