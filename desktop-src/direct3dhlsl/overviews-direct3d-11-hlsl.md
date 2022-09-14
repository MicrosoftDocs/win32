---
title: HLSL Shader Model 5
description: HLSL Shader Model 5
ms.assetid: 072c1ff2-ca1b-427c-9969-aa24ebb4ee38
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# HLSL Shader Model 5

This section contains overview material for the High-Level Shader Language, specifically the new features in shader model 5 introduced in Microsoft Direct3D 11.

## In This Section



| Item                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="Dynamic_Linking"></span><span id="dynamic_linking"></span><span id="DYNAMIC_LINKING"></span>[Dynamic Linking](overviews-direct3d-11-hlsl-dynamic-linking.md)<br/>                                 | Dynamic linking allows the runtime to make a decision at draw-time (rather than compile-time) about which code path to run. This reduces the shader proliferation problem caused by shaders with nearly identical input signatures.<br/>                                                                                                                         |
| <span id="Geometry_Shader_Features"></span><span id="geometry_shader_features"></span><span id="GEOMETRY_SHADER_FEATURES"></span>[Geometry Shader Features](overviews-direct3d-11-hlsl-gs-features.md)<br/> | New geometry shader features including: instancing, which provides a performance boost when the order of primitives in the stream doesn't matter, and multiple point output streams so a shader can output vertices on more than one stream.<br/>                                                                                                                |
| <span id="Tessellation"></span><span id="tessellation"></span><span id="TESSELLATION"></span>[Tessellation](/windows/desktop/direct3d11/direct3d-11-advanced-stages-tessellation)<br/>                                        | The Direct3D 11 runtime supports three new stages that implement tessellation, which converts low-detail subdivision surfaces into higher-detail primitives on the GPU. Tessellation tiles (or breaks up) high-order surfaces into suitable structures for rendering. The three tessellation stages are hull-shader, tessellator, and domain-shader stages.<br/> |



 

In addition, the reference section covers many new API elements for shader model 5 including: [attributes](d3d11-graphics-reference-sm5-attributes.md), [intrinsic functions](d3d11-graphics-reference-sm5-intrinsics.md), [shader model 5 objects and methods](d3d11-graphics-reference-sm5-objects.md), and [system values](d3d11-graphics-reference-sm5-system-values.md).

## Related topics

<dl> <dt>

[Programming Guide for HLSL](dx-graphics-hlsl-pguide.md)
</dt> </dl>

 

