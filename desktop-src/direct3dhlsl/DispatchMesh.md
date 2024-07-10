---
description: Is used to dispatch mesh shader threads for processing mesh primitives.
nms.assetid:
title: DispatchMesh
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- DispatchMesh
api_type:
- NA
---


# DispatchMesh

Is used to dispatch mesh shader threads for processing mesh primitives.

## Syntax


```syntax
void DispatchMesh(uint threadGroupCountX, uint threadGroupCountY, uint threadGroupCountZ, udt meshPayload);
```

## Parameters

| Item | Description |
|------|-------------|
| *threadGroupCountX* | [in] Specifies the number of thread groups dispatched in the x dimension.  || *threadGroupCountY* | [in] Specifies the number of thread groups dispatched in the y dimension.  || *threadGroupCountZ* | [in] Specifies the number of thread groups dispatched in the z dimension.  || *meshPayload* | [in] A structure that includes shader data for the dispatched mesh shader.  |
## Return value

 This function does not return a value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | **void** | **void** | 0 |
| *threadGroupCountX*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *threadGroupCountY*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *threadGroupCountZ*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *meshPayload*   | [**RayPayload**](../direct3d12/ray-payload.md) [**Struct**](../direct3dhlsl/dx-graphics-hlsl-struct.md) | **RayPayload** | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.5](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_5) and higher shader models | yes |

## Shader Stages

* [**Amplification Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#amplification-shader-and-mesh-shader)

## Remarks

DispatchMesh dispatches thread groups for mesh shaders, allowing flexible thread group generation based on runtime conditions.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [DispatchMesh - intrinsic](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#dispatchmesh-intrinsic)**