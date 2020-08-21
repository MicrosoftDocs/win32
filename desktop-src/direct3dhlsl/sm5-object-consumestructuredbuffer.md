---
title: ConsumeStructuredBuffer
description: An input buffer that appears as a stream the shader may pull values from. Only structured buffers can take T types that are structures.
ms.assetid: 373bdd97-6186-4bce-99bf-738a153234f6
keywords:
- ConsumeStructuredBuffer HLSL
topic_type:
- apiref
api_name:
- ConsumeStructuredBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# ConsumeStructuredBuffer

An input buffer that appears as a stream the shader may pull values from. Only structured buffers can take T types that are structures.



| Method                                                                    | Description                                 |
|---------------------------------------------------------------------------|---------------------------------------------|
| [**Consume**](sm5-object-consumestructuredbuffer-consume.md)             | Removes a value from the end of the buffer. |
| [**GetDimensions**](sm5-object-consumestructuredbuffer-getdimensions.md) | Gets the resource dimensions.               |



 

The UAV format bound to this resource needs to be created with the DXGI\_FORMAT\_UNKNOWN format.

The UAV bound to this resource must have been created with [**D3D11\_BUFFER\_UAV\_FLAG\_APPEND**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_buffer_uav_flag).

For more info about consume structured buffers, see both sections: [append and consume buffer](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources) and [structured buffer](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources).

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                | Supported |
|-----------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

 