---
title: ByteAddressBuffer
description: ByteAddressBuffer
ms.assetid: 809b5ee8-0a25-402e-8cf2-f5e7a8094ec6
keywords:
- ByteAddressBuffer HLSL
topic_type:
- apiref
api_name:
- ByteAddressBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ByteAddressBuffer

A read-only buffer that is indexed in bytes.



| Method                                                              | Description                   |
|---------------------------------------------------------------------|-------------------------------|
| [**GetDimensions**](sm5-object-byteaddressbuffer-getdimensions.md) | Gets the resource dimensions. |
| [**Load**](byteaddressbuffer-load.md)                              | Gets one value.               |
| [**Load2**](byteaddressbuffer-load2.md)                            | Gets two values.              |
| [**Load3**](byteaddressbuffer-load3.md)                            | Gets three values.            |
| [**Load4**](byteaddressbuffer-load4.md)                            | Gets four values.             |



 

You can use the **ByteAddressBuffer** object type when you work with raw buffers. For more info about raw viewing of buffers, see [Raw Views of Buffers](/windows/desktop/direct3d11/overviews-direct3d-11-resources-intro).

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Supported |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models [Shader Model 4](dx-graphics-hlsl-sm4.md) (Available through the Direct3D 11 API by using 10.0 or 10.1 feature level ([**D3D\_FEATURE\_LEVEL**](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_feature_level)\_10\_X) on devices that support compute shaders. For more info about compute shader support on downlevel hardware, see [Compute Shaders on Downlevel Hardware](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-compute-shaders).)<br/> | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
| x      | x    | x      | x        | x     | x       |



 

For more info about a byte address buffer, see the [byte addressable resource type](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources).

Shader Model 5 also implements a [read-write byte address buffer](sm5-object-rwbyteaddressbuffer.md).

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

