---
description: Returns true on helper lanes in pixel shaders.
nms.assetid:
title: IsHelperLane
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- IsHelperLane
api_type:
- NA
---


# IsHelperLane

Returns true on helper lanes in pixel shaders.

## Syntax


```syntax
bool IsHelperLane();
```

## Parameters

This function has no parameters.


## Return value

 A scalar boolean value. `True` if the executing thread is a helper lane. Otherwise, `False`.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | **bool** | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

IsHelperLane identifies whether the current thread is executing as a helper lane, useful for adaptive shading techniques.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [IsHelperLane](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6#is-helper-lane)**