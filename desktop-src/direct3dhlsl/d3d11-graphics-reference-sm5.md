---
title: Shader Model 5
description: This section contains the reference pages for HLSL Shader Model 5.
ms.assetid: ec646940-8901-45c5-a44c-434c8acae2aa
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- apiref
api_name: 
api_type: 
api_location: 
---

# Shader Model 5

This section contains the reference pages for HLSL Shader Model 5.

Shader Model 5 is a superset of the capabilites in [Shader Model 4](dx-graphics-hlsl-sm4.md). It has been designed using a common-shader core which provides a common set of features to all programmable shaders, which are only programmable using HLSL.



| Feature                   | Capability                                                                                                                                             |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| Instruction Set           | [**HLSL intrinsic functions**](dx-graphics-hlsl-intrinsic-functions.md)                                                                               |
| Vertex Shader Max         | No restriction                                                                                                                                         |
| Pixel Shader Max          | No restriction                                                                                                                                         |
| New Shader Profiles Added | cs\_4\_0, gs\_4\_0\*, ps\_4\_0\*, vs\_4\_0\*, cs\_4\_1, gs\_4\_1\*, ps\_4\_1\*, vs\_4\_1\*, cs\_5\_0, ds\_5\_0, gs\_5\_0, hs\_5\_0, ps\_5\_0, vs\_5\_0 |



 

\* - gs\_4\_0, gs\_4\_1, ps\_4\_0, ps\_4\_1, vs\_4\_0 and vs\_4\_1 were introduced in Shader Model 4.0, however, DirectX 11 adds support for [structured buffers](/windows/desktop/direct3d11/direct3d-11-advanced-stages-cs-resources) and byte address buffers to Shader Model 4 running on DirectX 10 hardware.

Shader Model 5 introduces the [compute shader](/windows/desktop/direct3d11/direct3d-11-advanced-stages-compute-shader) which provides high-speed general purpose computing.

A more complete listing of Shader Model 5 features is included in a listing of the [Direct3D 11 features](/windows/desktop/direct3d11/direct3d-11-features).

The [Shader Model 5 Assembly](shader-model-5-assembly--directx-hlsl-.md) section describes the assembly instructions that the Shader Model 5 supports.

## In This Section



| Item                                                                                                                                                                                                                                                        | Description                                                        |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="Shader_Model_5_Attributes"></span><span id="shader_model_5_attributes"></span><span id="SHADER_MODEL_5_ATTRIBUTES"></span>[Shader Model 5 Attributes](d3d11-graphics-reference-sm5-attributes.md)<br/>                                     | Reference pages for Shader Model 5 attributes.<br/>          |
| <span id="Shader_Model_5_Intrinsic_Functions"></span><span id="shader_model_5_intrinsic_functions"></span><span id="SHADER_MODEL_5_INTRINSIC_FUNCTIONS"></span>[Shader Model 5 Intrinsic Functions](d3d11-graphics-reference-sm5-intrinsics.md)<br/> | Reference pages for Shader Model 5 intrinsic functions.<br/> |
| <span id="Shader_Model_5_Objects"></span><span id="shader_model_5_objects"></span><span id="SHADER_MODEL_5_OBJECTS"></span>[Shader Model 5 Objects](d3d11-graphics-reference-sm5-objects.md)<br/>                                                    | Reference pages for Shader Model 5 objects and methods.<br/> |
| <span id="Shader_Model_5_System_Values"></span><span id="shader_model_5_system_values"></span><span id="SHADER_MODEL_5_SYSTEM_VALUES"></span>[Shader Model 5 System Values](d3d11-graphics-reference-sm5-system-values.md)<br/>                      | Reference pages for Shader Model 5 system values.<br/>       |



 

## Related topics

<dl> <dt>

[Shader Models vs Shader Profiles](dx-graphics-hlsl-models.md)
</dt> </dl>

 

