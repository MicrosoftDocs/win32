---
description: Performs a multi-wave prefix AND operation across all lanes in the wave and returns the result.
nms.assetid:
title: WaveMultiPrefixBitAnd
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- WaveMultiPrefixBitAnd
api_type:
- NA
---


# WaveMultiPrefixBitAnd

Performs a multi-wave prefix AND operation across all lanes in the wave and returns the result.

## Syntax


```syntax
any_int<> WaveMultiPrefixBitAnd(any_int<> value, uint<4> mask);
```

## Parameters

| Item | Description |
|------|-------------|
| *value* | [in] A template type parameter representing the input value. It can be a scalar, vector, or matrix.  || *mask* | [in] A template type parameter used to determine which active lanes to perform the operation on. Also can be a scalar, vector, or matrix.  |
## Return value

 The return type is a scalar, vector, or matrix of the type 'int' or 'uint'. This operation returns the result of a bitwise AND operation performed across all active lanes specified by the mask parameter.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**int**](../WinProg/windows-data-types), [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), [**int64_t**](../WinProg/windows-data-types), [**uint**](../WinProg/windows-data-types), [**uint16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), or [**uint64_t**](../WinProg/windows-data-types) | any |
| *value*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**int**](../WinProg/windows-data-types), [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), [**int64_t**](../WinProg/windows-data-types), [**uint**](../WinProg/windows-data-types), [**uint16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), or [**uint64_t**](../WinProg/windows-data-types) | any |
| *mask*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | 4 |

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

WaveMultiPrefixBitAnd computes the bitwise AND across wavefront threads, useful for parallel bit masking operations.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [WaveMultiPrefix*() Functions](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_5#wavemultiprefix-functions)**