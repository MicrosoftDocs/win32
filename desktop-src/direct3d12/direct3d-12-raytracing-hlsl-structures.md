---
title: Direct3D 12 Raytracing HLSL Structures
description: The following HLSL structures support the Direct3D 12 raytracing pipeline.
ms.assetid: 
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Raytracing HLSL Shaders

The following HLSL structures support the Direct3D 12 raytracing pipeline.

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Call Parameter Structure**](/call-parameter-structure.md)<br/>                              | A user-defined structure provided as an inout argument to a CallShader call, and as an inout parameter for the callable shader.<br/>                                                                                                                                                                                                                                              |
| [**Intersection Attributes Structure**](/intersection-attributes.md)<br/>                              | A user-defined structure that is provided as an inout argument in a TraceRay call, and as an inout parameter in the shader types that may access the ray payload.<br/>                                                                                                                                                                                                                                              |
| [**Ray Payload Structure**](/ray-payload.md)<br/>                              | A user-defined structure that is provided as an inout argument in a TraceRay call, and as an inout parameter in the shader types that may access the ray payload.<br/>                                                                                                                                                                                                                                              |
| [**RayDesc Structure**](/raydesc.md)<br/>                              | Flags passed to the TraceRay function to override transparency, culling, and early-out behavior.<br/>                                                                                                                                                                                                                                              |
| [**RaytracingAccelerationStructure Structure**](/raytracingaccelerationstructure.md)<br/>                              | A resource type that can be declared in HLSL and passed into **TraceRay** to indicate the top-level acceleration resource built using **BuildRaytracingAccelerationStructure**.<br/>                                                                                                                                                                                                                                              |





 

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





