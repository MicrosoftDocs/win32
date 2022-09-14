---
title: RWTexture1D
description: A read/write resource. | RWTexture1D
ms.assetid: 47866e5a-b26b-4264-9291-c8940882d662
keywords:
- RWTexture1D HLSL
topic_type:
- apiref
api_name:
- RWTexture1D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWTexture1D

A read/write resource.



| Method                                                        | Description                   |
|---------------------------------------------------------------|-------------------------------|
| [**GetDimensions**](sm5-object-rwtexture1d-getdimensions.md) | Gets the resource dimensions. |
| [**Load**](rwtexture1d-load.md)                              | Reads texture data.           |
| [**Operator\[\]**](sm5-object-rwtexture1d-operatorindex.md)  | Gets a resource variable.     |



 

You can prefix **RWTexture1D** objects with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will flush a UAV only within the current group.

A **RWTexture1D** object requires an element type in a declaration statement for the object. For example, the following declaration is correct:


```
RWTexture1D<float> tex;
```



Because a **RWTexture1D** object is a UAV-type object, its properties differ from a shader resource view (SRV)-type object, such as a [**Texture1D**](sm5-object-texture1d.md) object. For example, you can read from and write to a **RWTexture1D** object, but you can only read from a **Texture1D** object.

A **RWTexture1D** object cannot use methods from a [**Texture1D**](sm5-object-texture1d.md) object, such as [Sample](dx-graphics-hlsl-to-sample.md). However, because you can create multiple view types to the same resource, you can declare multiple texture types as a single texture in multiple shaders. For example, you can declare and use a **RWTexture1D** object as *tex* in a compute shader and then declare and use a **Texture1D** object as *tex* in a pixel shader.

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

 

 




