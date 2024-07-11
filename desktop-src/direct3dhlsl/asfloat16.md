---
description: Converts integer bit patterns to half-precision floating-point values.
nms.assetid:
title: asfloat16
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- asfloat16
api_type:
- NA
---


# asfloat16

Converts integer bit patterns to half-precision floating-point values.


## Syntax


```syntax
float16_t<> asfloat16(numeric16_only<> x);
```


## Parameters

| Item | Description |
|------|-------------|
| *x* | [in] The input vector or scalar to be converted to a float16 type.  |

## Return value

 Returns a scalar, elementwise vector, or elementwise matrix with its value(s) converted to a float16 type.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**half**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | any |
| *x* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md), [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md), or [**matrix**](../direct3dhlsl/dx-graphics-hlsl-matrix.md) | [**half**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), or [**uint16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | any |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|

## Shader Stages


## Remarks

asfloat16 converts 16-bit integer values to half-precision floating point values, optimizing storage and arithmetic in shaders.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [HLSL 16-Bit-Scalar-Types](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types)**