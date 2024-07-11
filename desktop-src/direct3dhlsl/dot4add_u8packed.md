---
description: Unsigned dot product of 4 x u8 vectors packed into i32, with accumulate to i32.
nms.assetid:
title: dot4add_u8packed
ms.topic: reference
ms.date: 07/11/2024
topic_type:
- APIRef
- kbSyntax
api_name:
- dot4add_u8packed
api_type:
- NA
---


# dot4add_u8packed

Unsigned dot product of 4 x u8 vectors packed into i32, with accumulate to i32.


## Syntax


```syntax
uint dot4add_u8packed(uint a, uint b, uint c);
```


## Parameters

| Item | Description |
|------|-------------|
| *a* | [in] The first input parameter of scalar and component type uint.  |
| *b* | [in] The second input parameter of scalar and component type uint.  |
| *c* | [in] The third input parameter of scalar and component type uint.  |

## Return value

 Returns a scalar with component type uint. The result is the sum of the products of the corresponding entries of the two input vectors along with the addition of the third parameter.
## Type Description

| Name  | [**Template Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md)| [**Component Type**](../direct3dhlsl/dx-graphics-hlsl-data-types.md) | Size |
|-------|--------------------------------------------------------------------|----------------------------------------------------------------------|------|
| *ret* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *a* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *b* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |
| *c* | [**scalar**](../direct3dhlsl/dx-graphics-hlsl-scalar.md) | [**uint**](../WinProg/windows-data-types) | 1 |

## Minimum Shader Model

This function is supported in the following shader models.
|Shader Model |	Supported|
|-------------|----------|
|[Shader Model 6.4](../direct3dhlsl/hlsl-shader-model-6-4-features-for-direct3d-12.md) and higher shader models | yes |

## Shader Stages


## Remarks

dot4add_u8packed computes a dot product with four 8-bit packed unsigned integer vectors, useful for SIMD optimizations.

## See also


- [**Intrinsic Functions (DirectX HLSL)**](../direct3dhlsl/dx-graphics-hlsl-intrinsic-functions.md)
- **See [Unsigned Integer Dot-Product of 4 Elements and Accumulate](../direct3dhlsl/hlsl-shader-model-6-4-features-for-direct3d-12.md#unsigned-integer-dot-product-of-4-elements-and-accumulate)**