---
description: Ensures non-uniform indexing for resources like textures in shaders.
nms.assetid:
title: NonUniformResourceIndex
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- NonUniformResourceIndex
api_type:
- NA
---


# NonUniformResourceIndex

Ensures non-uniform indexing for resources like textures in shaders.


## Syntax


```syntax
any<> NonUniformResourceIndex(any<> index);
```


## Parameters

| Item | Description |
|------|-------------|
| *index* | [in] This parameter represents the indexing value used  by the NonUniformResourceIndex function.  |

## Return value

 Returns the non-uniform resource index. The return type could be a scalar, vector, or matrix and component type of boolean, float, or integer depending on the context it's been used.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | **bool**, [**float**](../WinProg/windows-data-types), or [**int**](../WinProg/windows-data-types) | any |
| *index* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | **bool**, [**float**](../WinProg/windows-data-types), or [**int**](../WinProg/windows-data-types) | any |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

Use NonUniformResourceIndex to access resources in shaders where the access pattern is not uniform across all threads.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [NonUniformResourceIndex semantics](https://microsoft.github.io/DirectX-Specs/d3d/WorkGraphs#nonuniformresourceindex-semantics)**
 - [**Resource Binding**](../direct3d12/resource-binding-in-hlsl.md).