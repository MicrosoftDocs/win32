---
description: Allocates resources for ray queries in ray tracing shaders.
nms.assetid:
title: AllocateRayQuery
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- AllocateRayQuery
api_type:
- NA
---


# AllocateRayQuery

Allocates resources for ray queries in ray tracing shaders.

## Syntax


```syntax
uint AllocateRayQuery(uint flags);
```

## Parameters

| Item | Description |
|------|-------------|
| *flags* | [in] An integral scalar or vector that specifies the behavior of the ray query. This parameter defines how the ray intersects with the geometry in the scene.  |
## Return value

 Returns a scalar or vector of type uint, which represents a template type for AllocateRayQuery. This is used to manage a Ray Query object in GPU memory which will hold the required data to perform Ray Query operations.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *flags*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

AllocateRayQuery allocates resources for ray tracing queries, facilitating interactive ray tracing applications.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)