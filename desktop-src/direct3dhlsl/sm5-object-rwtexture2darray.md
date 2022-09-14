---
title: RWTexture2DArray
description: A read/write resource. | RWTexture2DArray
ms.assetid: 6a6f3655-f1c0-4d5b-91a2-d79da65858b8
keywords:
- RWTexture2DArray HLSL
topic_type:
- apiref
api_name:
- RWTexture2DArray
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWTexture2DArray

A read/write resource.



| Method                                                             | Description                   |
|--------------------------------------------------------------------|-------------------------------|
| [**GetDimensions**](sm5-object-rwtexture2darray-getdimensions.md) | Gets the resource dimensions. |
| [**Load**](rwtexture2darray-load.md)                              | Reads texture data.           |
| [**Operator\[\]**](sm5-object-rwtexture2darray-operatorindex.md)  | Gets a resource variable.     |



 

You can prefix **RWTexture2DArray** objects with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will flush a UAV only within the current group.

A **RWTexture2DArray** object requires an element type in a declaration statement for the object. For example, the following declaration is correct:


```
RWTexture2DArray<float> tex;
```



Because a **RWTexture2DArray** object is a UAV-type object, its properties differ from a shader resource view (SRV)-type object, such as a [**Texture2DArray**](sm5-object-texture2darray.md) object. For example, you can read from and write to a **RWTexture2DArray** object, but you can only read from a **Texture2DArray** object.

A **RWTexture2DArray** object cannot use methods from a [**Texture2DArray**](sm5-object-texture2darray.md) object, such as [Sample](dx-graphics-hlsl-to-sample.md). However, because you can create multiple view types to the same resource, you can declare multiple texture types as a single texture in multiple shaders. For example, you can declare and use a **RWTexture2DArray** object as *tex* in a compute shader and then declare and use a **Texture2DArray** object as *tex* in a pixel shader.

> [!Note]  
> The runtime enforces certain usage patterns when you create multiple view types to the same resource. For example, the runtime does not allow you to have both a UAV mapping for a resource and SRV mapping for the same resource active at the same time.

 

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

 

 




