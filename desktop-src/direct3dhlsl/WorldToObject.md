---
description: Converts world-space coordinates to object-space.
nms.assetid:
title: WorldToObject
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- WorldToObject
api_type:
- NA
---


# WorldToObject

Converts world-space coordinates to object-space.


## Syntax


```syntax
float<3@4> WorldToObject();
```


## Parameters

This function has no parameters.


## Return value

 Returns a scalar value of type float that represents the transformation from world space to object space.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**float**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.3](https://github.com/microsoft/DirectXShaderCompiler/wiki/Shader-Model-6.3) and higher shader models | yes |

## Shader Stages

* **Library Shader**
* [**Intersection Shader**](../direct3d12/intersection-shader.md)
* [**Anyhit Shader**](../direct3d12/any-hit-shader.md)
* [**Closesthit Shader**](../direct3d12/closest-hit-shader.md)

## Remarks

This is the inverse of the ObjectToWorld transformation

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [DXR Functional Spec](https://microsoft.github.io/DirectX-Specs/d3d/Raytracing.html)**