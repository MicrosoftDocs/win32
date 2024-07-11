---
description: Packs and clamps an unsigned 8-bit value.
nms.assetid:
title: pack_clamp_u8
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- pack_clamp_u8
api_type:
- NA
---


# pack_clamp_u8

Packs and clamps an unsigned 8-bit value.


## Syntax


```syntax
p32u8 pack_clamp_u8(sint16or32_only<4> v);
```


## Parameters

| Item | Description |
|------|-------------|
| *v* | [in] An input parameter which defines a normalized float4 vector.  |

## Return value

 Returns a 4 byte packed scalar holding the clamped values of the input parameter v, with each component being represented as an 8-bit integer. The clamping is applied in the range of [0,1], meaning all output values fall within this range. The packing process condenses the four 8-bit components into a single 4 byte scalar, providing an efficient method for storing and transmitting data. The return type is uint8_t4_packed.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint8_t4_packed**](../WinProg/windows-data-types) | 1 |
| *v* | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**int**](../WinProg/windows-data-types) or [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | 4 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

pack_clamp_u8 packs a clamped unsigned 8-bit integer into a 32-bit integer, useful for safe conversion and storage in buffers.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Pack Intrinsics](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Pack_Unpack_Intrinsics#pack-intrinsics)**