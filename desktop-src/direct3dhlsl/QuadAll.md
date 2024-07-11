---
description: Compares boolean across a quad.
nms.assetid:
title: QuadAll
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- QuadAll
api_type:
- NA
---


# QuadAll

Compares boolean across a quad.


## Syntax


```syntax
bool QuadAll(bool cond);
```


## Parameters

| Item | Description |
|------|-------------|
| *cond* | [in] A boolean value representing the condition that must be satisfied by all four components of a quad for the function to return true.  |

## Return value

 Returns a scalar boolean value that is true if the provided condition is true for all four components of the quad and false otherwise.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | **bool** | 1 |
| *cond* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | **bool** | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.7](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_7) and higher shader models | yes |

## Shader Stages

* **Library Shader**
* [**Compute Shader**](../direct3d11/direct3d-11-advanced-stages-compute-shader.md)
* [**Amplification Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#amplification-shader-and-mesh-shader)
* [**Mesh Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html)
* [**Pixel Shader**](../direct3dhlsl/dx-graphics-hlsl-writing-shaders-9.md#pixel-shader-basics)
* **Node Shader**

## Remarks

QuadAll evaluates whether all threads within a quad meet a condition, facilitating SIMD optimizations in pixel shaders.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [QuadAll](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_7_QuadAny_QuadAll#quadall)**