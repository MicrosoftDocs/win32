---
title: RWByteAddressBuffer
description: A read/write buffer that indexes in bytes.
ms.assetid: 8370c14c-5822-4240-942d-565aa223d48c
keywords:
- RWByteAddressBuffer HLSL
topic_type:
- apiref
api_name:
- RWByteAddressBuffer
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWByteAddressBuffer

A read/write buffer that indexes in bytes.



| Method                                                                                          | Description                         |
|-------------------------------------------------------------------------------------------------|-------------------------------------|
| [**GetDimensions**](sm5-object-rwbyteaddressbuffer-getdimensions.md)                           | Gets the resource dimensions.       |
| [**InterlockedAdd**](sm5-object-rwbyteaddressbuffer-interlockedadd.md)                         | Adds, atomically.                   |
| [**InterlockedAnd**](sm5-object-rwbyteaddressbuffer-interlockedand.md)                         | ANDs, atomically.                   |
| [**InterlockedCompareExchange**](sm5-object-rwbyteaddressbuffer-interlockedcompareexchange.md) | Compares and exchanges, atomically. |
| [**InterlockedCompareStore**](sm5-object-rwbyteaddressbuffer-interlockedcomparestore.md)       | Compares and stores, atomically.    |
| [**InterlockedExchange**](sm5-object-rwbyteaddressbuffer-interlockedexchange.md)               | Exchanges, atomically.              |
| [**InterlockedMax**](sm5-object-rwbyteaddressbuffer-interlockedmax.md)                         | Finds the max, atomically.          |
| [**InterlockedMin**](sm5-object-rwbyteaddressbuffer-interlockedmin.md)                         | Find the min, atomically.           |
| [**InterlockedOr**](sm5-object-rwbyteaddressbuffer-interlockedor.md)                           | ORs, atomically.                    |
| [**InterlockedXor**](sm5-object-rwbyteaddressbuffer-interlockedxor.md)                         | XORs, atomically.                   |
| [**Load**](rwbyteaddressbuffer-load.md)                                                        | Gets one value.                     |
| [**Load2**](rwbyteaddressbuffer-load2.md)                                                      | Gets two values.                    |
| [**Load3**](rwbyteaddressbuffer-load3.md)                                                      | Gets three values.                  |
| [**Load4**](rwbyteaddressbuffer-load4.md)                                                      | Gets four values.                   |
| [**Store**](sm5-object-rwbyteaddressbuffer-store.md)                                           | Sets one value.                     |
| [**Store2**](sm5-object-rwbyteaddressbuffer-store2.md)                                         | Sets two values.                    |
| [**Store3**](sm5-object-rwbyteaddressbuffer-store3.md)                                         | Sets three values.                  |
| [**Store4**](sm5-object-rwbyteaddressbuffer-store4.md)                                         | Sets four values.                   |



 

RWByteAddressBuffer objects can be prefixed with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will flush a UAV only within the current group.

The UAV format bound to this resource needs to be created with the DXGI\_FORMAT\_R32\_TYPELESS format.

The UAV bound to this resource must have been created with the [**D3D11\_BUFFER\_UAV\_FLAG\_RAW**](/windows/desktop/api/d3d11/ne-d3d11-d3d11_buffer_uav_flag).

You can use the **RWByteAddressBuffer** object type when you work with raw buffers. For more info about raw viewing of buffers, see [Raw Views of Buffers](/windows/desktop/direct3d11/overviews-direct3d-11-resources-intro).

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

 

