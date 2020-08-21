---
title: RWStructuredBuffer
description: A read/write buffer that can take a T type that is a structure.
ms.assetid: 8dd93b81-135d-4f28-898f-38510dc39af1
keywords:
- RWStructuredBuffer HLSL
topic_type:
- apiref
api_name:
- RWStructuredBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWStructuredBuffer

A read/write buffer that can take a T type that is a structure.



| Method                                                                     | Description                             |
|----------------------------------------------------------------------------|-----------------------------------------|
| [**DecrementCounter**](sm5-object-rwstructuredbuffer-decrementcounter.md) | Decrements the object's hidden counter. |
| [**GetDimensions**](sm5-object-rwstructuredbuffer-getdimensions.md)       | Gets the resource dimensions.           |
| [**IncrementCounter**](sm5-object-rwstructuredbuffer-incrementcounter.md) | Increments the object's hidden counter. |
| [**Load**](rwstructuredbuffer-load.md)                                    | Reads buffer data.                      |
| [**Operator\[\]**](sm5-object-rwstructuredbuffer-operatorindex.md)        | Returns a resource variable.            |



 

A resource variable can also be passed into any unordered or interlocked operation.

RWStructuredBuffer objects can be prefixed with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will only flush a UAV within the current group.

The UAV format bound to this resource needs to be created with the DXGI\_FORMAT\_UNKNOWN format.

To find out more about [structured buffers](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources), see the overview material.

## Minimum Shader Model

This object is supported in the following shader models.



| Shader Model                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Supported |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [Shader Model 5](d3d11-graphics-reference-sm5.md) and higher shader models [Shader Model 4](dx-graphics-hlsl-sm4.md) (Available through the Direct3D 11 API by using 10.0 or 10.1 feature level ([**D3D\_FEATURE\_LEVEL**](/windows/desktop/api/d3dcommon/ne-d3dcommon-d3d_feature_level)\_10\_X) on devices that support compute shaders. For more information about compute shader support on downlevel hardware, see [Compute Shaders on Downlevel Hardware](/windows/desktop/direct3d11/overviews-direct3d-11-devices-downlevel-compute-shaders).)<br/> | yes       |



 

This object is supported for the following types of shaders:



| Vertex | Hull | Domain | Geometry | Pixel | Compute |
|--------|------|--------|----------|-------|---------|
|        |      |        |          | x     | x       |



 

## See also

<dl> <dt>

[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)
</dt> </dl>

 

