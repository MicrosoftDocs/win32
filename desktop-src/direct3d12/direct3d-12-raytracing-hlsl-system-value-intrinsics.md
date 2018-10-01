---
title: Direct3D 12 Raytracing HLSL System Value Intrinsics
description: The following HLSL shaders support the Direct3D 12 raytracing pipeline.
ms.assetid: 
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 Raytracing HLSL System Value Intrinsics

System values are retrieved by using special intrinsic functions, rather than including parameters with special semantics in your shader function signature. 

## In this section

### Ray dispatch system values

| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DispatchRaysIndex**](dispatchraysindex.md)<br/>                              | Gets the current x and y location within the width and height obtained with the **DispatchRaysDimensions** system value intrinsic.<br/>                                                                                                                                                                                                                                              |
| [**DispatchRaysDimensions**](dispatchraysdimensions.md)<br/>                              | The width, height and depth values from the **D3D12\_DISPATCH\_RAYS\_DESC** structure specified in the originating **DispatchRays** call.<br/>                                                                                                                                                                                                                                              |

### Ray system values

| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WorldRayOrigin**](worldrayorigin.md)<br/>                              | The world-space direction for the current ray.<br/>                                                                                                                                                                                                                                              |
| [**WorldRayDirection**](worldraydirection.md)<br/>                              | The world-space direction for the current ray.<br/>                                                                                                                                                                                                                                              |
| [**RayTMin**](raytmin.md)<br/>                              | A float representing the current parametric starting point for the ray. <br/>                                                                                                                                                                                                                                              |
| [**RayTCurrent**](raytcurrent.md)<br/>                              | An unsigned integer containing the current **ray_flag** flags. <br/>                                                                                                                                                                                                                                              |
| [**RayFlags**](rayflags.md)<br/>                              | Invokes another shader from within a shader.<br/>                                                                                                                                                                                                                                              |

### Primitive/object space system values

| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**InstanceIndex**](instanceindex.md)<br/>                              | The autogenerated index of the current instance in the top-level raytracing acceleration structure.<br/>                                                                                                                                                                                                                                              |
| [**InstanceID**](instanceid.md)<br/>                              | The user-provided identifier for the instance on the bottom-level acceleration structure instance within the top-level structure.<br/>                                                                                                                                                                                                                                              |
| [**PrimitiveIndex**](primitiveindex.md)<br/>                              | The autogenerated index of the primitive within the geometry inside the bottom-level acceleration structure instance.<br/>                                                                                                                                                                                                                                              |
| [**ObjectRayOrigin**](objectrayorigin.md)<br/>                              | The object-space origin for the current ray.<br/>                                                                                                                                                                                                                                              |
| [**ObjectRayDirection**](objectraydirection.md)<br/>                              | The object-space direction for the current ray.<br/>                                                                                                                                                                                                                                              |
| [**ObjectToWorld3x4**](objecttoworld3x4.md)<br/>                              | A matrix for transforming from object-space to world-space.<br/>                                                                                                                                                                                                                                              |
| [**ObjectToWorld4x3**](objecttoworld4x3.md)<br/>                              | A matrix for transforming from object-space to world-space.<br/>                                                                                                                                                                                                                                              |
| [**WorldToObject3x4**](worldtoobject3x4.md)<br/>                              | A matrix for transforming from world-space to object-space<br/>                                                                                                                                                                                                                                              |
| [**WorldToObject4x3**](worldtoobject4x3.md)<br/>                              | A matrix for transforming from world-space to object-space<br/>                                                                                                                                                                                                                                              |
### Hit-specific system values

| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**HitKind**](hitkind.md)<br/>                              | Returns the value passed as the **HitKind** parameter to **ReportHit**.<br/>                                                                                                                                                                                                                                              |

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





