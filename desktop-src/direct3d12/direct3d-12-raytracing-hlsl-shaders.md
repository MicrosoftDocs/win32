---
title: Direct3D 12 Raytracing HLSL Shaders
description: The following HLSL shaders support the Direct3D 12 raytracing pipeline.
ms.assetid: 
ms.localizationpriority: low
ms.topic: article
ms.date: 05/31/2018
---

# Direct3D 12 Raytracing HLSL Shaders

The following HLSL shaders support the Direct3D 12 raytracing pipeline. These shaders are functions compiled into a library, with target model lib_6_3, and identified by an attribute *[shader("shadertype")]* on the shader function. See **Intrinsics** and **System Values** to see what is allowed for each shader type.

## In this section



| Topic                                                                                                       | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Any Hit Shader**](any-hit-shader.md)<br/>                              | A shader that is invoked when ray intersections are not opaque.<br/>                                                                                                                                                                                                                                              |
| [**Callable Shader**](callable-shader.md)<br/>                              | A shader that is invoked from another shader with the **CallShader** intrinsic.<br/>                                                                                                                                                                                                                                              |
| [**Closest Hit Shader**](closest-hit-shader.md)<br/>                              | A shader that is invoked when it is enabled and the closest hit has been determined or ray intersection search ended.<br/>                                                                                                                                                                                                                                              |
| [**Intersection Shader**](intersection-shader.md)<br/>                              | A shader that is used to implement custom intersection primitives for rays intersecting an associated bounding volume (bounding box).<br/>                                                                                                                                                                                                                                              |
| [**Miss Shader**](miss-shader.md)<br/>                              | A shader that is invoked when no ray intersections are found or accepted.<br/>                                                                                                                                                                                                                                              |
| [**Ray Generation Shader**](ray-generation-shader.md)<br/>                              | A shader that calls [**TraceRay**](traceray-function.md) to generate rays.<br/>                                                                                                                                                                                                                                              |

## Related topics

<dl> <dt>

[Core Reference](direct3d-12-core-reference.md)
</dt> <dt>

[Direct3D 12 Reference](direct3d-12-reference.md)
</dt> </dl>

 

 





