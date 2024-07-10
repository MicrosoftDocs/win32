---
description: Unpacks an unsigned 8-bit value into an unsigned 32-bit value.
nms.assetid:
title: unpack_u8u32
ms.topic: reference
ms.date: 07/10/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- unpack_u8u32
api_type:
- NA
---


# unpack_u8u32

Unpacks an unsigned 8-bit value into an unsigned 32-bit value.

## Syntax


```syntax
uint<4> unpack_u8u32(p32u8 pk);
```

## Parameters

| Item | Description |
|------|-------------|
| *pk* | [in] The parameter pk is an input to the 'unpack_u8u32' function. It is a uint input value, packed with 4 8-bit values which need to be unpacked.  |
## Return value

 This HLSL intrinsic function 'unpack_u8u32' returns a vector of 4 unsigned integers. Each component in the vector corresponds to an 8-bit value unpacked from the input uint parameter 'pk'. The returned values range from 0 to 255.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret*   | [**vector**](../direct3dhlsl/dx-graphics-hlsl-vector.md) | [**uint**](../WinProg/windows-data-types) | 4 |
| *pk*   | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint8_t4_packed**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.6](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_ShaderModel6_6) and higher shader models | yes |

## Shader Stages


## Remarks

unpack_u8u32 unpacks an unsigned 8-bit value into an unsigned 32-bit value, useful for data conversion in shaders.
## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Unpack Intrinsics](https://microsoft.github.io/DirectX-Specs/d3d/HLSL_SM_6_6_Pack_Unpack_Intrinsics#unpack-intrinsics)**