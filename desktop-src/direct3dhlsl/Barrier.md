---
description: Request a barrier for a set of memory types and/or thread group execution sync.
nms.assetid:
title: Barrier
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- Barrier
api_type:
- NA
---


# Barrier

Request a barrier for a set of memory types and/or thread group execution sync.

## Syntax


```syntax
void Barrier(NodeRecordOrUAV o, uint SemanticFlags);
```

## Parameters

| Item | Description |
|------|-------------|
| *o* | [in] This is the optional argument, which is typically used to specify a location of an array or a specific area in memory.  || *SemanticFlags* | [in] This is used to apply a specific semantic to the function, for example, ordering and grouping threads.  |
## Return value

 This function does not return a value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | **void** | **void** | 0 |
| *o*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) |  | 1 |
| *SemanticFlags*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.8](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_8) and higher shader models | yes |

## Shader Stages


## Remarks

Barrier synchronizes threads within a shader, ensuring data consistency and facilitating parallel computation.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Work Graphs Barrier Types](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs.html#barrier)**