---
description: Returns the result of the operation on groups of lanes identified by a bitmask.
nms.assetid:
title: WaveMultiPrefixProduct
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- WaveMultiPrefixProduct
api_type:
- NA
---


# WaveMultiPrefixProduct

Returns the result of the operation on groups of lanes identified by a bitmask.


## Syntax


```syntax
numeric<> WaveMultiPrefixProduct(numeric<> value, uint<4> mask);
```


## Parameters

| Item | Description |
|------|-------------|
| *value* | [in] The input value. This value can be a scalar, vector, or matrix with component type of float or int.  |
| *mask* | [in] A boolean mask that determines the lanes from which to calculate the prefix product.  |

## Return value

 Returns the prefix product of the specified input value over the active lanes, as determined by the mask. The return type will be the same type as the input value (scalar, vector, or matrix) with a component type of float or int.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**float**](../WinProg/windows-data-types) or [**int**](../WinProg/windows-data-types) | any |
| *value* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**float**](../WinProg/windows-data-types) or [**int**](../WinProg/windows-data-types) | any |
| *mask* | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | 4 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.5](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_5) and higher shader models | yes |

## Shader Stages

* **Library Shader**
* [**Compute Shader**](../direct3d11/direct3d-11-advanced-stages-compute-shader.md)
* [**Amplification Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html#amplification-shader-and-mesh-shader)
* [**Mesh Shader**](https://microsoft.github.io/DirectX-Specs/d3d/MeshShader.html)
* [**Pixel Shader**](../direct3dhlsl/dx-graphics-hlsl-writing-shaders-9.md#pixel-shader-basics)
* [**Vertex Shader**](../direct3dhlsl/dx-graphics-hlsl-writing-shaders-9.md#vertex-shader-basics)
* [**Hull Shader**](https://learn.microsoft.com/en-us/windows/uwp/graphics-concepts/hull-shader-stage--hs-)
* [**Domain Shader**](https://learn.microsoft.com/en-us/windows/uwp/graphics-concepts/domain-shader-stage--ds-)
* [**Geometry Shader**](https://learn.microsoft.com/en-us/windows/uwp/graphics-concepts/geometry-shader-stage--gs-)
* [**Raygeneration Shader**](../direct3d12/ray-generation-shader.md)
* [**Intersection Shader**](../direct3d12/intersection-shader.md)
* [**Anyhit Shader**](../direct3d12/any-hit-shader.md)
* [**Closesthit Shader**](../direct3d12/closest-hit-shader.md)
* [**Miss Shader**](../direct3d12/miss-shader.md)
* [**Callable Shader**](../direct3d12/callable-shader.md)
* **Node Shader**

## Remarks

WaveMultiPrefixProduct computes the product of values across wavefront threads, useful for parallel reduction operations.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [WaveMultiPrefix*() Functions](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_5#wavemultiprefix-functions)**