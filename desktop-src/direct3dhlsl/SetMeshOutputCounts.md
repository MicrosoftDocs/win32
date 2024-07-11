---
description: Is used to set the output counts for different types of mesh primitives in geometry shaders.
nms.assetid:
title: SetMeshOutputCounts
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- SetMeshOutputCounts
api_type:
- NA
---


# SetMeshOutputCounts

Is used to set the output counts for different types of mesh primitives in geometry shaders.


## Syntax


```syntax
void SetMeshOutputCounts(uint numVertices, uint numPrimitives);
```


## Parameters

| Item | Description |
|------|-------------|
| *numVertices* | [in] An integer that specifies the number of vertices to be output by the mesh shader.  |
| *numPrimitives* | [in] An integer that specifies the number of primitives to be output by the mesh shader.  |

## Return value

 This function does not return a value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | **void** | **void** | 0 |
| *numVertices* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *numPrimitives* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.5](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_5) and higher shader models | yes |

## Shader Stages

* [**Mesh Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html)

## Remarks

SetMeshOutputCounts configures the number of output vertices and primitives per mesh shader invocation, enabling dynamic mesh generation.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [SetMeshOutputCounts](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#setmeshoutputcounts)**