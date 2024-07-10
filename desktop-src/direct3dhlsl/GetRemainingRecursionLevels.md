---
description: Returns how many levels of recursion remain.
nms.assetid:
title: GetRemainingRecursionLevels
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- GetRemainingRecursionLevels
api_type:
- NA
---


# GetRemainingRecursionLevels

Returns how many levels of recursion remain.

## Syntax


```syntax
uint GetRemainingRecursionLevels();
```

## Parameters

This function has no parameters.


## Return value

 This intrinsic function returns a scalar template type with a component of unsigned integer (uint). The returned value represents the number of remaining recursion levels available in the current ray tracing shader invocation.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.8](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_8) and higher shader models | yes |

## Shader Stages

* **Node Shader**

## Remarks

GetRemainingRecursionLevels retrieves the remaining levels of recursion in a shader program, useful for managing recursive algorithms.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [GetRemainingRecursionLevels](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html#getremainingrecursionlevels)**