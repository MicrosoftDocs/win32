---
description: Unpacks a signed 8-bit value into a signed 32-bit value.
nms.assetid:
title: unpack_s8s32
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- unpack_s8s32
api_type:
- NA
---


# unpack_s8s32

Unpacks a signed 8-bit value into a signed 32-bit value.

## Syntax


```syntax
int<4> unpack_s8s32(p32i8 pk);
```

## Parameters

| Item | Description |
|------|-------------|
| *pk* | [in] A packed integer input.  |
## Return value

 Returns a vector with each component being an int type, unpacked from the input.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**int**](../WinProg/windows-data-types) | 4 |
| *pk*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**int8_t4_packed**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

unpack_s8s32 unpacks a signed 8-bit value into a signed 32-bit value, useful for data conversion in shaders.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Unpack Intrinsics](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Pack_Unpack_Intrinsics#unpack-intrinsics)**