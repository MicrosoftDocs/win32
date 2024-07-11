---
description: Packs an unsigned 8-bit value.
nms.assetid:
title: pack_u8
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- pack_u8
api_type:
- NA
---


# pack_u8

Packs an unsigned 8-bit value.


## Syntax


```syntax
p32u8 pack_u8(any_int16or32<4> v);
```


## Parameters

| Item | Description |
|------|-------------|
| *v* | [in] The input vector to be packed.  |

## Return value

 Returns a 4-byte packed scalar of template type uint8_t4_packed. Each unit contains a component of the original vector.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint8_t4_packed**](../WinProg/windows-data-types) | 1 |
| *v* | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**int**](../WinProg/windows-data-types), [**int16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types), [**uint**](../WinProg/windows-data-types), or [**uint16_t**](https://github.com/microsoft/DirectXShaderCompiler/wiki/16-Bit-Scalar-Types) | 4 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

pack_u8 packs an unsigned 8-bit integer into a 32-bit integer, useful for compact storage of smaller integers in buffers.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Pack Intrinsics](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Pack_Unpack_Intrinsics#pack-intrinsics)**