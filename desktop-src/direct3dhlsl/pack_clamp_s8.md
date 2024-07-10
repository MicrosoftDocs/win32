---
description: Packs and clamps a signed 8-bit value.
nms.assetid:
title: pack_clamp_s8
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- pack_clamp_s8
api_type:
- NA
---


# pack_clamp_s8

Packs and clamps a signed 8-bit value.

## Syntax


```syntax
p32i8 pack_clamp_s8(sint16or32_only<4> v);
```

## Parameters

| Item | Description |
|------|-------------|
| *v* | [in] This is an input parameter representing the scalar components to be packed into a 4 byte value.  |
## Return value

 This function returns a 4 byte packed scalar of type int8_t4_packed, where the scalar components defined by 'v' are clamped and packed into this return value.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**int8_t4_packed**](../WinProg/windows-data-types) | 1 |
| *v*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**int**](../WinProg/windows-data-types) or [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | 4 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

pack_clamp_s8 packs a clamped signed 8-bit integer into a 32-bit integer, useful for safe conversion and storage in buffers.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Pack Intrinsics](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Pack_Unpack_Intrinsics#pack-intrinsics)**