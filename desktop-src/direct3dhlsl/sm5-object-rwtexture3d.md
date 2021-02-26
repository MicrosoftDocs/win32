---
title: RWTexture3D
description: A read/write resource. | RWTexture3D
ms.assetid: 4d02810e-4f3c-4b20-b057-0ff27d6732b5
keywords:
- RWTexture3D HLSL
topic_type:
- apiref
api_name:
- RWTexture3D
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# RWTexture3D

A read/write resource.



| Method                                                        | Description                   |
|---------------------------------------------------------------|-------------------------------|
| [**GetDimensions**](sm5-object-rwtexture3d-getdimensions.md) | Gets the resource dimensions. |
| [**Load**](rwtexture3d-load.md)                              | Reads texture data.           |
| [**Operator\[\]**](sm5-object-rwtexture3d-operatorindex.md)  | Gets a resource variable.     |



 

You can prefix **RWTexture3D** objects with the storage class **globallycoherent**. This storage class causes memory barriers and syncs to flush data across the entire GPU such that other groups can see writes. Without this specifier, a memory barrier or sync will flush a UAV only within the current group.

A **RWTexture3D** object requires an element type in a declaration statement for the object. For example, the following declaration is correct:


```
RWTexture3D<float> tex;
```



Because a **RWTexture3D** object is a UAV-type object, its properties differ from a shader resource view (SRV)-type object, such as a [**Texture3D**](sm5-object-texture3d.md) object. For example, you can read from and write to a **RWTexture3D** object, but you can only read from a **Texture3D** object.

A **RWTexture3D** object cannot use methods from a [**Texture3D**](sm5-object-texture3d.md) object, such as [Sample](dx-graphics-hlsl-to-sample.md). However, because you can create multiple view types to the same resource, you can declare multiple texture types as a single texture in multiple shaders. For example, you can declare and use a **RWTexture3D** object as *tex* in a compute shader and then declare and use a **Texture3D** object as *tex* in a pixel shader.

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

 

 




