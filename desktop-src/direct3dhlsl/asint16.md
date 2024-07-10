---
description: Converts bit patterns to 16-bit integer values.
nms.assetid:
title: asint16
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- asint16
api_type:
- NA
---


# asint16

Converts bit patterns to 16-bit integer values.

## Syntax


```syntax
int16_t<> asint16(numeric16_only<> x);
```

## Parameters

| Item | Description |
|------|-------------|
| *x* | [in] This is a scalar, vector, or matrix parameter to be converted to type int16_t.  |
## Return value

 Returns a scalar, elementwise vector, or elementwise matrix with its value(s) converted to int16_t.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | any |
| *x*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**half**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), or [**uint16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | any |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

asint16 converts 16-bit integer values to signed integers, useful for unpacking data in shaders.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [HLSL 16-Bit-Scalar-Types](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types)**